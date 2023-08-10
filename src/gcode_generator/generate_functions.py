def draw_rectangle(width, height):
    '''
        Draw a hollow rectangle in GCODE starting from top right
    '''
    gcode = f'\nG1 X{round((-width), 3)} E1' if (height >= width) else f'\nG1 X{round((-width), 3)}'
    gcode += f'\nG1 Y{round((height), 3)} E1'
    gcode += f'\nG1 X{round((width), 3)} E1'
    gcode += f'\nG1 Y{round((-height), 3)} E1' if (width > height) else f'\nG1 Y{round((-height), 3)}'
    return gcode
def generate_wire(wire, cur_position, print_layer, extrusion_head):
    """
    Generates GCODE to print wire 
    Inputs:
        wire (Pad): pad to be printed
        cur_position (tuple) : XY coordinate of current position of extrusion head
        print_layer (str) : layer that the current subprocess is printing to
        extrusion_head (extrusion_head) : extrusion_head object containing head information
    Outputs:
        gcode (str) : gcode output with wire print information
        coordinates (tuple) : returns end of wire if wire was printed, else returns cur_position which is unchanged from input
    """
    gcode = ''
    coordinates = wire.coords

    ## move to start of next net, including speed change
    x_diff = float(coordinates[0][0]) - float(cur_position[0])
    y_diff = float(coordinates[0][1]) - float(cur_position[1])
    gcode += f'\nG1 F2000'
    gcode += f'\nG1 Z3'
    gcode += f'\nG1 X{round((x_diff/10000), 3)} Y{round((y_diff/10000), 3)}'
    gcode += f'\nG1 Z-3'
    gcode += f'\nG1 F{extrusion_head.trace_speed}'

    trace_num = 3 if (("B.Cu" == print_layer)) else 1

    for i in range(trace_num):
        direction = 1 if ((i % 2) == 0) else -1
        for i in range(len(coordinates)):
            if((i+1) != len(coordinates)):
                x_diff = float(coordinates[i+1][0]) - float(coordinates[i][0])
                y_diff = float(coordinates[i+1][1]) - float(coordinates[i][1])
                if((x_diff != 0) and (y_diff == 0)):
                    gcode += f'\nG1 X{direction * round((x_diff/10000), 3)} E1'
                elif((y_diff != 0) and (x_diff == 0)):
                    gcode += f'\nG1 Y{direction * round((y_diff/10000), 3)} E1'
                elif((y_diff != 0) and (x_diff != 0)):
                    gcode += f'\nG1 X{direction * round((x_diff/10000), 3)} Y{round((y_diff/10000), 3)} E1'

    return gcode, coordinates[-1] if (wire.layer == print_layer) else cur_position

def generate_pad(pad, component, cur_position, print_layer, extrusion_head):
    """
    Generates GCODE to print pad 
    Inputs:
        pad (Pad): pad to be printed
        component (Component) : component that the pad corresponds to (necessary for orientation, can be modified)
        cur_position (tuple) : XY coordinate of current position of extrusion head
        print_layer (str) : layer that the current subprocess is printing to
        extrusion_head (extrusion_head) : extrusion_head object containing head information
    Outputs:
        gcode (str) : gcode output with pad print information
        coordinates (tuple) : returns center of pad if pad was printed, else returns cur_position which is unchanged from input
    """
    ## move to pad position i need width, height, true position and cur_position
    gcode = ''
    width = (pad.height / 1000) if (abs(component.orientation) == 90) else (pad.width / 1000) ## clean this up
    height = (pad.width / 1000) if (abs(component.orientation) == 90) else (pad.height / 1000)

    pad.true_pos = ((pad.rel_pos[0] + component.pos[0]),(pad.rel_pos[1] + component.pos[1]))
    x_diff = pad.true_pos[0]*10 - float(cur_position[0])
    y_diff = pad.true_pos[1]*10 - float(cur_position[1])


    ## move to pad location, divided by 100 should print in milimiters
    gcode += f'\nG1 F2000'
    gcode += f'\nG1 Z3'
    gcode += f'\nG1 X{round((x_diff/10000), 3)} Y{round((y_diff/10000), 3)}'
    gcode += f'\nG1 Z-3'
    gcode += f'\nG1 F{extrusion_head.trace_speed}'
    ## start in bottom right
    gcode += f'\nG1 X{round((width/2), 3)} Y{round((-height/2),3)} E1'
    short_side = width if (width < height) else height
    long_side = width if (width > height) else height

    ## draw pad boundaries
    gcode += draw_rectangle(width, height)

    ## division/number of 'columns', similar to resolution? use 0.25 increments
    pad_div = int(short_side / 0.25)

    trace_width = short_side / pad_div
    for i in range(pad_div):
        y_print = long_side if (i % 2 == 0) else -long_side
        if(width == short_side):
            gcode += f'\nG1 Y{round(y_print, 3)} E1'
            gcode += f'\nG1 X{round((-trace_width), 3)} E1'
        else:
            gcode += f'\nG1 X{round(-y_print, 3)} E1'
            gcode += f'\nG1 Y{round((trace_width), 3)} E1'
    
    ## finalize the width
    if(i % 2 != 0):
        gcode += f'\nG1 Y{round(long_side, 3)}' if (width == short_side) else f'\nG1 X{round(-long_side, 3)}'

    
    ## go back to center
    gcode += f'\nG1 X{round((width/2), 3)} Y{round((-height/2),3)} E1'

    return gcode, (pad.true_pos[0]*10, pad.true_pos[1]*10) if (pad.layer == print_layer) else cur_position

def generate_via(via, cur_position, extrusion_head):
    """
    Generates GCODE to print via (vias are hardcoded as square pads with 1mm side, printed similar to a pad but in both layers)
    Inputs:
        via (Via): via to be printed
        cur_position (tuple) : XY coordinate of current position of extrusion head
        extrusion_head (extrusion_head) : extrusion_head object containing head information
    Outputs:
        gcode (str) : gcode output with via print information
        via.coords (tuple) : center position of via (via printing starts and ends at same point)
    """

    ## move to pad position i need width, height, true position and cur_position
    gcode = ''
    side = 1
    x_diff = via.coords[0] - float(cur_position[0])
    y_diff = via.coords[1] - float(cur_position[1])

    ## move to via location, divided by 100 should print in milimiters, modyinf speed when moving
    gcode += f'\nG1 F2000'
    gcode += f'\nG1 Z3'
    gcode += f'\nG1 X{round((x_diff/10000), 3)} Y{round((y_diff/10000), 3)}'
    gcode += f'\nG1 Z-3'
    gcode += f'\nG1 F{extrusion_head.trace_speed}'

    ## start in bottom right
    gcode += f'\nG1 X{round((side/2), 3)} Y{round((-side/2), 3)} E1'

    ## division/number of 'columns', similar to resolution?, less than pad bc of side
    pad_div = 4
    trace_width = side / pad_div
    for i in range(pad_div):
        y_print = side if (i % 2 == 0) else -side
        gcode += f'\nG1 Y{round(y_print, 3)} E1'
        gcode += f'\nG1 X{round((-trace_width), 3)} E1'

    ##finalize the width
    gcode += f'\nG1 Y{side} E1'

    ## go back to center
    gcode += f'\nG1 X{round((side/2), 3)} Y{round((-side/2), 3)} E1'

    return gcode, via.coords