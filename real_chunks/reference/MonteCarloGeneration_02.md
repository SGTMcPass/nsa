### 5 Verification

1. The model shall provide the ability to assign a common value to all runs:
    1. This value could be a fixed, user-defined value
    1. This value could be a random assignment, generated once and then applied to all runs
1. The model shall provide the capability to read values from a pre-generated file instead of generating its own values
1. The model shall provide the ability to randomly select from a discrete data set, including:
    1. enumerations,
    1. character-strings,
    1. boolean values, and
    1. numerical values
1. The model shall provide the capability to compute follow-on variables, the values of which are a function of one or more dispersed variables with values generated using any of the methods in requirements 1-5.
1. The model shall provide a record of the generated distributions, allowing for repeated execution of the same scenario using exactly the same conditions.
1. The model shall provide summary data of the dispersions which have been applied, including:
    1. number of dispersions
    1. types of dispersions
    1. correlations between variables

# 3 Model Specification

## 3.1 Code Structure

The model can be broken down into its constituent classes; there are two principle components to the model – the variables,
and the management of the variables.

### 3.1.1 Variable Management (MonteCarloMaster)

MonteCarloMaster is the manager of the MonteCarlo variables. This class controls how many sets of dispersed variables
are to be generated; for each set, it has the responsibility for
* instructing each variable to generate its own
