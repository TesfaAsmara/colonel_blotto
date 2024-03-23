# FOR CLEANING PROFILING FILES

import os
import matplotlib.pyplot as plt
import numpy as np

# Assuming the list of programs, CASTLES, and TROOPS
programs = ['sums', 'blotto', 'blotto_parallel', 'blotto_jit_py', 'blotto_jit_parallel_py', 'slowest_blotto_py']
CASTLES = [4]
TROOPS = [5, 10, 20, 30,40, 50, 60, 70, 80, 90,100]

# Loop through each program and plot a boxplot for each castle
for program in programs:
    for castle in CASTLES:
        for troop in TROOPS:
            file_path = f'profiling/{program}_c_{castle}_t_{troop}_profile.txt'
            # Check if the file exists before attempting to delete it
            if os.path.exists(file_path):
                # Delete the file
                os.remove(file_path)
                print(f"The file '{file_path}' has been successfully deleted.")
            else:
                print(f"The file '{file_path}' does not exist.")