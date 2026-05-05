# Lists to store different contamination levels
level1 = []
level2 = []
level3 = []
level4 = []
level0 = []

# List to store file data
data = []

# Read input file line by line
with open("contamination_analysis.txt") as f:
    for line in f:
        row = line.strip().split(" ")   # split id and chemical formula
        data.append(row)               # store in data list

# Create dictionary: id to chemical formula
d = {k[0]: k[1] for k in data}  

import re

# Function to count atoms in a chemical formula
def count_element(text, element):
    matches = re.findall(rf"{element}(\d*)", text)
    
    total = 0
    for m in matches:
        total += int(m) if m else 1
        
    return total


# Function to classify contamination level
def contamination_analysis(text):

    S = count_element(text, "S")
    O = count_element(text, "O")
    Na = count_element(text, "Na")
    Mg = count_element(text, "Mg")
    Cl = count_element(text, "Cl")

    levels = []

    if S>=1 and O>=4 and Na>=1: #level 1
        levels.append(1)
        S -= 1
        O -= 4
        Na -= 1

    if S>=1 and O>=3 and Mg>=1:  #level 2
        levels.append(2)
        S -= 1
        O -= 3
        Mg -= 1

    if O>=2 and Cl>=3: #level 3
        levels.append(3)

    if len(levels)==0: #level 0
        level0.append(text)

    elif len(levels) == 1:
        if levels[0] == 1:
            level1.append(text)
        elif levels[0] == 2:
            level2.append(text)
        elif levels[0] == 3:
            level3.append(text)

    else:
        level4.append(text)



# Run analysis for each chemical formula
for i in range(len(data)):
    contamination_analysis(data[i][1])


# Write Level 0 results to file
with open("Level_0.txt", 'w') as f:
    for item in level0:
        for key, value in d.items():
            if value == item:
                f.write(key + "\n")

# Write Level 1 results
with open("Level_1.txt", 'w') as f:
    for item in level1:
        for key, value in d.items():
            if value == item:
                f.write(key + "\n")

# Write Level 2 results
with open("Level_2.txt", 'w') as f:
    for item in level2:
        for key, value in d.items():
            if value == item:
                f.write(key + "\n")

# Write Level 3 results
with open("Level_3.txt", 'w') as f:
    for item in level3:
        for key, value in d.items():
            if value == item:
                f.write(key + "\n")

# Write Level 4 results
with open("Level_4.txt", 'w') as f:
    for item in level4:
        for key, value in d.items():
            if value == item:
                f.write(key + "\n")