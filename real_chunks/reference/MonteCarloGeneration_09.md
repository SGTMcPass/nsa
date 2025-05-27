### 5 Verification

 a wild-card, \<executive\> `MONTE_RUN_test/RUN*/monte_input.py`
* a batch-script,
* a set of batch-scripts launching subsets onto different machines,
* a load-management service, like SLURM
* any other mechanism tailored to the user’s currently available computing resources

The intention is that the model runs very early in the simulation sequence. If the model is inactive (as when running a regular, non-MonteCarlo run), it will take no action. But when this model is activated, the user should expect the simulation to terminate before it starts on any propagation.

**When a simulation executes with this model active, the only result of the simulation will be the generation of files containing the assignments to the dispersed variables. The simulation should be expected to terminate at t=0.**

## 4.1.1 Trick Users

The model is currently configured for users of the Trick simulation engine. The functionality of the model is almost exclusively independent of the chosen simulation engine, with the exceptions being the shutdown sequence, and the application of units information in the variables.

Found at the end of the `MonteCarloMaster::execute()` method, the following code:

```c++
exec_terminate_with_return(0, __FILE__, __LINE__,message.c_str());
```

is a Trick instruction set to end the simulation.

Found at the end of `MonteCarloVariable::insert_units()`, the following code:

```c++
// TODO: Pick a unit-conversion mechanism
// Right now, the only one available is Trick:
trick_units( pos_equ+1);
```

provides the call to

```c++
MonteCarloVariable::trick
