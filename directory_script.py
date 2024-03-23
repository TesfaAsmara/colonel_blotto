# A quick script started on 02/29/2024 to create directories

import os

# Specify the base directory where "results" is or will be located
base_dir = '/home/jovyan/data3'

# Ensure the base path for results exists
results_path = os.path.join(base_dir, 'results')
os.makedirs(results_path, exist_ok=True)

# Specify the range for the number of castles and troops
num_castles_range = [3]
num_troops_range = [5, 10, 20, 30, 40, 50, 60, 70, 80, 90,100]

for num_castles in num_castles_range:
    for num_troops in num_troops_range:
        # Format directory name
        dir_name = f"C{num_castles:02}_T{num_troops:03}"
        full_dir_path = os.path.join(results_path, dir_name)
        
        # Create directory
        try:
            os.makedirs(full_dir_path)
            print(f"Directory created: {full_dir_path}")
        except FileExistsError:
            print(f"Directory already exists: {full_dir_path}")
        except Exception as e:
            print(f"Error creating directory {full_dir_path}: {e}")


