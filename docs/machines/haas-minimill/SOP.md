# Haas Minimill Standard Operating Procedure

📄 [Download Official Manufacturer Manual (DOCX)](manual.docx)

---


## SAFETY FIRST (READ BEFORE USE)

Enclosure Safety: Never bypass or disable the door safety interlocks.  
Eye Protection: Always wear safety glasses when the machine is powered on to protect against flying chips and coolant splashes.  
Tooling Safety: Ensure all tools are securely seated in the tool changer and that pull studs are tightened to the correct specification.  
Clearance Check: Always "dry run" new programs with the Rapid Override turned down to check for potential tool crashes or clearance issues.  
Entanglement Hazard: Tie back long hair, remove loose clothing, and avoid dangling jewelry; do not wear gloves while the spindle is in motion.  

## BASIC OPERATION


### Power-On Sequence:

Turn the main breaker (located on the rear of the machine) to the ON position.  
Press the Power Up/Restart button on the control pendant.  
The machine will automatically home all axes (X, Y, and Z).  
Ensure the air pressure is at the required level (typically 85 psi) before operating.  

### Setting Offsets:

Work Offset: Use the jog handle and an edge finder or probe to locate the part's X and Y coordinates; input these into the G54 table.  
Tool Offset: Lower each tool to the top of the workpiece or a tool setter to define the Z-axis length; save these in the Tool Offset table.  

### Running a Job:

Upload your program via USB or network connection.  
Verify the program using the Graphics mode on the screen.  
Select Memory mode, turn on the coolant system, and press Cycle Start.  

## TROUBLESHOOTING

Machine Will Not Move: Check if the Emergency Stop is pressed or if the door is open.  
Alarm Active: Read the alarm code on the screen and refer to the Haas manual or press the Help button for a description.  
Tool Change Error: Ensure there is no debris in the tool changer carousel and that the air pressure is sufficient.  