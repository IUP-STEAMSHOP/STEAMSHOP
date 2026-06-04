# ShopBot CNC Milling Table

!!! info "Manual"
    📄 [Download Official Manufacturer Manual](manual.docx)

---


## SAFETY FIRST (READ BEFORE USE)

Constant Supervision: NEVER leave the CNC unattended while it is running.  
Personal Safety: Tie back long hair, remove loose clothing, and avoid dangling jewelry to prevent entanglement with moving axes.  
Emergency Stops: Locate the three red emergency stop buttons before starting any job.  
Eye and Ear Protection: Always wear safety glasses and hearing protection when the machine is in operation.  
Debris Management: Ensure the work area is clear of tools and debris that could interfere with gantry movement.  

## BASIC OPERATION


### Power-On Sequence:

Clear the bed of all obstructions and ensure the gantry moves freely.  
Turn ON the main power switch on the control box.  
Press the Blue Reset Button on the control box to engage the motors.  
Launch the ShopBot control software and run the Spindle Warm-up Routine.  

### Zeroing and Files:

Secure your material firmly to the bed using screws or clamps.  
Use the Z-Zero Plate and grounding clip to automatically set the bit height.  
Manually jog the machine to the starting corner of your material and set the X and Y Zero.  
Turn ON the Dust Collector and ensure the extractor is running.  
Load your part file, START the spindle, and click OK to begin.  

## TROUBLESHOOTING

Machine Will Not Move (Axis Stalled)  
Check E-Stop: Verify that all Emergency Stop buttons (on the control box and handheld pendant) are twisted and released.  
Reset Drive Power: Press the Blue Reset Button on the ShopBot control box. If the internal drivers have "tripped" due to a minor collision, they require a physical reset to engage the motors again.  
Software Connection: Ensure the ShopBot control software is in "Yellow" (Move) mode. If the software shows a "Connection Lost" error, check the USB cable and restart the control box.  
Limit Switches: If the gantry has hit a physical limit switch, you must manually move the machine off the switch using the arrow keys or by physically turning the lead screws (with power OFF).  
Spindle Will Not Start  
VFD Error: Check the display on the VFD (Variable Frequency Drive) box. If it shows an error code (e.g., "OL" for Overload), the spindle may have been pushed too hard.  
Interlock Key: Ensure the spindle enable key is in the ON position.  
Warm-up Routine: The spindle may refuse to run at high speeds if the mandatory Warm-up Routine has not been completed for the day.  
Manual Toggle: Ensure the software command to start the spindle has been acknowledged; many setups require you to press "Start" on a physical remote after clicking "OK" on the screen.  
Inaccurate Cuts or "Drifting" (Loss of Steps)  
Check Bit Sharpness: A dull bit creates excessive resistance, causing the motors to "lose steps" and drift from the programmed path.  
Secure Workpiece: If the material moves even slightly, the cut will be ruined. Double-check clamps, screws, or vacuum pressure.  
Collet Maintenance: Inspect the collet and nut. If they are dirty or worn, the bit can "creep" out of the spindle during a cut, leading to deeper-than-intended gouges.  
Feed and Speed: If the machine is "screaming" or vibrating, your feed rate may be too high or your spindle RPM too low for the material.  
Z-Zero Failed or Inconsistent  
Clean Plate: Ensure the aluminum Z-zero plate is clean and free of sawdust.  
Grounding Clip: Verify the grounding clip is attached to the spindle or the bit itself. If the circuit isn't completed, the bit will crash into the plate.  
Bit Conductivity: Some coated bits or dirty bits may not conduct electricity well; wipe the bit with a cloth before zeroing.  
When in Doubt  
Spacebar Stop: In ShopBot software, hitting the Spacebar will immediately stop all motion without killing power to the spindle (useful for minor errors).  
Emergency Stop: Use the Red E-Stop for serious issues (crashes, fire, or broken bits).  
Never Reach In: Never attempt to clear chips or move clamps while the gantry is in motion.  
Ask for help: If the machine makes a "clunking" sound, the drive gears (pinions) may be loose or worn; notify a supervisor immediately.  