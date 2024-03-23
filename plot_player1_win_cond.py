import matplotlib.pyplot as plt
from itertools import product

def generate_combinations(n):
    # Generate all combinations of '>', '=', '<' for n pairs
    operators = ['>', '=', '<']
    return list(product(operators, repeat=n))

def process_combinations(combinations):
    processed_combinations = []
    for combo in combinations:
        processed = []
        for i, operator in enumerate(combo):
            if operator == '>':
                processed.append(i + 1)
            elif operator == '=':
                processed.append(0)
            else:  # operator == '<'
                processed.append(-(i + 1))
        processed_combinations.append(processed)
    return processed_combinations

def count_operators(processed_combinations):
    counts = {'>': 0, '=': 0, '<': 0}
    for combo in processed_combinations:
        for val in combo:
            if val > 0:
                counts['>'] += 1
            elif val == 0:
                counts['='] += 1
            else:
                counts['<'] += 1
    return counts

def plot_operator_distribution(n_values):
    percentages = {'>': [], '=': [], '<': []}
    
    for n in n_values:
        combinations = generate_combinations(n)
        processed_combinations = process_combinations(combinations)
        counts = count_operators(processed_combinations)
        total = sum(counts.values())
        for operator in ['>', '=', '<']:
            percentages[operator].append(counts[operator] / total * 100)

    # Plotting
    plt.figure(figsize=(10, 6))
    for operator, values in percentages.items():
        plt.plot(n_values, values, label=f"Operator '{operator}'", marker='o')
    
    plt.xlabel('Number of Castles/Entries (n)')
    plt.ylabel('Percentage')
    plt.title('Percentage Distribution of Comparison Operators as n Grows')
    plt.legend()
    plt.grid(True)
    plt.xticks(n_values)
    plt.savefig(f'player_1_win_cond.png', dpi=300)
    plt.show()


n_values = range(1, 11)  # adjust this range as needed
plot_operator_distribution(n_values)
