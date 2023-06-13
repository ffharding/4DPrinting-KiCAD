import re
import math
class Component:
    def __init__(self, id, pos, side, orientation, type):
        self.id = id
        self.pos = pos
        self.side = side
        self.orientation = float(orientation)
        self.type = type
        self.pad_list = type.pad_list
        
class ComponentType:
    def __init__(self, type, outline, keepout, pad_list):
        self.type = type
        self.outline = outline
        self.keepout = keepout
        self.pad_list = pad_list
    def __str__(self):
        return f"{self.type}"
    
class PadType:
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
    
class Pad():
    def __init__(self, type, number, rel_pos,orientation = 0):
        self.number = number
        self.type = type
        self.rel_pos = (float(rel_pos[0]), float(rel_pos[1]))
        self.orientation = float(orientation) if (orientation != '') else orientation

        self.width = type.width
        self.height = type.height
        self.diameter = type.diameter
        self.shape = type.shape
        self.true_pos = None


def getComponents(data):

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
        pads = [Pad(padTypes[pad[0]], pad[3], (pad[4], pad[5]), pad[2]) for pad in pad_list]
        componentType = ComponentType(name, outline, keepout, pads)
        componentTypes.update({str(componentType): componentType})

    ### Get component information
    components_regex = re.compile(
        r'(\(component "?([^\s\"]+)"?[\s\S]*?(?=\s+\(component|\s+\)\s+\(library))'
        )
    components_results = components_regex.findall(data)       

    ## Complete component and pad information
    components = []
    component_regex = re.compile(
        r'\(place (\S+) ([\d\.-]+) ([\d\.-]+) (\w+) ([\d\.-]+)'
        )

    for match in components_results:
        component_result = component_regex.findall(match[0])
        for component in component_result:
            temp = list(component)
            componentType = componentTypes[match[1]]
            classy_component = Component(temp[0], (float(temp[1]), float(temp[2])), temp[3], float(temp[4]), componentType)
            components.append(classy_component)

    return components