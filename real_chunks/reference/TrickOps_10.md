### TrickOps > More Information

 your scripts are going to be run in a continuous integration (CI) testing framework such as GitHub Actions, GitLab CI, or Jenkins, because it suppresses all `curses` logic during job execution which itself expects `stdin` to exist.

When `TrickWorkflow` initializes, it reads the `config_file` and verifies the information given matches the expected convention. If a non-fatal error is encountered, a message detailing the error is printed to `stdout` and the internal timestamped log file under `log_dir`. A fatal error will `raise RuntimeError`. Classes which inherit from `TrickWorkflow` may also access `self.parsing_errors` and `self.config_errors` which are lists of errors encountered from parsing the YAML file and errors encountered from processing the YAML file respectively.

Moving on to the next few important lines of code in our `ExampleWorkflow.py` script.  The `def run(self):` line declares a function whose return code on run is passed back to the calling shell via `sys.exit()`. This is where we use the functions given to us by inherting from `TrickWorkflow`:


```python
      build_jobs      = self.get_jobs(kind='build')
      run_jobs        = self.get_jobs(kind='run')
      builds_status   = self.execute_jobs(build_jobs, max_concurrent=3, header='Executing all sim builds.')
      runs_status     = self.execute_jobs(run_jobs,   max_concurrent=3, header='Executing all sim runs.')
```

These four lines of code will build all simulations in our config file in parallel up to three at once, followed by running all simulation runs in parallel up to three at once.  The `get_jobs()` function
