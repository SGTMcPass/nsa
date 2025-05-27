### Trick Realtime Best Practices > Do's, Don'ts, and Wisdom > 5. Miscellaneous

.gnu.org/onlinedocs/gcc/Optimize-Options.html)
* [Clang Optimization Options](https://clang.llvm.org/docs/CommandGuide/clang.html#code-generation-options)


#### 1.5 Disable unused jobs in Trick sims

Jobs can be enabled and disabled from the input file with the following commands:

```
trick.exec_get_job(<job_name>, <instance_num>).enable()
trick.exec_get_job(<job_name>, <instance_num>).disable()
```

Alternatively, we can use:

```
trick.exec_set_job_onoff(<job_name>, <instance_num>, True|False)
```

If a job isn't necessary for a particular RUN scenario, consider disabling it. But, make sure that it doesn’t impact the rest of the sim.

##### Example:

Suppose ```SIM_submarine```'s S_define file contains the job ```submarine.diagnostics```:

```
...
(0.1, "scheduled")          submarine.diagnostics();
...
};
SubmarineSimObject dyn;
...
```
This job only transmits information. It doesn't affect the simulation, but does degrade realtime performance slightly. To disable it, we'll add the following to our input file:

```trick.exec_get_job("dyn.submarine.diagnostics", 0).disable()```


#### 1.6 Name the child threads in your Trick sim
Do this for easier identification of time spikes.

```trick.exec_get_thread(<thread_id>).set_name(<name>)```

##### Example:

In ```SIM_lander's``` ```S_define```, suppose we specify that ```lander.control()``` job is to run in thread 1 (C1):

``` C1  (0.1, "scheduled")          lander.control() ;```

Then in the input file, we add:

```trick.exec_get_thread(1).set_name("LanderControl")```

to name the C1 thread "LanderControl".


#### 1.7 Use ```default_data``` jobs to specify the default sim state. Customize it with the input file.

Prefer ```default_data``` jobs as the **primary** means of initializing your sim. Then, **customize** the default for different scenarios, with an input file. Try to make your sim capable of initializing to a valid state with an empty input file.

Doing this has several benefits.

1. The sim will initialize faster because ```default_data``` jobs are compiled rather that interpreted.

2. If you can test and confirm that your base, default, "empty input file" sim is initialized to a valid state, then it will be easier to identify errors when the sim is customized for different scenarios, via an input file. It saves time and reduces pain.

---
### 2. User Simulation Software
---

#### 2.1 Don't read from the disk during run-time.
Disk access is slow. If you need to read from disk, do it in
