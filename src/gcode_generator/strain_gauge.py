def generate_pad(height, width):
    """
    Generates GCODE to print pad 
    Inputs:
        pad (Pad): pad to be printed
        component (Component) : component that the pad corresponds to (necessary for orientation, can be modified)
        cur_position (tuple) : XY coordinate of current position of extrusion head
        print_layer (str) : layer that the current subprocess is printing to
    Outputs:
        gcode (str) : gcode output with pad print information
        coordinates (tuple) : returns center of pad if pad was printed, else returns cur_position which is unchanged from input
    """
    ## move to pad position i need width, height, true position and cur_position
    gcode = ''
    width = width ## clean this up
    height = height

    ## start in bottom right
    gcode += f'\nG1 X{width/2} Y{-height/2} E1'

    ## division/number of 'columns', similar to resolution?
    pad_div = 10
    trace_width = width / pad_div
    for i in range(pad_div):
        y_print = height if (i % 2 == 0) else -height
        gcode += f'\nG1 Y{y_print} E1'
        gcode += f'\nG1 X{-trace_width} E1'
    
    ## finalize the width
    gcode += f'\nG1 Y{height} E1'
    
    ## go back to center
    gcode += f'\nG1 X{width/2} Y{-height/2} E1'

    return gcode

def generate_wire(current_position, end_position):
    ## take current position (assume x direction for now)
    x_diff = end_position [0] - current_position[0]
    y_diff = end_position [1] - current_position[1]

    gcode = f'\nG1 X{x_diff} Y{y_diff} E1'

    return gcode

