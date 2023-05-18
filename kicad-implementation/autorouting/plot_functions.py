import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
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