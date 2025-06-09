** ** Firmware Notes ** **



**MOAI Firmware Firmware FULL CHANGELOG (Peopoly Dev)**

V.18 (Beta4)
increase Z Follow value to allow higher up movement

V.18 (Beta3)
set PM reset distance = 0 to disable PM motor
set Zfollow to negative value for up movement

V.18 (Beta2)

V.18 (Beta)
Setting definition change
Z-Follow 0-60 each unit represents 0.1mm the range of value is (-1) to (5)
Z-Follow 0 = -1 mm movement upward during peel
Z-Follow 60 = 5 mm movement downward during peel
For recommended z-follow for general printing, it is now 30 (2mm downward movement)

New commands:
M1001 X40 ;laser power change to 40
M1002 X5 ;wait for 5 seconds before continuing
M1003 X1800 ;moving build platform arm to z-axis reset spot of 1800 (in the setting) or 180mm down from the top
M1004 X50 ;peel motion 50 has no meaning
M1005 X10 ;change Pm moto speed to 10
M1006 X3 ;change Z Motor Speed to 3
M1007 X12 ;change Z Follows (distance) to 12
M1008 X15 ;change PM Reset Position to 15
M1009 X0 ;Set HE2 port LOW -- X1 ;Set HE2 port High
M1010 X0 ;Set HE3 port LOW -- X1 ;Set HE3 port High

V1.18
Print Duration
Updated default print values
Updated calibration adjustment
Update SD card read i/o.  please print directly from root directory instead of gcode directory.
Initial layers peel speed

V1.16 changelog 2018.3.15
Compensate X/Y
This adjust X/Y for distortions.  Since Galvo/laser setup only has distorion on Y-axis, adjustment to Y-axis is only needed.
Default value for Compensate X is 100
Default value for Compensate Y is 195
Rest of settings are consistent to Firmware 1.15

V1.15 changelog 20171122 
Allow finer calibration and leveling
- X / Y Size range increase from 400 to 1000.  What was 360 is now 900
- Default recommended value is set. Laser is at 58. PM and Z follow motor speed has been reduced as well as Tilt distance
- Laser does not fire when user adjust value in the setting
- User can now immediately cancel a print and it will followed with a peel action before raising the build plate to reduce peel force

V1.14 changelog 2017.09.25 
Allow finer calibration and leveling
- X / Y Size range increase from 100 to 400.  What was 90 is now 360
- Z Reset Position range, increase from 200 to 2000.  What was 188 is now 1880
- Z-follow can now be 0

V1.1x
>enter settings,  XY size is 4 times of recorded value. Z Reset Position is 10 times of the recorded value. Make sure you updated everything to recorded settings








