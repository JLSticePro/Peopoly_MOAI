import sys
import re

# Get the G-code file path from the command line arguments
sourceFile = sys.argv[1] 
# Importing
print("Importing G-Code\n")

# Read the G-code file
with open(sourceFile, "r") as f:
    lines = f.readlines()

# Process each line
print("Processing\n")
processed_lines = []
for line in lines:
    if line.strip().startswith("G1"):
        if re.search(r'[XYZxyz]', line) and not re.search(r'[Ee]', line):
            # Replace G1 with G0
            processed_lines.append(line.replace('G1', 'G0', 1))
        else:
            processed_lines.append(line)
    elif line.strip().startswith("M73"):
        processed_lines.append('')
    elif line.strip().startswith("M204"):
        processed_lines.append('')
    elif line.strip().startswith("M106"):
        processed_lines.append('')
    elif line.strip().startswith(";_SET_FAN"):
        processed_lines.append('')
    elif line.strip().startswith(";TYPE"):
        processed_lines.append('')
    elif line.strip().startswith(";WIDTH"):
        processed_lines.append('')
    elif line.strip().startswith(";MESH"):
        processed_lines.append('')
    elif line.strip().startswith(";TIME"):
        processed_lines.append('')
    else:
        processed_lines.append(line)
# Exporting
print("Exporting G-Code\n")
# Overwrite the original G-code file with the modified G-code
with open(sourceFile, "w") as of:
    of.writelines(processed_lines)
