import re
import generate_functions
def advanced_GCODE_gen(net_list, component_list):
    """
    Convert raw XY data into GCODE file that prints shape
    Inputs:
        raw: XY coordinates of points in shape outline
    Outputs:
        ADVANCED_GENERATED.GCODE: GCODE file
    """
    ## Parse raw data
    # cord_re = re.compile(r'([-\d]+),([-\d]+)')
    # cord_result = cord_re.findall(raw)
    # coordinates = []
    # for cord in cord_result:
    #     coordinates.append([float(cord[0]) / 10, float(cord[1]) / 10])

    ### Header for GCODE
    gcode_init = """G90  ;Change to absolute coordinates
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

    gcode = gcode_init
    coordinates = []
    for net in net_list:
        print(net.name)
        for wire in net.wire_list:
            gcode_result, cur_position = generate_functions.generate_net(wire.coords) ## probably will need changes
            gcode += gcode_result
    
    for component in component_list:
        for pad in component.pad_list:
            # gcode_result, cur_position = generate_functions.generate_pad(pad, cur_position)
            # gcode = gcode_result
            pass

    file = open("ADVANCED_GENERATED.GCODE", "w")
    file.writelines(gcode)
    file.close()
