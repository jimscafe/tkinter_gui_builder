# Try to impliment a different example gui

# +-------------------------------------------+
# |+-----------------------------------------+|
# ||+------------------------++-------------+||
# ||| Label Label            ||  Button     |||
# ||| Label Label            ||  Button     |||
# |||                        ||  Button     |||
# ||+------------------------++-------------+||
# |+-----------------------------------------+|
# |+-----------------------------------------+|
# ||             Exit                        ||
# |+-----------------------------------------+|
# +-------------------------------------------+

from s2_widgets import label1_1, label1_2, label2_1, label2_2, button1, button2, button3, exit_button
from container_builder import make_row, make_column
from place_functions import LEFT, CENTERED, RIGHT, EXPAND
from build import build_gui
import tkinter as TK

# Design structure
a = make_row(label1_1, label1_2, name='LabelRow1', alignment=(CENTERED, CENTERED), padding=(5,5,5), height=40)
b = make_row(label2_1, label2_2, name='LabelRow2', alignment=(CENTERED, CENTERED), padding=(5,5,5), height=40)
c = make_column(a,b, name='LabelRows')

d = make_column(button1, button2, button3, name='ButtonColumn', alignment=(CENTERED, CENTERED), padding=(5,5,5,5), width=120)
e = make_row(c,d, name='e', alignment=(CENTERED, CENTERED))

f = make_row(exit_button, name='f', alignment=(CENTERED, CENTERED), padding=(50,50), height=30)
g = make_column(e,f, name='g', alignment=(CENTERED, CENTERED))

# Or is this better?

"""
x = col
           row    col                       col
                      row label1, label2        Button 1
                      row label3, label4        Button2
                                                Button3
           row   exit
"""

root = TK.Tk()
build_gui(root, g)
exit_button.set_command(root.destroy)

root.mainloop()
