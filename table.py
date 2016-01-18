try:
    import tkinter as TK
    from tkinter.ttk import Button, Separator
except:
    import Tkinter as TK
    from ttk import Button

#from place_functions import CENTERED, Top_Window, Box, RIGHT
from constants import RIGHT
from widget import Widget

"""
Usage
        pt = PlaceTable(columns, data, view_rows=8)
        pt.create_frame(canvas, x = 10, y = 10)
The columns are column dictionaries
Data is two dimensional list - same no columns as column dicts 
canvas is the frame holding the table
"""

TABLE_CELLWIDTH = 100
TABLE_CELLHEIGHT = 20
TABLE_H_GAP = 3
TABLE_V_GAP = 3
TABLE_CELLALIGN = TK.CENTER
TABLE_COLOR = 'cornsilk' # Not visible!
TABLE_CELLCOLOR = 'dark sea green' # pink'
TABLE_TITLECOLOR = 'sea green' # 'lightblue'

class GTable(Widget):
    def __init__(self, name, columns=None, data=None, view_rows=None,
                 cellheight=TABLE_CELLHEIGHT, h_gap=TABLE_H_GAP,
                 v_gap=TABLE_V_GAP, color=TABLE_COLOR):
        Widget.__init__(self, name)
        self.color = color
        self.columns = columns
        self.data = data
        self.view_rows = view_rows
        self.v_gap = v_gap
        self.h_gap = h_gap
        self.cellheight = cellheight
        self.v_scroll = False
        if columns and data:
            if not view_rows:
                self.view_rows = len(data)
            self.v_scroll = (self.view_rows < len(data))
            self.table_dimensions()

    def create_widget(self):
        self.widget = TK.Frame(self.parent.widget)
        # Add column headings
        label_canvas = self.widget
        left = self.h_gap
        top = self.v_gap
        for col in self.columns:
            place_label(canvas=label_canvas, txt=col['text'], left=left, top=top,
                        width=col['width'], height=self.cellheight, bg=col['titlecolor'],
                        anchor=col['anchor'])
            left += col['width'] + self.h_gap
        # Add data labels, and string variables for each label
        self.cells = []
        top += self.cellheight + self.v_gap
        for i,row in enumerate(self.data): # row is a list
            if i >= self.view_rows: break
            cell_row = []
            left=self.h_gap
            s = Separator(label_canvas)
            s.place(x=0, y=top -2, relwidth=1.0)
            for j, col in enumerate(self.columns):
                value = TK.StringVar()
                value.set('{}'.format(self.data[i][j]))
                place_label(canvas=label_canvas, txt="", left=left, top=top,
                            width=col['width'], height=self.cellheight,
                            bg=col['cellcolor'], anchor=col['labelanchor'],
                            textvariable=value, name=':{}:{}'.format(i,j),
                            clicked=self._dataclick)
                cell_row.append(value)
                left += col['width'] + self.h_gap
            self.cells.append(cell_row)
            top += self.cellheight + self.v_gap
        self.top_row = 0
        # Add vertical scroll if needed
        if self.v_scroll:
            x = self.scroll_left
            y = self.scroll_top
            height = self.scroll_height
            z = len(self.data) - self.view_rows
            #vertical_scroll = TK.Scale(label_canvas.frame, orient=TK.VERTICAL,
            vertical_scroll = TK.Scale(label_canvas, orient=TK.VERTICAL,
                                from_=0, to=z, command=self.vert_scroll, showvalue=0)
            vertical_scroll.place(x=x, y=y, width=23, height=height)

    def populate_labels(self):
        for i, row  in enumerate(self.cells):
            row_no = i + self.top_row
            for j, col in enumerate(self.columns):
                var = row[j]
                var.set(self.data[row_no][j])

    def _dataclick(self, event):
        s = str(event.widget)
        d = s.split(':')
        row = d[1]
        col = d[2]
        print ('Row clicked', row)
        print ('Col clicked', col)
        self.data_clicked(int(row),int(col), self.top_row)
        
    def data_clicked(self, row, col):
        pass # This to be replaced


    def vert_scroll(self, x):
        self.top_row = int(x)
        self.populate_labels()

    def table_dimensions(self):
        top = self.v_gap
        left = self.h_gap
        no_rows = self.view_rows + 1 # Adsd column heading row
        col_widths = [c['width'] for c in self.columns]
        for col in col_widths:
            left += col + self.h_gap
        self.width = left
        for r in range(no_rows):
            top += self.cellheight + self.v_gap
        self.height = top
        if self.v_scroll:
            self.scroll_top = self.cellheight + 2 * self.v_gap
            self.scroll_height = self.height - self.scroll_top - self.v_gap
            self.scroll_left = self.width
            self.width += 23 

LABEL_FG = 'blue'
LABEL_BG = None  # Use parent background
LABEL_FONT = 'Helvetica'
LABEL_FONT_SIZE = 12
LABEL_ANCHOR = TK.E  # Right justified text
LABEL_HEIGHT = 20
LABEL_WIDTH = 100  # Maybe do not use this, but same for each label
LABEL_GAP = 10
LABEL_ALIGNMENT = RIGHT
LABEL_LEFT = TK.W

def create_column(text, width=None, state='disabled', align=TABLE_CELLALIGN,
                  cellcolor=TABLE_CELLCOLOR, titlecolor=TABLE_TITLECOLOR, labelalign = None):
    col = {}
    if not width: width = TABLE_CELLWIDTH
    if not labelalign: labelalign = align
    col['text'] = text
    col['width'] = width
    col['state'] = state
    col['anchor'] = align
    col['labelanchor'] = labelalign
    col['cellcolor'] = cellcolor
    col['titlecolor'] = titlecolor
    return col

def place_label(canvas, txt, left, top=0,
                alignment=LABEL_ALIGNMENT,
                label_gap=LABEL_GAP,
                fg=LABEL_FG,
                bg=LABEL_BG,
                font=LABEL_FONT,
                font_size=LABEL_FONT_SIZE,
                anchor=LABEL_ANCHOR,
                height=LABEL_HEIGHT,
                width=LABEL_WIDTH,
                textvariable=None,
                name='',
                clicked=None):
    if not bg:
        bg = canvas.color
    #l = TK.Label(canvas.frame, text=txt, font=(font, font_size), fg=fg,
    l = TK.Label(canvas, text=txt, font=(font, font_size), fg=fg,
                 background=bg, anchor=anchor, name=name)
    l.place(x=left, y=top, width=width, height=height)
    if clicked:
        l.bind('<Button-1>', clicked)
    if textvariable:
        l.config(textvariable=textvariable)
    return l

