### Interface Code Generator - ICG > Checksumming


units primitives allowed in the parameter comment fields of the data structure definition
files.

The ICG generates one source code file for each data structure definition file it
processes, with a file name in the form of io_src/io_<file_name>.c; where "io_" is a
standard prefix for all ICG generated files, and <file_name> is the original data
structure definition file name.

Any characters or statements the ICG recognizes as valid syntax, but does not process,
will be echoed to the screen with an informative message on why it did not process the
parameter.

In general, the following items are not processed by the ICG:
1. global parameters decalred outside of a struct, union, or enum typedef,
1. all parameter declarations of a type other than the basic C types listed in the
   Parameter Data Types section or the types contained within the data structure and
   enumerated type databases (structure and enumerated types previously processed by the ICG),
1. all parameters that have a "**" in the measurement units field of the parameter comment, and
1. all function declarations.

The ICG will always give the "ICG complete." message upon successful completion of processing.

## Building Model Source

Trick's main processor, CP handles building models from a high level.  However,
developers may desire to build a local cache of source and include files in a model
directory.  Or the developer may want to build a library from a model directory of
source and include files.  Trick's make_build and UNIX's make may be used for these
purposes.

### Makefile Generator - make_build

The make_build processor takes the src and include files in a model
