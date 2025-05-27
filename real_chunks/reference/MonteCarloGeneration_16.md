### 5 Verification

 method runs. This is particularly useful if it is desired to compare two distribution sets for the same run.

    ```monte_carlo.master.monte_dir = “MONTE_RUN_1_vers2”```

* Changing the input file name. It is expected that most applications of this model will run with a typical organization of a Trick simulation. Consequently, the original input file is probably named input.py, and this is the default setting for the input_file_name variable. However, to support other cases, this variable is public and can be changed at any time between construction and the execution of the `MonteCarloMaster::execute()` method.

    ```monte_carlo.master.input_file_name = “modified_input.py”```

* Padding the filenames of the generated files. By default, the generated RUN directories in the generated MONTE_* directory will have their numerical component padded according to the number of runs. When:
    * between 1 - 10 runs are generated, the directories will be named RUN_0, RUN_1, …
    * between 11-100 runs are generated, the directories will be named RUN_00, RUN_01, …
    * between 101-1000 runs are generated, the directories will be named RUN_000, RUN_001, …
    * etc.

    Specification of a minimum padding width is supported. For example, it might be desired to create 3 runs with names RUN_00000, RUN_00001, and RUN_00002, in which case the minimum-padding should be specified as 5 characters

    ```monte_carlo.master.minimum_padding = 5```

* Changing the run-name. For convenience, the
