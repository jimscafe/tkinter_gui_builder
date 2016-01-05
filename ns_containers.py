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
        self.widget = None # Override this if necessary
        self.widgettype = CONTAINER
        self.name = name
        self.type = None
        self.horizontal = None
        self.vertical = None
        self.children = []
        self.packed = False
        self.widget = widget
        self.relief = TK.GROOVE # Default
        self.inner_margins = (0,0,0,0)
        self.outer_margins = (0,0,0,0)
        # Margins for container
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


outercontainer = CT('Outer')

toprow = CT('TopRow')
toprow.height = 40

middlerow = CT('MiddleRow')
middlerow.height=60

bottomrow = CT('BottomRow')
bottomrow.height=60
