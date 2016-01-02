import tkinter as TK
from tkinter import ttk

class WG():
    def __init__(self):
        self.parent = None
        self.inner_margins = (0,0,0,0)
        self.outer_margins = (0,0,0,0)
        self.widget = None
        self.widgettype = 'Label'
        self.packed = False
        self.text = None
        self.command = None
        self.anchor = TK.W # Default
        self.x = -1
        self.y = -1
        self.args = []

    def create_widget(self, options = None):
        if self.widgettype == 'Label':
            self.widget = ttk.Label(self.parent.widget, text=self.text, background='lightgreen', anchor=self.anchor)
        elif self.widgettype == 'Button':
            self.widget = ttk.Button(self.parent.widget, text=self.text, command = self.command)

    def set_text(self, text):
        self.text = text
        if self.widget:
            self.widget.configure(text=self.text)

    def set_command(self, command):
        if self.widgettype == 'Button':
             self.command = command
             if self.widget:
                 self.widget.configure(command=self.command)

title = WG()
title.width = 100
title.height = 20
title.name = 'Title'
title.id = 'title'
title.text = 'Problem' #'Problem Resolution'
title.anchor = TK.CENTER

description = WG()
description.width = 100
description.height = 30
description.name = 'Description'
description.id = 'description'
description.anchor = TK.W
description.text = 'Missing MSG File'

solution = WG()
solution.width = 100
solution.height = 30
solution.name = 'Solution'
solution.id = 'solution'
solution.anchor = TK.W
solution.text = 'Create New'

solve = WG()
solve.width = 100
solve.height = 30
solve.name = 'Solve'
solve.id = 'solve'
solve.text = 'Fix Problem'
solve.widgettype = 'Button'

exit_button = WG()
exit_button.width = 100
exit_button.height = 30
exit_button.name = 'Quit'
exit_button.id = 'quit'
exit_button.text = 'Quit'
exit_button.widgettype = 'Button'