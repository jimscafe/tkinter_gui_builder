# What is the simplest way to set up a gui window?

# Import the objects, widgets and containers

# Top row label centered width
# Middle row two labels + button, width, gaps, centered
# Bottom row two labels, width, gap, centered
# Heights and vertical gaps required

# Rows calculated width, largest all other rows expanded
# 

from ns_widgets import title, description, solution, solve, exit_button
from ns_containers import outercontainer, toprow, middlerow, bottomrow
from place_functions import LEFT, CENTERED, RIGHT, EXPAND
from build import build_gui
import tkinter as TK

outercontainer.add_column(0,toprow,0, middlerow,0, bottomrow,0, EXPAND)
toprow.add_row(30,title,30, CENTERED, vertical=CENTERED)
middlerow.add_row(10,description, 10, solution, 10, solve, 40, LEFT, vertical=CENTERED)
bottomrow.add_row(0, exit_button, 0, CENTERED, vertical=CENTERED)

root = TK.Tk()

description.set_text('File deleted')
solution.set_text('Create new file')
exit_button.set_command(root.destroy)


build_gui(root, outercontainer)
#build_gui(root, toprow)
#build_gui(root, middlerow)

root.mainloop()