### Using Monte Carlo > Function Overview

| mc\_read								| Gets the connection device and reads the incoming string into a user specified buffer.																											|
| mc\_set\_current\_run					| Sets the current run being processed.																																								|
| mc\_set\_custom\_post\_text			| Sets the string to be appended to the core slave dispatch.																																		|
| mc\_set\_custom\_pre\_text			| Sets the string to be prepended to the core slave dispatch.																																		|
| mc\_set\_custom\_slave\_dispatch		| Sets the boolean integer indicating if custom slave dispatches have been enabled.																													|
| mc\_set\_dry\_run						| Sets the boolean integer indicating the current run is a dry run.																																	|
| mc\_set\_enabled						| Sets the boolean integer indicating if this is a Monte Carlo simulation.																															|
| mc\_set\_localhost\_as\_remote		| Sets the boolean integer indicating if the localhost should be treated as a remote machine and use remote shells.																					|
| mc\_set\_max\_tries					| Sets the number of times that a run may be dispatched. Default is two. Zero is limitless.																											|
| mc\_set\_num\_runs					| Sets the number of runs to do.																																									|
| mc\_set\_timeout						| Sets the number of seconds the master should wait for a run to complete.																															|
| mc\_set\_user\_cmd\_string			| Sets the string containing the options that are passed to the remote shell when spawning new slaves.																								|
| mc\_set\_verbosity					| Sets an integer indicating the level of verbosity. <br> 0 = No Messages <br> 1 = Error Messages <br> 2 = Error and Informational Messages <br> 3 = Error, Informational, and Warning Messages		|
| mc\_start\_slave						| Starts the specified slave.																																										|
| mc\_stop\_slave						| Stops the specified slave.																																										|
| mc\_write								| Gets the connection device and writes the user specified buffer into it.																															|
| mc\_is\_slave							| Returns a boolean integer indicating if the current executive is running as a slave.																												|

[Continue to Master Slave](Master-Slave)
