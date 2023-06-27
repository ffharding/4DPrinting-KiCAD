### Add one operation line at a time using the coordinates
def generate_net(wire, cur_position, print_layer):
    gcode = ''
    coordinates = wire.coords

    ## move to start of next net
    x_diff = float(coordinates[0][0]) - float(cur_position[0])
    y_diff = float(coordinates[0][1]) - float(cur_position[1])
    gcode += f'\nG1 Z2'
    gcode += f'\nG1 X{x_diff/10000} Y{y_diff/10000}'
    gcode += f'\nG1 Z-2'
    for i in range(len(coordinates)):
        if((i+1) != len(coordinates)):
            x_diff = float(coordinates[i+1][0]) - float(coordinates[i][0])
            y_diff = float(coordinates[i+1][1]) - float(coordinates[i][1])
            if((x_diff != 0) and (y_diff == 0)):
                gcode += f'\nG1 X{x_diff/10000}'
            elif((y_diff != 0) and (x_diff == 0)):
                gcode += f'\nG1 Y{y_diff/10000}'
            elif((y_diff != 0) and (x_diff != 0)):
                gcode += f'\nG1 X{x_diff/10000} Y{y_diff/10000}'
            gcode = (gcode + ' E1') if (wire.layer == print_layer) else gcode
    cur_position = coordinates[-1]

    return gcode, cur_position

def generate_pad(pad, component, cur_position, print_layer):

    ##move to pad position i need width, height, true position and cur_position
    gcode = ''
    width = (pad.height / 1000) if (abs(component.orientation) == 90) else (pad.width / 1000) ## clean this up
    height = (pad.width / 1000) if (abs(component.orientation) == 90) else (pad.height / 1000)

    x_diff = pad.true_pos[0]*10 - float(cur_position[0])
    y_diff = pad.true_pos[1]*10 - float(cur_position[1])

    ## move to pad location, divided by 100 should print in milimiters
    gcode += f'\nG1 Z2'
    gcode += f'\nG1 X{x_diff/10000} Y{y_diff/10000}'
    gcode += f'\nG1 Z-2'
    ## start in bottom right
    gcode += f'\nG1 X{width/2} Y{-height/2} E1' if (pad.layer == print_layer) else f'\nG1 X{width/2} Y{-height/2}'

    ##division/number of 'columns', similar to resolution?
    pad_div = 10
    trace_width = width / pad_div
    for i in range(pad_div):
        y_print = height if (i % 2 == 0) else -height
        gcode += f'\nG1 Y{y_print} E1' if (pad.layer == print_layer) else f'\nG1 Y{y_print}'
        gcode += f'\nG1 X{-trace_width} E1' if (pad.layer == print_layer) else f'\nG1 X{-trace_width}'
    
    ##finalize the width
    gcode += f'\nG1 Y{height} E1' if (pad.layer == print_layer) else f'\nG1 Y{height}'
    
    ## go back to center
    gcode += f'\nG1 X{width/2} Y{-height/2} E1' if (pad.layer == print_layer) else f'\nG1 X{width/2} Y{-height/2}'

    return gcode, (pad.true_pos[0]*10, pad.true_pos[1]*10)
