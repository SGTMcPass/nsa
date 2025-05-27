### Using Monte Carlo > Function Overview

| [Home](/trick) → [Documentation Home](../Documentation-Home) → [Simulation Capabilities](Simulation-Capabilities) → Monte Carlo |
|------------------------------------------------------------------|

# Introduction
Monte Carlo is an advanced simulation capability provided by Trick that allows users to repeatedly run copies of a simulation with different input values. Users can vary the input space of a simulation via input file, random value generation, or by calculating values from previous Monte Carlo runs in a process called optimization.

# Design
### Master
The master controller for any given Monte Carlo simulation delegates run information to distributed slave instances. The master is responsible for spawning and managing the state of all slaves for a given simulation.

![MonteCarlo-Master-LifeCycle](images/MonteCarlo-Master-LifeCycle.png)


### Slave
A Monte Carlo slave simulation is responsible for the execution of the runs delegated by the master controller. Should a simulation run fail, the slave will inform the master and continue running until explicitly killed or disconnected. Slaves consume only a single CPU and run only one job at a time. If you want to increases parallelism, you should create multiple slaves. Creating one slave per CPU is a reasonable approach.

![MonteCarlo-Slave-LifeCycle](images/MonteCarlo-Slave-LifeCycle.png)


### Monte Carlo Jobs
There are 8 Monte Carlo specific Trick jobs that users can use to direct how their Monte Carlo simulation runs.

| Trick Job						| Description																		|
|-------------------------------|-----------------------------------------------------------------------------------|
| **monte\_master\_init**		| Runs once in the master upon initialization and before any slaves are created.	|
| **monte\_master\_pre**		| Runs in the master before each run is dispatched.									|
| **monte\_master\_post**		| Runs in the master each time a slave completes a run.								|
| **monte\_master\_shutdown**	| Runs once in the master after all runs have completed.							|
| **monte\_slave\_init**		| Runs once in each slave upon initialization.										|
| **monte\_slave\_pre**			| Runs in the slave before each received dispatch is executed. 						|
| **monte\_slave\_post**		| Runs in the slave each time this slave completes a run.							|
| **monte\_slave\_shutdown**	| Runs once in the slave before termination.										|


![MonteCarlo-JobOrder](images/MonteCarlo-JobOrder.png)


# Using Monte Carlo
## Enabling Monte Carlo
In order to use Monte Carlo functionality, it is necessary to first enable Monte Carlo in the simulation input file.
```python
trick.mc_set_enabled(1)
```

## Variable Types
There are four different Monte Carlo variable types available to users: **File**, **Random**, **Calculated**, **Fixed**

### File
MonteVarFile allows users to store specific values in an column delimited input file.
```python
FileVariable = trick.MonteVarFile("variable_name", "input_file_name", column_number, "variable_unit")
trick_mc.mc.add_variable(FileVariable)
```

The columns in the input file can be separated by tabs or spaces; both will work and can even be combined in the same file on the same line. The left most column is typically the run number, though this is not a requirement; variable values can begin in this column if desired.
```
0 50 1959
1 60 1402
2 75	5832
3 43	7823
4	02	4935
5	19	6928
```

### Random
MonteVarRandom allows users to randomly generate input values by using a distribution formula.
```python
RandomVariable = trick.MonteVarRandom("variable_name", distribution, "variable_unit", engine)
RandomVariable.set_seed(1)
RandomVariable.set_sigma(0.6667)
RandomVariable.set_mu(4.0)
RandomVariable.set_min(-4.0)
RandomVariable.set_max(4.0)
RandomVariable.set_sigma_range(0)
trick_mc.mc.add_variable(RandomVariable)
```

There are three distribution methods for random value generation: **Gaussian**, **Poisson**, and **Flat**

[**Gaussian distribution**](https://en.wikipedia.org/wiki/Normal_distribution), otherwise known as normal distribution, will generate a typical bell curve of distributed values. <br>
[**Poisson distribution**](https://en.wikipedia.org/wiki/Poisson_distribution) will generate a distribution to match a Poisson curve. <br>
[**Flat distribution**](https://en.wikipedia.org/wiki/Uniform_distribution_(continuous)) will generate a uniform distribution of values between the minimum and maximum. This
