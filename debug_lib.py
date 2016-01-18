

def print_node(obj):
    if obj.parent:
        parent = obj.parent.name
    else:
        parent = 'None'
    print ('{:12} ({:12}) width={:4}: height={:4} : x={:4} : y={:4}'.format(obj.name, parent, obj.width, obj.height, obj.x, obj.y))
    return '' # No error