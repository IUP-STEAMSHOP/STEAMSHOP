# Haas UMC-500

!!! info "Manual"
    📄 [Download Official Manufacturer Manual](manual.docx)

---


## SAFETY FIRST (READ BEFORE USE)

Enclosure Safety: Never bypass or disable the door safety interlocks.  
Eye Protection: Always wear safety glasses when the machine is powered on to protect against flying chips and coolant splash.  
Tooling Safety: Ensure all tools are securely seated in the tool changer and that pull studs are tightened to the correct specification.  
5-Axis Motion: Be aware that the table (B and C axes) can move simultaneously with the spindle; ensure all workholding and parts clear the machine casting during rotation.  
Clearance Check: Always "dry run" new programs with the Rapid Override turned down to check for potential tool crashes.  

## BASIC OPERATION


### Power-On Sequence:

Turn the main breaker (located on the rear of the machine) to the ON position.  
Press the Power Up/Restart button on the control pendant.  
The machine will automatically home all axes, including the rotary table.  
Ensure the air pressure is at the required level and the coolant is flowing correctly before operating.  

### Setting Offsets:

Work Offset: Use the jog handle and a probe or edge finder to locate the part's X, Y, and Z coordinates; input these into the G54-G59 tables.  
Tool Offset: Use the automatic tool setter (if equipped) to define the length and diameter of each tool.  

### Running a Job:

Upload your program via USB or network connection.  
Verify the program using Graphics mode on the screen.  
Select Memory mode, ensure the lid is closed, and press Cycle Start.  

## TROUBLESHOOTING

Machine Will Not Move: Check if the Emergency Stop is pressed or if the door is open.  
Alarm Active: Read the alarm code on the screen and refer to the machine's internal help menu.  
Coolant/Water Flow Alarm: Check the reservoir level and ensure hoses are not kinked.  