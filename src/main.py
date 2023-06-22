from kicad_to_xml import component_parser, net_parser
from gcode_generator import advanced_generator
from autorouting import autorouter
import os
def start():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)
    filepath = autorouter.run()
    file_ses = open(f"{filepath}.ses", "r") ## EVERYTHING IS IN MICROMETERS
    data = file_ses.read()
    file_ses.close()
    net_list = net_parser.get_nets(data)
         
    file_dsn = open(f"{filepath}.dsn", "r") ## EVERYTHING IS IN MICROMETERS
    data2 = file_dsn.read()
    file_dsn.close()
    component_list = component_parser.getComponents(data2)

    advanced_generator.advanced_GCODE_gen(filepath, net_list, component_list)
