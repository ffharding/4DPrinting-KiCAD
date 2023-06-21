import pcbnew
import os
dir = os.getcwd
def run(dir):
    """
    Create front copper gerber file into the indicated directory
    Inputs:
        dir: directory
    Outputs:
        gerber file
    """
    os.chdir(dir)
    board = pcbnew.GetBoard()
    plot = pcbnew.PLOT_CONTROLLER(board)
    plot_options = plot.GetPlotOptions()
    plot_options.SetPlotFrameRef(False)
    plot.SetLayer(pcbnew.F_Cu)

    plot.OpenPlotfile("front_copper", pcbnew.PLOT_FORMAT_GERBER, "front_Copper")
    print("Plotting to " + plot.GetPlotFileName())
    plot.PlotLayer()
    plot.ClosePlot()
