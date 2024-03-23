import matplotlib.pyplot as plt
from scipy.special import factorial
import numpy as np

# Function to calculate the expression (C+T-1)! / (T! * (C-1)!)
def calculate_combinations(C, T):
    return factorial(C + T - 1) / (factorial(T) * factorial(C - 1))

# Define the range of castles and troops
castles = [2, 3, 4, 5, 6, 7, 8, 9, 10]  # Example: 2 to 10 castles
troops = range(1, 101)  # Troops from 1 to 100

# Plotting
plt.figure(figsize=(10, 6))

for C in castles:
    combinations = [calculate_combinations(C, T) for T in troops]
    plt.plot(troops, combinations, label=f'Castles: {C}', marker='o')

plt.xlabel('Number of Soldiers (S)')
plt.ylabel('Number of Configurations (C)')
plt.title('Growth of Configurations as Soldiers Increase for Each Number of Castles')
plt.legend()
plt.yscale('log')  # Use logarithmic scale to better visualize the growth
plt.grid(True)
plt.savefig(f'configuration_size.png', dpi=300)
plt.show()
