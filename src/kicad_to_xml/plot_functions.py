import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import math
def plot_Path(path, color):
    '''
    Plots the path of a track by plotting one line at a time to comply in the correct order
    Inputs:
        path: xy coordinates of the vertices of path
        color: color of track
    Output:
        Plot to pyplot
    '''
    length = len(path)
    for i in range(length):
        if((i+1) != length):
            x = [path[i][0], path[i+1][0]]
            y = [path[i][1], path[i+1][1]]
            plt.plot(x,y, color=color)

def plot_Via(coordinates):
    '''
    Plots vias
    Inputs:
        coordinate: coordinate of center of via
    Output:
        Plot to pyplot
    '''
    left, bottom = (coordinates[0] - 5000/2,coordinates[1] - 5000/2)
    rect=mpatches.Rectangle((left,bottom),5000,5000,
                                fill=True,
                                color='yellow',
                               linewidth=2)
    plt.gca().add_patch(rect)

def rotate(orientation, height, width, x, y):
    """
    Rotate the pad counterclockwise using math calculations for position
    """
    width, height = height, width
    rad_sin = math.sin(math.radians(orientation))
    rad_cos = math.cos(math.radians(orientation))
    x, y = (rad_cos * x - rad_sin * y, rad_sin * x + rad_cos * y)

    return height, width, x, y

def plot_Pad(pad, component):
    '''
    Plot pad to pyplot using pad information and component position
    Inputs:
        pad: Pad object
        component: Component object
    Output:
        Plot to pyplot
    '''
    component_pos = component.pos
    pad_x, pad_y = pad.rel_pos
    width = pad.width
    height = pad.height
    if (component.orientation != 0):
        print(component.orientation)
        height, width, pad_x, pad_y   = rotate(component.orientation, height, width, pad_x, pad_y)
    pad.true_pos = (component_pos[0] + pad_x,component_pos[1] + pad_y)
    left, bottom = (pad.true_pos[0] - width/2,pad.true_pos[1] - height/2)
    rect=mpatches.Rectangle((left*10,bottom*10),width*10,height*10,
                                fill=True,
                                color='red',
                            linewidth=2)
    plt.gca().add_patch(rect)