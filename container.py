from place_functions import ROW, COLUMN, CENTERED, TOP, BOTTOM
from tkinter import ttk
import tkinter as TK

CONTAINER = 'container'

class CT():
    def __init__(self, name, widget=None):
        self.width = -1
        self.height = -1
        self.x = -1
        self.y = -1
        self.parent = None
        self.widgettype = CONTAINER
        self.name = name
        self.type = None
        self.horizontal = None
        self.vertical = None
        self.children = []
        self.widget = widget
        self.relief = TK.GROOVE # Default
        # Internal Margins for container
        self.left=0
        self.right=0
        self.top=0
        self.bottom = 0

    def add_row(self, *args, **kwargs):
        self.type = ROW
        self.horizontal = args[-1]
        self.args = args[:-1]
        #print (args)
        # Default vertical to CENTERED
        self.vertical = kwargs.get('vertical',CENTERED)
        #print (kwargs)

    def add_column(self, *args, **kwargs):
        self.type = COLUMN
        self.vertical = args[-1]
        self.args = args[:-1]
        self.horizontal = kwargs.get('horizontal',CENTERED)
        #print (args)

    def create_widget(self, options = None):
        self.widget = ttk.Frame(self.parent.widget, width=self.width, height=self.height, relief=self.relief)

# ----------------------------------------------------------------------------------------
# Layout options for container children
# ----------------------------------------------------------------------------------------
"""
COLUMN                                                      +----------------+
Vertical:    Top, Centered, Bottom  (All children)          |                |  VT,VC,VB 
Horizontal   Left, Centered, Right  (All children)          |  +--------+    |  HL,HC,HR
Width        All children the same                          |  |        |    |  WAS 
             Expand all children to width of container      |  +--------+    |  WEX
             Individual                                     |                |  WIN
Height       All same                                       |  +--------+    |  HAS
             Individual                                     |  |        |    |  HIN
                                                            |  +--------+    |
                                                            |                |
                                                            +----------------+

ROW
Vertical:    Top, Centered, Bottom  +-----------------------------------+
Horizontal   Left, Centered, Right  |                                   |
Width        All same               |   +----------+  +------------+    |
             Individual             |   |          |  |            |    |
Height       All same               |   +----------+  +------------+    |
             Expand                 |                                   |       HEX
             Individual             +-----------------------------------+
"""
# ----------------------------------------------------------------------------------------








