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
G1 Z0.62 ;Print surface height 2 mm
G91  ;Change to relative coordinates
; Move to initial position
G1 Z5
G1 X120 Y150 ; Center
M6 T15 O1 X0 Y0 Z0 I1 ;Move to declared offset position now
G1 X-30 Y-89.425 ; Bottom left for KiCAD
G1 Z-5
;M0
; Set trace speed
G1 F200
;Printing vias
G1 F2000
G1 Z3
G1 X38.0 Y67.004
G1 Z-3
G1 F200
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
G1 F2000
G1 Z3
G1 X18.0 Y0.0
G1 Z-3
G1 F200
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
G1 F2000
G1 Z3
G1 X-35.0 Y-19.004
G1 Z-3
G1 F200
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
G1 F2000
G1 Z3
G1 X11.0 Y-4.0
G1 Z-3
G1 F200
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
;Printing pads
;Printing traces
G1 F2000
G1 Z3
G1 X24.0 Y23.004
G1 Z-3
G1 F200
G1 X-18.0 E1
G1 X18.0 E1
G1 X-18.0 E1
G1 F2000
G1 Z3
G1 X-17.0 Y-19.004
G1 Z-3
G1 F200
G1 X11.0 E1
G1 Y-4.0 E1
G1 X-11.0 E1
G1 Y4.0 E1
G1 X11.0 E1
G1 Y-4.0 E1