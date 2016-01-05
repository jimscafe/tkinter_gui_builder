from place_functions import ROW, COLUMN, CENTERED, LEFT,RIGHT, EXPAND
import sys

def traverse_tree(root, process, top_down=False, debug=False):
    # Applies process bottom up
    if top_down:
        append = lambda x,y: x.insert(0,y)
    else:
        append = lambda x,y: x.append(y)
    # append = lambda x,y: x.insert(0,y) # For top down traversing

    ans = ''
    stack = []
    expanded = []
    stack.append(root)
    while stack:
        node = stack[-1]
        if node.name in expanded:
            if debug: print ('Process node', node.name)
            error =  process(node)
            if error:
                ans = error
                break
            stack.pop()
        else:
            # Add children to stack
            if debug: print ('Expand Node:', node.name, node.args)
            if node.args:
                for i, child in enumerate(node.args):
                    if (i % 2 != 0): # Odd - child
                        append(stack, child)
                        #stack.append(child)
            expanded.append(node.name)
    #sys.exit(0)
    return ans

def process_node_width(node):
    if node.args:
        calculate_width(node)
    if node.width > 0: # OK
        #print ('Node:', node.name, 'width:', node.width)
        return ''
    else:
        return 'Cannot calculate node width: ' + node.name

def process_node_height(node):
    if node.args:
        calculate_height(node)
    if node.height > 0: # OK
       return ''
    else:
        return 'Cannot calculate node height: ' + node.name


def calculate_width(container):
    # If row add up child widths
    # If column use widest child
    # If width is set, still look at children
    #print ('Calculating widths')
    #print ('Current width', container.width)
    #print (container.args)
    #print (container.name, ':', container.type)
    if container.args:
        if all_children_have_widths(container):
            if container.type == ROW:
                width = 0
                for i, child in enumerate(container.args):
                    #print (i,x)
                    if (i % 2 == 0): # Even
                        width += child # Padding
                    else: #odd
                        width += child.width
                #print ('Calculated width:', container.name,width)
                container.width = max(container.width, width)
            elif container.type == COLUMN:
                # We might only have the width of the child, not the left and right margins
                width = 0
                for i, child in enumerate(container.args):
                    if (i % 2 != 0): # Odd - child
                        width = max(width, container.left + child.width + container.right)
                container.width = max(container.width, width)
                # If container requires children to expand
                if container.vertical == EXPAND:
                    for i, child in enumerate(container.args):
                        if (i % 2 != 0): # Odd - child
                            child.width = container.width - container.left - container.right

        else: # Drill down - using traverse this should never happen
            for i, child in enumerate(container.args):
                if (i % 2 != 0): # Odd
                    calculate_width(child) # Even if already has width, maybe some children do not
    else:
        print ('-'*70)
        print ('Problem calculating widths')
        print ('-'*70)
        sys.exit(1)

def calculate_height(container):
    #print ('Calculating height')
    #print ('Current width', container.width)
    #print (container.args)
    #print (container.name)
    if container.type == ROW:
        tallest_child = 0
        for i, child in enumerate(container.args):
            #print (i,child)
            if (i % 2 != 0): #Odd
                tallest_child = max(tallest_child, container.top + child.height + container.bottom)
        #print ('Tallest child', tallest_child)
        #print ('Container Height', container.height)
        container.height = max(container.height, tallest_child)
    else:
        height = 0
        for i, x in enumerate(container.args):
            #print (i,x)
            if (i % 2 == 0): #even
                height += x
            else: #odd
                height += x.height
        #print ('Calculated height:', container.name,height)
        container.height = max(container.height, height)


def calculate_child_x_coordinates(container):
    # Make sure all children have widths
    #print ('Children x coordinates')
    if all_children_have_widths(container):
        if container.type == ROW:
            left = 0
            for i, x in enumerate(container.args):
                #print (i,x)
                if (i % 2 == 0): #Even - a gap
                    left += x
                else: # Odd a widget - child
                    x.x = left
                    left = x.x + x.width
                    #print (x.name, x.width)
        elif container.type == COLUMN:
            for i, child in enumerate(container.args):
                if (i % 2 != 0): # Odd - child
                    child.x = container.left
    else:
        print ('Error, children without widths')

def calculate_child_y_coordinates(container):
    # Make sure all children have heights
    print ('Children y coordinates', container.name)
    if all_children_have_widths(container):
        if container.type == ROW:
            top = 0
            for i, child in enumerate(container.args):
                if (i % 2 != 0): # Odd child
                    child.y = container.top
        elif container.type == COLUMN:
            top = 0 # Ignores container .top - uses args
            for i, x in enumerate(container.args):
                if (i % 2 == 0): #Even - a gap
                    top += x
                else: # Odd a widget - child
                    x.y = top
                    #print (x.name, x.y)
                    top = x.y + x.height
    else:
        print ('Error, children without heights')
    #print ('---')

def all_children_have_widths(container):
    ans = True
    for i, x in enumerate(container.args):
        if (i % 2 != 0): #Odd
            if x.width < 1:
                ans = False
    return ans

def all_children_have_heights(container):
    ans = True
    for i, x in enumerate(container.args):
        if (i % 2 != 0): #Odd
            if x.height < 1:
                ans = False
    return ans


def alignment_adjustments(node):
    # If child alignment is center, recalculate the x coordinates - ignore left/right margins
    #print ('Alignment adjustments', node.name)
    if node.args:
        if node.type == ROW:
            if node.horizontal == CENTERED: # Horizontal align all children
                #print ('Horizontal Centered')
                left = int((node.args[1].x + node.width - node.args[-2].x - node.args[-2].width) / 2)
                #print (node.args)
                #print ('Left', left)
                #print (node.args[1].x)
                adjustment = left - node.args[1].x
                #print (adjustment)
                for i, child in enumerate(node.args):
                    if (i % 2 != 0): #Odd
                        child.x += adjustment
            if node.vertical == CENTERED: # Vertical align each child
                for i, child in enumerate(node.args):
                    if (i % 2 != 0): #Odd
                        top = int((node.height - child.height) / 2)
                        child.y = top
        elif node.type == COLUMN:
            if node.horizontal == CENTERED: # Horizontal align all children
                for i, child in enumerate(node.args):
                    if (i % 2 != 0): #Odd
                        left = int((node.width - child.width) / 2)
                        child.x = left
            if node.vertical == CENTERED: # Vertical align each child
                top = int((node.args[1].y + node.height - node.args[-2].y - node.args[-2].height) / 2)
                adjustment = top - node.args[1].y
                for i, child in enumerate(node.args):
                    if (i % 2 != 0): #Odd
                        child.y += adjustment

        for child in node.children:
            alignment_adjustments(child)

