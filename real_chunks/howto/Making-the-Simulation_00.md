### Simulation Compilation Environment Variables > Cleaning Up

| [Home](/trick) → [Documentation Home](../Documentation-Home) → [Building a Simulation](Building-a-Simulation) → Making the Simulation |
|------------------------------------------------------------------|


## Simulation Compilation Environment Variables

The -Ipaths in TRICK_CFLAGS and TRICK_CXXFLAGS tell Trick where to find model source files.  The flags also can contain compiler settings, for instance the -g flag is used for compiling in debug mode. See section Trick_Environment for more detail and information on variables for linking in external libraries, setting the compiler etc.

## Making the Simulation for the First Time.

Makefiles contain all of the rules for building the simulation. When a simulation is ready to be built for the very first time, the configuration processor script (CP) is executed in the simulation directory.

```
UNIX prompt> trick-CP
```

CP creates a small makefile and calls "make" to start the simulation build process. The small makefile is the same from simulation to simulation. It can even be copied from another simulation directory, skipping the CP step entirely. Once the small makefile is created, CP does not need to be run again, compilation can be accomplished by running "make".

When make is invoked, it calls CP to process the user-created S_define file. CP finds all source code related to the simulation, builds the code using a C/C++ compiler, and puts it all together to make one executable. CP also builds code generated from user source.  This is done for model documentation, Python input, unit specifications, variable descriptions etc.

After the initial CP is run, when there are changes made to model source code or the S_define file, they are recompiled using make.

```
UNIX prompt> make
```

## How Trick Finds Simulation Source Code

Trick compiles all user model source code referenced in the S_define either through file inclusion or user supplied "library dependencies".  Trick begins at the S_define and recursively follows code dependencies to create the entire source tree.

Header files are double pound "##" included in the S_define.  Each header file is recursively parsed to determine all lower level header files on which the top level header is dependent on. Doing this for all double pound files yields the full list of header files.

Model source files are found through LIBRARY DEPENDENCIES specified in the Trick header comment at the top of the S_define and model source files.  A recursive search is made beginning at the S_define, following all model source and header files. For details, see S_define_Library_Dependencies and Library_Dependencies.

Once the entire source tree is created, rules to compile all of these files are written to the makefile.

## Changing Simulation Compilation through Makefile Overrides

Sometimes a programmer may want Trick to pick up specific compiler flags or some special makefile rule for building a model or building the simulation. Trick allows the programmer to override the default Makefile rules with
