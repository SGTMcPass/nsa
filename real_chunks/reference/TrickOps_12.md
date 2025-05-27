### TrickOps > More Information


      self.report()           # Print Verbose report
      self.status_summary()   # Print a Succinct summary
      return (builds_status or runs_status or self.config_errors)
```

The `ExampleWorkflow.py` script uses sims/runs provided by trick to exercise *some* of the functionality provided by TrickOps. This script does not have any comparisons, post-run analyses, or valgrind runs defined in the YAML file, so there is no execution of those tests in this example.

## `compare:` - File vs. File Comparisons

In the `TrickWorkflow` base class, a "comparison" is an easy way to compare two logged data files via an `md5sum` compare.  Many sim workflows generate logged data when their sims run and want to compare that logged data to a stored off baseline (a.k.a regression) version of that file to answer the question: "has my sim response changed?". TrickOps makes it easy to execute these tests by providing a `compare()` function at various levels of the architecture which returns 0 (`False`) on success and 1 (`True`) if the files do not match.

In the YAML file, the `compare:` section under a specific `run:` key defines the comparison the user is interested in. For example consider this YAML file:

```
SIM_ball:
    path: path/to/SIM_ball
    runs:
      RUN_foo/input.py:
      RUN_test/input.py:
        compare:
          - path/to/SIM_ball/RUN_test/log_a.csv vs. regression/SIM_ball/log_a.csv
          - path/to/SIM_ball/RUN_test/log_b.trk vs. regression/SIM_ball/log_b.tr
