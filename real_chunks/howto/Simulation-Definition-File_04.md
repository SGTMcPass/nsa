### Trick Header Comment > Create Connections

 same tag will be
modified in the same manner.  For example, if jobA and jobB are tagged BLUE, the input file may
have a statement:

```python
trick.add_read(13.0, """trick.exec_set_job_cycle("BLUE" , 0.001)""")
```

This will change the frequency of the jobs to 1 millisecond.  You might also disable the jobs
tagged BLUE with the following:

```python
trick.add_read(10.0, """trick.exec_set_job_onoff("BLUE" , False)""")
```

### Job Phasing

The next field of a job declaration is an optional phase number specification in the form of a
capital P immediately followed by an integer phase ID number from 1 to 65534, e.g., P1, P2, P3, etc.
Without a specified phase field, the default phase number is 60000.  The phase specification may be
used on all class jobs to sequence the execution of jobs in the same class.  Jobs tagged with P1
execute first, then P2, etc.  Jobs with the same phase number are executed in the order they are
in the S_define.

### Execution Schedule Time Specification

The execution schedule specification specifies the job's execution cycle time, start time, and
stop time. The time specs must be a comma separated list of floating point numbers enclosed by
parentheses, e.g. (1.0,0.5,10.0) would execute a module starting at 0.5 seconds, and every 1.0
seconds thereafter until 10.0 seconds was reached (9.5 seconds would be the time of the last
job call). The start and stop fields are optional; e.g. (1.0,0.5) does the same as the previous
example except the module will keep being called after 10.0 seconds. Also, a (1.0) specification
will start the job at 0.0 (the default) and continue calling the job at 1.0 second intervals.

Only the jobs categorized as CYCLIC or also
the freeze_scheduled job class (see Table SD_1 below) require the execution time specification.
All schedule time specifications are in seconds.

All other job classes categorized in Table SD_1 should NOT specify an execution time specification:
- NON-CYCLIC (red color) of course do not require a spec because they run only once.
- FRAME-BOUNDARY (blue color) are tied to each execution frame and not a cycle time.
- INTEGRATOR (cyan color) are specified via the state integration specifications for the simulation (see Section 4.4.7).ME-BOUNDARY (blue color) are tied to each execution frame and not a cycle time.
- INTEGRATOR (cyan color) are specified via the state integration
