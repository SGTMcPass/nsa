### Using Monte Carlo > Function Overview

.set_max(4.0)
RandomVariable.set_sigma_range(0)
trick_mc.mc.add_variable(RandomVariable)
```

There are three distribution methods for random value generation: **Gaussian**, **Poisson**, and **Flat**

[**Gaussian distribution**](https://en.wikipedia.org/wiki/Normal_distribution), otherwise known as normal distribution, will generate a typical bell curve of distributed values. <br>
[**Poisson distribution**](https://en.wikipedia.org/wiki/Poisson_distribution) will generate a distribution to match a Poisson curve. <br>
[**Flat distribution**](https://en.wikipedia.org/wiki/Uniform_distribution_(continuous)) will generate a uniform distribution of values between the minimum and maximum. This distribution can only use the **set\_min() and set\_max()** functions.

| Distribution Variables		| Function																				| Description																																																										|
|-------------------------------|---------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Seed							| MonteVarRandom.set\_seed()															| This is the randomization seed.																																																					|
| Sigma							| MonteVarRandom.set\_sigma()															| This is the standard deviation. The larger this value, the broader the bell curve will be.																																						|
| Mu							| MonteVarRandom.set\_mu()																| This value specifies the center of the bell curve.																																																|
| Min <br> Max					| MonteVarRandom.set\_min() <br> MonteVarRandom.set\_max()								| These are the absolute cutoff limits. Any values outside of these bounds are discarded.																																							|
| Rel\_min <br> Rel\_max		| MonteVarRandom.set\_min\_is\_relative() <br> MonteVarRandom.set\_max\_is\_relative()	| These booleans specify if the minimum and maximum values are relative to the Mu value. If the **Mu** is 20 and both the **relative minimum** and **relative maximum** are 5, then the **actual minimum** is 15 and the **actual maximum** is 25.	|

There are also several different psuedo-random engines available to choose from. If no engine is specified, Trick will default to its own random number engine.

| Engine						|
|-------------------------------|
| NO\_ENGINE					|
| TRICK\_DEFAULT\_ENGINE		|
| RANLUX\_BASE\_01\_ENGINE		|
| RANLUX\_64\_BASE\_01\_ENGINE	|
| MINSTD\_RAND\_ENGINE			|
| MT19937\_ENGINE				|
| MT19937\_64\_ENGINE			|
| RANLUX\_24\_BASE\_ENGINE		|
| RANLUX\_44\_BASE\_ENGINE		|
| RANLUX\_24\_ENGINE			|
| RANLUX\_44\_ENGINE			|
| KNUTH\_B\_ENGINE				|

### Calculated
Calculated values are created in user-designed Monte Carlo jobs. The primary purpose of the MonteVarCalculated variable type is for optimization.
```python
CalculatedVariable = trick.MonteVarCalculated("variable_name", "variable_unit")
trick_mc.mc.add_variable(CalculatedVariable)
```

### Fixed
Fixed values are not changed from simulation to simulation.
```python
FixedVariable = trick.MonteVarFixed("variable_name", variable_value, "variable_unit")
trick_mc.mc.add_variable(FixedVariable)
```

## Runs
Users can specify how many times they wish for a simulation to run by using the following function:
```python
trick.mc_set_num_runs(100)
```

For a series of **randomly generated values**, Monte Carlo will execute the simulation the number of times specified.

For a series of values listed in an **input file**, Monte Carlo will execute the number of runs specified and will not exceed the number of runs in the input file.

For multiple variables listed in **multiple input files**, Monte Carlo will execute the fewest number of runs specified and will not exceed the fewest number of runs in any given input file.

## Ranges
After establishing the number of simulation runs, users can specify subsets within that number that the simulation should focus on. If no range is specified, all runs will be dispatched.

```python
trick.mc_add_range(25, 50)
trick.mc_add_range(73)
trick.mc_add_range(90, 100)
```
These three function calls will tell Monte Carlo to only process runs 25-50, 73, and 90-100. The values are inclusive and additive.

## Creating Slaves
The simplest way to create a new slave is to call `trick.mc_add_slave` with the machine name in
