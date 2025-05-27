### 5 Verification

 be registered with the master in the constructor rather than in an additional method, with the same caveats presented earlier.

```c++
class MonteCarloSimObject : public Trick::SimObject
{
 public:
  MonteCarloMaster                master;
  MonteCarloVariableRandomUniform x_uniform;
  MonteCarloVariableRandomNormal  x_normal;
  ...
  MonteCarloSimObject(std::string location)
  :
    master(location),
    x_uniform("object.x_uniform", 0, 10, 20),
    x_normal ("object.x_normal", 0, 0, 5),
    ...
{ };
  void process_variables() {
    master.add_variable(x_uniform);
    master.add_variable(x_normal);
    ...
};
  {
    P_MONTECARLO ("initialization") master.execute();
} };
MonteCarloSimObject monte_carlo("monte_carlo.master");
```

### 4.3.2 input-file Access

If using a (compiled) C++ implementation with the registration conducted at construction, the `generate_dispersions` flag is not used in the input file.

```python
if monte_carlo.master.active:
 if monte_carlo.master.generate_dispersions:
 exec(open(“Modified_data/monte_variables.py").read())
```

(where monte_variables.py is the file containing the mc_var = … content described earlier)

```python
if monte_carlo.master.active:
 if monte_carlo.master.generate_dispersions:
 monte_carlo_variables.process_variables()
```

If using a (compiled) C++ implementation with a method to process the registration, that method call must be contained inside the `generate_dispersions` gate in
