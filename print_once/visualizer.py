import matplotlib.pyplot as plt
import numpy as np

def read_matrix(file_path):
    matrix = []
    with open(file_path, 'r') as file:
        for line in file:
            row = [float(x.strip()) for x in line.split(',')]
            matrix.append(row)
    return matrix

# Example usage:
file_path = '/home/jovyan/data3/results/C03_T100/results.txt'  

matrix = read_matrix(file_path)

# Define colors for ones, zeros, and losses
colors = ['gray', 'green', 'red']
cmap = plt.cm.colors.ListedColormap(colors, N=3)

plt.figure(figsize=(8, 6))
plt.imshow(matrix, cmap=cmap, interpolation='nearest')
plt.colorbar(ticks=[0, 1, 2], label='Value', boundaries=[-0.5, 0.5, 1.5, 2.5])
plt.xlabel('Column')
plt.ylabel('Row')
plt.title('Heatmap of Matrix')
plt.savefig('results_viz.png', dpi=300)
plt.show()  # Display the heatmap
