### Using Monte Carlo > Function Overview

 will not exceed the fewest number of runs in any given input file.

## Ranges
After establishing the number of simulation runs, users can specify subsets within that number that the simulation should focus on. If no range is specified, all runs will be dispatched.

```python
trick.mc_add_range(25, 50)
trick.mc_add_range(73)
trick.mc_add_range(90, 100)
```
These three function calls will tell Monte Carlo to only process runs 25-50, 73, and 90-100. The values are inclusive and additive.

## Creating Slaves
The simplest way to create a new slave is to call `trick.mc_add_slave` with the machine name in the input file.

```python
trick.mc_add_slave("localhost")
```

Each slave will consume a single CPU and run one job at a time. If you have multiple CPUs, it can be reasonable to create a slave for each.

```python
import multiprocessing
for i in range(multiprocessing.cpu_count()):
    trick.mc_add_slave("localhost")
```

You can distribute your slaves across any machines that have your simulation compiled on them.

```python
trick.mc_add_slave("localhost")
trick.mc_add_slave("remote-machine")
trick.mc_add_slave("other-machine")
trick.mc_add_slave("extra-machine")
trick.mc_add_slave("secret-machine")
```

### Modifying Slave Options

`trick.mc_add_slave` is nice and simple, and it's generally all you need. However, [`MonteSlave`](https://github.com/nasa/trick/blob/master/include/trick/MonteCarlo.hh) has a few options you might want to modify. For instance, you can change the remote shell from `ssh` to something else or add arguments to the remote shell invocation. To do that, you need a reference to the `MonteSlave`, but `mc_add_slave`, being a C function, cannot return a class instance. But don't worry! It's easy to create one yourself.

```python
# instantiate the slave
slave = trick.MonteSlave("machine-name")
# now I can access its members
slave.remote_shell = trick.TRICK_RSH # who needs security?
# finally, add it to Trick
trick_mc.mc.add_slave(slave)
```

If you're curious about the last time, we are calling the `add_slave` function of the [`MonteCarlo`](https://github.com/nasa/trick/blob/master/include/trick/MonteCarlo.hh) instance (`mc`) of the [`MonteCarloSimObject`](https://github.com/nasa/trick/blob/master/share/trick/sim_objects/default_trick_sys.sm) instance (`trick_mc`).
## Notes
1. [SSH](https://en.wikipedia.org/wiki/Secure_Shell) is is the default remote shell.
1. Each slave will work in parallel with other slaves, greatly reducing the computation time of a Monte Carlo.
1. The faster a machine is, the more work it can do.
1. If a slave dies, the master will redistribute the missing work.
1. Communication between the master and slaves is done via sockets.
1. Monte Carlo slaves are CPU hogs. They do not play nice with the users of other machines.
1. Monte Carlo always runs distributed. If no slave is manually added, a single slave on `localhost` is created.
1. Slaves can be created in **monte\_master\_pre** and **monte\_master\_post** jobs.

## Data Logging
Each Monte Carlo run generates data logging files in a **MONTE_** directory on the machine that processed the run. Existing run directories are not cleaned and are overwritten when a new Monte Carlo simulation begins.

| Data File					| Description																																												|
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| monte\_header				| This file contains the input file lines that configured the initial state of the Monte Carlo simulation. Information on the number of runs and the variables specified are in this file.	|
| monte\_runs				| This file lists the values used for each variable on each run.																															|
| run\_summary				| This file contains the summary statistical information that is printed out to the screen after a run completes.																			|
| monte\_input				| This file contains the input file commands necessary to rerun a single run as a stand alone simulation. It can be found in the RUN_ folder used to store the run's information.			|

## Dry Runs
A dry run generates only the **monte_runs** and **monte_header** files without actually processing any runs. Dry runs can be used to verify input values before dedicating resources to a full Monte Carlo simulation.
```python
trick.mc
