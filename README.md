# tkinter_gui_builder
Easily Create Simple Gui Screens (Currently using tkinter)

# Gui Builder

## Create Gui objects in Nodes for a Tree

Trying to make creating a simple gui very quick and easy to understand in terms of containers and widgets.

It is important that the code in some way resemble the screen for easy recognition of gui structure. The main code should be easy to read.

Initially the containers are frames, but 'virtual boxes' will be added that are not a gui widget.

Very early stage of development, playing with ideas.

Run new_start.py
(Python 3.5)

The file ns_widgets.py is mainly for defining the labels, buttons etc.
The file ns_containers.py is for defining frames (later boxes)

These three files are the only ones required to be created to have a simple application.

The file build.py creates the gui
         calc_libs.py calculates heights widths, x and y co-ordinates, takes care of alignment and expanded containers.
         place_functions.py is from a different approach but am using the TopWindow class.

I prefer code to be easy to understand rather than efficient, hence the tree traversal code. I have avoided using recursion for the same reason and also for the easier ability to exit at a known point. Recursion was used in earlier attempts.

example (from new_start.py)

~~~
outercontainer.add_column(0,toprow,0, middlerow,0, bottomrow,0, EXPAND)
toprow.add_row(30,title,30, CENTERED, vertical=CENTERED)
~~~

The outer container is a column of frames (containers), hence the code
0,toprow,0, middlerow,0, bottomrow,0, EXPAND
means there are three containers each with zero padding and their widths (because it is a colmn) will be expanded to all have the same width. So the code 30,title,30, CENTERED, vertical=CENTERED for the toprow frame. its child (a label) will be centered, and vertically centered. The padding (30) will be ignored if this row is not the widest as the frame will be expanded.

I hope this all makes sense...