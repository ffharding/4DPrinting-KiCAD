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
G1 X237.7 E1
G1 X4.0 Y-4.0 E1
G1 Y-2.3 E1
G1 X-1.6 Y-1.6 E1
G1 X-174.6 E1
G1 X-3.1 Y3.1 E1
G1 X-7.4 Y-7.4 E1
G1 Y-3.2 E1
G1 X0.8 Y-0.8 E1
G1 X182.0 E1
G1 X5.5 Y-5.5 E1
G1 Y-132.1 E1
G1 X-16.4 E1
G1 X-5.6 Y5.6 E1
G1 Y119.4 E1
G1 X2.6 Y2.6 E1
G1 X-0.8 Y0.8 E1
G1 X-55.9 E1
G1 Y-120.2 E1
G1 X9.8 Y-9.8 E1
G1 X5.3 Y5.3 E1
G1 Y112.5 E1
G1 X0.8 Y0.8 E1
G1 X26.2 E1
G1 X2.2 Y-2.2 E1
G1 Y-122.2 E1
G1 X-3.5 E1
G1 X-5.8 Y5.8 E1
G1 Y109.3 E1
G1 X-1.0 Y1.0 E1
G1 X-10.2 E1
G1 Y-117.2 E1
G1 X3.7 Y-3.7 E1
G1 X-102.4 E1
G1 X-4.2 Y4.2 E1
G1 Y112.4 E1
G1 X8.8 Y8.8 E1
G1 X16.4 Y-16.4 E1
G1 Y-97.3 E1
G1 X36.9 Y36.9 E1
G1 Y87.4 E1
G1 X-3.0 Y3.0 E1
G1 X-77.1 E1
G1 X-8.5 Y-8.5 E1
G1 Y-123.1 E1
G1 X-4.8 Y4.8 E1
G1 X-56.8 E1