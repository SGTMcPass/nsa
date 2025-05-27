### TrickOps > More Information

  # Slurm: https://slurm.schedmd.com/documentation.html
  sbj = mgh.get_sbatch_job(monte_dir="path/to/MONTE_RUN_mc")
  # Execute the sbatch job, which queues all runs in SLURM for execution
  # Use hpc_passthrough_args ='--wait' to block until all runs complete
  ret = self.execute_jobs([sbj])

  # Instead of using SLURM, generated runs can be executed locally through
  # TrickOps calls on the host where this script runs. First get a list of
  # run jobs
  run_jobs = mgh.get_generated_run_jobs(monte_dir="path/to/MONTE_RUN_mc")
  # Then execute all generated SingleRun instances, up to 10 at once
  ret = self.execute_jobs(run_jobs, max_concurrent=10)
```

Note that the number of runs to-be-generated is configured somewhere in the `input.py` code and this module cannot robustly know that information for any particular use-case. This is why `monte_dir` is a required input to several functions - this directory is processed by the module to understand how many runs were generated.


## More Information

A lot of time was spent adding `python` docstrings to the modules in the `trickops/` directory and tests under the `trickops/tests/`. This README does not cover all functionality, so please see the in-code documentation and unit tests for more detailed information on the framework capabilities.

[Continue to Software Requirements](../software_requirements_specification/SRS)
