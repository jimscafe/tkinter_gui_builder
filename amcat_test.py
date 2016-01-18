
from sample_widgets import exit_button
from constants import WIN, HIN, VT, HL, VC, VB, HAS, HC, WEX
from container import GFrame_Row, GFrame_Column, HBox, VBox
from table import GTable
from sample_table import SampleTable, crc_table
from build import build_gui
import tkinter as TK
from tkinter import ttk
from pymongo import MongoClient
from widget import GLabel, GButton

mongo = MongoClient('localhost', 27017 )
db = mongo.Production
jobs = db.Jobs
job_recs = jobs.find({"company":'MTC', "customer":'CRC'})
x = list(job_recs)
x = sorted(x, key = lambda y: y['received'], reverse=True)
#print (x)
print ('-')
print (x[0])

title = GLabel('Title', width=300, height=20)
title.set_text('Latest CRC Jobs')


header = GFrame_Row('Header', [title], height = 40, parms=[WIN, HIN, HC, VC,[0,0,0], [0,0]])

tb = crc_table(x)
con1 = VBox('Box1', [tb])
con2 = GFrame_Row('Row4',[exit_button], height=40, parms=[WIN, HIN, HC, VC,[0,0,0], [0,0]])
con3 = HBox('Box2', [header,con1, con2])

root = TK.Tk()

g = con3
build_gui(root, g)
exit_button.set_command(root.destroy)
title.widget.configure(foreground="black", font='arial 14 bold', background='white')

#print ('-')
#print (x[0])

#for key in x[0]:
#    print (key)
#y = sorted(x, key = lambda y: y['received'], reverse=True)
#print ('-')
#print (y[0])

root.mainloop()
