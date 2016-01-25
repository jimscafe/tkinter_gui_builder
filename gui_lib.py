# traverse_tree(root, process, top_down=False, debug=False):
# Used as parameter to traverse_tree
#    create_widgets
#    process_node_width
#    process_node_height
#    calculate_x
#    calculate_y
#    assign_parent

from constants import ROW, COLUMN, WAS, WIN, WEX, HAS, HIN, HEX, HL, HC, HR, VT, VC, VB

import tkinter as TK
import sys

def create_widgets(node):
    if node.parent:
        if not node.widget:
            node.create_widget()
        #print (node.name)
        node.widget.place(x=node.x, y=node.y,width=node.width, height=node.height)
    return ''

def process_node_width(node):
    if node.children:
        set_container_child_widths(node)
    if node.width > 0: # OK
        #print ('Node:', node.name, 'width:', node.width)
        return ''
    else:
        return 'Cannot calculate node width: ' + node.name

def process_node_height(node):
    if node.children:
        set_container_child_heights(node)
    if node.height > 0: # OK
       return ''
    else:
        return 'Cannot calculate node height: ' + node.na
        
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
            if debug: print ('Expand Node:', node.name, node.children)
            if node.children:
                for child in node.children:
                    append(stack, child)
                        #stack.append(child)
            expanded.append(node.name)
    return ans

# ----------------------------------------------------------------------------------------------------------------------
# Widths
# ----------------------------------------------------------------------------------------------------------------------
def set_container_child_widths(node):
    if node.children:
        if node.type == ROW:
            # WIS requires no adjustment
            if node.width_type == WAS:
                # Children widths all set the same (largest)
                children_same_width(node)
            if node.width_type in (WAS, WIN, WEX):
                node.width = max(node.width, total_row_width(node.children, node.child_h_padding))
            else:
                print ('Not implemented', node.width_type)
                sys.exit(1)
            if node.height_type ==  WEX:
                total_child_width = 0
                for child in node.children:
                    total_child_width += child.width
                if total_child_width:
                    for child in node.children:
                        child.width = int(child.width * node.width / total_child_width)

        elif node.type == COLUMN:
            if node.width_type == WIN:
                # Calculate widest label + gaps
                width = largest_child_width_with_gaps(node)
                #for child in node.children:
                #    width = max(width, node.child_h_padding[0] + child.width + node.child_h_padding[1])
                #print (width)
                node.width = max(node.width, width)
            elif node.width_type == WAS:
                children_same_width(node)
                node.width = max(node.width,  node.child_h_padding[0] + node.children[0].width + node.child_h_padding[1])
            elif node.width_type == WEX:
                for child in node.children:
                    node.width = max(node.width, child.width)
                for child in node.children:
                    child.width = node.width
            else:
                print ('Not implemented', node.type, node.width_type)
                sys.exit(1)
        else:
            print ('Node.type not implemented', node.type)
            sys.exit(1)

def total_row_width(children, padding=[0,0]):
    i = 0
    width = padding[i]
    for child in children:
        i += 1
        width += child.width + padding[i]
        padding.append(0)
    return width

def children_same_width(node):
    width = 0
    for child in node.children:
        width = max(width, child.width)
    for child in node.children:
        child.width = width

def largest_child_width_with_gaps(node):
    width = 0
    for child in node.children:
        width = max(width, node.child_h_padding[0] + child.width + node.child_h_padding[1])
    return width

# ----------------------------------------------------------------------------------------------------------------------
# Heights
# ----------------------------------------------------------------------------------------------------------------------
def set_container_child_heights(node):
    if node.children:
        if node.type == COLUMN:
            if node.height_type == HAS:
                # Children widths all set the same (largest)
                children_same_heights(node)
            if node.height_type in (HAS, HIN, HEX):
                node.height = max(node.height, total_row_height(node.children, node.child_v_padding))
            else:
                print ('Not implemented',node.type, node.height_type)
                sys.exit(1)
            if node.height_type ==  HEX:
                total_child_height = 0
                for child in node.children:
                    total_child_height += child.height
                if total_child_height:
                    for child in node.children:
                        child.height = int(child.height * node.height / total_child_height)
        elif node.type == ROW:
            if node.height_type == HIN:
                height = largest_child_height_with_gaps(node)
                node.height = max(node.height, height)
            elif node.height_type == HAS:
                children_same_heights(node)
                node.height = max(node.height,  node.child_v_padding[0] + node.children[0].height + node.child_v_padding[1])
            elif node.height_type == HEX:
                for child in node.children:
                    node.height = max(node.height, child.height)
                for child in node.children:
                    child.height = node.height
            else:
                print ('Not implemented',node.type, node.height_type)
                sys.exit(1)
        else:
            print ('Not implemented', node.type, node.height_type)
            sys.exit(1)

def total_row_height(children, padding=[0, 0]):
    i = 0
    height = padding[i]
    for child in children:
        i += 1
        height += child.height + padding[i]
        padding.append(0)
    return height

def children_same_heights(node):
    height = 0
    for child in node.children:
        height = max(height, child.height)
    for child in node.children:
        child.height = height

def largest_child_height_with_gaps(node):
    height = 0
    for child in node.children:
        height = max(height, node.child_v_padding[0] + child.height + node.child_v_padding[1])
    return height

#-----------------------------------------------------------------------------------------------------------------------
# x co-ordinates
#-----------------------------------------------------------------------------------------------------------------------
def calculate_x(node):
    # Calculate x corodinate of node children
    #print (node.child_h_padding)
    if node.children:
        if all_children_have_widths(node):
            if node.type == ROW:
                if node.x_align in [HL, HC, HR]:
                    # Use the padding to set x coordinates
                    i = 0
                    left = node.child_h_padding[0]
                    for child in node.children:
                        child.x = left
                        node.child_h_padding.append(0) # make sure there are enough
                        i += 1
                        left += child.width + node.child_h_padding[i]
                else:
                    print ('Node.x_align not implemented', node.type, node.x_align)
                    sys.exit(1)
                if node.x_align == HC: # Adjust x coordinate if centered
                    #print ('Horizontal Centered')
                    #print (node.name)
                    left = int((node.children[0].x + node.width - node.children[-1].x - node.children[-1].width) / 2)
                    #print ('Left', left)
                    #print ('Node width', node.width)
                    #print (node.children[-1].x)
                    #print (node.children[-1].width)
                    adjustment = left - node.children[0].x
                    for child in node.children:
                        child.x += adjustment
                if node.x_align == HR: # Adjust x coordinate if right justified
                    # Important if container width set
                    left_total_width = total_row_width(node.children, node.child_h_padding)
                    adjustment = node.width - left_total_width - node.children[0].x
                    for child in node.children:
                        child.x += adjustment
            elif node.type == COLUMN:
                if node.width_type == WEX: # Expand,  all x is 0
                    for child in node.children:
                        child.x = 0
                elif node.x_align == HL: # Each child has y coordinate of padding[0]
                    for child in node.children:
                        child.x = node.child_h_padding[0]
                elif node.x_align == HC:
                    for child in node.children:
                        child.x = int((node.width - child.width)/2)
                elif node.x_align == HR:
                    for child in node.children:
                        child.x = node.width - child.width - node.child_h_padding[1]
                else:
                    print ('Node.x_align not implemented', node.type, node.x_align)
                    sys.exit(1)
            else:
                print ('Node.type not implemented(x)', node.type)
                sys.exit(1)

#-----------------------------------------------------------------------------------------------------------------------
# y co-ordinates
#-----------------------------------------------------------------------------------------------------------------------
def calculate_y(node):
    # Calculate x corodinate of node children
    #print (node.child_h_padding)
    if node.children:
        if all_children_have_heights(node):
            if node.type == ROW:
                if node.height_type == HEX: # Expand all y is 0
                    for child in node.children:
                        child.y = 0
                elif node.y_align == VT: # Each child has y coordinate of padding[0]
                    for child in node.children:
                        child.y = node.child_v_padding[0]
                elif node.y_align == VC:
                    for child in node.children:
                        child.y = int((node.height - child.height)/2)
                elif node.y_align == VB:
                    for child in node.children:
                        child.y = node.height - child.height - node.child_v_padding[1]
                else:
                    print ('Node aligntype not implemented', node.type, node.y_align)
                    sys.exit(1)
            elif node.type == COLUMN:
                if node.y_align in [VT, VC, VB]: #, HC, HR]:
                    # Use the padding to set y coordinates
                    i = 0
                    top = node.child_v_padding[0]
                    for child in node.children:
                        child.y = top
                        node.child_v_padding.append(0) # make sure there are enough
                        i += 1
                        top += child.height + node.child_v_padding[i]
                else:
                    print ('Node.x_align not implemented', node.type, node.x_align)
                    sys.exit(1)
                if node.y_align == VC: # Adjust y coordinate if centered
                    top = int((node.children[0].y + node.height - node.children[-1].y - node.children[-1].height) / 2)
                    adjustment = top - node.children[0].y
                    for child in node.children:
                        child.y += adjustment
                if node.y_align == VB: # Adjust x coordinate if right justified
                    # Important if container width set
                    total_height = total_row_height(node.children, node.child_h_padding)
                    print (total_height)
                    adjustment = node.height - total_height - node.children[0].y
                    for child in node.children:
                        child.y += adjustment
            else:
                print ('Node.type not implemented(y)', node.type)
                sys.exit(1)

def all_children_have_widths(node):
    ans = True
    for child in node.children:
        if child.width < 1:
                ans = False
    return ans

def all_children_have_heights(node):
    ans = True
    for child in node.children:
        if child.height < 1:
                ans = False
    return ans

# ----------------------------------------------------------------------------------------------------------------------
def assign_parent(node):
    if node.children:
        #print ('Parent', node.name)
        for child in node.children:
            #print ('..Child', child.name)
            child.parent = node
    return ''
