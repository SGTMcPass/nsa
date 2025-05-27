### TrickOps > More Information

 will be transformed into a `Job()` instance that can be retrieved and executed via `execute_jobs()` just like any other test. All analyze jobs are assumed to return 0 on success, non-zero on failure.  One example use case for this would be creating a `jupytr` notebook that contains an analysis of a particular run.

## Defining sets of runs using [integer-integer] range notation

The `yaml` file for your project can grow quite large if your sims have a lot of runs. This is especially the case for users of monte-carlo, which may generate hundreds or thousands of runs that you may want to execute as part of your TrickOps script. In order to support these use cases without requiring the user to specify all of these runs individually, TrickOps supports a zero-padded `[integer-integer]` range notation in the `run:` and `compare:` fields. Consider this example `yaml` file:

```yaml
SIM_many_runs:
  path: sims/SIM_many_runs
  runs:
    RUN_[000-100]/monte_input.py:
      returns: 0
      compare:
        sims/SIM_many_runs/RUN_[000-100]/log_common.csv vs. baseline/sims/SIM_many_runs/log_common.csv
        sims/SIM_many_runs/RUN_[000-100]/log_verif.csv  vs. baseline/sims/SIM_many_runs/RUN_[000-100]/log_verif.csv
```
In this example, `SIM_many_runs` has 101 runs. Instead of specifying each individual run (`RUN_000/`, `RUN_001`, etc), in the `yaml` file, the `[000-100]`
