### 5 Verification

 will configure the run for a monte-carlo analysis but without re-generating the dispersion files.

```python
monte_carlo.master.active = True
monte_carlo.master.generate_dispersions = False
```

* Execution of the original input file. This line opens the original input file so that when this file is executed, the original input file is also executed automatically.

```python
exec(open('RUN_1/input.py').read())
```

* Assignment to simulation variables. This section always starts with the assignment to the run-number, which is also found in the name of the run, so RUN_0 gets a 0, RUN_1 gets a 1, etc. This value can be used, for example, to generate data sweeps as described in section MonteCarloPythonLineExec above.

```python
monte_carlo.master.monte_run_number = 0
object.test_variable1 = 5
object.test_variable1 = 1.23456789
...
```

## 4.5 Extension

The model is designed to be extensible and while we have tried to cover the most commonly used applications, complete anticipation of all use-case needs is impossible. The most likely candidate for extension is in the area of additional distributions. In this case:
* A new distribution should be defined in its own class
* That class shall inherit from MonteCarloVariable or, if it involves a random generation using a distribution found in the C++ `<random>` library, from MonteCarloVariableRandom.
    * Populate the command variable inherited from MonteCarloVariable. This is the STL string representing the content that the MonteCarloMaster will place into the generated dispersion files.
    * Call
