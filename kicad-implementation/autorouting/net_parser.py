import re
import pyperclip
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
    def __str__(self):
        return f"{self.name}({self.wire_list})"
    def addWire(self, wire):
        self.wire_list.append(wire)

class Wire:
    '''
    Summary:
        Wire class stores wire information for easier unpacking

    Attributes:
        layer (str): Layer where route is located
        width (float): Width of the wire (should be 1.6 mm)
        coords (list) : List of critical xy coordinates of path (start, turn and/or end points)
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

    Attributes: 
        name (str): Assigned name of via 
        coords (tuple): xy position
    '''
    def __init__(self, name, coords):
        self.name = name
        self.coords = coords

file = open(r"kicad-files-components\SensorTemp.ses", "r") ## EVERYTHING IS IN MICROMETERS
data = file.read()
file.close()

def getNets(data):

    ## Parse component data
    net_regex = re.compile(r'(\(net "([\w\-\(\)]+)"?[\s\S]*?(?=\(net|\s+\)\s+\)\s+\)\s+\)))')
    wire_regex = re.compile(r'(\(wire\s+\(([\s\d\w\.\-]+)+\)\s+(\)|\(type))')       
    path_info_regex = re.compile(r'path (\S+) (\d+)')


    net_matches = net_regex.findall(data)
    for match in net_matches:
        name = match[1]
        net_match = match[0]
        wire_matches = wire_regex.findall(net_match)
        for wire_match in wire_matches:
            paths_list =  wire_match[1]
            print(path_info_regex.findall(paths_list)[0])



if __name__ == '__main__':
    getNets(data)
