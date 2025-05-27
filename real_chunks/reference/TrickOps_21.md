### TrickOps > More Information

 run jobs with phase 0  (All generated runs & RUN_test/input.py)

    # SIM_external must build before SIM_car and SIM_monte, for project-specific reasons
    builds_status1 = self.execute_jobs(first_build_jobs,  max_concurrent=3, header='Executing 1st phase sim builds.')
    # SIM_car and SIM_monte can build at the same time with no issue
    builds_status2 = self.execute_jobs(second_build_jobs, max_concurrent=3, header='Executing 2nd phase sim builds.')
    # SIM_monte's 'RUN_nominal/input.py --monte-carlo' generates runs
    runs_status1   = self.execute_jobs(first_run_jobs,    max_concurrent=3, header='Executing 1st phase sim runs.')
    # SIM_monte's 'MONTE_RUN_nominal/RUN*/monte_input.py' are the generated runs, they must execute after the generation is complete
    runs_status2   = self.execute_jobs(second_run_jobs,   max_concurrent=3, header='Executing 2nd phase sim runs.')
```
Astute observers may have noticed that `SIM_external`'s `RUN_test/input.py` technically has no order dependencies and could execute in either the first or second run job set without issue.

A couple important points on the motivation for this capability:
* Run phasing was primarly developed to support testing monte-carlo and checkpoint sim scenarios, where output from a set of scenarios (like generated runs or dumped checkpoints) becomes the input to another set of sim scenarios.
* Sim phasing exists primarly to support testing scenarios where sims are poorly architectured or immutable, making them unable to be
