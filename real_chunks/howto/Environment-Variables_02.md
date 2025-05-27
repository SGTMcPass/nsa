### Adding ${TRICK_HOME}/bin to PATH > TRICK_CFLAGS and TRICK_CXXFLAGS > MAKEFLAGS

 to a colon separated list of files that should be bypassed.

This excludes files from SWIG only, still allowing ICG to process them.

Example ```S_overrides.mk```:
```
TRICK_SWIG_EXCLUDE += :models/SwigExclude.hh
TRICK_SWIG_EXCLUDE += :models/Swig_Exclude_Dir
```

### TRICK_FORCE_32BIT

To force Trick to compile in 32-bit on 64-bit systems, set the TRICK_FORCE_32BIT environment variable to 1. Setting this variable appends "-m32" automatically to TRICK_CFLAGS and TRICK_CXXFLAGS.
4.2.6 TRICK_HOST_CPU

Trick determines a system specific suffix to append to object code directory names. By default this is determined automatically by Trick. The user may override this by setting the TRICK_HOST_CPU environment variable.

### TRICK_LDFLAGS

TRICK_LDFLAGS include linker flags. TRICK_LDFLAGS is used when linking the simulation executable. It is rare to set this variable.

### TRICK_SFLAGS

TRICK_SFLAGS includes header file search directories and macro define variables. TRICK_SFLAGS is used when parsing the S_define file.

### TRICK_USER_LINK_LIBS

Additional library and library directories to include when linking a simulation.

An example of adding a library search path, a library to be searched for, and a full path library.

bash
```
export TRICK_USER_LINK_LIBS="-L/full/path/to/libs -lfile1 /another/path/to/a/libfile2.a"
```

[t]csh
```
setenv TRICK_USER_LINK_LIBS "-L/full/path/to/libs -lfile1 /another/path/to/a/libfile2.a"
```
### TRICK_GTE_EXT

`TRICK_GTE_EXT` allows you to compile exported `make` variables into your sim executable so that default values are available for them at run time. These "baked in" variables will use the default compile-time values only if they are not already defined at run time. You do this by adding them to `TRICK_GTE_EXT`, which is a space-delimited list of names.

**[Defining Variables](https://www.gnu.org/software/make/manual/html_node/Environment.html)**
You can define a variable directly in a makefile by making an assignment to it. However, variables can also come from the environment in which `make` is run. Every environment variable that `make` sees when it starts up is transformed into a `make` variable with the same name and value. However, an explicit assignment in a makefile, or with a command argument, overrides the environment.

**[Exporting Variables](https://www.gnu.org/software/make/manual/html_node/Variables_002fRecursion.html)**
`make` exports a variable if any of the following are true:

1. it is
