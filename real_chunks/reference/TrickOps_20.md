### TrickOps > More Information

.get_jobs(kind='analysis', phase=range(0, TrickWorkflow.allowed_phase_range['max'+1]))
```
Note that since analysis jobs are directly tied to a single named run, they inherit the `phase` value of their run as specfied in the `yaml` file. In other words, do not add a `phase:` section indented under any `analyze:` section in your `yaml` file.

It's worth emphasizing that the specfiication of a non-zero `phase` in the `yaml` file, by itself, does not affect the order in which actions are taken.  **It is on the user of TrickOps to use this information to order jobs appropriately**.  Here's an example in code of what that might look for the example use-case described by the `yaml` file in this section:

```python
    first_build_jobs  = self.get_jobs(kind='build', phase=-1) # Get all build jobs with phase -1 (SIM_external)
    second_build_jobs = self.get_jobs(kind='build', phase=0)  # Get all build jobs with phase 0 (SIM_car & SIM_monte)
    first_run_jobs    = self.get_jobs(kind='run', phase=-1)   # Get all run jobs with phase -1 (RUN_nominal/input.py --monte-carlo)
    second_run_jobs   = self.get_jobs(kind='run', phase=0)    # Get all run jobs with phase 0  (All generated runs & RUN_test/input.py)

    # SIM_external must build before SIM_car and SIM_monte, for project-specific reasons
    builds_status1 = self.execute_jobs(first_build_jobs,  max_concurrent
