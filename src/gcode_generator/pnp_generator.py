pnp_init = """G90  ;Change to absolute coordinates
T4  ;The following settings will apply to the head on T15
M756 S0.1  ;Used in further calculations (0.1mm layer height)
M6 T15 O1 X102.4 Y-23.5 Z0 ;Declare head offsets
M721 S10000 E100 P-100 T15  ;Set unprime values
M722 S10000 E100 P-100 T15  ;Set prime values
M221 S2.5 T15 P100 W0.337 Z0.5  ;Inner diameter of syringe needle tip to be used for T15: 0.337mm
M82  ;Absolute E values
M229 E0 D0  ;Doesn't use custom E values
G28 X0 Y0  ;Send the printer head to the physical home
G92 X0 Y0  ;Reset coordinates
G1 X0 Y0 F2400  ;Go to these coordinates at speed 2400 mm/min
G1 Z10  ;Go to height of 1.22 mm
;M723 S5000 E5350 T15
;M0
M632 H2 S1 P1 T23
G4 S2"""
def PNP_generator(components, holder_location, component_offset):
    gcode = ""
    for component in components:
        offset = component_offset[(component.type).name]
        offset = {'X':0, 'Y':0, 'Z':0} ## erase this after component_offset is correctly imported
        gcode += f";{(component.type).name}"
        gcode += f"G1 X{holder_location['X'] + offset['X']} Y{holder_location['Y'] + offset['Y']} Z{holder_location['Z'] + offset['Z']}"
        gcode += """G4 S4
G1 Z20""" ## added from PNP test.GCODE, dont know if it needs to change
        gcode += f"G1 X{component.pos(0) + offset['X']} Y{component.pos(1) + offset['Y']} Z25"
        gcode += """G1 Z15
M632 H2 S2 T23
G4 S2
M632 H0 S6 V1 P0 T23
G4 S20
G1 Z30 F100
G1 F2400
M632 H2 S1 P1 T23
G4 S2""" ## added from PNP test.GCODE, dont know if it needs to change
    gcode

holder_location = {'X':30, 'Y':130, 'Z':10} ## input from somewhere, probably a XML in export_GCODE.py
component_offset = {} ## dictionary with dictionaries off offsets per component, defaulted to 0 now for testing on line 22
