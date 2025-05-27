### 5 Verification

 with value above that of the mean; min does not mean “distance to the left of the mean”, it means the smallest acceptable value relative to the mean.

`truncate_low( double limit, TruncationType)`

This method provides a one-sided truncation. All generated values will be above the limit specification.

`truncate_high( double limit, TruncationType)`

This method provides a one-sided truncation. All generated values will be below the limit specification.

`untruncate()`

This method removes previously configured truncation limits.

#### 4.3.3.6 MonteCarloVariableRandomStringSet

The construction arguments are:
1. variable name
2. seed for random generator

This type of MonteCarloVariable contains a STL-vector of STL-strings containing the possible values that can be assigned by this generator. This vector is NOT populated at construction time and must be configured.

`add_string(std::string new_string)`

This method adds the specified string (`new_string`) to the vector of available strings

#### 4.3.3.7 MonteCarloVariableRandomUniform

The construction arguments are:
1. variable name
2. seed for random generator, defaults to 0
3. lower-bound of distribution, default to 0
4. upper-bound for distribution, defaults to 1

There is no additional configuration beyond the constructor

#### 4.3.3.8 MonteCarloVariableRandomUniformInt

The construction arguments are:
1. variable name
2. seed for random generator, defaults to 0
3. lower-bound of distribution, default to 0
4. upper-bound for distribution, defaults to 1

There is no additional configuration
