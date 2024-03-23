import os
import matplotlib.pyplot as plt
import numpy as np

# Assuming the list of programs, CASTLES, and TROOPS
programs = ['sums', 'blotto', 'blotto_parallel', 'blotto_jit_py', 'blotto_jit_parallel_py', 'slowest_blotto_py']
CASTLES = [3]
TROOPS = [5, 10, 20, 30, 40, 50, 60, 70, 80, 90,100] #, 30, 40, 50, 60, 70, 80, 90, 100, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 

def extract_times_from_file(filename):
    times = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for i,line in enumerate(lines):
            if 'elapsed' in line and i < len(lines)-3:
                parts = line.split()
                print(parts)
                time_str = parts[2][0:-7]  # Get the part containing elapsed time
                print(filename)
                minutes, seconds = map(float, time_str.split(':'))  # Split minutes and seconds
                total_time = minutes * 60 + seconds  # Convert to seconds
                times.append(total_time)
    return times

# Loop through each program and plot a boxplot for each castle
for program in programs:
    for castle in CASTLES:
        data = []
        configurations = []  # Initialize configurations list
        for troop in TROOPS:
            filename = f'profiling/{program}_c_{castle}_t_{troop}_profile.txt'
            times = extract_times_from_file(filename)
            if times:
                data.append(times)
                # Append the number of configurations for each troop
                filename = f"/home/jovyan/data3/results/C{castle:02}_T{troop:03}/results.txt"
                with open(filename, "r") as file:
                    numConfigurations = len(file.readline().split())
                    configurations.append(str(numConfigurations))
            else:
                print(f"Time data not found in file: {filename}")
                data.append([0])  # Use a list with a single 0 to avoid errors in boxplot
                configurations.append('Unknown')

        # Plotting
        plt.figure(figsize=(12, 6))
        plt.boxplot(data, labels=configurations, showmeans=True)
        plt.xlabel('Number of Configurations')
        plt.ylabel('Execution Time (seconds)')
        plt.title(f'Execution Time for {program} - Trench {castle}')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()  # Adjust layout to make room for the rotated x-axis labels

        # Save the figure to a file for the current program and castle
        plt.savefig(f'{program}_castle_{castle}_execution_times_boxplot.png', dpi=300)
        plt.show()