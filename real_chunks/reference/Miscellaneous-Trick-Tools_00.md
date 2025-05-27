### Interface Code Generator - ICG > Checksumming

| [Home](/trick) → [Documentation Home](../Documentation-Home) → Miscellaneous Trick Tools |
|------------------------------------------------------------------|

## Interface Code Generator - ICG

ICG is the processor that %Trick uses to parse header files.  It is normally called
internally from the main %Trick processor, CP.  However, it may be used manually by
developers.

The ICG parses developer created data structure definition files and generates
runtime executive input/output source code.  The source code generated is compiled
into a simulation which uses the types parsed.

The command syntax for the ICG is as follows (with restrictions outlined afterward):

```
UNIX prompt> ICG [-d] [-D <define>] [-U <undefine>] <filename>.h
UNIX prompt> ICG -u
```

The ICG can process multiple files at a
time and does accept UNIX wild card character designations (*.h) in the filename. The
optional "-d" (for debug) argument tells the ICG to echo every character successfully
parsed from the file; if a syntax error occurs in the file, the user will know the exact
character which caused the problem.  The optional "-D" and "-U" arguments are compiler
directives, used in concert with #defines, #undefs etc. and work like their CFLAGS
counterparts.  The optional "-u" argument tells ICG to display the current measurement
units primitives allowed in the parameter comment fields of the data structure definition
files.

The ICG generates one source code file for each data structure definition file it
processes, with a file name in the form of io_src/io_<file_name>.c
