import matplotlib.pyplot as plt

# Assuming the data is stored in a multiline string
data = """/home/jovyan/data3/results/C02_T005/: 0 bytes
/home/jovyan/data3/results/C02_T010/: 4 bytes
/home/jovyan/data3/results/C02_T020/: 12 bytes
/home/jovyan/data3/results/C02_T030/: 16 bytes
/home/jovyan/data3/results/C02_T040/: 36 bytes
/home/jovyan/data3/results/C03_T005/: 12 bytes
/home/jovyan/data3/results/C03_T010/: 80 bytes
/home/jovyan/data3/results/C03_T020/: 6252 bytes
/home/jovyan/data3/results/C03_T030/: 11084 bytes
/home/jovyan/data3/results/C03_T040/: 18656 bytes
"""

# Parsing the data
sizes = {}
for line in data.strip().split('\n'):
    parts = line.split(': ')
    path = parts[0]
    size = int(parts[1].split(' ')[0])
    
    # Corrected extraction of castle and troop numbers
    directory_name = path.split('/')[-1]  # Correctly target the last element after splitting
    print(directory_name)
#     C, T = directory_name.split('_')
#     castle = int(C[1:])
#     troop = int(T[1:])
    
#     # Organize data by castle
#     if castle not in sizes:
#         sizes[castle] = []
#     sizes[castle].append((troop, size))

# # Plotting
# for castle, values in sizes.items():
#     # Sort by troop number
#     values.sort(key=lambda x: x[0])
#     troops, size_values = zip(*values)  # Rename to avoid conflict with 'sizes' dict
    
#     plt.plot(troops, size_values, label=f'Castle {castle}', marker='o')

# plt.xlabel('Number of Troops')
# plt.ylabel('Directory Size (bytes)')
# plt.title('Directory Sizes by Number of Troops')
# plt.legend()
# plt.grid(True)
# plt.savefig('directory_size_plot.png', dpi=300)
# plt.show()
