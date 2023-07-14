import pcbnew
from pcbnew import wxPointMM
def addFootprint(ft_id, ft_lib, ft_ref,  mm_pos, orientation):
    ## Convert position to wxPoint
    pos = wxPointMM(*mm_pos)
    print(f'name = {ft_id}, orientation = {orientation} and orientation type = {type(orientation)}')
    ## Load Footprint
    footprint = pcbnew.FootprintLoad(ft_lib, ft_id)
    footprint.SetReference(ft_ref)
    footprint.SetPosition(pos)
    footprint.SetOrientation(orientation*10)
    print(f'name = {ft_id}, orientation = {orientation} and orientation after = {footprint.GetOrientation()}')
    return footprint