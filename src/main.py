import re
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from kicad_to_xml import plot_functions
from kicad_to_xml import component_parser
from gcode_generator import advanced_generator
from autorouting import autorouter
import os
class Net:
    '''
    Summary:
        Net class stores net information for easier unpacking

    Attributes:
        name (str): Assigned name of net 
        wire_list (list): List of wires connected to the net
        via_list (list) : List of vias connected to the net
    '''
    def __init__(self, name, wire_list, via_list):
        self.name = name
        self.wire_list = wire_list
        self.via_list = via_list
    def addWire(self, wire):
        self.wire_list.append(wire)

class Wire:
    '''
    Summary:
        Wire class stores wire information for easier unpacking

    Attributes:
        layer (str): Layer where route is located
        width (float): Width of the wire (should be 1.6 mm)
        coords (list) : List of critical xy coordinates of route (start, turn and/or end points)
    '''
    def __init__(self, layer, width, coords):
        self.layer = layer
        self.width = width
        self.coords = coords
    def __str__(self):
	    return f"Layer: {self.layer}, Width: {self.width}, Coordinates: ({self.coords})"
class Via:
    '''
    Summary:
        Via class stores via information for easier unpacking

    Attributes:3 
        name (str): Assigned name of via 
        coords (tuple): xy position
    '''
    def __init__(self, name, coords):
        self.name = name
        self.coords = coords
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
filepath = autorouter.run()

file_ses = open(f"{filepath}.ses", "r") ## EVERYTHING IS IN MICROMETERS
data = file_ses.read()
file_ses.close()

## REGEX for taking information from files for nets
wire_regex = re.compile(r'(\(wire\s+\(([\s\d\w\.\-]+)+\)\s+(\)|\(type))') 
net_regex = re.compile(r'(\(net "([\w\-\(\)]+)"?[\s\S]*?(?=\(net|\s+\)\s+\)\s+\)\s+\)))')
wire_info_regex = re.compile(r'path (\S+) (\d+)')
wire_xy_regex = re.compile(r' ([-\d]+) ([-\d]+)')
via_regex = re.compile(r'\(via \"(.+)\" ([-\d]+) ([-\d]+)')


net_result = net_regex.findall(data)
net_list = []

for i in range(len(net_result)):
    net_name = net_result[i][1]
    wire_result = wire_regex.findall(net_result[i][0])
    via_result = via_regex.findall(net_result[i][0])
    wire_list = []
    for j in range(len(wire_result)):
        info_result = wire_info_regex.findall(wire_result[j][1])
        info_result = wire_info_regex.findall(wire_result[j][1])
        layer, width = info_result[0]
        xy_result = wire_xy_regex.findall(wire_result[j][1])
        wire = Wire(layer=layer, width=width, coords=xy_result)
        wire_list.append(wire)
    via_list = [
         Via(
              result[0], (float(result[1]), float(result[2]))
              ) for result in via_result
         ]
    net_list.append(Net(net_name, wire_list,via_list))



tracks = []

for net in net_list:
    coords_list = []
    for wire in net.wire_list:
            coords_list.append(wire)
    tracks.append(coords_list)
    track_count = 1
    for track in tracks:
        x = []
        y = []
        for wire in track:
            path = [(float(x),float(y)) for (x,y) in wire.coords]
            if(wire.layer == "F.Cu"):
                color = 'r'
            else:
                color = 'b'
            plot_functions.plot_Path(path, color)
    for via in net.via_list:
        plot_functions.plot_Via(via.coords)

     
file_dsn = open(f"{filepath}.dsn", "r") ## EVERYTHING IS IN MICROMETERS
data2 = file_dsn.read()
file_dsn.close()
component_list = component_parser.getComponents(data2)

for component in component_list:
    for pad in component.pad_list:
        plot_functions.plot_Pad(pad, component)
plt.savefig(f'{filepath}.png')
advanced_generator.advanced_GCODE_gen(filepath, net_list, component_list)

