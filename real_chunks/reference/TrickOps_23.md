### TrickOps > More Information

 Print to the screen and log a message internally
# Define my own custom job and run it using execute_jobs()
myjob = Job(name='my job', command='sleep 10', log_file='/tmp/out.txt', expected_exit_status=0)
self.execute_jobs([myjob])
```

## Regarding the Design: Why do I have to write my own script?

You may be thinking, "sure it’s great that it only takes a few lines of python code to use this framework, but why isn’t TrickOps just a generic cmdline interface that I can use? Why isn't it just this?":

```bash
./trickops --config project_config.yml
```

This is purposeful -- handling every project-specific constraint is impossible. Here's a few examples of project-specific constraints that make a generic catch-all `./trickops` script very difficult to implement:
*  "I want to fail testing on SIM_a, but SIM_b build is allowed to fail!"
    - Solution: Project-specific script defines success with `sys.exit(<my_critera>)`
*  "I need to add project-specific key-value pairs in the YAML file!"
    - Solution: Project specific script reads `self.config` to get these
*  "I don’t want to use `koviz`, I want to generate errors plots with matlab!"
    - Solution: Project specific script extends `class Comparison`
*  "I have a pre-sim-build mechanism (like `matlab`) that complicates everything!"
    - Solution: Project specific script runs `execute_jobs()` on custom `Job`s before normal sim builds are executed


## Tips & Best Practices

* Commit your YAML file to your project. What gets tested
