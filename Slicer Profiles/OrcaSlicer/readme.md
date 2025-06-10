**Peopoly Moai for OrcaSlicer**

(Do once - All) Import the "Peopoly_Moai.orca_printer" file into OrcaSlicer
(Do once - Linux or Mac) Copy "Peoploly_Moai_gCode_Processor.py" into your OrcaSlicer "Resources" folder
(Do once - Linux or Mac) Open OrcaSlicer, add the path to the .py script in "Process" "Others" "Post-processing Scripts" for the solid and hollow profiles, then save the profiles. Orcaslicer will process the gcode automatically when you export the gCode file.
(Do once - MS Windows) Install Python to Windows. Copy "Peoploly Moai gCode Processor.py" into your gCode or models folder.

**Work-Flow:**
For most resin-type models:
- Arrange, support, and hollow your models in a resin tool such as LycheeSlicer or ChituBox 
- Export the model as an .obj or .stl file
- Import the model into OrcaSlicer onto the Moai plate
- RUN "FIX MODEL" as the resin tools leave broken non-manifold edges.
- Choose solid profile if you pre-hollowed the model
- Choose hollow profile for regular FDM models, or chunky models directly on the plate. 
- Slice the model and review
- Save the gCode to a file 
  - Mac and Linux can process the py code during the file save.
  - Windows you will need to drag and drop the .gCode file onto the .py code file to run the script.
- Put into the "gcode" folder of a properly formatted FAT32 SD card and print!

**Set speed multiplier for your resin conditions**
One profile (width, height, speed ratios) should work for all resins. Instead of adjusting print speed in the slicer, adjust the speed multiplier on the Moai to match the cure speed of the installed resin. Cure speeds are dependent on material, transparency, and temperatures and are outside the scope of the slicer release. You will have to experiment with your materials. Testing shows that old slow resins print around x5 speed, fast modern resins can print upwards of x40 speed, With most resins curing around the x20 to x30 range.

**Machine settings recommendations:*
Use "Laser Power" of around "60" or less for 64u dot size / line width, and 50u layer height max.
Use "Laser Power" of around "50" or less for 50u dot size / line width, and 40u layer height max.

**Use Lift to Peel for Film-based Vats**
Set "XY Speed Set" (print speed multiplier) x"5" to x"50" to match the resin cure speed.
Set "Z initial speed" (Z Lift Speed) "5" to "10" depending on your resin viscosity.
Set "Z moto speed" (Z Return Speed) "15" to "30" depending on your resin viscosity.
Set "PM initial speed" (Tilt Peel Speed) to "0". 
Set "PM moto Speed" (Tilt Peel Speed) to "0". 
Set "Z Follows" (Z Lift Height) "-300" for 3mm of lift to release layer from film.
Set "PM Reset Position" (Tilt Peel Distance) to "0" to disable vat tilting.

**Version Notes:**
1.0 (Release) 2025-06-09 JLS
OrcaSlicer base printer, material, and slicer profiles created
Starter profiles provided for 50 micron printing, solid or hollow.
Python script written for post-processing of gcode from Orca or Cura to make Moai compatible.

