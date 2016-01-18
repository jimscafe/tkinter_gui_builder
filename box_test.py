

from constants import WIN, HIN, VT, HL, VC, VB, HAS, HC, WEX
from container import GFrame_Row, GFrame_Column, HBox, VBox
from build import build_gui
import tkinter as TK

con1 = GFrame_Row('Row1', [], width = 100, height = 40, parms=[WIN, HIN, HL, VC,[], []])
con2 = GFrame_Row('Row2', [], width = 150,  height=30, parms=[WIN, HAS, HL, VC,[], []])
#con3 = GFrame_Column('Column1', [con1, con2], parms=[WIN, HIN, HL, VC,[0,0,0], [0,0]])
con3 = HBox('Box1', [con1, con2])
#con3 = VBox('Box1', [con1, con2])
#con3 = HBox('Box1', [con1, con2], width=200, height = 100)
#con3 = VBox('Box1', [con1, con2], width=200, height = 100)


root = TK.Tk()

g = con3
build_gui(root, g)
con1.widget.config(bg="red")
con2.widget.config(bg="blue")
con3.widget.config(bg="green")

root.mainloop()