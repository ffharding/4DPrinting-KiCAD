from autorouting import getDSN
from autorouting import  autoroute_dsn
# import pcbnew
import os
def run():
    filepath = ((pcbnew.GetBoard()).GetFileName().split('.kicad_pcb'))[0] ## one liner for getting filepath
    getDSN.genDSN(filepath)
    autoroute_dsn.autoroute_dsn(filepath)
    return filepath
    
