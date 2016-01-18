# Copy the delivery by due date in the various job stages for the weeks
# Currently last week, this week, next week

from current_delivery import current_delivery
from crc_lib import get_crc_all_jobs
from widget import GLabel, GButton
from container import GFrame_Row, GFrame_Column, HBox, VBox
from constants import WIN, HIN, VT, HL, VC, VB, HAS, HC, WEX
from sample_widgets import exit_button
from table import GTable, create_column, LABEL_LEFT
from build import build_gui
import tkinter as TK


def main(alljobs, stagelist):
    #print (x)
    print ('-')
    print (alljobs[0])
    stage = stagelist[0]
    #stage = 'ced'
    print ('-'*70)
    weeks = current_delivery(alljobs, stage)

    #for week in weeks:
    #    print (week['title'])
    #    for job in week['jobs']:
    #        print (job['jobname'])

 
    title = GLabel('Title', width=300, height=20, text='Latest CRC Jobs')

    header = GFrame_Row('Header', [title], height = 40, parms=[WIN, HIN, HC, VC,[0,0,0], [0,0]])
    footer = GFrame_Row('Footer',[exit_button], height=40, parms=[WIN, HIN, HC, VC,[0,0,0], [0,0]])

    stagelabel = GLabel('Title', width=100, height=20, text=stage)
    stagerow = GFrame_Row('StageRow',[stagelabel], height=40, parms=[WIN, HIN, HC, VC,[0,0,0], [0,0]])

    # Create stage selection button
    cedbutton = GButton('GetCED', width=100, height=30, text='CED')
    initialbutton = GButton('GetInitial', width=100, height=30, text='Initial')
    secondpagesbutton = GButton('SecondPages', width=100, height=30, text='Second Pages')
    finalpagesbutton = GButton('FinalPages', width=100, height=30, text='Final Pages')
    sbutton = GFrame_Row('SButtonRow',[cedbutton, initialbutton, secondpagesbutton, finalpagesbutton], height=40, parms=[WIN, HIN, HC, VC,[0,0,0], [0,0]])

    widgets = [header, sbutton, stagerow]
   # Create table
    for i, week in enumerate(weeks):
        tb = create_stuff(i, week)
        widgets.append(tb)
    widgets.append(footer) 
    con3 = HBox('MainBox', widgets)

    root = TK.Tk()

    g = con3
    build_gui(root, g)
    status = ['quit']
    exit_button.set_command(root.destroy)
    cedbutton.set_command(lambda: clicked(root, status, 'ced') )
    initialbutton.set_command(lambda: clicked(root, status, 'initial') )
    secondpagesbutton.set_command(lambda: clicked(root, status, '2ndpages') )
    finalpagesbutton.set_command(lambda: clicked(root, status, 'finalpages') )
    title.widget.configure(foreground="black", font='arial 14 bold', background='white')
    stagelabel.widget.configure(foreground="black", font='arial 12 bold', background='white')
    root.mainloop()
    # Now which button was pressed?
    return status

def clicked(root, x, stage):
    x.insert(0,stage)
    x.pop()
    root.destroy()

def create_stuff(i, week):
    weektitle = GLabel('WeekTitle' + str(i), width=300, height=20)
    weektitle.set_text(week['title'])
    if week['jobs']:
        wrow = GFrame_Row('WRow'+str(i), [weektitle], height = 40, parms=[WIN, HIN, HC, VC,[0,0,0], [0,0]])
        tb = crc_table(week['jobs'])
        b = VBox('Box1'+str(i), [tb])
        return HBox('Box2'+str(i), [weektitle, b])
    else:
        return weektitle

def crc_table(jobdata): # Data is list of dictionaries
    columns = [create_column('Name',width = 300, labelalign=LABEL_LEFT), create_column('Due'), create_column('Actual'), create_column('Comment',width = 500, labelalign=LABEL_LEFT) ]
    data = []
    for r in jobdata:
        row = [r['jobname'], r['duedate'], r['delivered'], r['comment']]
        data.append(row)
    t = GTable('table1',columns, data, view_rows=min(20, len(jobdata)))
    #t.data_clicked = data_clicked
    return t

if __name__ == '__main__':
    alljobs = get_crc_all_jobs()
    alljobs = sorted(alljobs, key = lambda y: y['received'], reverse=True)
    status = ['initial']
    while True:
        status = main(alljobs, status)
        print (status)
        if status[0] == 'quit':
            break

