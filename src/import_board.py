import xml.etree.ElementTree as ET
from kicad_import import netlist_manager, footprint_functions, connect_pads
import pcbnew
import os
def import_components():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)
    print(os.getcwd())
    path = r'kicad_import\footprint_complex.xml'
    footprint_tree = ET.parse(path)
    footprint_root = footprint_tree.getroot()

    ## Get Board and Add footprint to board
    board = pcbnew.GetBoard()

    ## Import Netlist
    net_list = netlist_manager.import_netlist(board)
    
    for component in footprint_root:
        x, y = component.find('position')
        footprint = footprint_functions.addFootprint(component.get('name'), component.find('path').text, component.find('ref').text, (float(x.text), float(y.text)), float(component.find('orientation').text))
        connect_pads.netlist_connect(footprint, net_list)
        board.Add(footprint)
    

    pcbnew.Refresh()

import_components()