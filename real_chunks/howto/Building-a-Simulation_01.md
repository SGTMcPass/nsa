### Root

 job dependencies for distributed process simulations.
1. With a complete simulation definition file, the developer invokes the Trick simulation Configuration Processor (CP). CP reads the simulation definition file and generates all simulation specific source code for the runtime executive, and all ASCII data base files for the user interface. CP also compiles the simulation specific source code and links in the object code libraries. Trick takes care of all executive, I/O, and file management chores that have traditionally given simulation developers fits in the past.
1. The developer may now create data product specification files, if data analysis is required. These files specify logged parameters to access, and display data in either plot or table format.
1. We now move into the simulation user domain (included in the developer’s domain). At this point the simulation is ready to operate. The user must first generate an input file.
1. The user now may execute one or more simulation runs.
1. During or after simulation execution the user may use the UI to post process simulation output data in either plot or tabular format.

[Continue to Model Source Code](Model-Source-Code)
