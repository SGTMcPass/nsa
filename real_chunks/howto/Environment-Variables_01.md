### Adding ${TRICK_HOME}/bin to PATH > TRICK_CFLAGS and TRICK_CXXFLAGS > MAKEFLAGS

rc
UNIX Prompt> echo $TRICK_CFLAGS
-Wall -I/user/mooo/trick_models
```

Example 2: Add "-I/user/mooo/trick_models" through the simulation S_overrides.mk file

We need to edit the S_overrides.mk file in the simulation to be built.

Add the following line.

```
TRICK_CFLAGS="$TRICK_CFLAGS -I/user/mooo/trick_models"
```

This will not show up in the current shell environment, but will be set for each command that the makefile executes.

### TRICK_CONVERT_SWIG_FLAGS

TRICK_CONVERT_SWIG_FLAGS contains flags sent to the convert_swig utility. Currently the flags only support "-s" which allows convert_swig to process STLs.

### TRICK_SWIG_FLAGS and TRICK_SWIG_CFLAGS

TRICK_SWIG_FLAGS are the options that are passed to SWIG (see the SWIG documentation). TRICK_SWIG_CFLAGS are the the options passed to the c/c++ compiler when compiling SWIG objects.

### TRICK_EXCLUDE

A colon separated list of directories to skip when processing files.

It is possible to instruct all CP functions to skip entire directories using the environment variable TRICK_EXCLUDE. Set this variable to a colon separated list of directories which you wish CP to bypass. All header files found in TRICK_EXCLUDE will not be processed. All source code files found in TRICK_EXCLUDE will not be compiled or linked into the simulation.

This environment variable does the job of both TRICK_ICG_EXCLUDE and TRICK_SWIG_EXCLUDE simulataneously.

This feature is useful to bring in packages as a library.

### TRICK_ICG_EXCLUDE

A colon separated list of directories to skip when processing header files.

It is possible to instruct ICG to skip entire directories using the environment variable TRICK_ICG_EXCLUDE. Set this variable to a colon separated list of directories which you wish ICG to bypass. This is useful when there is code which you do not wish Trick to have any knowledge of (i.e. you don’t need any of the parameters recorded or input processable).

This excludes files from ICG only, while still allowing SWIG to process them.

### TRICK_SWIG_EXCLUDE

A colon separated list of files and directories to skip when generating Python interface files.

It is possible to instruct SWIG to skip entire directories and files using the environment variable TRICK_SWIG_EXCLUDE. Set this variable to a colon separated list of files that should be bypassed.

This excludes files from SWIG only, still allowing ICG to process them.

Example ```S_overrides.mk```:
```
TRICK_SWIG_EXCLUDE += :models/SwigExclude.hh
TRICK_SWIG_EXCLUDE += :models/Swig_Exclude_Dir
```

### TRICK_FORCE_32BIT

To force Trick to compile in 32-bit on
