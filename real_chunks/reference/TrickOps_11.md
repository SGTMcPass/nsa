### TrickOps > More Information

, header='Executing all sim runs.')
```

These four lines of code will build all simulations in our config file in parallel up to three at once, followed by running all simulation runs in parallel up to three at once.  The `get_jobs()` function is the easiest way to get a set of jobs from the pool of jobs we defined in our config file of a certain `kind`. It will return a list of `Job` instances matching the `kind` given. For example `build_jobs = self.get_jobs(kind='build')` means "give me a list of every job which builds a simulation defined in my config file".  These `Job` instances can then be passed as a list to the `execute_jobs()` function which manages their execution and collection of their return codes and output.  `execute_jobs` will start the list of `Job`s given to it, running a maximum of `max_concurrent` at a time, and returns 0 (`False)` if all jobs success, 1 (`True`) if any job failed. `kind` can be: `'build'`, `'run'`, `'valgrind'`, or `'analysis'`.

The last three lines simply print a detailed report of what was executed and manage the exit codes so that `ExampleWorkflow.py`'s return code can be trusted to report pass/fail status to the calling shell in the typical linux style: zero on success, non-zero on failure.

```python
      self.report()           # Print Verbose report
      self.status_summary()   # Print a Succinct summary
      return (builds_status or runs_status or self.config_errors)
```

The `ExampleWorkflow.py` script uses sims/runs
