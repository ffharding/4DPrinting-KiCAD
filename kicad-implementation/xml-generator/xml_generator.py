import os

# raw_data = [[('145290000', '-83820000'), ('137947500', '-83820000'), ('163070000', '-66040000'), ('145290000', '-83820000')]], [[('163890000', '-74829000'), ('162294700', '-74829000'), ('152495000', '-84628700'), ('137181200', '-84628700'), ('162294700', '-74829000'), ('152495000', '-84628700'), ('137181200', '-84628700'), ('136372500', '-83820000')]]
# track_data = [[[('136372500', '-83820000')]], [[('137947500', '-83820000')]], [[('162050000', '-66040000')]], [[('163070000', '-66040000')]], [[('134530000', '-74829000')]], [[('163890000', '-74829000')]], [[('144914300', '-66040000'), ('162050000', '-66040000'), ('136125300', '-74829000'), ('144914300', '-66040000'), ('134530000', '-74829000'), ('136125300', '-74829000')]], [[('145290000', '-83820000'), ('137947500', '-83820000'), ('163070000', '-66040000'), ('145290000', '-83820000')]], [[('163890000', '-74829000'), ('162294700', '-74829000'), ('152495000', '-84628700'), ('137181200', '-84628700'), ('162294700', '-74829000'), ('152495000', '-84628700'), ('137181200', '-84628700'), ('136372500', '-83820000')]]]
# pad_data = [[[('136372500', '-83820000')]]]
# raw_data = raw_data[0][0]
def xml_gen(track_data, pad_data):
    """
    Stores track and pad data in custom XML file. Missing information.
    Inputs:
        track_data: XY coordinates of tracks
        pad_data: XY coordinates of pads
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
    for pad in pad_data:
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

# xml_gen(track_data, pad_data)

