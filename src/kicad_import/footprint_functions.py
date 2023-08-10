import pcbnew
from pcbnew import wxPointMM

def addFootprint(ft_id, ft_lib, ft_ref,  mm_pos, orientation):
    '''
        Adding footprints from xml library to Footprint object for pcbnew
        Inputs:
            ft_id (str): Footprint ID
            ft_lib (str): Path to footprint library
            ft_ref (str) : Footprint reference
            mm_pos (tuple) : XY coordinates of footprint
            orientation (float) : Angle of orientation of footprint
        Output:
            footprint (FOOTPRINT) : PCBNEW FOOTPRINT object including newly created footprint
    '''
    ## Convert position to wxPoint
    pos = wxPointMM(*mm_pos)
    ## Load Footprint
    footprint = pcbnew.FootprintLoad(ft_lib, ft_id)
    footprint.SetReference(ft_ref)
    footprint.SetPosition(pos)
    footprint.SetOrientation(orientation*10)
    return footprint

def addVia(board, mm_pos, diamater, netcode):
    '''
        Adding vias from xml library to VIA object for pcbnew
        Inputs:
            board (BOARD): BOARD object containing PCB board information
            mm_pos (tuple) : XY coordinates of via
            diameter (float): Diameter of via in milimeters
            netcode (int) : Code reference Net from netlist
        Output:
            via (FOOTPRINT) : PCBNEW VIA object including newly created via
    '''
    ## Convert position to wxPoint
    pos = wxPointMM(*mm_pos)
    ## Load via
    via = pcbnew.PCB_VIA(board)
    via.SetNetCode(int(netcode))
    via.SetPosition(pos)
    via.SetWidth(int(diamater * pcbnew.IU_PER_MM))
    return via