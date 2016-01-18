# Base widget classes
import tkinter as TK
from tkinter import ttk


class Widget():
    def __init__(self, name='', width = -1, height = -1):
        self.name = name
        self.parent = None
        self.widget = None
        self.text = None
        self.command = None
        self.x = -1
        self.y = -1
        self.width = width
        self.height = height
        self.children = []

    def set_text(self, text):
        self.text = text
        if self.widget:
            self.widget.configure(text=self.text)

class GLabel(Widget):
    def __init__(self, name, width, height, text=''):
        Widget.__init__(self, name, width, height)
        self.text = text

    def create_widget(self, options = None):
        #print (self.parent.widget.winfo_class())
        #self.widget = ttk.Label(self.parent.widget, text=self.text, background='lightgreen')
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
