# Control reports for amcat

# Show latest jobs and buttons for due jobs at different stages - separate windows
from pymongo import MongoClient
from widgetnode import GLabel, GButton
from containernode import GFrame_Row, GFrame_Column, HBox, VBox
from constants import WIN, HIN, VT, HL, VC, VB, HAS, HC, WEX
from build import build_gui
from current_delivery import current_delivery
from tablenode import GTable, create_column, LABEL_LEFT
import tkinter as TK
from tkinter import messagebox
from crc_lib import get_crc_all_jobs

class Main():
    def __init__(self):
        # Initialise database
        self.children = {}
        alljobs = get_crc_all_jobs()
        self.job_recs = alljobs
        self.root = TK.Tk()

        title = GLabel('Title', width=300, height=20, text = 'AMCAT')
        header = GFrame_Row('Header', [title], height = 40, parms=[WIN, HIN, HC, VC,[0,0,0], [0,0]])
        tb = crc_newjobstable(self.job_recs)
        newjobs = HBox('Box1', [tb])
        # Add buttons on the left
        duedatetitle = GLabel('DueDateTitle', width=100, height=30, text = 'Due Dates')
        self.ced_button = GButton('CED', width=100, height=30, text='CED')
        self.ced_button.set_command(lambda: self.create_stage('ced'))
        b2 = GButton('Initial', width=100, height=30, text='Initial')
        b2.set_command(lambda: self.create_stage('initial'))
        b3 = GButton('2ndPages', width=100, height=30, text='2nd Pages')
        b3.set_command(lambda: self.create_stage('2ndpages'))
        b4 = GButton('FinalPages', width=100, height=30, text='Final Pages')
        b4.set_command(lambda: self.create_stage('finalpages'))
        duedatebuttons = GFrame_Column('DueDateButtons',[duedatetitle,self.ced_button, b2,b3,b4], width = 140, parms=[WIN, HIN, HC, VC,[0,0,0], [0,0, 0]])

        centerbox  = VBox('CenterBox',[duedatebuttons, newjobs])

        footer = create_footer(self.root)
        widgets = [header, centerbox, footer]
        self.mainbox = HBox('MainBox', widgets)
        build_gui(self.root, self.mainbox)
        title.widget.configure(foreground="black", font='arial 14 bold', background='white')
        duedatetitle.widget.configure(foreground="black", font='arial 12 bold', background='white')
        self.root.mainloop()

    def create_stage(self, stage):
        status = self.children.get(stage, None)
        if status:
            parentName = status.widget.winfo_parent()
            #print (parentName)
            parent = status.widget._nametowidget(parentName)
            parent.destroy()
            self.children[stage] = None
        else:
            self.children[stage] = self.create_stage_window(stage)
            self.children[stage].root.protocol("WM_DELETE_WINDOW", lambda: self.create_stage(stage))
            #self.children[stage].root.overrideredirect(1) # Removes window border and all the buttons on the top right
            #self.children[stage].root.lift()

    def create_stage_window(self, stage):
        stagelabel = GLabel(stage+'StageTitle', width=100, height=20, text=stage)
        stagerow = GFrame_Row(stage+'StageRow',[stagelabel], height=40, parms=[WIN, HIN, HC, VC,[0,0,0], [0,0]])
        stagerow.configure(background='black')
       # Create table
        widgets = [stagerow]
        weeks = current_delivery(self.job_recs, stage)
        for i, week in enumerate(weeks):
            tb = create_stage_table(i, week)
            widgets.append(tb)
        stage_window = HBox(stage+'MainBox', widgets)
        # Position Topwindow right of buttons
        x, y = self.ced_button.get_absolute_x_y()
        x += self.ced_button.width + 10
        build_gui(None, stage_window, xpos=x)
        #stagerow.widget.configure(background='black')
        return stage_window
# ----------------------------------------------------------------------------------------------------------------------
# New (latest) jobs table
# ----------------------------------------------------------------------------------------------------------------------
def crc_newjobstable(jobdata): # Data is list of dictionaries
    jobdata = sorted(jobdata, key = lambda y: y['received'], reverse=True)

    columns = [create_column('Name',width = 300, labelalign=LABEL_LEFT), create_column('Received'), create_column('Pages'), create_column('ms Pages'),
              create_column('Chapters'), create_column('PE',width = 250, labelalign=LABEL_LEFT) ]
    data = []
    for r in jobdata:
        no_chapters = 0
        if 'chapters' in r:
            try:
                no_chapters = len(r['chapters'])
            except:
                no_chapters = 0
        row = [r['jobname'], r['received'], r.get('estpages', 0), r.get('estpages', 0), no_chapters,
               r.get('PE', '')]
        data.append(row)
    t = GTable('table1',columns, data, view_rows=20)
    t.set_data_clicked(newjobs_clicked)
    return t

def newjobs_clicked(tablenode, row, col, top):
    print (tablenode.name, row, col, top)

# ----------------------------------------------------------------------------------------------------------------------
# Delivery stage
# ----------------------------------------------------------------------------------------------------------------------
def create_stage_table(i, week):
    weektitle = GLabel('WeekTitle' + str(i), width=300, height=20)
    weektitle.set_text(week['title'])
    if week['jobs']:
        tb = crc_duedatetable(week['jobs'])
        b = VBox('Box1'+str(i), [tb])
        return HBox('Box2'+str(i), [weektitle, b])
    else:
        return weektitle

def crc_duedatetable(jobdata): # Data is list of dictionaries
    columns = [create_column('Name',width = 300, labelalign=LABEL_LEFT), create_column('Due'), create_column('Actual'), create_column('Comment',width = 500, labelalign=LABEL_LEFT) ]
    data = []
    for r in jobdata:
        row = [r['jobname'], r['duedate'], r['delivered'], r['comment']]
        data.append(row)
    t = GTable('table1',columns, data, view_rows=min(20, len(jobdata)))
    t.set_data_clicked(due_stage_clicked)
    return t

def create_footer(root):
    # Close application
    b = GButton('Quit', width=100, height=30, text='Quit')
    b.set_command(root.destroy)
    ft = GFrame_Row('RowFooter',[b], height=40, parms=[WIN, HIN, HC, VC,[0,0,0], [0,0]])
    return ft

def due_stage_clicked(tablenode, row, col, top):
    if col == 3: # For the comments column
        messagebox.showinfo('Title', tablenode.cells[row][col].get() )
        tablenode.get_root().attributes('-topmost', 1)
        #tablenode.get_root().lift() # Make grid back on top

if __name__ == '__main__':
    m = Main()

