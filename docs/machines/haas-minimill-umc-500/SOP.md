# Haas Minimill / UMC-500 Standard Operating Procedure

📄 [Download Official Manufacturer Manual (DOCX)](manual.docx)

---


## SAFETY FIRST (READ BEFORE USE)

Enclosure Safety: Never bypass the door interlocks. The spindle and axes will stop if the door is opened during a cycle.  
Eye Protection: Safety glasses are mandatory at all times when the machine is powered on.  
Tooling: Ensure all tools are securely seated in the tool changer and the pull studs are tightened to spec.  
Clearance: Always "dry run" new programs with the Rapid Override turned down to check for potential tool crashes.  

## BASIC OPERATION


### Power-On Sequence:

Turn the main breaker (rear of machine) to the ON position.  
Press Power Up/Restart on the control pendant.  
The machine will home all axes (X, Y, Z, and A/B for the UMC-500).  

### Setting Offsets:

Use the jog handle to move the tool to the top of the workpiece for the Z-offset.  
Use a probe or edge finder to locate the X and Y work coordinates.  
Input values into the Work Offset table (e.g., G54).  
Troubleshooting  
Machine Has Power but Won't Move  
Check E-Stop: Verify that the Emergency Stop button is not depressed.  
Door Interlock: Ensure the enclosure doors are fully closed; the machine will not move if the safety interlock is open.  
Restart Control: Power cycle the control panel to clear any temporary software hang-ups.  
Power Cycle: Turn off the entire machine, wait 30 seconds, and restart to reset the internal drives.  
Spindle or Axis Alarm Active  
Read the Screen: Check the specific alarm code displayed on the control panel for a detailed description of the fault.  
Reset Alarms: Press the RESET button to clear non-critical errors.  
Way Lube/Air: Confirm that the air pressure is at the required levels and the automatic lubricator is not empty.  
Cuts Not Accurate or Poor Finish  
Check Tooling: Inspect the tool for wear, chips, or dullness; ensure it is properly seated in the spindle.  
Verify Offsets: Re-check your tool and work offsets to ensure the machine knows the exact position of the material.  
Coolant Flow: Ensure the coolant is hitting the tool-workpiece interface to prevent overheating and tool deflection.  
Tool Changer Error  
Clear Obstructions: Check for metal chips or debris that may be preventing the tool changer from moving freely.  
Air Pressure: Low air pressure often prevents the tool release piston from firing correctly.  
Manual Recovery: Use the machine’s "Tool Changer Recovery" mode to step through the cycle and clear the jam safely.  
When in Doubt  
STOP the machine: Press the Emergency Stop immediately if you hear unusual noises.  
Power down safely: Shut the system down according to the standard sequence.  
Ask for help: Consult a supervisor or trained operator before attempting manual repairs.  
No Testing: Never "test" a fix while the machine is active or a program is running  