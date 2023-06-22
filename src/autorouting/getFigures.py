import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from autorouting import plot_functions

def getFigure(filepath, net_list, component_list):
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
    for component in component_list:
        for pad in component.pad_list:
            plot_functions.plot_Pad(pad, component)
    plt.savefig(f'{filepath}.png')