### 5 Verification

00000, RUN_00001, and RUN_00002, in which case the minimum-padding should be specified as 5 characters

    ```monte_carlo.master.minimum_padding = 5```

* Changing the run-name. For convenience, the run-name is provided as an argument in the MonteCarloMaster::activate(...) method. The run_name variable is public, and can be reset after activation and before the `MonteCarloMaster::execute()` method runs. Because this setting determines which run is to be launched from the dispersion files, resetting run_name has limited application – effectively limited to correcting an error, which could typically be more easily corrected directly.

    ```monte_carlo.master.run_name = “RUN_2”```

## 4.3 MonteCarlo Variables (MonteCarloVariable)

The instantiation of the MonteCarloVariable instances is typically handled as a user-input to the simulation without requiring re-compilation. As such, these are usually implemented in Python input files. This is not a requirement, and these instances can be compiled as part of the simulation build. Both cases are presented.

### 4.3.1 Instantiation and Registration

For each variable to be dispersed, an instance of a MonteCarloVariable must be created, and that instance registered with the MonteCarloMaster instance:

1. Identify the type of dispersion desired
2. Select the appropriate type of MonteCarloVariable to provide that dispersion.
3. Create the new instance using its constructor.
4. Register it with the MonteCarloMaster using the `MonteCarloMaster::add_variable( MonteVarloVariable&)` method

#### 4.3.1.1 Python input file
