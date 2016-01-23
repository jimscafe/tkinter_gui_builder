__author__ = 'Paul'

class Node():
    def __init__(self, name='', width = -1, height = -1):
        self.name = name
        self.parent = None
        self.widget = None
        self.text = None
        self.command = None
        self.x = -1
        self.y = -1
        self.width = width
        self.height = height
        self.children = []
        self.config = {}
        self.type = None

    def configure(self, **kwargs):
        self.config = kwargs
        if self.widget:
            self.widget.configure(self.config)

    def get_absolute_x_y(self): # Get the x poisiotn on the monitor screen
        x = self.x
        y = self.y
        node = self
        while node.parent:
            node = node.parent
            x += node.x
            y += node.y
        #print ('Widget x before geometry', x)
        #print ('Widget root geometry    ', node.root.geometry())
        s = node.root.geometry() # Root position - size
        s, sx, sy = s.split('+')
        x += int(sx)
        y += int(sy)
        return x, y

    def what_widget(self):
        if self.widget:
            return self.parent.widget.winfo_class()

    def get_root_node(self):
        node = self
        while node.parent:
            node = node.parent
        return node

    def get_root(self):
        return self.get_root_node().root