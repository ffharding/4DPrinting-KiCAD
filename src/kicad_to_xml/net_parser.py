import re
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

    Attributes: 
        name (str): Assigned name of via 
        coords (tuple): xy position
    '''
    def __init__(self, name, coords):
        self.name = name
        self.coords = coords

def get_nets(data):
    """
    Parses data from Specctra Session (.ses) file into a list of nets containing routing information
    Inputs:
        data (str): Specctra Session file data
    Outputs:
        net_list (list): list of nets parsed into Net user classes
    """
    ## REGEX for taking information from files for nets
    wire_regex = re.compile(r'(\(wire\s+\(([\s\d\w\.\-]+))') 
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
    return net_list