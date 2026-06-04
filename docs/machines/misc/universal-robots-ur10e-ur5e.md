# Universal Robots UR10e / UR5e

!!! info "Manual"
    📄 [Download Official Manufacturer Manual](manual.docx)

---


## SAFETY FIRST (READ BEFORE USE)

Collaborative Safety: While designed to work alongside humans, always perform a risk assessment for the specific end-effector (gripper/tool) being used.  
Emergency Stop: Ensure the E-Stop on the Teach Pendant is within reach at all times during manual or automatic operation.  
Pinch Points: Keep hands clear of joints and the mounting flange during movement, especially when the robot is in "Free Drive" mode.  
Backdrive: In the event of an emergency or power loss, the joints can be moved manually by applying significant force; use this only for safety extraction.  

## BASIC OPERATION


### Power-On Sequence:

Turn the power switch on the Control Box to ON.  
On the Teach Pendant, tap the Power Icon (bottom left) and select Power On.  
Once initialized, tap Release Brakes. You will hear a series of clicks as the joints unlock.  
The robot status light on the top of the pendant will turn green when ready.  

### Programming & Movement:

Free Drive: Hold the black button on the back of the Teach Pendant to manually move the robot arm to a desired position.  
Waypoints: Use the PolyScope interface to "Add Waypoint" and save positions for your program.  
Graphics Tab: Use the 3D visualization to verify the robot's intended path before running the program at full speed.  
Speed Slider: Always start a new program with the speed slider set to 10% or lower to check for collisions.  

## TROUBLESHOOTING

Protective Stop: This occurs if the robot detects a collision or abnormal force. Check for obstructions, then tap the popup to Resume.  
Joint Limit: If a joint reaches its mechanical limit, use the jog arrows or Free Drive to move the robot back into its working envelope.  
Communication Error: Check that the cable between the Control Box and the Robot Arm is securely connected and the locking ring is tightened.  