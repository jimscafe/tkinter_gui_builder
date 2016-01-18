
from gui_lib import traverse_tree, process_node_width, process_node_height, assign_parent, calculate_x, calculate_y
from gui_lib import create_widgets
from container import create_top_window
from debug_lib import print_node

import sys

def build_gui(master, top):
    print ('-'*70)
    traverse_tree(top, print_node)
    print ('-'*70)
    error = traverse_tree(top, process_node_width)
    if error:
        print (error)
        sys.exit(1)
    traverse_tree(top, process_node_width, top_down=True) # For expanding containers inside expanding containers
    traverse_tree(top, print_node)
    error = traverse_tree(top, process_node_height)
    if error:
        print (error)
        sys.exit(1)
    traverse_tree(top, process_node_height, top_down = True)
    print ('-'*70)
    traverse_tree(top, assign_parent, top_down = True)
    traverse_tree(top, print_node)
    traverse_tree(top,calculate_x)
    print ('-'*70)
    traverse_tree(top, print_node)
    traverse_tree(top,calculate_y)
    print ('-'*70)
    top.x = 0
    top.y = 0
    traverse_tree(top, print_node)
    create_top_window(master, top)
    traverse_tree(top, create_widgets, top_down=True)
    print ('-'*70)
    traverse_tree(top, print_node, top_down=True)
    print ('-'*70)
