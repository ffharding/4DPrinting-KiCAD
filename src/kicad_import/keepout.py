import pcbnew
from pcbnew import wxPointMM, wxPoint
## set stuff

def draw_keepout(board, points, layer):
    new_area = pcbnew.ZONE(board)
    vector = pcbnew.wxPoint_Vector(0)
    for point in points:
        vector.append(wxPointMM(*point))
    new_area.AddPolygon(vector)
    new_area.SetLayer(board.GetLayerID(layer))
    new_area.SetIsRuleArea(True)
    new_area.SetDoNotAllowTracks(True)
    return new_area

board = pcbnew.GetBoard()
points = [(134.264, 62.0776), (125.374, 62.2808), (125.222, 52.7812), (134.163, 52.6288), (134.264, 62.0776)]
layer = 'F.Cu'
# path = 
new_area = draw_keepout(board, points, layer)
board.Add(new_area)
pcbnew.Refresh()