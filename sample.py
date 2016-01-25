# Sample using new coordinate and dimension library

# Recreate the libraries as needed
# See s2_sample.py

from constants import WIN, HIN, VT, HL, VC, VB, HAS, HC, WEX
from containernode import GFrame_Row, GFrame_Column, HBox, VBox
from build import build_gui
import tkinter as TK

from sample_widgets import label1, label2, label3, label4, button1, button2, button3, exit_button

def tick():
    print (root.geometry())
    root.after(500, tick) # Constantly loop through this code

def resize_test():
    # See what happens when the app width is changed and build called again
    con8.width += 40
    build_gui(root, con8)

con1 = GFrame_Row('Row1', [label1, label2], height = 40, parms=[WIN, HIN, HL, VC,[5,5,5], [0,0]])
con1.configure(background='lightblue')
con2 = GFrame_Row('Row2', [label3, label4], height=40, parms=[WIN, HAS, HL, VC,[5,5,5], [0,0]])
con2.configure(background='lightgrey')
#con3 = GFrame_Column('Column1', [con1, con2], parms=[WIN, HIN, HL, VC,[0,0,0], [0,0]])

con3 = HBox('Con3', [con1,con2])
con3.configure(background='grey')

con4 = GFrame_Column('Column2', [button1, button2, button3], width=150, parms=[WIN, HIN, HC, VC,[0,0], [5,5,5]])
con4.configure(background='grey')
#con5 = GFrame_Row('Row3', [con3, con4], parms=[WIN, HIN, HL, VC,[0,0,0], [0,0]])
con5 = VBox('Con5',[con3, con4])
con5.configure(background='lightgreen')

con6 = GFrame_Row('Row4',[exit_button], height=40, parms=[WIN, HIN, HC, VC,[0,0,0], [0,0]])
con6.configure(background='green')
con7 = GFrame_Column('Column3',[con5, con6], parms=[WEX, HIN, HL, VC,[0,0,0], [0,0]]) # Expand frames con5 and con6 to fit con7 width
con7.configure(background='pink')
con8 = HBox('Con7', [con5,con6])
con8.configure(background='yellow')

def resize(event):
    print ('Resize')
    print("The new dimensions are:",event.width,"x",event.height)
    print (root.geometry())



root = TK.Tk()
#root.bind("<Configure>", resize)
g = con8
build_gui(root, g)
exit_button.set_command(root.destroy)
button1.configure(text='Resize')
button1.set_command(resize_test)
#tick()
root.mainloop()

