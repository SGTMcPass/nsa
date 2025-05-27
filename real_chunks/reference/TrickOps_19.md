### TrickOps > More Information

 filtered by them when calling helper functions like `self.get_jobs(kind, phase)`. Some examples:
```python
    build_jobs = self.get_jobs(kind='build')                   # Get all build jobs regardless of phase
    build_jobs = self.get_jobs(kind='build', phase=0)          # Get all build jobs with (default) phase 0
    build_jobs = self.get_jobs(kind='build', phase=-1)         # Get all build jobs with phase -1
    build_jobs = self.get_jobs(kind='build', phase=[0, 1, 3])  # Get all build jobs with phase 0, 1, or 3
    build_jobs = self.get_jobs(kind='build', phase=range(-10,11)) # Get all build jobs with phases between -10 and 10
```
This can be done for runs and analyses in the same manner:
```python
    run_jobs = self.get_jobs(kind='run')                # Get all run jobs regardless of phase
    run_jobs = self.get_jobs(kind='run', phase=0)       # Get all run jobs with (default) phase 0
    # Get all run jobs with all phases less than zero
    run_jobs = self.get_jobs(kind='run',      phase=range(TrickWorkflow.allowed_phase_range['min'],0))
    # Get all analysis jobs with all phases zero or greater
    an_jobs  = self.get_jobs(kind='analysis', phase=range(0, TrickWorkflow.allowed_phase_range['max'+1]))
```
Note that since analysis jobs are directly tied to a single named run, they inherit the `phase` value of their run as specfied
