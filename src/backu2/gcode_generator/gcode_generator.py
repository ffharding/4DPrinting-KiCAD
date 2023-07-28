from gcode_generator import generate_functions
def GCODE_gen(filepath, print_layer, net_list, component_list, gcode_header):
    """
    Handle generation of front and back GCODE files using parsed net and components information
    Inputs:
        filepath (str): directory where GCODE files are to be saved
        print_layer (str) : layer of PCB GCODE that function will generate
        net_list (list) : list containing net objects
        component_list (list) : list containing component objects
        gcode_header (str) : header of GCODE file imported from extruder head config file
    Outputs:
        .GCODE file : Generated GCODE file in specified directory
    """

    ### Header for GCODE
    gcode = gcode_header
    cur_position = (0,0)
    for net in net_list:
        for wire in net.wire_list:
            gcode_result, cur_position = generate_functions.generate_wire(wire, cur_position, print_layer) ## probably will need changes
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