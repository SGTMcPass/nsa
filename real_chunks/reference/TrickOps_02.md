### TrickOps > More Information

## The YAML File

The YAML file is a required input to the framework which defines all of the tests your project cares about. This is literally a list of sims, each of which may contain runs, each run may contain comparisons and post-run analyses and so on. Here's a very simple example YAML file for a project with two sims, each having one run:

```yaml
SIM_spacecraft:
  path: sims/SIM_spacecraft
  runs:
    RUN_test/input.py:
      returns: 0

SIM_visiting_vehicle:
  path: sims/SIM_visiting_vehicle
  runs:
    RUN_test/input.py:
      returns: 0
```
Simple and readable, this config file is parsed by `PyYAML` and adheres to all normal YAML syntactical rules.  Additionally the Trick-Workflow expected convention for defining sims, runs, comparisons, etc. is described in the `TrickWorkflow` docstrings and also summarized in detail below:

```yaml
globals:
  env:                 <-- optional literal string executed before all tests, ex: ". env.sh"
SIM_abc:               <-- required unique name for sim of interest, must start with SIM
  path:                <-- required SIM path relative to project top level
  description:         <-- optional description for this sim
  labels:              <-- optional list of labels for this sim, can be used to get sims
      - model_x            by label within the framework, or for any other project-defined
      - verification       purpose
  build_args:          <-- optional literal args passed to trick-CP during sim build
  binary:              <-- optional name of sim binary, defaults to S_main_{cpu}.exe
