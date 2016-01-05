# Build automatic containers

DEFAULT_HEIGHT = 20

from container import CT
from place_functions import LEFT, CENTERED, RIGHT, EXPAND

def make_row(*args, **kwargs):
    # args = (widgets.WG object, widgets.WG object)
    # kwargs = {'name': 'LabelRowLeft', 'padding': (5, 5, 5), 'alignment': ('centered', 'centered')}
    print (args)
    print (kwargs)
    c = CT(kwargs['name'])
    padding = list(kwargs.get('padding', [0,0]))
    alignment = kwargs.get('alignment', (CENTERED, CENTERED))
    i = 0
    parms = [padding[i]]
    for widget in args:
        i += 1
        parms.append(widget)
        parms.append(padding[i])
        padding.append(0) # In case many default padding needed
    parms.append(alignment[0])
    print (parms)
    c.add_row(*parms, vertical=alignment[1])
    c.height = kwargs.get('height', DEFAULT_HEIGHT)
    return c

def make_column(*args, **kwargs):
    print (args)
    print (kwargs)
    c = CT(kwargs['name'])
    padding = list(kwargs.get('padding', [0,0]))
    alignment = kwargs.get('alignment', (EXPAND, EXPAND))
    i = 0
    parms = [padding[i]]
    for widget in args:
        i += 1
        parms.append(widget)
        parms.append(padding[i])
        padding.append(0) # In case many default padding needed
    parms.append(alignment[1])
    print (parms)
    c.add_column(*parms, horizontal=alignment[0])
    c.height = kwargs.get('height', DEFAULT_HEIGHT)
    if 'width' in kwargs:
        c.width = kwargs['width']
    return c
