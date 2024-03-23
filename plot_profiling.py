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
CASTLES = [2, 3]
TROOPS = [5, 10, 20, 30 ,40, 50, 60, 70, 80, 90, 100]
programs = ['sums', 'blotto', 'blotto_parallel','blotto_jit_py', 'blotto_jit_parallel_py', 'slowest_blotto_py']

# Loop through each castle and create a plot
for castle in CASTLES:
    plt.figure(figsize=(10, 6))
    
    # Prepare the data for each program
    times = {program: [] for program in programs}
    
    # Extract the time for each program and troop count for the current castle
    for troop in TROOPS:
        for program in programs:
            filename = f'profiling/{program}_c_{castle}_t_{troop}_profile.txt'
            time = extract_time_from_file(filename)
            if time is not None:
                times[program].append(time)
            else:
                print(f"Time data not found in file: {filename}")
    
    # Plotting the data for the current castle
    for program, time_data in times.items():
        plt.plot(TROOPS, time_data, label=program, marker='o')
    
    plt.xlabel('Number of Troops')
    plt.ylabel('Execution Time (seconds)')
    plt.title(f'Execution Time vs Number of Troops for Castle {castle}')
    plt.legend()
    plt.grid(True)
    
    # Save the figure to a file for the current castle
    plt.savefig(f'execution_times_castle_{castle}.png', dpi=300)
    
    # Optionally display the plot
    # plt.show()

# Close all figures to free memory
plt.close('all')
