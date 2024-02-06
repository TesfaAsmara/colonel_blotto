import os
import matplotlib.pyplot as plt

def extract_time_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if 'real' in line:
                parts = line.split()
                time_parts = parts[1].split('m')  # Split "0m0.223s" into ["0", "0.223s"]
                minutes = float(time_parts[0])  # Extract minutes
                seconds = float(time_parts[1][:-1])  # Extract seconds and remove 's'
                total_time = minutes * 60 + seconds
                return total_time
    return None

# Define the castles, troops, and programs
# CASTLES = 2
# TROOPS = [25, 50, 75, 100, 150, 300, 600]
CASTLES = 3
# 10, 25
TROOPS = [5, 10, 15]
programs = ['sums', 'blotto', 'blotto_jit_py', 'slowest_blotto_py']

# Prepare the data 
times = {program: [] for program in programs}

# Extract the time for each program and troop count
for troop in TROOPS:
    for program in programs:
        filename = f'profiling/{program}_c_{CASTLES}_t_{troop}_profile.txt'
        time = extract_time_from_file(filename)
        if time is not None:
            times[program].append(time)
        else:
            print(f"Time data not found in file: {filename}")


# Plotting the data
for program, time_data in times.items():
    plt.plot(TROOPS, time_data, label=program)

plt.xlabel('Number of Troops')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time vs Number of Troops')
plt.legend()

# Save the figure to a file
plt.savefig('execution_times.png', dpi=300)

# Optionally display the plot
# plt.show()
