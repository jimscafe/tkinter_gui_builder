# Widget classes
from basic_node import Node
import tkinter as TK
from tkinter import ttk

class Widget(Node):
    def __init__(self, name='', width = -1, height = -1):
        Node.__init__(self, name, width, height)

    def set_text(self, text):
        self.text = text
        if self.widget:
            self.widget.configure(text=self.text)

class GLabel(Widget):
    def __init__(self, name, width, height, text=''):
        Widget.__init__(self, name, width, height)
        self.text = text

    def create_widget(self, options = None):
        self.widget = TK.Label(self.parent.widget, text=self.text, background='lightgreen')

class GButton(Widget):
    def __init__(self, name, width, height, text=''):
        Widget.__init__(self, name, width, height)
        self.text = text

    def create_widget(self, options = None):
        self.widget = ttk.Button(self.parent.widget, text=self.text, command = self.command)

    def set_command(self, command):
         self.command = command
         if self.widget:
             self.widget.configure(command=self.command)
