### 5 Verification

 RUN_02, RUN_03, etc. each of which will contain one of the generated dispersion files.
* In the instructions written into the generated dispersion files to execute the content of the input file found in `<argument>`.

#### 4.2.2.3 Additional Configurations

There are additional configurations instructing the MonteCarloMaster on the generation of the new dispersion files. Depending on the use-case, these could either be embedded within the `if monte_carlo.master.generate_dispersions:` block of the original input file, or in the secondary input file (or command-line arguments if configured to do so).

* Number of runs is controlled with a single statement, e.g.

    ```monte_carlo.master.set_num_runs(10)```

* Generation of meta-data. The meta-data provides a summary of which variables are being dispersed, the type of dispersion applied to each, the random seeds being used, and correlation between different variables. This is written out to a file called MonteCarlo_Meta_data_output in the MONTE_* directory.

    ```monte_carlo.master.generate_meta_data = True```

* Changing the name of the automatically-generated monte-directory. By default, this takes the form “MONTE_\<run_name\>” as assigned in the MonteCarloMaster::activate(...) method. The monte_dir variable is public and can be reset after activation and before the `MonteCarloMaster::execute()` method runs. This is particularly useful if it is desired to compare two distribution sets for the same run.

    ```monte_carlo.master.monte_dir = “MONTE_RUN_1_vers2”```

* Changing the input file name. It
