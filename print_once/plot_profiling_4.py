# FOR PROFILING WITH TIME COMMAND FROM SH WHEN EXECUTING EXECUTE_COMMANDS.PY

import os
import matplotlib.pyplot as plt
import numpy as np

# Assuming the list of programs, CASTLES, and TROOPS
programs = ['sums', 'blotto', 'blotto_parallel', 'blotto_jit_py', 'blotto_jit_parallel_py', 'slowest_blotto_py']
CASTLES = [2]
TROOPS = [5, 10, 20, 30, 40, 50, 60, 70, 80, 90]

def extract_times_from_file(filename):
    times = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if 'Iteration' in line:
                parts = line.split()
                try:
                    elapsed_time = float(parts[-2][:-6])  # Extracting the elapsed time
                    times.append(elapsed_time)
                except ValueError:
                    pass  # Ignore lines where time extraction fails
    return times

# Loop through each program and plot a boxplot for each castle
for program in programs:
    for castle in CASTLES:
        data = []
        for troop in TROOPS:
            filename = f'profiling/{program}_c_{castle}_t_{troop}_profile.txt'
            times = extract_times_from_file(filename)
            if times:
                data.append(times)
            else:
                print(f"Time data not found in file: {filename}")
                data.append([0])  # Use a list with a single 0 to avoid errors in boxplot

        # Plotting
        plt.figure(figsize=(12, 6))
        plt.boxplot(data, labels=TROOPS, showmeans=True)
        plt.xlabel('Number of Troops')
        plt.ylabel('Execution Time (seconds)')
        plt.title(f'Execution Time Distribution for {program} - Castle {castle}')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()  # Adjust layout to make room for the rotated x-axis labels

        # Save the figure to a file for the current program and castle
        plt.savefig(f'{program}_castle_{castle}_execution_times_boxplot.png', dpi=300)
        plt.show()
