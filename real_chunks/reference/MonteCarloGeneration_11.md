### 5 Verification

 construction of this instance takes a single argument, a STL-string describing its own location within the simulation data-structure.

The MonteCarloMaster class has a single public-interface method call, `MonteCarloMaster::execute()`. This method has 2 gate-keeping flags that must be set (the reason for there being 2 will be explained later):
* `active`
* `generate_dispersions`

If either of these flags is false (for reference, `active` is constructed as false and `generate_dispersions` is constructed as true) then this method returns with no action. If both are true, then the model will generate the dispersions, write those dispersions to the external files, and shut down the simulation.

An example S-module

```c++
class MonteCarloSimObject : public Trick::SimObject
{
 public:
 MonteCarloMaster master; // <--- master is instantiated
 MonteCarloSimObject(std::string location)
 :
 master(location) // <--- master is constructed with this STL-string
 {
 P_MONTECARLO ("initialization") master.execute(); // <--- the only function
call
 }
};
MonteCarloSimObject monte_carlo("monte_carlo.master"); // <--- location of “master”
                                                               is passed as an
                                                               argument
```

### 4.2.2 Configuration

The configuration of the MonteCarloMaster is something to be handled as a user-input to the simulation without requiring re-compilation; as such, it is typically handled in a Python input file. There are two sections for configuration:
* modifications to the regular input file, and
* new file-input or other external monte-carlo initiation
