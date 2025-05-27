### Trick Header Comment > Create Connections

 header files.  They include the model class and structure definitions as well as C prototypes for
functions used in the S_define file.  Double pound files are copied, minus one pound, to S_source.hh.

## User Header Code Block

This section of the S_define (encapsulated by "%header{...%}") can be used for including header files
directly into the S_source.hh. Header files listed here will not be input processed.

## User Code Block

This section of the S_define (encapsulated by %{.....%}) can be used for any user specific
global C code. CP will simply insert this section of code into the S_source.c file after
all header files are included. Typically this feature is used as a quick method for customizing
simulations with additions of global variables and functions.

## Simulation Object Definition

A simulation definition file may contain any number of simulation object definitions.
A simulation object definition is of the form: class <sim_object_name> : public Trick::SimObject { ... }.
All sim objects must inherit from the Trick::SimObject or a derivative.  A sim object definition
may contain zero or more data structure declarations and zero or more module declarations.

## Model Classes and Data Structures

Model classes and data structures are declared within a sim object. Model classes and data structures
may be public, protected, or private within the sim object.  Standard C++ privacy rules apply to
all data with the sim object. Sim object protected and private data will not be accessible to the input
processor.

Intrinsic types are allowed as sim object data members.

## Job Declarations

Jobs are the hands and feet of the simulation.  They are the building blocks for the
simulation.  Jobs are C or C++ routines with special Trick tags that determine scheduling,
object dependencies, etc.

Jobs only appear in the constructor of the sim object.

```
[C<#>] [{job_tag}] [P<#>] ([<cycle_time>, [<start_time>, [<stop_time>,]]] <job_class>) <module>([args]) ;
```

Most of these fields are optional depending on how the module is classified or utilized
within the sim. The following subsections detail the usage and purpose of each of these fields.

### Child Thread Specification

The first field of a module declaration is an optional child process specification in
the form of a capital C immediately followed by an integer child ID number; i.e. C1, C2, C3,
etc. The child process specification allows parallel processing for simulation modules.

Every simulation has a parent process. A child specification will result in the spawning of
a thread for each distinct child ID specified. More than one job can be specified for each child ID.
Jobs with child specifications will run in parallel with other jobs within each software frame,
so users may be required to specify job dependencies (see Section 4.4.10) to keep parallel
