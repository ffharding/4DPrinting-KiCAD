from gcode_generator import generate_functions
def GCODE_gen(filepath, print_layer, net_list, component_list, gcode_header, extrusion_head):
    """
    Handle generation of front and back GCODE files using parsed net and components information
    Inputs:
        filepath (str): directory where GCODE files are to be saved
        print_layer (str) : layer of PCB GCODE that function will generate
        net_list (list) : list containing net objects
        component_list (list) : list containing component objects
        gcode_header (str) : header of GCODE file imported from extruder head config file
        extrusion_head (extrusion_head) : extrusion_head object containing head information
    Outputs:
        .GCODE file : Generated GCODE file in specified directory
    """

    ### Header for GCODE

    gcode = gcode_header
    cur_position = (0,0)
    gcode += "\n;Printing vias"
    for net in net_list:
        for via in net.via_list:
            ## vias will be printed on both layers, if it is top layer, print 3 pads with 0.5
            if(print_layer == 'F.Cu'):
                gcode += "\nG1 Z-1" ## move down
                for i in range(2):
                    gcode_result, cur_position = generate_functions.generate_via(via, cur_position, extrusion_head)
                    gcode += gcode_result
                    gcode += "\nG1 Z0.5 E1"
            gcode_result, cur_position = generate_functions.generate_via(via, cur_position, extrusion_head)
            gcode += gcode_result
    gcode += "\n;Printing pads"
    for component in component_list:
        for pad in component.pad_list:
            gcode_result, cur_position = generate_functions.generate_pad(pad, component, cur_position, print_layer, extrusion_head)
            if (pad.layer == print_layer):
                gcode += gcode_result
    gcode += "\n;Printing traces"
    for net in net_list:
        for wire in net.wire_list:
            gcode_result, cur_position = generate_functions.generate_wire(wire, cur_position, print_layer, extrusion_head) ## probably will need changes
            if (wire.layer == print_layer):
                gcode += gcode_result 

    file = open(f"{filepath}_{print_layer}.GCODE", "w")
    file.writelines(gcode)
    file.close()