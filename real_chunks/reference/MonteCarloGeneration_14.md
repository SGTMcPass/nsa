### 5 Verification

onte_carlo.py”).read())
 if monte_carlo.master.generate_dispersions:
 exec(open(“Modified_data/monte_variables.py").read())
else:
 exec(open(“Log_data/log_for_regular.py”).read())
```
 3. If the `generate_dispersions` flag is also set to true, the `MonteCarloMaster::execute()` method will execute,
generating the dispersion files and shutting down the simulation.

#### 4.2.2.2 Initiating MonteCarlo

Somewhere outside this file, the `active` and generate_dispersion flags must be set. This can be performed either in a separate input file or via a command-line argument. Unless the command-line argument capability is already supported, by far the easiest mechanism is to create a new input file that subsequently reads the existing input file:

```
monte_carlo.master.activate("RUN_1")
exec(open("RUN_1/input.py").read())
```

The activate method takes a single string argument, representing the name of the run. This must be exactly the same name as the directory containing the original input file, “RUN_1” in the example above. This argument is used in 2 places (\<argument\> in these descriptions refers to the content of the argument string):

* In the creation of a `MONTE_<argument>` directory. This directory will contain some number of sub-directories identified as, for example, RUN_01, RUN_02, RUN_03, etc. each of which will contain one of the generated dispersion files.
* In the instructions written into the generated dispersion files to execute the content of the input file found in `<argument>`.

#### 4.2.
