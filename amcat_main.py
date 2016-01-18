# Control reports for amcat

# Show latest jobs and buttons for due jobs at different stages - separate windows
from pymongo import MongoClient
from widget import GLabel, GButton
from container import GFrame_Row, GFrame_Column, HBox, VBox
from constants import WIN, HIN, VT, HL, VC, VB, HAS, HC, WEX
from build import build_gui
from current_delivery import current_delivery
from table import GTable, create_column, LABEL_LEFT
import tkinter as TK
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

        duedatetitle = GLabel('DueDateTitle', width=100, height=30, text = 'Due Dates')
        b1 = GButton('CED', width=100, height=30, text='CED')
        #b1.set_command(self.create_ced)
        b1.set_command(lambda: self.create_stage('ced'))
        b2 = GButton('Initial', width=100, height=30, text='Initial')
        b2.set_command(self.create_initial)
        b3 = GButton('2ndPages', width=100, height=30, text='2nd Pages')
        b3.set_command(self.create_2ndpages)
        b4 = GButton('FinalPages', width=100, height=30, text='Final Pages')
        b4.set_command(self.create_finalpages)
        duedatebuttons = GFrame_Column('DueDateButtons',[duedatetitle,b1, b2,b3,b4], width = 140, parms=[WIN, HIN, HC, VC,[0,0,0], [0,0, 0]])

        centerbox  = VBox('CenterBox',[duedatebuttons, newjobs])

        footer = create_footer(self.root)
        widgets = [header, centerbox, footer]
        mainbox = HBox('MainBox', widgets)
        build_gui(self.root, mainbox)
        title.widget.configure(foreground="black", font='arial 14 bold', background='white')
        duedatetitle.widget.configure(foreground="black", font='arial 12 bold', background='white')
        self.root.mainloop()

    def create_ced(self):
        self.create_stage('ced')

    def create_initial(self):
        self.create_stage('initial')

    def create_2ndpages(self):
         self.create_stage('2ndpages')

    def create_finalpages(self):
        self.create_stage('finalpages')

    def create_stage(self, stage):
        status = self.children.get(stage, None)
        if status:
            parentName = status.widget.winfo_parent()
            print (parentName)
            parent = status.widget._nametowidget(parentName)
            parent.destroy()
            self.children[stage] = None
        else:
            self.children[stage] = self.ced_stage = self.create_stage_window(stage)

    def create_stage_window(self, stage):
        stagelabel = GLabel(stage+'StageTitle', width=100, height=20, text=stage)
        stagerow = GFrame_Row(stage+'StageRow',[stagelabel], height=40, parms=[WIN, HIN, HC, VC,[0,0,0], [0,0]])
       # Create table
        widgets = [stagerow]
        weeks = current_delivery(self.job_recs, stage)
        for i, week in enumerate(weeks):
            tb = create_stage_table(i, week)
            widgets.append(tb)
        stage_window = HBox(stage+'MainBox', widgets)
        build_gui(None, stage_window)
        return stage_window

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
        dd = r.get('duedates', None)
        row = [r['jobname'], r['received'], r.get('estpages', 0), r.get('estpages', 0), no_chapters,
               r.get('PE', '')]
        data.append(row)
    t = GTable('table1',columns, data, view_rows=20)
    return t

def create_stage_table(i, week):
    weektitle = GLabel('WeekTitle' + str(i), width=300, height=20)
    weektitle.set_text(week['title'])
    if week['jobs']:
        wrow = GFrame_Row('WRow'+str(i), [weektitle], height = 40, parms=[WIN, HIN, HC, VC,[0,0,0], [0,0]])
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
    return t

def create_footer(root):
    # Close application
    b = GButton('Quit', width=100, height=30, text='Quit')
    b.set_command(root.destroy)
    ft = GFrame_Row('RowFooter',[b], height=40, parms=[WIN, HIN, HC, VC,[0,0,0], [0,0]])
    return ft



if __name__ == '__main__':
    m = Main()

