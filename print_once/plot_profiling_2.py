import matplotlib.pyplot as plt
import numpy as np  # Importing for potential numerical operations

# Assuming the definition of extract_time_from_file remains the same, but modified to return all times
def extract_times_from_file(filename):
    times = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if 'real' in line:
                parts = line.split()
                time_parts = parts[1].split('m')
                minutes = float(time_parts[0])
                seconds = float(time_parts[1][:-1])
                total_time = minutes * 60 + seconds
                times.append(total_time)
    return times

# Program, castles, and troops configuration
programs = ['sums', 'blotto', 'blotto_parallel', 'blotto_jit_py', 'blotto_jit_parallel_py', 'slowest_blotto_py']
CASTLES = [2, 3]
TROOPS = [5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Collecting and plotting data
for program in programs:
    plt.figure(figsize=(10, 6))
    data_to_plot = []  # This will be a list of lists of times for each troop count
    for castle in CASTLES:
        for troop in TROOPS:
            filename = f'profiling/{program}_c_{castle}_t_{troop}_profile.txt'
            times = extract_times_from_file(filename)
            if times:
                data_to_plot.append(times)

        # Plotting the box plot for the current program and castle
        plt.boxplot(data_to_plot, positions=range(1, len(TROOPS) + 1), widths=0.35, patch_artist=True, boxprops=dict(facecolor='skyblue'))
        plt.xticks(range(1, len(TROOPS) + 1), TROOPS)
        plt.xlabel('Number of Troops')
        plt.ylabel('Execution Time (seconds)')
        plt.title(f'Execution Times for {program} - Castle {castle}')
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.savefig(f'{program}_castle_{castle}_execution_times_boxplot.png', dpi=300)
        plt.show()
        data_to_plot.clear()  # Clear data for the next castle or program
