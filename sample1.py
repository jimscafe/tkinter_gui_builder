import tkinter as TK

from widgetnode import GLabel, GButton
from containernode import GFrame_Row, GFrame_Column, HBox, VBox
from constants import WIN, HIN, VT, HL, VC, VB, HAS, HC, WEX
from build import build_gui


root = TK.Tk()

t = GLabel('Title', width=300, height=20, text = 'AMCAT')

header = GFrame_Row('Header', [t], parms=[WIN, HIN, HC, VC,[10,10], [15,15]])

b1 = GButton('Save', width=100, height=30, text='Save')
b1.set_command(root.destroy)
b2 = GButton('Cancel', width=100, height=30, text='Cancel')

footer = GFrame_Row('RowFooter',[b1, b2], height=40, parms=[WIN, HIN, HC, VC,[10,5,10], [0,0]])

main_container = HBox('main', [header,footer])

build_gui(root, main_container)

root.mainloop()