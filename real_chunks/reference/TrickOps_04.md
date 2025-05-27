### TrickOps > More Information

 d vs. e            are supported as long as they match the pattern in the parent run.
        - ...                All non-list values are ignored and assumed to be used to define
        - ...                an alternate comparison method in a class extending this one
      analyze:         <-- optional arbitrary string to execute as job in bash shell from
                           project top level, for project-specific post-run analysis
      phase:           <-- optional phase to be used for ordering runs if needed
      valgrind:        <-- optional string of flags passed to valgrind for this run.
                           If missing or empty, this run will not use valgrind
non_sim_extension_example:
  will: be ignored by TrickWorkflow parsing for derived classes to implement as they wish
```

Almost everything in this file is optional, but there must be at least one top-level key that starts with `SIM` and it must contain a valid `path: <path/to/SIM...>` with respect to the top level directory of your project. Here, `SIM_abc` represents "any sim" and the name is up to the user, but it *must* begin with `SIM` since `TrickWorkflow` purposefully ignores any top-level key not beginning with `SIM` and any key found under the `SIM` key not matching any named parameter above.  This design allows for extensibility of the YAML file for non-sim tests specific to a project.

There is *no limit* to number of `SIM`s, `runs:`, `compare:` lists, `valgrind` `runs:` list, etc.  This file is intended to contain every Sim and and every sim's run, and every run
