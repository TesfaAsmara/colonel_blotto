# Path to the file
file_path = '/home/jovyan/data3/results/C03_T100/results.txt'

# Initialize a dictionary to hold the wins, losses, and total games for each index
strategy_stats = {}

# Function to update the stats
def update_stats(index, result):
    if index not in strategy_stats:
        strategy_stats[index] = {'wins': 0, 'losses': 0, 'ties': 0, 'total': 0}
    if result == '1':
        strategy_stats[index]['wins'] += 1
    elif result == '-1':
        strategy_stats[index]['losses'] += 1
    else: # Assuming the result can only be 1, -1, or tie (0)
        strategy_stats[index]['ties'] += 1
    strategy_stats[index]['total'] += 1

# Open the file and process each line
with open(file_path, 'r') as file:
    for line in file:
        parts = line.strip().split('_')
        if len(parts) == 3:
            index1, index2, result = parts
            update_stats(index1, result)
            # Inverse result for symmetry
            inverse_result = '1' if result == '-1' else '-1' if result == '1' else '0'
            update_stats(index2, inverse_result)

# Calculate win rates and find the index with the highest win rate
highest_win_rate = -1
best_index = None
for index, stats in strategy_stats.items():
    # Exclude ties from win rate calculation if desired
    win_rate = stats['wins'] / (stats['total'] - stats['ties']) if (stats['total'] - stats['ties']) > 0 else 0
    if win_rate > highest_win_rate:
        highest_win_rate = win_rate
        best_index = index

print(f"Index with the highest win rate: {best_index} (Win rate: {highest_win_rate:.2f})")
