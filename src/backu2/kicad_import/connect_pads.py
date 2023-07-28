import pcbnew

def netlist_connect(component, net_list):
    '''
        Summary:
            Check reference of nodes in each net and connect pads to net if necessary
    '''
    component_ref = component.GetReference()
    for net in net_list:
        for node in net.node_list:
            if(node.ref == component_ref):
                pad = component.FindPadByNumber(node.pin)
                pad.SetNet(net.net_object)