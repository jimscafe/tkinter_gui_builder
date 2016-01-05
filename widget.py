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
