import re
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import plot_functions
import component_parser
# import xml_generator
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
wire_regex = re.compile(r'(\(wire\s+\(([\s\d\w\.\-]+)\)\s+\))')
net_regex = re.compile(r'(\(net \"(Net-\(\S+\))\"(\s+\(wire\s+\((path (\S+) (\d+)(\s+)((\d+) (-?\d+)(\s+))+\)+)\s+\)+)+(\s+\(via ([\S ]+)\s+\))*\s+\))+')
wire_info_regex = re.compile(r'path (\S+) (\d+)')
wire_xy_regex = re.compile(r' ([-\d]+) ([-\d]+)')
via_regex = re.compile(r'\(via \"(.+)\" ([-\d]+) ([-\d]+)')


net_result = net_regex.findall(data)
nets = []
classy_net = []
for i in range(len(net_result)):
    net_name = net_result[i][1]
    nets.append(net_result[i][0])
    wire_result = wire_regex.findall(net_result[i][0])
    via_result = via_regex.findall(net_result[i][0])
    classy_wires = []
    for j in range(len(wire_result)):
        info_result = wire_info_regex.findall(wire_result[j][1])
        layer, width = info_result[0]
        xy_result = wire_xy_regex.findall(wire_result[j][1])
        classy_wire = Wire(layer=layer, width=width, coords=xy_result)
        classy_wires.append(classy_wire)
    classy_vias = [Via(result[0], (float(result[1]), float(result[2]))) for result in via_result]
    classy_net.append(Net(net_name, classy_wires,classy_vias))

tracks = []

for net in classy_net:
    coords_list = []
    for wire in net.wires:
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

     
file2 = open(r"kicad-files-components\SensorTemp.dsn", "r") ## EVERYTHING IS IN MICROMETERS
data2 = file2.read()
file2.close()
components = component_parser.getComponents(data2)

for component in components:
    print(component.type)
    for pad in component.pads:
        plot_functions.plot_Pad(pad, component)
plt.show()

