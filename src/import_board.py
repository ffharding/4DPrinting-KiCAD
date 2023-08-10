import xml.etree.ElementTree as ET
from kicad_import import netlist_manager, footprint_functions, connect_pads, drawing_functions
import pcbnew
import os
import export_GCODE
def start():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)
    
    ## Import XML
    path = r'kicad_import\board_information.xml'
    footprint_tree = ET.parse(path)
    footprint_root = footprint_tree.getroot()
    components = footprint_root.find('components')
    keepouts = footprint_root.find('keepouts')
    vias = footprint_root.find('vias')
    ## Get Board and Add footprint to board
    board = pcbnew.GetBoard()

    ## Import Netlist
    net_list = netlist_manager.import_netlist(board)
    
    for component in components:
        x, y = component.find('position')
        footprint = footprint_functions.addFootprint(component.get('name'), component.find('path').text, component.find('ref').text, (float(x.text), float(y.text)), float(component.find('orientation').text))
        connect_pads.netlist_connect(footprint, net_list)
        board.Add(footprint)

    for keepout in keepouts:
        layer = (keepout.find('layer')).text
        points = []
        for point in keepout.find('points'):
            x, y = point
            points.append((float(x.text), float(y.text) * -1))
        new_area = drawing_functions.draw_keepout(board, points, layer)
        board.Add(new_area)
    
    for via in vias:
        x, y = via.find('position')
        via = footprint_functions.addVia(board, (float(x.text), float(y.text)), float(via.find('diameter').text), int(via.find('netcode').text) )
        board.Add(via)
    edge_cuts = drawing_functions.add_rectangle(board, (0,0), (60, -100), 0.1, 'Edge.Cuts')
    board.Add(edge_cuts)
    pcbnew.Refresh()