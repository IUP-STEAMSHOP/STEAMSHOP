# Original Prusa MINI+

!!! info "Manual"
    📄 [Download Official Manufacturer Manual](manual.docx)

---


## SAFETY FIRST (READ BEFORE USE)

General Safety: Never leave the printer unattended during the first layer.  
Pinch Hazard: Keep hands clear of the moving X, Y, and Z axes during operation.  
Heat Hazard: The nozzle can reach 280°C and the heatbed 100°C. Do not touch until cooled.  
Clothing: Tie back long hair and remove loose clothing or jewelry.  

### Uploading Files:

Open PrusaSlicer, load your model (how to do that)  
Design/Print alterations like: size, support, infill, brim,etx.  
Select the filament color/type/brand that you will be using.  
Determine print speed/quality  
Slice your model in PrusaSlicer using the Mini+shaper profile.  
Export the .gcode file to a USB drive.  

### Power-On Sequence:

Insert the USB drive into the printer’s port.  
Check that the top and bottom of the removable build plate is clean and free of debris.  
Switch the power button (on the right side) to ON.  
Wait for the LCD screen to initialize.  
Load the filament color/type/brand that you selected in PrusaSlicer  
Select the file from the menu and press the knob to start.  

## BED LEVELING & FIRST LAYER

Mesh Bed Leveling: The printer runs this automatically before every print to ensure the bed is flat.  
Z-Calibration: If the first layer is too high (gaps) or too low (squished), adjust the Live Z setting during the first layer print.  

## TROUBLESHOOTING

Machine Will Not Start  
Check Power: Verify the power cable is securely plugged into the printer and the wall outlet.  
Check Switch: Ensure the main power switch on the side of the electronics box is in the ON position.  
Check Fuse: If the screen remains dark while switched on, inspect the fuse located in the power entry module.  
Print Not Adhering to Bed  
Clean Surface: Wipe the magnetic steel sheet with 90% Isopropyl Alcohol to remove skin oils or dust. Check under the removable steel sheet for any debris.  
Check First Layer: Ensure the nozzle height is correct; if it is too high, your extruded filament will look more like round string. Use the Live Adjust Z menu to lower the nozzle during the first layer. Ideally, the filament should appear flattened. BEST PRACTICE: Run a First Layer Calibration – located “here”  
Check Bed Temperature: Confirm the bed temperature matches the filament manufacturer's requirements (Generalized e.g., 60°C for PLA, ? °C for PETG, 100°C for ABS).  
Filament Not Extruding  
Check Temperature: Ensure the nozzle is heated to the correct melting temperature for the loaded material. Generalized e.g., 215°C for PLA, etc  
Check Tension: Inspect the extruder idler screw; if it is too loose, the gears will not grip the filament. The top of the screw is relatively flush with the plastic assembly.  
Check for Clogs: If the motor is clicking, perform a "Cold Pull" or use a thin needle to clear the nozzle tip. Or get help. Caution: The Nozzle hottest part!  
Loading Filament  
Filament from Spool: Filament not reaching the filament drive motor. Apply pressure towards filament sensor to ensure the the filament reaches the motor.  
X/Y/Z Axis Movement Error  
Check Obstructions: Ensure there are no zip ties, debris, or cables blocking the path of the toolhead or the bed.  
Check Belt Tension: Verify that the belts are tight and not slipping on the motor pulleys.  
Check Lubrication: If movements are loud or jittery, apply a small amount of machine lubricant to the smooth linear rods.  
Poor Print Quality (Stringing or Blobs)  
Check Filament: Moisture in the filament can cause stringing; try a fresh spool or dry the current one.  
Check Slicer Settings: Ensure the "Retraction" settings in your slicer software are optimized for the MINI+.  
Check Nozzle: Inspect the nozzle for wear; a worn-out nozzle will lead to inconsistent extrusion.  