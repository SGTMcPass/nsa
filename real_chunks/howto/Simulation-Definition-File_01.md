### Trick Header Comment > Create Connections

 Comment

This optional section of the S_define file is a C style comment found anywhere in the S_define file.
CP will parse the Trick Header comment looking for library dependencies and default data.  Library
dependencies are model source code files that are added to the list of files to be compiled and
linked into the simulation.  These dependencies differ from the ones found in the actual model source
code in that they are the full relative path to the actual source code file, not the resulting object file.
CP also looks for old style default data files.  Each default data entry has 3 fields, the structure type, the
instance name, and the relative path to the default data file.  CP will read in the default data file
substituting each occurrence of the structure type in the file with the instance name.  All of the default
data files are concatenated to the S_default.dat file.

### S_define Library Dependencies
```
LIBRARY DEPENDENCY:
    ((relative_path/model_1.c)
     (relative_path/model_2.cpp))
```

Library dependencies list out model source code files required by the simulation.  There are several
locations to add library dependencies, one of which is in the S_define file.  The format of
dependencies in the S_define file is a relative path to the model source file.  The path is relative
to -I include paths found in TRICK_CFLAGS and TRICK_CXXFLAGS.

For example if the full path to our model is /this/is/a/full/path/to/model.c and in our TRICK_CFLAGS
we have -I/this/is/a/full as one of the included search paths, the library dependency must complete the
full path to the file, in this case path/to/model.c.  Library dependendencies in the S_define file
differ from ones found in model source code as they must be the full path to the source file not the
object file.

## Include files

There are two types of includes in the S_define file.

### Single pound "#" includes.

Include files with a single pound "#" are parsed as they are part of the S_define file.  They are
treated just as #include files in C or C++ files.  These files usually include other sim objects or
instantiations as part of the S_define file.

### Double pound "#" includes.

Include files with a double pound "##" are not parsed as part of the S_define file.  These files are the
model header files.  They include the model class and structure definitions as well as C prototypes for
functions used in the S_define file.  Double pound files are copied, minus one pound, to S_source.hh.

## User Header Code Block

This section of the S_define (encapsulated by "%header{...%}") can be used for including header files
directly into the S_source.hh. Header files listed here will not be input
