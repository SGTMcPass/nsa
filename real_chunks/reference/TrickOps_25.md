### TrickOps > More Information

.
* If `TrickWorkflow` encounters non-fatal errors while verifying the content of the given YAML config file, it will add those errors to the internal `self.config_errors` list of strings. If you want your script to return non-zero on any non-fatal error, include `self.config_errors` in the criteria used for  `sys.exit(<success_criteria>)`. Similar recommendation for `self.parsing_errors` which contains all errors found while parsing the YAML file.
* Treat the YAML file like your project owns it.  You can store project-specific information and retrieve that information in your scripts by accessing the `self.config` dictionary. Anything not recognized by the internal validation of the YAML file is ignored, but that information is still provided to the user. For example, if you wanted to store a list of POCS in your YAML file so that your script could print a helpful message on error, simply add a new entry `project_pocs: email1, email2...` and then access that information via `self.config['project_pocs']` in your script.

## `MonteCarloGenerationHelper` - TrickOps Helper Class for `MonteCarloGenerate.sm` users

TrickOps provides the `MonteCarloGenerationHelper` python module as an interface between a sim using the `MonteCarloGenerate.sm` (MCG) sim module and a typical Trick-based workflow.  This module allows MCG users to easily generate monte-carlo runs and execute them locally or alternatively through an HPC job scheduler like SLURM. Below is an example usage of the module. This example assumes:
1. The using script inherits from or otherwise leverages `TrickWorkflow`,
