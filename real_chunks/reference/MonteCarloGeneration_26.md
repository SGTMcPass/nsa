### 5 Verification



The construction arguments are:
1. variable name
2. seed for random generator, defaults to 0
3. lower-bound of distribution, default to 0
4. upper-bound for distribution, defaults to 1

There is no additional configuration beyond the constructor

#### 4.3.3.9 MonteCarloVariableSemiFixed

The construction arguments are:
1. variable name
2. reference to the MonteCarloVariable whose generated value is to be used as the fixed value.

There is no additional configuration beyond the constructor.

#### 4.3.3.10 MonteCarloPythonLineExec

The construction arguments are:
1. variable name
2. an STL-string providing the Python instruction for the computing of the value to be assigned to the specified variable.

There is no additional configuration beyond the constructor.

#### 4.3.3.11 MonteCarloPythonFileExec
The construction argument is:
1. name of the file to be executed from the generated input file.

There is no additional configuration beyond the constructor.

## 4.4 Information on the Generated Files

This section is for informational purposes only to describe the contents of the automatically-generated dispersion files. Users do not need to take action on any content in here.

The generated files can be broken down into 3 parts:
* Configuration for the input file. These two lines set the flags such that when this file is executed, the content of the original input file will configure the run for a monte-carlo analysis but without re-generating the dispersion files.

```python
monte_carlo.master.active = True
monte_carlo.master.generate_dispersions = False
```

* Execution of the original input
