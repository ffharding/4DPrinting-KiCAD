import pcbnew
def genDSN(path):
    """
    Create SPECCTRA design file into the indicated directory
    Inputs:
        path (str) : directory
    Outputs:
        .dsn file at "path" directory
    """
    pcbnew.ExportSpecctraDSN(f'{path}.dsn')
