### 5 Verification

 match (including the case of a dimensionless value), this method is not needed.
* This method is not applicable to all types of MonteCarloVariable; use with MonteCarloVariableRandomBool and MonteCarloPython* is considered undefined behavior.

#### 4.3.3.2 MonteCarloVariableFile

The construction arguments are:

1. variable name
2. filename containing the data
3. column number containing data for this variable
4. (optional) first column number. This defaults to 1, but some users may want to zero-index their column numbers, in which case it can be set to 0.

There is no additional configuration beyond the constructor

There is no additional configuration beyond the constructor.

#### 4.3.3.3 MonteCarloVariableFixed

The construction arguments are:
1. variable name
2. value to be assigned

Additional configuration for this model includes the specification of the maximum number of lines to skip between runs.
`max_skip`.  This public variable has a default value of 0 – meaning that the next run will be drawn from the next line of data, but this can be adjusted.

#### 4.3.3.4 MonteCarloVariableRandomBool

The construction arguments are:
1. variable name
2. seed for random generator
There is no additional configuration beyond the constructor.

#### 4.3.3.5 MonteCarloVariableRandomNormal

The construction arguments are:
1. variable name
2. seed for random generator, defaults to 0
3. mean of distribution, defaults to 0
4. standard-deviation of distribution, defaults to 1.

The normal distribution may be truncated, and there
