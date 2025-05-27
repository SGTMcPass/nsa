### Using Monte Carlo > Function Overview

	| This file lists the values used for each variable on each run.																															|
| run\_summary				| This file contains the summary statistical information that is printed out to the screen after a run completes.																			|
| monte\_input				| This file contains the input file commands necessary to rerun a single run as a stand alone simulation. It can be found in the RUN_ folder used to store the run's information.			|

## Dry Runs
A dry run generates only the **monte_runs** and **monte_header** files without actually processing any runs. Dry runs can be used to verify input values before dedicating resources to a full Monte Carlo simulation.
```python
trick.mc_set_dry_run(1)
```

## Optimization
Monte Carlo is capable of running input values that have been derived from the results of previous runs. Monte Carlo is not capable of autonomous and intelligent decision making; it is the responsibility of the user to design the optimization logic by hand.

Optimization code is typically located in either the **monte_master_pre** or **monte_master_post** jobs. There is no hard and fast rule on how to implement optimization, so choose the best method for your specific simulation.

## Function Overview
There are a number of Monte Carlo functions that are available to the user. The following table consists of various C functions that can be called in the input file via:
```python
trick.mc_function_name(function_parameter, "function_parameter2", . . .)
```

| Function Name							| Description																																														|
|--------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| mc\_add\_range						| Adds the specified range to the list of valid ranges. Both the start and end values are inclusive.																								|
| mc\_add\_slave						| Adds the specified slave.																																											|
| mc\_get\_connection\_device\_port		| Returns an integer containing the port of the connection device.																																	|
| mc\_get\_current\_run					| Returns an unsigned integer containing the current run being processed.																															|
| mc\_get\_custom\_post\_text			| Returns a string containing text to be appended to the core slave dispatch.																														|
| mc\_get\_custom\_pre\_text			| Returns a string containing text to be prepended to the core slave dispatch.																														|
| mc\_get\_custom\_slave\_dispatch		| Returns a boolean integer indicating if custom slave dispatches have been enabled.																												|
| mc\_get\_dry\_run						| Returns a boolean integer indicating if this run is a dry run.																																	|
| mc\_get\_enabled						| Returns a boolean integer indicating if this is a Monte Carlo simulation.																															|
| mc\_get\_localhost\_as\_remote		| Returns a boolean integer indicating if the localhost should be treated as a remote machine and use remote shells.																				|
| mc\_get\_max\_tries					| Returns an unsigned integer indicating the number of times that a run may be dispatched. Defaults to two. Zero is limitless.																		|
| mc\_get\_num\_runs					| Returns an unsigned integer indicating the number of runs specified by the user.																													|
| mc\_get\_slave\_id					| Returns an unsigned integer indicating the unique identifier assigned to the slave.																												|
| mc\_get\_timeout						| Returns a double indicating the number of seconds the master should wait for a run to complete.																									|
| mc\_get\_user\_cmd\_string			| Returns a string containing the options that are passed to the remote shell when spawning new slaves.																								|
| mc\_get\_verbosity					| Returns an integer indicating the level of verbosity. <br> 0 = No Messages <br> 1 = Error Messages <br> 2 = Error and Informational Messages <br> 3 = Error, Informational, and Warning Messages	|
| mc\_read								| Gets the connection device and reads the incoming string into a user specified buffer.																											|
| mc\_set\_current\_run					| Sets the current run being processed.																																								|
| mc\_set\_custom\_post\_text			| Sets the string to be appended to the core slave dispatch.																																		|
| mc\_set\_custom\_pre\_text			| Sets the string to be prepended to the core slave dispatch.																																		|
| mc\_set\_custom\_slave\_dispatch		| Sets the boolean integer indicating if custom slave dispatches have been enabled.																													|
| mc\_set\_dry\_run						|
