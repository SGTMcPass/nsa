### Simulation Compilation Environment Variables > Cleaning Up

 header files. For details, see S_define_Library_Dependencies and Library_Dependencies.

Once the entire source tree is created, rules to compile all of these files are written to the makefile.

## Changing Simulation Compilation through Makefile Overrides

Sometimes a programmer may want Trick to pick up specific compiler flags or some special makefile rule for building a model or building the simulation. Trick allows the programmer to override the default Makefile rules with a facility we are calling "makefile overrides".

For overrides in model directories, a user can create a file called `makefile_overrides`. This file allows the user to augment or override rules in the main simulation `makefile`. `makefile_overrides` applies to all files in the directory in which it is located. Additionally, special treatment is afforded to directories specifically named `src`. In such directories, if no `makefile_overrides` exists, the parent directory is searched as well, and any `makefile_overrides` found there applies to the files in `src` in addition to the parent directory. Again, searching of the parent directory only occurs for directories named `src`, and the search does not extend beyond the immediate parent directory. This special treatment of `src` is a relic of the past, and you should prefer putting `makefile_overrides` in the same directory as the source files themselves.

Additional make-like syntax is available in `makefile_overrides` to apply changes to subsets of files. `objects:` will be replaced with all object files to be created from all source files in the directory. For instance,

```make
objects: TRICK_CXXFLAGS += -Wall
```

will cause all source files in the directory to be compiled with the additional flags. You can select a subset of files by extension by prepending `objects:` with the extension to affect:

```make
cpp_objects: TRICK_CXXFLAGS += -Wextra
```
will cause only files ending in `.cpp` to receive the additional flags.

Other possibilities are: ```c_objects``` , ```f_objects``` , ```l_objects``` , ```y_objects``` , ```C_objects``` , ```cc_objects``` , ```cxx_objects``` , and
```CPLUSPLUS_objects``` .

For overrides in sim directories, there is a sim specific overrides file called `S_overrides.mk`. If this file is present in the sim directory, it is included after the directory-specific overrides. The rules in this file are the last word in how things are going to compile.

### Example Of How To Add a Pre-compiled Library to the Simulation

Go to simulation dir.

```
UNIX Prompt> cd /user/me/trick_sims/SIM_ball_L1
```

Edit a file called "S_overrides.mk". Append to the TRICK_USER_LINK_LIBS variable.

```
TRICK_USER_LINK_LIBS = -L/path/to/library -lmy_lib
```
### Example Of How
