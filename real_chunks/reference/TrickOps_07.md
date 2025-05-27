### TrickOps > More Information

, log_dir='/tmp/',
            trick_dir=trick_top_level, config_file="/tmp/config.yml", cpus=3, quiet=quiet)
    def run( self):
      build_jobs      = self.get_jobs(kind='build')
      run_jobs        = self.get_jobs(kind='run')

      builds_status = self.execute_jobs(build_jobs, max_concurrent=3, header='Executing all sim builds.')
      runs_status   = self.execute_jobs(run_jobs,   max_concurrent=3, header='Executing all sim runs.')
      self.report()           # Print Verbose report
      self.status_summary()   # Print a Succinct summary
      return (builds_status or runs_status or self.config_errors)
if __name__ == "__main__":
    sys.exit(ExampleWorkflow(quiet=(True if len(sys.argv) > 1 and 'quiet' in sys.argv[1] else False)).run())
```
Let's look at a few key parts of the example script. Here, we create a new class arbitrarily named `ExampleWorkflow` which inherits from `TrickWorkflow`, which is a class provided by the `TrickWorkflow.py` module. As part of its class setup, it clones a new `trick` repo from GitHub and places it in `/tmp/`. Since '/tmp/trick' provides many example sims and runs, we eat our own dogfood here and use it to represent our `project_top_level` for example purposes.

```python
from TrickWorkflow import *
class ExampleWorkflow(TrickWorkflow):
    def __init__( self, quiet, trick_top_level='/tmp/trick'):
        # Real projects already have trick somewhere, but for this example, just clone &
