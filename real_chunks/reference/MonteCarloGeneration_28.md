### 5 Verification

 C++ `<random>` library, from MonteCarloVariableRandom.
    * Populate the command variable inherited from MonteCarloVariable. This is the STL string representing the content that the MonteCarloMaster will place into the generated dispersion files.
    * Call the `insert_units()` method inherited from MonteCarloVariable
    * Set the `command_generated` flag to true if the command has been successfully generated.

## 4.6 Running generated runs within an HPC framework

Modern HPC (High Performance Computing) labs typically have one or more tools for managing the execution of jobs across multiple computers.  There are several linux-based scheduling tools, but this section focuses on running the generated runs using a SLURM (Simple Linux Utility for Resource Management) array job.  Consider this script using a simulation built with gcc 4.8 and a user-configured run named `RUN_example` which has already executed once with the Monte-Carlo Generation model enabled to generate 100 runs on disk:

```bash
#SBATCH --array=0-99

# This is an example sbatch script demonstrating running an array job in SLURM.
# SLURM is an HPC (High-Performance-Computing) scheduling tool installed in
# many modern super-compute clusters that manages execution of a massive
# number of user-jobs.  When a script like this is associated with an array
# job, this script is executed once per enumerated value in the array. After
# the Monte Carlo Generation Model executes, the resulting RUNs can be queued
# for SLURM execution using a script like this. Alternatively, sbatch --wrap
# can be used.  See the SLURM documentation
