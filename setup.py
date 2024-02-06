# --------------------------------------------------------------------------------
# Filename: setup.py
# Author: Tesfa Asmara
# Date Created: 01/02/2024
# Description: This script will configure a Mambaforge environment on NRP machines.
# --------------------------------------------------------------------------------

import os
from pathlib import Path


# os.system(f"$SHELL")
# os.system(f"mamba create -n blotto")
# os.system(f"mamba activate blotto")

# Path to the conda environment
conda_path = Path("/opt/conda/envs/blotto/")

# Path where pip should install packages
pip_install_cmd = Path("/bin/pip install")

# Pip packages to install
pip_packages = []

# Conda packages to install
conda_packages = ["numba", "joblib"]

# Go ahead and install the pip packages
for pkg in pip_packages:
    os.system(f"{conda_path / pip_install_cmd} {cmd}")

# Go ahead and install the conda packages using Mambaforge
for pkg in pip_packages:
    os.system(f"mamba install {cmd} -y")