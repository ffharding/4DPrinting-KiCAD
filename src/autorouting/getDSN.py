import pcbnew
import os
dir = os.getcwd
def genDSN(path):
    """
    Create SPECCTRA design file into the indicated directory
    Inputs:
        dir: directory
    Outputs:
        .dsn file
    """
    pcbnew.ExportSpecctraDSN(f'{path}.dsn')
