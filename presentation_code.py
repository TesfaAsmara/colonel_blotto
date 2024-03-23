import subprocess
import os

# Constants
CASTLES = [2]
TROOPS = [5, 10]
profile_dir = "profiling"

# Create the profiling directory
os.makedirs(profile_dir, exist_ok=True)

# Function to create an empty file
def create_file(filename):
    with open(filename, "w") as f:
        pass  # Just create the file, don't write anything

for castle in CASTLES:
    for troop in TROOPS:
        print(f"Running for {castle} castles and {troop} troops")
        create_file(f"{profile_dir}/sums_c_{castle}_t_{troop}_profile.txt")
        create_file(f"{profile_dir}/blotto_c_{castle}_t_{troop}_profile.txt")
        create_file(f"{profile_dir}/blotto_jit_py_c_{castle}_t_{troop}_profile.txt")
        create_file(f"{profile_dir}/blotto_jit_parallel_py_c_{castle}_t_{troop}_profile.txt")
        create_file(f"{profile_dir}/slowest_blotto_py_c_{castle}_t_{troop}_profile.txt")

# Function to run a command and redirect its output
def run_command(command, output_file):
    with open(output_file, "w") as f:
        subprocess.run(command, shell=True, stdout=f, stderr=subprocess.STDOUT)

# Loop through each troop value and run the commands
for castle in CASTLES:
    for troop in TROOPS:
        print(f"Running for {castle} castles and {troop} troops")
        run_command(f"time ./sums -c {castle} -t {troop}", f"{profile_dir}/sums_c_{castle}_t_{troop}_profile.txt")
        run_command(f"time ./blotto -c {castle} -t {troop}", f"{profile_dir}/blotto_c_{castle}_t_{troop}_profile.txt")
        run_command(f"time python blotto_jit.py -c {castle} -t {troop}", f"{profile_dir}/blotto_jit_py_c_{castle}_t_{troop}_profile.txt")
        run_command(f"time python blotto_jit_parallel.py -c {castle} -t {troop}", f"{profile_dir}/blotto_jit_parallel_py_c_{castle}_t_{troop}_profile.txt")
        run_command(f"time python slowest_blotto.py -c {castle} -t {troop}", f"{profile_dir}/slowest_blotto_py_c_{castle}_t_{troop}_profile.txt")

# Finally, run the plotting script
subprocess.run("python plot_profiling.py", shell=True)
