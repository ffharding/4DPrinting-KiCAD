import re
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import plot_functions
# import xml_generator
import pyperclip
#import getPlot
#from pcbnew import wxPoint, wxPointMM
# import pcbnew
# import getPlot
#getPlot.run()
class Net:
    def __init__(self, name, wires, vias):
        self.name = name
        self.wires = wires
        self.vias = vias
    def __str__(self):
        return f"{self.name}({self.wires})"
    def addWire(self, wire):
        self.wires.append(wire)
class Wire:
    def __init__(self, layer, width, coords):
        self.layer = layer
        self.width = width
        self.coords = coords
    def __str__(self):
	    return f"Layer: {self.layer}, Width: {self.width}, Coordinates: ({self.coords})"
class Via:
     def __init__(self, name, coords):
        self.name = name
        self.coords = coords       
    
file = open(r"kicad-files-components\SensorTemp.ses", "r") ## EVERYTHING IS IN MICROMETERS
data = file.read()
file.close()

## REGEX for taking information from files for nets
net = re.compile(r'\((net \S+\s+((\(wire\s+\(([\s\d\w\.\-]+)\)\s+\))\s+)+(\(via \S+ \d+ [\-\d]+\s+\)\s+)*)\)')
wire = re.compile(r'(\(wire\s+\(([\s\d\w\.\-]+)\)\s+\))')
test = re.compile(r'(\(net \"(Net-\(\S+\))\"(\s+\(wire\s+\((path (\S+) (\d+)(\s+)((\d+) (-?\d+)(\s+))+\)+)\s+\)+)+(\s+\(via ([\S ]+)\s+\))*\s+\))+')
wire_info = re.compile(r'path (\S+) (\d+)')
wire_xy = re.compile(r' ([-\d]+) ([-\d]+)')
via = re.compile(r'\(via \"(.+)\" ([-\d]+) ([-\d]+)')


test_result = test.findall(data)
nets = []
classy_net = []
for i in range(len(test_result)):
    net_name = test_result[i][1]
    nets.append(test_result[i][0])
    wire_result = wire.findall(test_result[i][0])
    via_result = via.findall(test_result[i][0])
    classy_wires = []
    for j in range(len(wire_result)):
        info_result = wire_info.findall(wire_result[j][1])
        layer, width = info_result[0]
        xy_result = wire_xy.findall(wire_result[j][1])
        classy_wire = Wire(layer=layer, width=width, coords=xy_result)
        classy_wires.append(classy_wire)
    classy_vias = [Via(result[0], (float(result[1]), float(result[2]))) for result in via_result]
    classy_net.append(Net(net_name, classy_wires,classy_vias))

wires = []
for i in range(len(nets)):
    wire_result = wire.findall(nets[i])
    # print(wire_result)
    wires.append(wire_result)
wire_result = wire.findall(nets[0])

tracks = []

for net in classy_net:
    coords_list = []
    for wire in net.wires:
        #  print(wire)
            coords_list.append(wire)
    tracks.append(coords_list)
    track_count = 1
    for track in tracks:
        x = []
        y = []
        for wire in track:
            path = [(float(x),float(y)) for (x,y) in wire.coords] ## double check units
            if(wire.layer == "F.Cu"):
                color = 'r'
            else:
                color = 'b'
            plot_functions.plot_Path(path, color)
    for via in net.vias:
        plot_functions.plot_Via(via.coords)


file2 = open(r"kicad-implementation\autorouting\sensorV2-front_copper.gbr", "r")
data2 = file2.read()
file2.close()

pad_shape = re.compile(r'(TO\.P),(\w+).+?X([0-9\-]+)Y([0-9\-]+)', re.S)
pads = pad_shape.findall(data2)
side = 700000
pad_number = 1
pad_data = []
for pad in pads:
    pad_number += 1
    shape = pad[1]
    if(shape == 'BT1'):
            width = side * 4
            height = side * 5
            shape = "rectangle"
    else:
            width = side
            height = side
            shape = "square"

    x = float(pad[2])
    y = float(pad[3])
    pad_data.append((x,y,width,height,shape))
    left, bottom = (x - width/2,y - height/2)
    rect=mpatches.Rectangle((left/100,bottom/100),width/100,height/100,
                                fill=True,
                                color='red',
                               linewidth=2/100)
    plt.gca().add_patch(rect)
plt.show()

