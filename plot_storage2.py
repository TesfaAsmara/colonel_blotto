from scipy.special import comb
import matplotlib.pyplot as plt
import numpy as np
import os  # Added for file size measurement

def calculate_combinations(C, T):
    return comb(C + T - 1, T, exact=True)

def calculate_bits(S, T, C):
    return 2 * (np.log2(S) * T * C)/8

file_path = 'directory_sizes.txt'
directory_sizes = {}
results_file_sizes = {}  # New dictionary to store results.txt file sizes

castles = [2, 3]
troops = [5, 10, 20, 30, 40, 50, 60, 70, 80, 90]

# Example: Populate results_file_sizes with data (this step would depend on how you've stored or can access the size data)
# for castle in castles:
#     for troop in troops:
#         filepath = f"data3/results/C{castle:02}_T{troop:03}/results.txt"
#         # Assuming file exists and size is in bytes
#         results_file_sizes[(castle, troop)] = os.path.getsize(filepath) if os.path.exists(filepath) else 0

with open(file_path, 'r') as file:
    for line in file:
        parts = line.strip().split(': ')
        path, size_str = parts[0], parts[1]
        size = int(size_str.split(' ')[0])

        _, directory_name = path.split('/results/')
        directory_name = directory_name.rstrip('/')
        C, T = directory_name.split('_')
        castle, troop = int(C[1:]), int(T[1:])
        
        if castle not in directory_sizes:
            directory_sizes[castle] = {}
        directory_sizes[castle][troop] = size

for castle in castles:
    plt.figure(figsize=(10, 6))

    configurations = [calculate_combinations(castle, troop) for troop in troops]
    bits = [calculate_bits(troop, castle, calculate_combinations(castle, troop)) for troop in troops]
    sizes_values = [directory_sizes[castle].get(troop, 0) for troop in troops]  # Directory sizes
    results_sizes = [results_file_sizes.get((castle, troop), 0) for troop in troops]  # results.txt file sizes

    # Plot for directory sizes
    plt.plot(configurations, sizes_values, label='Directory Size (bytes)', marker='o')
    # Plot for bits calculation
    plt.plot(configurations, bits, label='Theoretical Calculation (bytes)', marker='x', linestyle='--')
    # Plot for results.txt file sizes
    plt.plot(configurations, results_sizes, label='Results.txt Size (bytes)', marker='^', linestyle=':')

    plt.title(f'Castle {castle}: Storage and Calculations')
    plt.xlabel('Number of Configurations')
    plt.ylabel('Bytes')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'overlay_plot_castle_{castle}.png')
    plt.show()
