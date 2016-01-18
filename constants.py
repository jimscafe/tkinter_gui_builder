ROW = 'row'
COLUMN = 'column'
HBOX = 'h_box' # Has 2 children (also containers), expands children H & V
# ----------------------------------------------------------------------------------------
# Layout options for container children
# ----------------------------------------------------------------------------------------
"""
COLUMN                                                      +----------------+
Vertical:    Top, Centered, Bottom  (All children)          |                |  VT,VC,VB
Horizontal   Left, Centered, Right  (All children)          |  +--------+    |  HL,HC,HR
Width        All children the same                          |  |        |    |  WAS
             Expand all children to width of container      |  +--------+    |  WEX
             Individual                                     |                |  WIN
Height       All same                                       |  +--------+    |  HAS
             Individual                                     |  |        |    |  HIN
                                                            |  +--------+    |
                                                            |                |
                                                            +----------------+

ROW
Vertical:    Top, Centered, Bottom  +-----------------------------------+
Horizontal   Left, Centered, Right  |                                   |
Width        All same               |   +----------+  +------------+    |
             Individual             |   |          |  |            |    |
Height       All same               |   +----------+  +------------+    |
             Expand                 |                                   |       HEX
             Individual             +-----------------------------------+

Note: Absolute x and y option?
"""
# ----------------------------------------------------------------------------------------

VT = 'V-Top'
VC = 'V-Cent'
VB = 'V-Bot'
HL = 'H-Left'
HC = 'H-Cent'
HR = 'H-Right'
WAS = 'Width-Same'
WEX = 'Width-Exp' # Ignores padding
WIN = 'Width-Ind'
HAS = 'Height-Same'
HEX = 'Height-Exp' # Ignores padding
HIN = 'Height-Ind'

RIGHT = 'right'