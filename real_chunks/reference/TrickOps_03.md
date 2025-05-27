### TrickOps > More Information

 or for any other project-defined
      - verification       purpose
  build_args:          <-- optional literal args passed to trick-CP during sim build
  binary:              <-- optional name of sim binary, defaults to S_main_{cpu}.exe
  size:                <-- optional estimated size of successful build output file in bytes
  phase:               <-- optional phase to be used for ordering builds if needed
  parallel_safety:     <-- <loose|strict> strict won't allow multiple input files per RUN dir.
                           Defaults to "loose" if not specified
  runs:                <-- optional dict of runs to be executed for this sim, where the
    RUN_1/input.py --foo:  dict keys are the literal arguments passed to the sim binary
    RUN_2/input.py:        and the dict values are other run-specific optional dictionaries
    RUN_[10-20]/input.py:  described in indented sections below. Zero-padded integer ranges
                           can specify a set of runs with continuous numbering using
                           [<starting integer>-<ending integer>] notation
      returns: <int>   <---- optional exit code of this run upon completion (0-255). Defaults
                             to 0
      compare:         <---- optional list of <path> vs. <path> comparison strings to be
        - a vs. b            compared after this run is complete. Zero-padded integer ranges
        - d vs. e            are supported as long as they match the pattern in the parent run.
        - ...                All non-list values are ignored and assumed to be used to define
        - ...                an alternate comparison method in a class extending this one
