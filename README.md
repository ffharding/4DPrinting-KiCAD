# 4DPrinting KiCAD Repository
The objective of the repository is to store the files needed to implement KiCAD automating into the design flow of the 4DPrinting project, including code to automatically generate files and custom components.

## Features 
### 1. kicad-import
This features consist on the code required to import the user input such as the components chosen by the user, the desired placement of these components and the information that relate the components (what the final PCB is designed for). The output of this feature is the base KICAD file that starts the automating design flow.
### 2. autorouting
Autoroute the PCB created using the freerouting open source module and automate the creation of the finished PCB that will be printed.
### 3. xml-generator
Generate an XML file with the already finished and autorouted PCB for better data management.
### 4. gcode-generator
Generate GCODE from the XML file with PCB data.
