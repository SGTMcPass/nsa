### 5 Verification

e_carlo.master.generate_dispersions:
 monte_carlo_variables.process_variables()
```

If using a (compiled) C++ implementation with a method to process the registration, that method call must be contained inside the `generate_dispersions` gate in the input file:
```
if monte_carlo.master.active:
 # add only those lines such as logging configuration
```

### 4.3.3 Configuration

For all variable-types, the variable_name is provided as the first argument to the constructor. This variable name must include the full address from the top level of the simulation. After this argument, each variable type differs in its construction arguments and subsequent configuration options.

#### 4.3.3.1 MonteCarloVariable

MonteCarloVariable is an abstract class; its instantiable implementations are presented below. There is one important configuration for general application to these implementations, the setting of units. In a typical simulation, a variable has an inherent unit-type; these are often SI units, but may be based on another system. Those native units may be different to those in which the distribution is described. In this case, assigning the generated numerical value to the variable without heed to the units mismatch would result in significant error.

```set_units(std::string units)```

This method specifies that the numerical value being generated is to be interpreted in the specified units.

Notes
* if it is known that the variable’s native units and the dispersion units match (including the case of a dimensionless value), this method is not needed.
* This method is not applicable to all types of MonteCarloVariable; use with MonteCarloVariableRandomBool and MonteCarloPython* is considered undefined behavior.

####
