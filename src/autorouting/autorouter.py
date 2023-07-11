from autorouting import getDSN
from autorouting import  autoroute_dsn
import pcbnew
def run():
    """
    Gets the filepath from the KiCAD file and communicates with DSN and .ses generators (autorouting)
    Outputs:
        filepath (str) : global filepath of Specctra DSN and Specctra Session files with board information
    """
    filepath = ((pcbnew.GetBoard()).GetFileName().split('.kicad_pcb'))[0] ## one liner for getting filepath
    getDSN.genDSN(filepath)
    autoroute_dsn.autoroute_dsn(filepath)
    return filepath
    
