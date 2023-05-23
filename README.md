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

## Components
### 4DPrinting.pretty
The .pretty folder is a KiCAD library containing custom component footprints created for the base schematic of the projcet, inlcuding components designed to be printed and those components that were modified to fit the specifications of the project (through hole to surface mount components). 

| Component      | Description |
| ------------- |:-------------:|
| Battery.kicad_mod      | Footprint for battery cell pack connected with flywires to +/- pads     |
| MODULE_ESP-M2.kicad_mod      | Footprint for ESP-M2 wifi chip downloaded from SnapEDA: https://www.snapeda.com/parts/ESP-M2/Doctors%20of%20Intelligence%20%26%20Technology%20Co.%2C%20LTD/view-part/?ref=search&t=%20ESP-M2%20    |
| TPU.kicad_mod      | Footprint for printed unit TPU   |
| charge_port.kicad_mod      | Footprint for 3.5mm charging port for battery   |
| custom_lf356.kicad_mod      | Footprint for LF356 chip converted to surface mount device |
| switch.kicad_mod      | Footprint for push button switch |
| voltage_regulator.kicad_mod      | Footprint for LD1117v33 voltage regulator converted to surface mount device |

## Installation
Clone repository into local machine using the following commmands in terminal or Git Bash:
```
git clone https://github.com/ffharding/4DPrinting-KiCAD.git
```
More information into Git repositories can be found on the [offical Git documentation](https://docs.github.com/en/repositories).

After cloning the repository and installing the required software([KiCAD 6.0](https://www.kicad.org/download/) and [freerouting](https://github.com/freerouting/freerouting/releases
)), open the plugin directory from KiCAD using the instructions included in the documentation folder and copy the source code of the feature to test.
