import matplotlib.pyplot as plt

# Read input file
with open("input.txt") as f:
    data = f.readline().strip().split(",")   # Read first line (Vin, Vout, tolerance)
    Vin = int(data[0])                       # Input voltage
    Vout = int(data[1])                      # Desired output voltage
    t = float(data[2])                       # Tolerance range

    Resistor_Values_String = f.readline().strip().split(",")  # Read resistor values
    Resistor_Values = list(map(int, Resistor_Values_String))  # Convert to integers

    pairs = []   # List to store all possible resistor pairs

    # Generate all possible resistor pairs
    for i in range(len(Resistor_Values)):
        Sub_Resistor_Values = Resistor_Values[i:]
        for j in range(1, len(Sub_Resistor_Values)):
            pair = [Sub_Resistor_Values[0], Sub_Resistor_Values[j]]
            pairs.append(pair)

# List to store valid resistor pairs within tolerance
Sub_pairs = []

# Filter pairs based on voltage divider condition
for i in range(len(pairs)):

    
    if Vout - t <= Vin * pairs[i][0] / sum(pairs[i]) <= Vout + t:
        pairs_ = []
        pairs_.append(pairs[i][1])   # Swap order (R1, R2)
        pairs_.append(pairs[i][0])
        Sub_pairs.append(pairs_)

    
    if Vout - t <= Vin * pairs[i][1] / sum(pairs[i]) <= Vout + t:
        Sub_pairs.append(pairs[i])

# Calculate power for each valid pair
power = []
for j in range(len(Sub_pairs)):
    p = Vin**2 / sum(Sub_pairs[j])   # Power formula
    power.append(p)



if not Sub_pairs:
    exit()

# Find index of minimum power pair
k = power.index(min(power))

# Write best resistor pair to file
with open("output.txt", "w") as f:
    f.write(f"{Sub_pairs[k][0]}, {Sub_pairs[k][1]}")

# Extract best resistor values
R2 = Sub_pairs[k][1]
R1 = Sub_pairs[k][0]

# Calculate output voltage variation with load resistance
Vnew_Values = []
RL = list(range(10, 1001, 10))   # Load resistance from 10 to 1000

for i in RL:
    R3 = (R2 * i) / (R2 + i)      # Parallel combination of R2 and RL
    Vnew = Vin * R3 / (R1 + R3)   # Voltage divider formula
    Vnew_Values.append(Vnew)

# Plot graph
plt.plot(RL, Vnew_Values)
plt.xlabel('Resistance(ohms)')
plt.ylabel('Voltage(V)')
plt.title('Voltage vs Resistance')
plt.grid()
plt.show() 