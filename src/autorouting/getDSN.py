import pcbnew
import os
dir = os.getcwd
def genDSN(dir):
    """
    Create SPECCTRA design file into the indicated directory
    Inputs:
        dir: directory
    Outputs:
        .dsn file
    """
    os.chdir(dir)
    pcbnew.ExportSpecctraDSN('board_information.dsn')
