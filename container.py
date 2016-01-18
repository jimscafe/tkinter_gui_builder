import tkinter as TK
from tkinter import ttk

from constants import ROW, COLUMN, HBOX
from constants import WIN, HIN, VT, HL, VC, VB, HAS, HC, WEX, HEX

class Container():
    def __init__(self, name, children=[],width=-1,height=-1, parms=[]):
        self.width = width
        self.height = height
        self.x = -1
        self.y = -1
        self.parent = None
        self.name = name
        self.type = None
        self.children = children
        self.widget = None
        self.relief = TK.GROOVE # Default
        if parms:
            self.width_type = parms[0]
            self.child_h_padding = parms[4]
            self.height_type = parms[1]
            self.child_v_padding = parms[5]
            self.x_align = parms[2]
            self.y_align = parms[3]

    def create_widget(self, options = None):
        self.widget = TK.Frame(self.parent.widget, width=self.width, height=self.height, relief=self.relief)

class GFrame_Row(Container):
    def __init__(self, name, children, width=-1, height=-1, parms=[]):
        Container.__init__(self, name, children, width, height, parms)
        self.type = ROW


class GFrame_Column(Container):
    def __init__(self, name, children, width=-1, height=-1, parms=[]):
        Container.__init__(self, name, children, width, height, parms)
        self.type = COLUMN

class HBox(Container): # Has 2 children (also containers in column), expands children H
   def __init__(self, name, children, width=-1, height=-1):
        Container.__init__(self, name, children, width, height, parms=[WEX, HEX, HL, VC,[0,0,0], [0,0]])
        self.type = COLUMN

class VBox(Container): # Has 2 children (also containers in row), expands children V
   def __init__(self, name, children, width=-1, height=-1):
        Container.__init__(self, name, children, width, height, parms=[WEX, HEX, HL, VC,[0,0,0], [0,0]])
        self.type = ROW


def create_top_window(master, node, center=True):
    if not master:
        master = TK.Toplevel()
    if center:
        center_window(master, node.width, node.height)
    node.widget = TK.Frame(master, relief=node.relief)
    node.widget.place(x=node.x, y=node.y,width=node.width, height=node.height)


def center_window(root, w=300, h=200): # Center main application window
    # set screen width and height
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
"""
s = Style()
s.configure('My.TFrame', background='red')

mail1 = Frame(root, style='My.TFrame')
"""