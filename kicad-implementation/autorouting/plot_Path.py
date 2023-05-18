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