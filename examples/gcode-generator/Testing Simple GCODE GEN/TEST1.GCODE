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
G1 X23.77 E1
G1 X0.4 Y-0.4 E1
G1 Y-0.23 E1
G1 X-0.16 Y-0.16 E1
G1 X-17.46 E1
G1 X-0.31 Y0.31 E1
G1 X-0.74 Y-0.74 E1
G1 Y-0.32 E1
G1 X0.08 Y-0.08 E1
G1 X18.2 E1
G1 X0.55 Y-0.55 E1
G1 Y-13.21 E1
G1 X-1.64 E1
G1 X-0.56 Y0.56 E1
G1 Y11.94 E1
G1 X0.26 Y0.26 E1
G1 X-0.08 Y0.08 E1
G1 X-5.59 E1
G1 Y-12.02 E1
G1 X0.98 Y-0.98 E1
G1 X0.53 Y0.53 E1
G1 Y11.25 E1
G1 X0.08 Y0.08 E1
G1 X2.62 E1
G1 X0.22 Y-0.22 E1
G1 Y-12.22 E1
G1 X-0.35 E1
G1 X-0.58 Y0.58 E1
G1 Y10.93 E1
G1 X-0.1 Y0.1 E1
G1 X-1.02 E1
G1 Y-11.72 E1
G1 X0.37 Y-0.37 E1
G1 X-10.24 E1
G1 X-0.42 Y0.42 E1
G1 Y11.24 E1
G1 X0.88 Y0.88 E1
G1 X1.64 Y-1.64 E1
G1 Y-9.73 E1
G1 X3.69 Y3.69 E1
G1 Y8.74 E1
G1 X-0.3 Y0.3 E1
G1 X-7.71 E1
G1 X-0.85 Y-0.85 E1
G1 Y-12.31 E1
G1 X-0.48 Y0.48 E1
G1 X-5.68 E1
G1 X0.0 Y0.0
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
G1 X0.0 Y15.38
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