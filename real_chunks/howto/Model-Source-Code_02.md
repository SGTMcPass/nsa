### Programming Language Support > Source Files > Trick Version Compatibility

 parsers will realize that it is a C++ file and handle it appropriately. If the extension is *.h, Trick will assume it is a C file (not C++). If you want to make a C++ header file name with the *.h extension, you must explicitly tell Trick it is a C++ file with the `LANGUAGE: (C++)` declaration in the Trick comment header.

#### Telling ICG to ignore this header file, `ICG: (No)`

If `ICG: (No)` is in the comment header, Trick will not to process the header. This is useful if the header contains anything that Trick cannot process, or if the programmer wishes Trick to skip this header. For skipping entire sets of headers, see next item.

If `ICG: (Nocomment)` is in the comment header, Trick will not process any comments within the file. This option is useful if the user wants ICG to process the file but the file does not have comments that are Trick compliant.

#### Library Dependencies
Library dependencies are the model source code files required by the simulation.
They can be listed 1) within model header files, 2) within model source files,
or 3) within the `S_define`. Each library dependency only needs to be listed once,
and the preferred approach is to list each library dependency within its
respective model header file.

<b>Listing Library Dependencies Within Model Header Files:</b> (preferred approach)<br>
Listing library dependencies within the model header files is as simple as
providing the path of each source file for which the header file makes
declarations. The path should be relative to the base path that was set in
S_overrides.mk (See the link below).

[Compiling and Building the Simulation](https://nasa.github.io/trick/tutorial/ATutAnalyticSim#compiling-and-building-the-simulation)

By doing it this way, you don't have to recall every single source file in your
simulation when you're listing the library dependencies. You only need to list
the source files relevant to the current header file, and Trick does the heavy
lifting by bringing them all together when it processes the header files.

A model header consistent with this approach would contain a
`LIBRARY DEPENDENCY` field that looked like the following:<br>
```
LIBRARY DEPENDENCY:
    ((relative_path/source_file.c)
     (relative_path/other_source_file.cpp))
```

<b>Listing Library Dependencies Within Model Source Files:</b><br>
If you find it more intuitive to instead list library dependencies for each
model source file, it is possible to do so. In each model source file, list the
object files and libraries that the current model source file depends on.
Self-references are allowed, but not necessary. For a file `this.c` which calls
* a function within the file `that.c`
* a
