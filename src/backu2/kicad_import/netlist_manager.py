import re
import pcbnew
class Net():
    '''
        Summary:
            Created Net class to store NETINFO object from pcbnew, including nodes info that will connect pads
    '''
    def __init__(self, net_object, node_list):
        self.net_object = net_object
        self.node_list = node_list

class Node():
    '''
        Node of net, includes pin and reference information
    '''
    def __init__(self, ref, pin):
        self.ref = ref
        self.pin = pin


### Get nets from netlist file using regex, create NET class inmediatly
def import_netlist(board):
    '''
        Imports net information from netlist file and converts it to Net objects compatible with PCBNEW
        Input:
            board (BOARD) : BOARD object from pcbnew with current board information
        Output:
            net_list (list) : list of Net objects
    '''
    netlist_raw = open(r'kicad_import\Test3.net', 'r')
    netlist_data = netlist_raw.read()
    netlist_raw.close()


    net_regex = re.compile(r'(net \(code "(\S+)"\) \(name "(\S+)"\)[\s\S]*?(?=\)\)\)))')
    node_regex = re.compile(r'\(node \(ref "(\S+)"\) \(pin "(\S+)"\)')
    net_data = net_regex.findall(netlist_data)

    net_list = []
    for net in net_data:
        node_data = node_regex.findall(net[0])
        node_list = [Node(node[0], node[1]) for node in node_data]
        net_code = net[1]
        net_name = net[2]
        print(net_code, net_name)
        new_net = Net(pcbnew.NETINFO_ITEM(board, net_name, int(net_code)), node_list)
        net_list.append(new_net)
        board.Add(new_net.net_object) ## it is necessary to add net objects to board item, prevents crashes
        
    return net_list