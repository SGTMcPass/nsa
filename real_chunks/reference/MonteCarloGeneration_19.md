### 5 Verification

persions` flag is completely redundant because the variables are already registered by the time the input file is executed. Realize, however, that doing so does carry the overhead of registering those variables with the MonteCarloMaster every time the simulation starts up. This can a viable solution when there are only a few MonteCarloVariable instances, but is generally not recommended; using an independent method (process_variables) allows restricting the registering of the variables to be executed only when generating new dispersions.

```c++
class MonteCarloVarSet {
 private:
  MonteCarloMaster & master;
 public:
  MonteCarloVariableRandomUniform x_uniform;
  MonteCarloVariableRandomNormal x_normal;
  ...
  MonteCarloVarSet( MonteCarloMaster & master_)
   :
   master(master_),
   x_uniform("object.x_uniform", 0, 10, 20),
   x_normal ("object.x_normal", 0, 0, 5),
   ...
 { };

 void process_variables() {
   master.add_variable(x_uniform);
   master.add_variable(x_normal);
 ...
 }
};
```

#### 4.3.1.3 C++ implementation within a Trick S-module:

Instantiating the variables into the same S-module as the master is also a viable design pattern. However, this can lead to a very long S-module so is typically only recommended when there are few variables. As with the C++ implementation in a class, the variables can be registered with the master in the constructor rather than in an additional method, with the same caveats presented earlier.

```c++
class MonteCarloSimObject : public Trick::SimObject
{
 public:
  MonteCarloMaster                master;
  Monte
