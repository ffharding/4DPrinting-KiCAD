from gcode_generator import generate_functions
def advanced_GCODE_gen(filepath, print_layer, net_list, component_list, gcode_header):
    """
    Convert raw XY data into GCODE file that prints shape
    Inputs:
        raw: XY coordinates of points in shape outline
    Outputs:
        ADVANCED_GENERATED.GCODE: GCODE file
    """

    ### Header for GCODE
    # gcode = gcode_init.initialize_GCODE()
    gcode = gcode_header
    cur_position = (0,0)
    for net in net_list:
        for wire in net.wire_list:
            gcode_result, cur_position = generate_functions.generate_net(wire, cur_position, print_layer) ## probably will need changes
            if (wire.layer == print_layer):
                gcode += gcode_result
        for via in net.via_list:
            ## vias will be printed on both layers
            gcode_result, cur_position = generate_functions.generate_via(via, cur_position)
            gcode += gcode_result
    for component in component_list:
        for pad in component.pad_list:
            gcode_result, cur_position = generate_functions.generate_pad(pad, component, cur_position, print_layer)
            if (pad.layer == print_layer):
                gcode += gcode_result

    file = open(f"{filepath}_{print_layer}.GCODE", "w")
    file.writelines(gcode)
    file.close()