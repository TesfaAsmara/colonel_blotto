import matplotlib.pyplot as plt

# Path to the directory_sizes.txt file
file_path = 'directory_sizes.txt'

# Data structure to hold directory sizes for each castle
directory_sizes = {}

with open(file_path, 'r') as file:
    for line in file:
        # Extract relevant parts from each line
        parts = line.strip().split(': ')
        path, size_str = parts[0], parts[1]
        size = int(size_str.split(' ')[0])  # Convert size to integer

        directory_name = path.split('/')[-2]  # Use the last part of the path
        if '_' in directory_name:  # Check if the directory_name contains an underscore
            C, T = directory_name.split('_')
            castle = int(C[1:])
            troop = int(T[1:])
            
            # Organize data by castle, then by troop
            if castle not in directory_sizes:
                directory_sizes[castle] = {}
            directory_sizes[castle][troop] = size
        else:
            print(f"Skipping unrecognized directory format: {directory_name}")

# Plotting
for castle, sizes in directory_sizes.items():
    troops = sorted(sizes.keys())
    sizes_values = [sizes[troop] for troop in troops]
    
    plt.figure(figsize=(10, 6))
    plt.plot(troops, sizes_values, marker='o', linestyle='-')
    plt.title(f'Directory Size as Troops Grow for Castle {castle:02d}')
    plt.xlabel('Number of Troops')
    plt.ylabel('Directory Size (bytes)')
    plt.grid(True)
    plt.savefig(f'directory_size_castle_{castle:02d}.png', dpi=300)
    plt.show()