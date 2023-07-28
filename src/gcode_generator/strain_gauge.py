#### wire thickness, clearance, full width, full height

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

gcode = """G90  ;Change to absolute coordinates
T15  ;The following settings will apply to the head on T15
M756 S0.1  ;Used in further calculations (0.1mm layer height)
M6 T15 O1 X0 Y0 Z0  ;Declare head offsets
M721 S10000 E100 P-100 T15  ;Set unprime values
M722 S10000 E100 P-100 T15  ;Set prime values
M221 S1.8 T15 P100 W0.337 Z0.5  ;Inner diameter of syringe needle tip to be used for T15: 0.337mm
M82  ;Absolute E values
M229 E0 D0  ;Doesn't use custom E values
G28 X0 Y0  ;Send the printer head to the physical home
G92 X0 Y0  ;Reset coordinates
G1 X0 Y0 F2400  ;Go to these coordinates at speed 2400 mm/min
G1 Z2  ;Go to height of 2 mm
G91  ;Change to relative coordinates
; Move to initial position
G1 Z5
G1 X277.5 Y84.5
G1 X-11.5 Y2
G1 Z-5
; Set trace speed
G1 F400"""
gcode += generate_pad(2, 2)
gcode += generate_wire((266, 86.5), (246, 86.5))
file = open(r"gcode_generator\test.GCODE", "w")
file.writelines(gcode)
file.close()

