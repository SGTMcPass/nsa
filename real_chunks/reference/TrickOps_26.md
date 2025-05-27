### TrickOps > More Information

 generate monte-carlo runs and execute them locally or alternatively through an HPC job scheduler like SLURM. Below is an example usage of the module. This example assumes:
1. The using script inherits from or otherwise leverages `TrickWorkflow`, giving it access to `self.execute_jobs()`
2. `SIM_A` is already built and configured with  the `MonteCarloGenerate.sm` sim module
3. `RUN_mc/input.py` is configured with to generate runs when executed, specifically that `monte_carlo.mc_master.generate_dispersions == monte_carlo.mc_master.active == True` in the input file.

```python
# Instantiate an MCG helper instance, providing the sim and input file for generation
mgh = MonteCarloGenerationHelper(sim_path="path/to/SIM_A", input_path="RUN_mc/input.py")
# Get the generation SingleRun() instance
gj = mgh.get_generation_job()
# Execute the generation Job to generate RUNS
ret = self.execute_jobs([gj])

if ret == 0:  # Successful generation
  # Get a SLURM sbatch array job for all generated runs found in monte_dir
  # SLURM is an HPC (High-Performance-Computing) scheduling tool installed on
  # many modern super-compute clusters that manages execution of a massive
  # number of jobs. See the official documentation for more information
  # Slurm: https://slurm.schedmd.com/documentation.html
  sbj = mgh.get_sbatch_job(monte_dir="path/to/MONTE_RUN_mc")
  # Execute the sbatch job, which queues all runs in SL
