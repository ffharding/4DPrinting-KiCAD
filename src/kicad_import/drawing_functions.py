import pcbnew
from pcbnew import wxPointMM

def add_line(start, end, trace_width, layer = 'Edge.Cuts'):
    '''
        Adds line segment to board.
        Inputs:
            start (tuple) : start point of the segment
            end (tuple) : end point of the segment
            layer (str) : valid string name of a kicad layer (default to Edge.Cuts)
    '''
    board = pcbnew.GetBoard()
    segment = pcbnew.PCB_SHAPE(board)
    segment.SetShape(pcbnew.SHAPE_T_SEGMENT)
    segment.SetStart(wxPointMM(*start))
    segment.SetEnd(wxPointMM(*end))
    segment.SetLayer(board.GetLayerID(layer))
    segment.SetWidth(int(trace_width * pcbnew.IU_PER_MM))
    board.Add(segment)

def add_rectangle(board, start, end, trace_width, layer):
    '''
        Adds rectangle to board.
        Inputs:
            start (tuple) : upper left corner of the rectangle
            end (tuple) : lower right corner of the rectangle
            trace_width (float) : width of sides (trace of drawing)
            layer (str) : valid string name of a kicad layer (default to Edge.Cuts)
    '''
    rect = pcbnew.PCB_SHAPE(board)
    rect.SetShape(pcbnew.SHAPE_T_RECT)
    rect.SetStart(wxPointMM(*start))
    rect.SetEnd(wxPointMM(*end))
    rect.SetLayer(board.GetLayerID(layer))
    rect.SetWidth(int(trace_width * pcbnew.IU_PER_MM))
    
    return rect

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