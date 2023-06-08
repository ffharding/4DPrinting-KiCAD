### Add one operation line at a time using the coordinates
def generate_net(coordinates):
    gcode = ''
    for i in range(len(coordinates)):
        cur_position = coordinates[i]
        if((i+1) != len(coordinates)):
            x_diff = float(coordinates[i+1][0]) - float(coordinates[i][0])
            y_diff = float(coordinates[i+1][1]) - float(coordinates[i][1])
            if((x_diff != 0) and (y_diff == 0)):
                gcode += f'\nG1 X{x_diff/1000} E1'
            elif((y_diff != 0) and (x_diff == 0)):
                gcode += f'\nG1 Y{y_diff/1000} E1'
            elif((y_diff != 0) and (x_diff != 0)):
                gcode += f'\nG1 X{x_diff/1000} Y{y_diff/1000} E1'
    print(gcode)
    return gcode, cur_position

def generate_pad(pad, cur_position):
    ##move to pad position
    print(pad)