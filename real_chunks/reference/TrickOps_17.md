### TrickOps > More Information

if.csv
```
In this example, `SIM_many_runs` has 101 runs. Instead of specifying each individual run (`RUN_000/`, `RUN_001`, etc), in the `yaml` file, the `[000-100]` notation is used to specify a set of runs. All sub-fields of the run apply to that same set. For example, the default value of `0` is used for `returns:`, which also applies to all 101 runs. The `compare:` subsection supports the same range notation, as long as the same range is used in the `run:` named field. Each of the 101 runs shown above has two comparisons. The first `compare:` line defines a common file to be compared against all 101 runs. The second `compare:` line defines run-specific comparisons using the same `[integer-integer]` sequence.  Note that when using these range notations zero-padding must be consistent, the values (inclusive) must be non-negative, and the square bracket notation must be used with the format `[minimum-maximum]`.


## `phase:` - An optional mechanism to order builds, runs, and analyses

The `yaml` file supports an optional parameter `phase: <integer>` at the sim and run level which allows the user to easily order sim builds, runs, and/or analyses, to suit their specific project constraints. If not specified, all sims, runs, and analyses, have a `phase` value of `0` by default. Consider this example `yaml` file with three sims:

```yaml
SIM_car:
  path: sims/SIM_car

SIM_monte:
  path: sims/SIM_monte
  runs:
