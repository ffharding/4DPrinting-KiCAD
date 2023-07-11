import xml.etree.ElementTree as ET
class extruder_head():
    '''
    Summary:
        extruder_head class stores head information parser from xml config file

    Attributes:
        name (str): Assigned name of net 
        yoke (str): mounting device
        slot (str) : header slot
        target_head (str) : identifier for chosen head
        head_offset (dict) : dictionary containg XYZ coordinates of head offset
        retraction_speed (str) : speed at which unprime moves should be executed; this is normally 10,000
        motor_steps (str) : number of pulses on the feed (extrusion) motor to execute
        retract_delay (str) : number of milliseconds relative to the end of the move to begin the unprime (retract) action; a negative
        syringe_parameter (str) : syringe needle setup parameter (M221 by specification as of 7/7/2023)
        homing_sequence (str) : sequence setting up relative origin for coordinates
        cleareance (str) : height clearance for movement
        trace_speed (str) : speed of trace movements whlie prining
    '''
    def __init__(self, config_xml_path):
        config_tree = ET.parse(config_xml_path)
        config_root = config_tree.getroot()
        self.parse_params(*config_root)

    def parse_params(self, head_init, retraction_settings, syringe_setup, homing_sequence, init_sequence, trace_setup):
        """
        Converts XML XYZ head offset in to a dictionary with coordinates
        Inputs:
            *config_root : unpacked list of xml root object containg head config information
        """
        self.yoke = head_init.find('yoke').text
        self.slot = head_init.find('slot').text
        self.target_head = f'{self.yoke}{self.slot}'
        self.head_offset = self.get_headoffset(head_init)

        self.retraction_speed = retraction_settings.find('retraction_speed').text 
        self.motor_steps = retraction_settings.find('motor_steps').text  #
        self.retract_delay = retraction_settings.find('retract_delay').text

        self.syringe_parameter = syringe_setup.find('syringe_parameter').text

        self.homing_sequence = homing_sequence ## Nothing for now

        self.clearance = init_sequence.find('clearance').text

        self.trace_speed = trace_setup.find('trace_speed').text


    def get_headoffset(self, head_init):
        """
        Converts XML XYZ head offset in to a dictionary with coordinates
        Inputs:
            head_init: xml root object containing head initialization branch
        Outputs:
            ADVANCED_GENERATED.GCODE: GCODE file
        """
        head_offset_dict = {}
        for coord in head_init.find('head_offset'):
            head_offset_dict[coord.tag] = coord.text
        return head_offset_dict

def initialize_GCODE(extrusion_head):
    '''
        Initialize GCODE with specified extrusion head
    '''
    """
    Initialize GCODE with specified extrusion head
    Inputs:
        extrusion_head: extrusion head name (make sure that matches config file)
    Outputs:
        gcode_init: GCODE initialization header
    """
    head = extruder_head(f'config\{extrusion_head}_config.xml')
    
    head_init = f"""G90  ;Change to absolute coordinates
T{head.target_head}  ;The following settings will apply to the head on T15
M756 S0.1  ;Used in further calculations (0.1mm layer height)"""
    
    head_offset_declaration = 'M6 T' + head.target_head + ' O1 X' + head.head_offset['X'] + ' Y' + head.head_offset['Y'] + ' Z' + head.head_offset['Z'] + '  ;Declare head offsets' ## this format allows dictionary use
    
    retraction_settings = f"""M721 S{head.retraction_speed} E{head.motor_steps} P{head.retract_delay} T{head.target_head}  ;Set unprime values
M722 S{head.retraction_speed} E{head.motor_steps} P{head.retract_delay} T{head.target_head}  ;Set prime values"""
    
    syringe_setup = f"""M{head.syringe_parameter} S1.8 T15 P100 W0.337 Z0.5  ;Inner diameter of syringe needle tip to be used for T15: 0.337mm
M82  ;Absolute E values
M229 E0 D0  ;Doesn't use custom E values"""
    
    homing_sequence = """G28 X0 Y0  ;Send the printer head to the physical home
G92 X0 Y0  ;Reset coordinates
G1 X0 Y0 F2400  ;Go to these coordinates at speed 2400 mm/min
G1 Z0  ;Go to height of 0 mm
G91  ;Change to relative coordinates"""

    init_sequence = f"""; Move to initial position
G1 Z2 ;Print surface height 2 mm
G1 Z{head.clearance}
M6 T15 O1 X0 Y0 Z0 I1 ;Move to declared offset position now
G1 X277.5 Y84.5
G1 X-11.5 Y2
G1 Z-{head.clearance}"""
    
    trace_setup = f"""; Set trace speed
G1 F{head.trace_speed}"""

    gcode_init = f'{head_init}\n{head_offset_declaration}\n{retraction_settings}\n{syringe_setup}\n{homing_sequence}\n{init_sequence}\n{trace_setup}'
    
    return gcode_init
