import tkinter as TK
from tkinter import ttk

CENTERED = 'centered'
LEFT = 'left'
RIGHT = 'right'
TOP = 'top'
BOTTOM = 'bottom'

EXPAND = 'expand'
ROW = 'row'
COLUMN = 'column'

# ------------------------------------------------------------------------------

class Box():
    def __init__(self, parent, horizontal,vertical , color):
        # Calculate horizontal parameters left and width
        self.left, self.width = set_horizontal(horizontal)
        self.top, self.height = set_vertical(vertical)
        print ('Box')
        print (self.left, self.width)
        print (self.top, self.height)
        self.right = self.left + self.width
        self.bottom = self.top + self.height
        self.parent = parent
        self.color = color
        self.frame = TK.Frame(parent.frame, width=self.width, height=self.height, background=color)
        self.frame.place(x=self.left, y=self.top)

# ------------------------------------------------------------------------------

class PlaceWidget():
    def __init__(self, widget, horizontal, vertical):
        self.widget = widget
        self.left, self.width = set_horizontal(horizontal)
        self.top, self.height = set_vertical(vertical)
        print ('Widget')
        print (self.left, self.width)
        print (self.top, self.height)
        self.widget.place(x=self.left, y=self.top,width=self.width, height=self.height)
        self.right = self.left + self.width
        self.bottom = self.top + self.height

# ------------------------------------------------------------------------------
#  Calcuating posdition functions
# ------------------------------------------------------------------------------
def set_horizontal(horizontal):
    if horizontal[0] == 'left-gap-expand-gap-right':
        left = int(horizontal[1]) + int(horizontal[2])
        width = int( horizontal[4]) - left - int(horizontal[3])
    if horizontal[0] == 'left-gap-width':
        left = int(horizontal[1]) + int(horizontal[2])
        width = int(horizontal[3])
    if horizontal[0] == 'right-gap-width':
        left = int(horizontal[1]) - int(horizontal[2]) - int(horizontal[3])
        width = int(horizontal[3])
    if horizontal[0] == 'left-center-width-right':
        gap =  (int(horizontal[3]) - int(horizontal[1]) - int(horizontal[2])) / 2
        left = int(horizontal[1]) + int(gap)
        width = int(horizontal[3]) - int(horizontal[1]) - 2 * gap
    return left, width

def set_vertical(vertical):
    if vertical[0] == 'top-gap-height':
        top = int(vertical[1]) + int(vertical[2])
        height = int(vertical[3])
    if vertical[0] == 'bottom-gap-height':
        top = int(vertical[1]) - int(vertical[2]) - int(vertical[3])
        height = int(vertical[3])
    if vertical[0] == 'top-gap-expand-gap-bottom':
        top = int(vertical[1]) + int(vertical[2])
        height = int(vertical[4]) - int(vertical[3]) - top
    if vertical[0] == 'top-center-height-bottom':
        gap =  (int(vertical[3]) - int(vertical[1]) - int(vertical[2])) / 2
        top = int(vertical[1]) + int(gap)
        height = int(vertical[3]) - int(vertical[1]) - 2 * gap
    return top, height

# ------------------------------------------------------------------------------
# Main window - new top window
# ------------------------------------------------------------------------------


class Top_Window():
    def __init__(self, root, position, width, height, background="#fffff0", quit_button=False):
        if root:
            self.frame = root
        else:
            self.frame = TK.Tk()
        if position == CENTERED:
            self.center_window( width, height)
        self.left = 0
        self.width = width
        self.right = self.left + self.width
        self.top = 0
        self.height = height
        self.bottom = self.top + self.height
        self.color = background
        self.frame.config(background=background)
        if quit_button:
            quit_button = PlaceWidget(ttk.Button(self.frame, text='Quit', command = self.frame.destroy),
                                            horizontal= ('right-gap-width', self.width, '10', '100'),
                                            vertical  = ('bottom-gap-height', self.height, '10','30'))

    def center_window(self, w=300, h=200):
        # get screen width and height
        ws = self.frame.winfo_screenwidth()
        hs = self.frame.winfo_screenheight()
        # calculate position x, y
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.frame.geometry('%dx%d+%d+%d' % (w, h, x, y))
