### 5 Verification

3. Create the new instance using its constructor.
4. Register it with the MonteCarloMaster using the `MonteCarloMaster::add_variable( MonteVarloVariable&)` method

#### 4.3.1.1 Python input file implementation for Trick:

When the individual instances are registered with the master, it only records the address of those instances. A user may create completely new variable names for each dispersion, or use a generic name as illustrated in the example below. Because these are typically created within a Python function, it is important to add the thisown=False instruction on each creation to prevent its destruction when the function returns.

```python
mc_var = trick.MonteCarloVariableRandomUniform( "object.x_uniform", 0, 10, 20)
mc_var.thisown = False
monte_carlo.master.add_variable(mc_var)
mc_var = trick.MonteCarloVariableRandomNormal( "object.x_normal", 0, 0, 5)
mc_var.thisown = False
monte_carlo.master.add_variable(mc_var)
```

#### 4.3.1.2 C++ implementation in its own class:

In this case, the instances do have to be uniquely named.

Note that the registering of the variables could be done in the class constructor rather than in an additional method (process_variables), thereby eliminating the need to store the reference to MonteCarloMaster. In this case, the `generate_dispersions` flag is completely redundant because the variables are already registered by the time the input file is executed. Realize, however, that doing so does carry the overhead of registering those variables with the MonteCarloMaster every time the simulation starts up. This
