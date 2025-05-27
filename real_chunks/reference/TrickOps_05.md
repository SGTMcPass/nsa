### TrickOps > More Information

 is *no limit* to number of `SIM`s, `runs:`, `compare:` lists, `valgrind` `runs:` list, etc.  This file is intended to contain every Sim and and every sim's run, and every run's comparison and so on that your project cares about.  Remember, this file represents the *pool* of tests, not necessarily what *must* be tested every time your scripts which use it run.

## Learn TrickOps with an Example Workflow that uses this Trick Repository

Included in TrickOps is `ExampleWorkflow.py`, which sets up a simple "build all sims, run all runs" testing script in less than 20 lines of code!  It clones the Trick repo from https://github.com/nasa/trick.git, writes a YAML file describing the sims and runs to test, then uses TrickOps to build sims and run runs in parallel. To see it in action, simply run the script:

```bash
cd trick/share/trick/trickops/
./ExampleWorkflow.py
```
When running, you should see output that looks like this:

![ExampleWorkflow In Action](images/trickops_example.png)

When running this example script, you'll notice that tests occur in two phases. First, sims build in parallel up to three at a time. Then when all builds complete, sims run in parallel up to three at a time. Progress bars show how far along each build and sim run is at any given time. The terminal window will accept scroll wheel and arrow input to view current builds/runs that are longer than the terminal height. Before the script finishes, it reports a summary of what was done, providing a list of which sims and runs were successful
