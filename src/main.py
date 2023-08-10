import export_GCODE
import import_board

def run():
    '''
        Summary:
            import_board: manage the creation of KiCAD files and the importing of information from XML and netlist
            export_GCODE: use the .ses and .dsn files created by import_board and generate GCODE
    '''
    import_board.start()
    export_GCODE.start()