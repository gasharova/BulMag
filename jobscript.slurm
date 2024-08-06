#!/bin/bash -l
#SBATCH --account=lp_h_ds_2023_2024
#SBATCH --cluster=wice
#SBATCH --nodes=1
#SBATCH --job-name=bloom_filter_testing_gasharova
# 5 minutes?
#SBATCH --time=02:00:00

module load Python/3.11.3-GCCcore-12.3.0
module show Python/3.11.3-GCCcore-12.3.0

source ~/env2/bin/activate

# Print Python version and path
# python --version
# which python

# List installed packages
pip list

python benchmark.py

deactivate
