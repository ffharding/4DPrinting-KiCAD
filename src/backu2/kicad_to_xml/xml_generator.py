def xml_gen(track_data, component_data):
    """
    Stores track and pad data in custom XML file. Missing information.
    Inputs:
        track_data: XY coordinates of tracks
        component_data: information of components
    Outputs:
        XML_DATA.xml: XML file with custom structure
    """
    xml_file = ''''''
    xml_file = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
    xml_file += "\n<board>"
    xml_file += "\n\t<layers>"
    xml_file += "\n\t\t<f.cu>"
    xml_file += "\n\t\t\t<wire>"
    for track in track_data:
        track = track[0]
        xml_file += "\n\t\t\t\t<track>"
        for coord in track:
            x = coord[0]
            y = coord[1]
            xml_line = "<from>X:" + x + ",Y:" + y + "</from>"
            xml_file += ("\n\t\t\t\t\t" + xml_line)
        xml_file += "\n\t\t\t\t</track>"
    xml_file += "\n\t\t\t</wire>"
    xml_file += "\n\t\t\t<pads>"
    for pad in component_data:
        xml_file += "\n\t\t\t\t<pad>"
        for coord in pad:
            x = coord[0]
            y = coord[1]
            xml_line = "<position>X:" + x + ",Y:" + y + "</position>"
            xml_file += ("\n\t\t\t\t\t" + xml_line)
        xml_line = "<width>56</width>"
        xml_file += ("\n\t\t\t\t\t" + xml_line)
        xml_line = "<type>rectangle</type>"
        xml_file += ("\n\t\t\t\t\t" + xml_line)
        xml_file += "\n\t\t\t\t</pad>"
    xml_file += "\n\t\t\t</pads>"
    xml_file += "\n\t\t</f.cu>"
    xml_file += "\n\t</layers>"
    xml_file += "\n</board>"
    file = open("XML_DATA.xml", "w")
    file.writelines(xml_file)
    file.close()


