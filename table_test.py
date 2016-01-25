
from sample_widgets import label1, label2, label3, label4, button1, button2, button3, exit_button
from constants import WIN, HIN, VT, HL, VC, VB, HAS, HC, WEX
from containernode import GFrame_Row, GFrame_Column, HBox, VBox
from tablenode import GTable
from sample_table import SampleTable
from build import build_gui
import tkinter as TK

tb = SampleTable()
con1 = VBox('Box1', [tb])
con2 = GFrame_Row('Row4',[exit_button], height=40, parms=[WIN, HIN, HC, VC,[0,0,0], [0,0]])
con3 = HBox('Box2', [con1, con2])

root = TK.Tk()

g = con3
build_gui(root, g)
exit_button.set_command(root.destroy)

root.mainloop()
