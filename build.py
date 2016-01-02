
import place_functions as pf
from calc_libs import calculate_child_x_coordinates, alignment_adjustments,\
                      calculate_child_y_coordinates, traverse_tree, process_node_width, process_node_height
from ns_containers import CONTAINER
import tkinter as TK
from tkinter import ttk

def build_gui(master, top):
    # Make containers frames
    # Calculate widths
    # Calculate heights
    # Get x,y of widgets and frames
    #master.geometry('{}x{}'.format(400, 200))
    #print ('Top', top.name, top.type, top.horizontal, top.vertical)
    #print (top.args)
    # We need to calculate widths, heights first
    print ('-'*70)
    traverse_tree(top, print_node)
    print ('-'*70)
    error = traverse_tree(top, process_node_width)
    if error: print (error)
    error = traverse_tree(top, process_node_height)
    if error: print (error)
    traverse_tree(top, assign_parent)
    main = pf.Top_Window(master , pf.CENTERED, width=top.width, height=top.height, background='slategray')
    top.widget = main.frame
    top.x = 0
    top.y = 0
    print ('Root node:' ,top.name, top.x, top.y, top.width, top.height)
    print ('-'*70)
    traverse_tree(top, print_node)
    traverse_tree(top, calculate_coordinates, top_down=True)
    traverse_tree(top, create_widgets, top_down=True)
    print ('-'*70)
    traverse_tree(top, print_node, top_down=True)
    print ('-'*70)
    return

def create_widgets(node):
    if node.parent:
        node.create_widget()
        node.widget.place(x=node.x, y=node.y,width=node.width, height=node.height)
    return ''

def calculate_coordinates(node):
    # Calculate the x and y co-ordinates of the node
    if node.args:
        calculate_child_x_coordinates(node)
        calculate_child_y_coordinates(node)
        alignment_adjustments(node)
    return ''


def print_node(obj):
    if obj.parent:
        parent = obj.parent.name
    else:
        parent = 'None'
    print ('{:12} ({:12}) width={:4}: height={:4} : x={:4} : y={:4}'.format(obj.name, parent, obj.width, obj.height, obj.x, obj.y))
    return '' # No error

def align(node):
    alignment_adjustments(node)
    return ''

def conf_place(node):
    node.place_configure(x=node.x, y=node.y)

def assign_parent(node):
    if node.args:
        for i, child in enumerate(node.args):
            if (i % 2 != 0): #Odd
                child.parent = node
    return ''
    """
    colors = ['pink','lightblue','green']
    calculate_child_x_coordinates(top)
    calculate_child_y_coordinates(top)
    for i, child in enumerate(top.args):
        if (i % 2 != 0): #Odd
            #calculate_child_x_coordinates(top)
            #calculate_child_y_coordinates(top)
            if child.widgettype == CONTAINER:
                #print (child.name, child.x, child.y, child.width, child.height)
                # Would like to use child.create_widget()
                child.create_widget()
                #child.widget = TK.Frame(main.frame, width=child.width, height=child.height, background=colors[-1])
                colors.pop()
                child.widget.place_configure(x=child.x, y=child.y)
                # Assume children are labels!!
                calculate_child_x_coordinates(child)
                calculate_child_y_coordinates(child)
                for i, grandchild in enumerate(child.args):
                    if (i % 2 != 0): #Odd
                        #calculate_child_x_coordinates(child)
                        #calculate_child_y_coordinates(child)
                        l = TK.Label(child.widget, text=grandchild.text, fg='blue', background='red', anchor=grandchild.anchor)
                        l.place(x=grandchild.x, y=grandchild.y,width=grandchild.width, height=grandchild.height)
                        alignment_adjustments(child)
                        l.place_configure(x=grandchild.x, y=grandchild.y)
    """
