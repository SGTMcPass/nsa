### TrickOps > More Information

 the run level
r = self.get_sim('SIM_ball').get_run('RUN_test/input.py')
ret = r.compare()             # Execute all comparisons for run 'RUN_test/input.py'
```

In all three of these options, `ret` will be 0 (`False`) if all comparisons succeeded and 1 (`True`) if at least one comparison failed.  You may have noticed the `get_jobs()` function does not accept `kind='comparison'`. This is because comparisons are not `Job` instances. Use `compare()` to execute comparisons and `get_jobs()` with `execute_jobs()` for builds, run, analyses, etc.

### Koviz Utility Functions

When a comparison fails, usually the developer's next step is to look at the differences in a plotting tool. TrickOps provides an interface to [koviz](https://github.com/nasa/koviz), which lets you quickly and easily generate error plot PDFs when a set of comparisons fail. This requires that the `koviz` binary be on your user `PATH` and that your `koviz` version is newer than 4/1/2021.  Here are a couple examples of how to do this:

```python
# Assuming we're in a python script using TrickWorkflow as a base class and have
# executed a compare() which has failed...

# OPTION 1: Get all koviz report jobs for all failed comparisons in your YAML file
(koviz_jobs, failures) = self.get_koviz_report_jobs()
# Execute koviz jobs to generate the error plots, up to four at once
if not failures:
  self.execute_jobs(koviz_jobs, max_concurrent=4, header
