
from table import GTable, create_column, LABEL_LEFT

def SampleTable():
    # Note the width and height dimensions need the columns and data - maybe provide blank data
    columns = [create_column('One'), create_column('Two'), create_column('Three', width=200), create_column('Four')]
    data = []
    rows = 15
    for r in range(rows):
        row = []
        for j, col in enumerate(columns):
            row.append('{}-{}'.format(r, j))
        data.append(row)
    t = GTable('table1',columns, data, view_rows=8)
    t.data_clicked = data_clicked
    return t

def data_clicked(x,y, top_row):
    print ('Main frame')
    print ('Data clicked is {}, {}'.format(x,y))
    print ('Top row (scrolling):{}'.format(top_row))
    # Adjust for scrolling later
    print ('Clicked on (row, col) {} : {}'.format(x+top_row, y))

def crc_table(jobdata): # Data is list of dictionaries
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
        #for j, col in enumerate(columns):
        #    row.append('{}-{}'.format(r, j))
        data.append(row)
    t = GTable('table1',columns, data, view_rows=20)
    t.data_clicked = data_clicked
    return t
