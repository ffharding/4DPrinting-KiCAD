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
G1 Z0  ;Go to height of 0 mm
G91  ;Change to relative coordinates
; Move to initial position
G1 Z2 ;Print surface height 2 mm
G1 Z5
M6 T15 O1 X0 Y0 Z0 I1 ;Move to declared offset position now
G1 X277.5 Y84.5
G1 X-11.5 Y2
G1 Z-5
; Set trace speed
G1 F400
G1 Z2
G1 X46.7982 Y43.5594
G1 Z-2
G1 Y-24.7002 E1
G1 Z2
G1 X-3.6294 Y24.7002
G1 Z-2
G1 X3.6294 E1
G1 Z2
G1 X3.8956 Y24.7245
G1 Z-2
G1 Y-24.7245 E1
G1 X-3.8956 E1
G1 Z2
G1 X3.8956 Y24.7245
G1 Z-2
G1 X0.5 Y-0.5 E1
G1 Y1 E1
G1 X-0.25 E1
G1 Y-1 E1
G1 X-0.25 E1
G1 Y1 E1
G1 X-0.25 E1
G1 Y-1 E1
G1 X-0.25 E1
G1 Y1 E1
G1 X0.5 Y-0.5 E1
G1 Z2
G1 X-7.525 Y-24.7245
G1 Z-2
G1 X0.5 Y-0.5 E1
G1 Y1 E1
G1 X-0.25 E1
G1 Y-1 E1
G1 X-0.25 E1
G1 Y1 E1
G1 X-0.25 E1
G1 Y-1 E1
G1 X-0.25 E1
G1 Y1 E1
G1 X0.5 Y-0.5 E1
G1 Z2
G1 X3.6294 Y-24.7002
G1 Z-2
G1 X0.5 Y-0.5 E1
G1 Y1 E1
G1 X-0.25 E1
G1 Y-1 E1
G1 X-0.25 E1
G1 Y1 E1
G1 X-0.25 E1
G1 Y-1 E1
G1 X-0.25 E1
G1 Y1 E1
G1 X0.5 Y-0.5 E1
G1 Z2
G1 X-15.4859 Y36.9224
G1 Z-2
G1 Y5.6771 E1
G1 X6.7726 E1
G1 Z2
G1 X0.0 Y0.0
G1 Z-2
G1 X0.5 Y-0.5 E1
G1 Y1 E1
G1 X-0.25 E1
G1 Y-1 E1
G1 X-0.25 E1
G1 Y1 E1
G1 X-0.25 E1
G1 Y-1 E1
G1 X-0.25 E1
G1 Y1 E1
G1 X0.5 Y-0.5 E1
G1 Z2
G1 X-6.7726 Y-5.6771
G1 Z-2
G1 X0.5 Y-0.5 E1
G1 Y1 E1
G1 X-0.25 E1
G1 Y-1 E1
G1 X-0.25 E1
G1 Y1 E1
G1 X-0.25 E1
G1 Y-1 E1
G1 X-0.25 E1
G1 Y1 E1
G1 X0.5 Y-0.5 E1
G1 Z2
G1 X0.569 Y-42.9961
G1 Z-2
G1 Y39.288 E1
G1 Z2
G1 X0.0 Y-39.288
G1 Z-2
G1 X0.5 Y-0.5 E1
G1 Y1 E1
G1 X-0.25 E1
G1 Y-1 E1
G1 X-0.25 E1
G1 Y1 E1
G1 X-0.25 E1
G1 Y-1 E1
G1 X-0.25 E1
G1 Y1 E1
G1 X0.5 Y-0.5 E1
G1 Z2
G1 X0.0 Y39.288
G1 Z-2
G1 X0.5 Y-0.5 E1
G1 Y1 E1
G1 X-0.25 E1
G1 Y-1 E1
G1 X-0.25 E1
G1 Y1 E1
G1 X-0.25 E1
G1 Y-1 E1
G1 X-0.25 E1
G1 Y1 E1
G1 X0.5 Y-0.5 E1