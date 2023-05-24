import re

class Component:
    def __init__(self, id, coords, side, orientation, name):
        self.id = id
        self.coords = coords
        self.side = side
        self.orientation = orientation
        self.name = name
class PadType:
    def __init__(self, name, shape, layer, shapeData):
        self.name = name
        self.shape = shape
        self.layer = layer
        self.shapeData = shapeData.split(' ')

        self.width = None
        self.height = None
        self.diameter = None

        self.DesignShape(self.shape, self.shapeData)

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

class ComponentType:
    def __init__(self, name, outline, keepout, pins):
        self.name = name
        self.outline = outline
        self.keepout = keepout
        self.pins = pins
    

file = open(r'kicad-files-components\SensorTemp.dsn', 'r')
data = file.read()
file.close()


## Get pad type information (\S+)\s+(\(shape \((\w+) (\S+) ([-\d\.\s]+)\)\))
padtype_regex = re.compile(
    r'(\(padstack "?([^\s\"]+)"?[\s\S]*?(?=\s+\(padstack|\s+\)\s+\)))'
    )

padshape_regex = re.compile(
    r'shape \((\w+) (\S+) ([-\d.\s]+)'
    )

padtype_result = padtype_regex.findall(data)
pads = []
for match in padtype_result:
    padshape_result = padshape_regex.findall(match[0])
    for pad in padshape_result:
        pad = list(pad)
        pad = PadType(match[1], pad[0], pad[1], pad[2])
        pads.append(pad)

### Get component type information
componentType_regex = re.compile(
    r'(\(image "?([^\s\"]+)"?[\s\S]*?(?=\s+\(image|\s+\)\s+\)|\s+\(padstack))'
    )
componentType_result = componentType_regex.findall(data)

componentTypeOutline_regex = re.compile(r'\(outline[^\n]+')
componentTypePin_regex = re.compile(r'\(pin (\S+) (\d+) ([-\d\.]+) ([-\d\.]+)')
componentTypeKeepout_regex = re.compile(r'\(((keepout|via_keepout)[\s\S]*?(?=\)\)))')


componentTypes = [] ## Dictionaries will probably be better on the long term
for match in componentType_result:
    name = match[1]
    outline = componentTypeOutline_regex.findall(match[0])
    keepout = componentTypeKeepout_regex.findall(match[0])
    pins = componentTypePin_regex.findall(match[0])
    componentType = ComponentType(name, outline, keepout, pins)
    componentTypes.append(componentType)


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
        classy_component = Component(temp[0], (float(temp[1]), float(temp[2])), temp[3], float(temp[4]), match[1])
        components.append(classy_component)

