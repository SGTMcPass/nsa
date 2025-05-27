### 5 Verification

```c++
// TODO: Pick a unit-conversion mechanism
// Right now, the only one available is Trick:
trick_units( pos_equ+1);
```

provides the call to

```c++
MonteCarloVariable::trick_units(
 size_t insertion_pt)
{
 command.insert(insertion_pt, " trick.attach_units(\"" + units + "\",");
 command.append(")");
```

which appends Trick instructions to interpret the generated value as being represented in the specified units.

The rest of the User’s Guide will use examples of configurations for Trick-simulation input files

## 4.1.2 Non-Trick Users

To configure the model for simulation engines other than Trick, the Trick-specific content identified above should be replaced with equivalent content that will result in:
* the shutdown of the simulation, and
* the conversion of units from the type specified in the distribution specification to the type native to the variable to which the generated value is to be assigned.

While the rest of the User’s Guide will use examples of configurations for Trick-simulation input files, understand that these are mostly just C++ or Python code setting the values in this model to make it work as desired. Similar assignments would be required for any other simulation engine.

## 4.2 MonteCarlo Manager (MonteCarloMaster)

### 4.2.1 Instantiation

The instantiation of MonteCarloMaster would typically be done directly in the S_module. The construction of this instance takes a single argument, a STL-string describing its own location within the simulation data-structure.

The MonteCarloMaster class has a single public-interface method call, `MonteCarloMaster::execute()`. This method has 2
