import os
import subprocess
from concurrent.futures import ProcessPoolExecutor

# Configuration
ITERATIONS = 10
CASTLES = [5]
TROOPS = [100] # 5, 10, 20, 30, 40, 50, 60, 70, 80, 90,
print(CASTLES, TROOPS)
PROFILE_DIR = "profiling"

# Ensure the profiling directory exists
os.makedirs(PROFILE_DIR, exist_ok=True)

def run_command(command):
    """Run a single command in the shell and capture its output."""
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = process.communicate()
    return stdout.decode(), stderr.decode()

def run_iteration(castle, troop, iteration):
    """Wrapper function to run an iteration for a given castle, troop, and iteration number."""
    commands = [
        f"./sums -c {castle} -t {troop}",
        f"./blotto -c {castle} -t {troop}"
        # ,
        # f"./blotto_parallel -c {castle} -t {troop}",
        # f"python blotto_jit.py -c {castle} -t {troop}",
        # f"python blotto_jit_parallel.py -c {castle} -t {troop}",
        # f"python slowest_blotto.py -c {castle} -t {troop}"
    ]
    
    for command in commands:
        stdout, stderr = run_command(f"ulimit -s unlimited; {command}")
        # stdout, stderr = run_command(f"time {command}")
        filename = os.path.join(PROFILE_DIR, command.split()[0].lstrip("./") + f"_c_{castle}_t_{troop}_profile.txt")
        with open(filename, "a") as file:  # Append mode
            file.write(f"Iteration {iteration}:\n {stdout}\n {stderr}\n")

def main():
    # Create a process pool to execute commands in parallel
    with ProcessPoolExecutor(max_workers=4) as executor:
        futures = []
        for castle in CASTLES:
            for troop in TROOPS:
                for iteration in range(1, ITERATIONS + 1):
                    futures.append(executor.submit(run_iteration, castle, troop, iteration))
        
        # Wait for all futures to complete
        for future in futures:
            future.result()

    print("All iterations completed.")

if __name__ == "__main__":
    main()
