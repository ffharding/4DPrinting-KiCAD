import matplotlib.pyplot as plt
from autorouting import plot_functions

def getFigure(filepath, net_list, component_list):
    """
    Helper function that generates image of expected routing with pads
    Inputs:
        filepath (str) : filepath of the generated image
        net_list (list) : list containing Net objects with net information
        component_list (list) : list containing Component objects with component information
    Outputs:
        image (png) : png generated
    """
    tracks = []

    for net in net_list:
        coords_list = []
        for wire in net.wire_list:
                coords_list.append(wire)
        tracks.append(coords_list)
        for track in tracks:
            for wire in track:
                path = [(float(x),float(y)) for (x,y) in wire.coords]
                if(wire.layer == "F.Cu"):
                    color = 'r'
                else:
                    color = 'b'
                plot_functions.plot_Path(path, color)
        for via in net.via_list:
            plot_functions.plot_Via(via.coords)
    for component in component_list:
        for pad in component.pad_list:
            plot_functions.plot_Pad(pad, component)
    plt.savefig(f'{filepath}.png')