import re
import math
def rotate(orientation, x, y):
    """
    Rotate the pad counterclockwise using math calculations for position
    Inputs:
        orientation (int): angle at which point needs to be rotated to relative to origin
        x (int) : x coordinate of point
        y (int) : y coordinate of point
    Outputs:
        x (int) : x coordinate of rotated point
        y (int) : y coordinate of rotated point
    """
    rad_sin = math.sin(math.radians(orientation))
    rad_cos = math.cos(math.radians(orientation))
    x, y = (rad_cos * x - rad_sin * y, rad_sin * x + rad_cos * y)

    return x, y

class Component:
    '''
    Summary:
        Component class stores component information for easier unpacking

    Attributes:
        id (str): Assigned name of component
        pos (tuple): XY position of component relative to board origin
        side (str) : side at which the component is placed
        orientation (float) : orientation at whcih the component is placed
        type (ComponentType) : user defined class containing component type information
        pad_list (list) : list of Pad objects imported from component type
    '''
    def __init__(self, id, pos, side, orientation, type):
        self.id = id
        self.pos = pos
        self.side = side
        self.orientation = float(orientation)
        self.type = type
        self.pad_list = type.pad_list

        self.fix_pad_position(self.pad_list, self.pos, self.orientation)
        
    def fix_pad_position(self, pad_list, component_pos, component_orientation):
        '''
            Fixes the position of pads in component's pad_list to
            true position instead of relative position
        '''
        for pad in pad_list:
            pad.calc_true_pos(component_pos, component_orientation)
class ComponentType:
    '''
    Summary:
        Component type stores global component information

    Attributes:
        type (str): name of component type
        outline (str): information of component outline (drawing)
        keepout (str) : component routing keepout limits
        pad_list (list) : list of Pad objects to the corresponding components
    '''
    def __init__(self, type, outline, keepout, pad_list):
        self.type = type
        self.outline = outline
        self.keepout = keepout
        self.pad_list = pad_list
    def __str__(self):
        return f"{self.type}"
    
class PadType:
    '''
    Summary:
        Pad type stores global pad information

    Attributes:
        type (str): name of pad type
        shape (str): name of pad shape
        layer (str) : layer where the pad is placed
        shapeData (list) : important measurements for pad printing(width/height or diameter)
    '''
    def __init__(self, type, shape, layer, shapeData):
        self.type = type
        self.shape = shape
        self.layer = layer
        self.shapeData = shapeData.split(' ')

        self.width = None
        self.height = None
        self.diameter = None

        self.DesignShape(self.shape, self.shapeData)

    def __str__(self):
        return f"{self.type}"
    
    def DesignShape(self, shape, shapeData):
        '''
            Given shape and shapeData, design necessary values
            to plot pad
        '''
        if shape == 'rect':
            self.width = float(shapeData[2]) - float(shapeData[0])
            self.height = float(shapeData[3]) - float(shapeData[1])
        elif shape == 'circle':
            self.diameter = float(shapeData[0])
    
class Pad:
    '''
    Summary:
        Pad class containing individual pad information

    Attributes:
        number (int) : reference number of pad relative to component pin number
        type (PadType) : PadType object containing general pad information 
        rel_pos (tuplke) : pad position relative to component
        orientation (float) : pad orientation relative to default component orientation
        layer (str) : layer where the pad is placed (imported from PadType)
        width (float) : horizontal width of pad (imported from PadType)
        height (float) : vertical height of pad (imported from PadType)
        diameter (float) : diameter of pad (imported from PadType)
        shape (str) : shape of pad (imported from PadType)
        true_pos (tuple) : true position of the pad relative to the board 

    '''
    def __init__(self, type, number, rel_pos,orientation = 0):
        self.number = number
        self.type = type
        self.rel_pos = (float(rel_pos[0]), float(rel_pos[1]))
        self.orientation = float(orientation) if (orientation != '') else orientation
        self.layer = type.layer
        
        self.width = type.width
        self.height = type.height
        self.diameter = type.diameter
        self.shape = type.shape
        self.true_pos = None
    def calc_true_pos(self, component_pos, component_orientation):
        ''' 
            Calculate the true position of pad using position of
            component and relative position, considering orientation of component as well
        '''
        self.rel_pos = rotate(component_orientation, self.rel_pos[0], self.rel_pos[1]) if (component_orientation != 0)  else self.rel_pos
        self.true_pos = (component_pos[0] + self.rel_pos[0], component_pos[1] + self.rel_pos[1])


def getComponents(data):
    """
    Parses data from Specctra DSN file into a list of components containing routing information
    Inputs:
        data (str): Specctra DSN file data
    Outputs:
        component_list (list): list of components parsed into Component user classes
    """
    ## Get pad type and pad shape information 
    padtype_regex = re.compile(
        r'(\(padstack "?([^\s\"]+)"?[\s\S]*?(?=\s+\(padstack|\s+\)\s+\)))'
        )

    padshape_regex = re.compile(
        r'shape \((\w+) (\S+) ([-\d.\s]+)'
        )

    padtype_result = padtype_regex.findall(data)

    padTypes = {}
    for match in padtype_result:
        padshape_result = padshape_regex.findall(match[0])
        for pad in padshape_result:
            padType = list(pad)
            padType = PadType(match[1], pad[0], pad[1], pad[2])
            padTypes.update({str(padType): padType})


    ### Get component type information
    component_type_regex = re.compile(
        r'(\(image "?([^\s\"]+)"?[\s\S]*?(?=\s+\(image|\s+\)\s+\)|\s+\(padstack))'
        )
    component_type_result = component_type_regex.findall(data)

    component_type_outline_regex = re.compile(r'\(outline[^\n]+')
    componen_type_pin_regex = re.compile(r'\(pin (\S+) (\(rotate ([-\d]+)\) )*(\d+) ([-\d\.]+) ([-\d\.]+)')
    component_type_keepout_regex = re.compile(r'\(((keepout|via_keepout)[\s\S]*?(?=\)\)))')


    componentTypes = {}
    for match in component_type_result:
        name = match[1]
        outline = component_type_outline_regex.findall(match[0])
        keepout = component_type_keepout_regex.findall(match[0])
        pad_list = componen_type_pin_regex.findall(match[0])
        pads = [Pad(padTypes[pad[0]], int(pad[3]), (pad[4], pad[5]), pad[2]) for pad in pad_list]
        componentType = ComponentType(name, outline, keepout, pads)
        componentTypes.update({str(componentType): componentType})

    ### Get component information
    components_regex = re.compile(
        r'(\(component "?([^\s\"]+)"?[\s\S]*?(?=\s+\(component|\s+\)\s+\(library))'
        )
    components_results = components_regex.findall(data)       

    ## Complete component and pad information
    component_list = []
    component_regex = re.compile(
        r'\(place (\S+) ([\d\.-]+) ([\d\.-]+) (\w+) ([\d\.-]+)'
        )

    for match in components_results:
        component_result = component_regex.findall(match[0])
        for component in component_result:
            temp = list(component)
            componentType = componentTypes[match[1]]
            classy_component = Component(temp[0], (float(temp[1]), float(temp[2])), temp[3], float(temp[4]), componentType)
            component_list.append(classy_component)
    return component_list