G90  ;Change to absolute coordinates
T15  ;The following settings will apply to the head on T15
M756 S0.1  ;Used in further calculations (0.1mm layer height)
M6 T15 O1 X0 Y0 Z0  ;Declare head offsets
M721 S10000 E100 P-100 T15  ;Set unprime values
M722 S10000 E100 P-100 T15  ;Set prime values
M221 S1.8 T15 P100 W0.337 Z0.5  ;Inner diameter of syringe needle tip to be used for T15: 0.337mm
M82  ;Absolute E values
M229 E0 D0  ;Doesn't use custom E values
G28 X0 Y0  ;Send the printer head to the physical home
G92 X0 Y0  ;Reset coordinates
G1 X0 Y0 F2400  ;Go to these coordinates at speed 2400 mm/min
G1 Z2  ;Go to height of 2 mm
G91  ;Change to relative coordinates
; Move to initial position
G1 Z5
G1 X277.5 Y84.5
G1 X-11.5 Y2
G1 Z-5
; Set trace speed
G1 F400
G1 Z2
G1 X128.49 Y-82.39
G1 Z-2
G1 X-5.1002 E1
G1 Y-15.38 E1
G1 X5.1002 E1
G1 Z2
G1 X0.0 Y0.0
G1 Z-2
G1 X1.0 Y-1.77 E1
G1 Y3.54 E1
G1 X-0.2 E1
G1 Y-3.54 E1
G1 X-0.2 E1
G1 Y3.54 E1
G1 X-0.2 E1
G1 Y-3.54 E1
G1 X-0.2 E1
G1 Y3.54 E1
G1 X-0.2 E1
G1 Y-3.54 E1
G1 X-0.2 E1
G1 Y3.54 E1
G1 X-0.2 E1
G1 Y-3.54 E1
G1 X-0.2 E1
G1 Y3.54 E1
G1 X-0.2 E1
G1 Y-3.54 E1
G1 X-0.2 E1
G1 Y3.54 E1
G1 X1.0 Y-1.77 E1
G1 Z2
G1 X0.0 Y15.38
G1 Z-2
G1 X1.0 Y-1.77 E1
G1 Y3.54 E1
G1 X-0.2 E1
G1 Y-3.54 E1
G1 X-0.2 E1
G1 Y3.54 E1
G1 X-0.2 E1
G1 Y-3.54 E1
G1 X-0.2 E1
G1 Y3.54 E1
G1 X-0.2 E1
G1 Y-3.54 E1
G1 X-0.2 E1
G1 Y3.54 E1
G1 X-0.2 E1
G1 Y-3.54 E1
G1 X-0.2 E1
G1 Y3.54 E1
G1 X-0.2 E1
G1 Y-3.54 E1
G1 X-0.2 E1
G1 Y3.54 E1
G1 X1.0 Y-1.77 E1