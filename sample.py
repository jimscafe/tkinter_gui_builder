# Sample using new coordinate and dimension library

# Recreate the libraries as needed
# See s2_sample.py

from constants import WIN, HIN, VT, HL, VC, VB, HAS, HC, WEX
from container import GFrame_Row, GFrame_Column, HBox, VBox
from build import build_gui
import tkinter as TK

from sample_widgets import label1, label2, label3, label4, button1, button2, button3, exit_button


con1 = GFrame_Row('Row1', [label1, label2], height = 40, parms=[WIN, HIN, HL, VC,[5,5,5], [0,0]])
con2 = GFrame_Row('Row2', [label3, label4], height=40, parms=[WIN, HAS, HL, VC,[5,5,5], [0,0]])
#con3 = GFrame_Column('Column1', [con1, con2], parms=[WIN, HIN, HL, VC,[0,0,0], [0,0]])

con3 = HBox('Con3', [con1,con2])

con4 = GFrame_Column('Column2', [button1, button2, button3], width=150, parms=[WIN, HIN, HC, VC,[0,0], [5,5,5]])
#con5 = GFrame_Row('Row3', [con3, con4], parms=[WIN, HIN, HL, VC,[0,0,0], [0,0]])
con5 = VBox('Con5',[con3, con4])

con6 = GFrame_Row('Row4',[exit_button], height=40, parms=[WIN, HIN, HC, VC,[0,0,0], [0,0]])
con7 = GFrame_Column('Column3',[con5, con6], parms=[WEX, HIN, HL, VC,[0,0,0], [0,0]]) # Expand frames con5 and con6 to fit con7 width
con7 = HBox('Con7', [con5,con6])


root = TK.Tk()

g = con7
build_gui(root, g)
exit_button.set_command(root.destroy)

root.mainloop()
