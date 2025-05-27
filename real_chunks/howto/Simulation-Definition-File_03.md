### Trick Header Comment > Create Connections

,
etc. The child process specification allows parallel processing for simulation modules.

Every simulation has a parent process. A child specification will result in the spawning of
a thread for each distinct child ID specified. More than one job can be specified for each child ID.
Jobs with child specifications will run in parallel with other jobs within each software frame,
so users may be required to specify job dependencies (see Section 4.4.10) to keep parallel jobs
from stepping on each other's common data access. The collection of the parent process and all
of its children defined in one S_define file is referred to as a Process Group (PG). A simulation
can be composed of multiple synchronized or non-synchronized PGs which will be discussed in more
detail in Section 4.4.12. and Section 7.2.

In most cases, for maximum execution performance, jobs should only be specified to run on a child
process if the host workstation has more than one CPU; and preferably, one CPU per child specified.
With the same rule in mind, using more than one PG in the simulation design should only occur when
the simulation has parallel components and multiple process/multiple computers are available. When
the host workstation has only one CPU, a simulation with a job running on a child will be much slower
than the same simulation with no children. There are exceptions to this rule, like running asynchronous
background modules on a child that only runs the child during the wait cycle of a simulation set up for
real-time operations.

Child IDs start at 1 and may skip any integer values. The Trick Executive will spawn enough threads
to accomodate the highest Child ID specified in the S_define file.  Jobs without a child specification
will be executed by the parent process. Jobs with a C1 child specification will be executed by the
first child thread; jobs with a C2 specification will be executed by the second child thread; and so on.

Child Threads have three different scheduling choices.  See [Executive Scheduler](https://nasa.github.io/trick/documentation/simulation_capabilities/Executive-Scheduler) -> [Thread Control](https://nasa.github.io/trick/documentation/simulation_capabilities/Executive-Scheduler#thread-control) for child thread scheduling
details.

### Job Tagging

This optional field allows you to tag a job or set of jobs.  The tag is surrounded in curly
braces.  In the input file, you may then operate on the tag.  All jobs with the same tag will be
modified in the same manner.  For example, if jobA and jobB are tagged BLUE, the input file may
have a statement:

```python
trick.add_read(13.0, """trick.exec_set_job_cycle("BLUE" , 0.001)""")
```

This will change the frequency of the jobs to 1 millisecond.  You might also disable the jobs
tagged BLUE
