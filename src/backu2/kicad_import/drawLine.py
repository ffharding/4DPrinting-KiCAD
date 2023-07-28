import pcbnew
import csv
from pcbnew import wxPoint, wxPointMM

def add_line(start, end, layer=pcbnew.Edge_Cuts):
    board = pcbnew.GetBoard()
    segment = pcbnew.PCB_SHAPE(board)
    segment.SetShape(pcbnew.SHAPE_T_SEGMENT)
    segment.SetStart(start)
    segment.SetEnd(end)
    segment.SetLayer(layer)
    segment.SetWidth(int(0.1 * pcbnew.IU_PER_MM))
    board.Add(segment) 

board = pcbnew.GetBoard()

def run(filename):
    '''
        ------------------------
    Plots the lines of a csv file containing point_list in XY coordinate format.
    function run(filemame):
        filename parameter is a non encoded .csv file containing rows of x and y coordinates
    sample functional .csv file
    1, 2
    3, 1
    61, 86

    where column 1 is the x coordinate of the point and column 2 is y coordinates.

    ------------------------
    '''
    point_list = []
    with open(filename, 'r') as csvfile:
       datareader = csv.reader(csvfile)
       i = 0
       for row in datareader:
           point= wxPointMM(float(row[0]), float(row[1]))
           point_list.append(point)
           if(len(point_list)>=2):
               add_line(point_list[i-1], point_list[i])
           i += 1
    pcbnew.Refresh()
       
