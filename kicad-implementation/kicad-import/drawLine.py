import pcbnew
import csv
import os
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
    Plots the lines of a csv file containing points in XY coordinate format.
    function run(filemame):
        filename parameter is a non encoded .csv file containing rows of x and y coordinates
    sample functional .csv file
    1, 2
    3, 1
    61, 86

    where column 1 is the x coordinate of the point and column 2 is y coordinates.

    ------------------------
    '''
    points = []
    os.chdir('C:\\Users\\Franco\\OneDrive\\Documentos\\Purdue\\Fall 2022\\Research 4D\\KiCad Files\\Organized Tests')
    with open(filename, 'r') as csvfile:
       datareader = csv.reader(csvfile)
       i = 0
       for row in datareader:
           point= wxPointMM(float(row[0]), float(row[1]))
           points.append(point)
           if(len(points)>=2):
               add_line(points[i-1], points[i])
           i += 1
    pcbnew.Refresh()
       
