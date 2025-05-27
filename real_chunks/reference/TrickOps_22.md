### TrickOps > More Information

, where output from a set of scenarios (like generated runs or dumped checkpoints) becomes the input to another set of sim scenarios.
* Sim phasing exists primarly to support testing scenarios where sims are poorly architectured or immutable, making them unable to be built independently.


## Where does the output of my tests go?

All output goes to a single directory `log_dir`, which is a required input to the `TrickWorkflow.__init__()` function. Sim builds, runs, comparisons, koviz reports etc. are all put in a single directory with unique names.  This is purposeful for two reasons:

1. When a failure occurs, the user can always find verbose output in the same place
1. Easy integration into  CI artifact collection mechanisms. Just collect `log_dir` to get all verbose output for successful and failed tests alike.

Logging for the `TrickWorfklow` itself, including a list of all executed tests will automatically be created in `<log_dir>/log.<timestamp>.txt`

## Other Useful Examples

```python
# Assuming you are within the scope of a class inheriting from TrickWorkflow ...
self.report()                  # Report colorized verbose information regarding the pool of tests
s = self.status_summary()      # Print a succinct summary regarding the pool of tests
myvar = self.config['myvar'])  # Access custom key 'myvar' in YAML file
tprint("My important msg")     # Print to the screen and log a message internally
# Define my own custom job and run it using execute_jobs()
myjob = Job(name='my job', command='sleep 10', log_file='/tmp/out.txt', expected_exit_status=0)
self
