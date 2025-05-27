### TrickOps > More Information

phase` value of `0` by default. Consider this example `yaml` file with three sims:

```yaml
SIM_car:
  path: sims/SIM_car

SIM_monte:
  path: sims/SIM_monte
  runs:
    RUN_nominal/input.py --monte-carlo:        # Generates the runs below
      phase: -1
    MONTE_RUN_nominal/RUN_000/monte_input.py:  # Generated run
    MONTE_RUN_nominal/RUN_001/monte_input.py:  # Generated run
    MONTE_RUN_nominal/RUN_002/monte_input.py:  # Generated run
    MONTE_RUN_nominal/RUN_003/monte_input.py:  # Generated run
    MONTE_RUN_nominal/RUN_004/monte_input.py:  # Generated run

# A sim with constraints that make the build finnicky, and we can't change the code
SIM_external:
  path: sims/SIM_external
  phase: -1
  runs:
    RUN_test/input.py:
      returns: 0
```
Here we have three sims: `SIM_car`, `SIM_monte`, and `SIM_external`. `SIM_car` and `SIM_monte` have the default `phase` of `0` and `SIM_external` has been assigned `phase: -1` explicitly.  If using non-zero phases, jobs can be optionally filtered by them when calling helper functions like `self.get_jobs(kind, phase)`. Some examples:
```python
    build_jobs = self.get_jobs(kind='build')                   # Get all build jobs regardless of phase
    build_jobs = self.get_jobs(kind
