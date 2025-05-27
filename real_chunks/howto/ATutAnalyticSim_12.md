### Building & Running a Trick-based Simulation > Running The Simulation > Sim Execution

`. We intend for this path to be relative to the
`models` directory that we created in our `SIM_cannon_analytic` directory. The complete
path to our cannon.h header file should be:

```
${HOME}/trick_sims/SIM_cannon_analytic/models/cannon/include/cannon_analytic.h
```

We need to specify either the absolute path to the `models` directory, or the
relative location of the `models` directory with respect to the top-level
simulation directory (the location of S_define) as the base-path.
We can specify the base-path(s) to the compilers, and to Trick, by adding
-I*dir* options, that contain the base-paths, to `$TRICK_CFLAGS` and
`$TRICK_CXXFLAGS`.

The easiest, and most portable way of setting `TRICK_CFLAGS` for your simulation
is to create a file named **`S_overrides.mk`** in your simulation directory, and
then add the following lines to it:

<a id=listing_8_s_overrides.mk></a>
**Listing 8 - `S_overrides.mk`**

```sh
TRICK_CFLAGS += -Imodels
TRICK_CXXFLAGS += -Imodels
```

When Trick encounters relative paths in an S_define, it prepends these base-path(s)
to the relative paths to create a complete path to the file, thus allowing it to be
located.

#### Additional Compiler Flag Recommendations

Some additional compiler flags recommendations are provided in the `.cshrc` and
`.profile` snippets below. They tell the compilers to provide debugging support
and to check for and warn of possibly dubious code constructs.

##### For Your .profile File
```bash
export TRICK_CFLAGS="-g -Wall -Wmissing-prototypes -Wextra -Wshadow"
export TRICK_CXXFLAGS="-g -Wall -Wextra -Wshadow"

```

##### For Your .cshrc File
```bash
TRICK_CFLAGS= -g -Wall -Wmissing-prototypes -Wextra -Wshadow
TRICK_CXXFLAGS= -g -Wall -Wextra -Wshadow
```

### trick-CP
The source code and environment are set up. The Trick simulation build tool is
called **trick-CP** (Trick Configuration Processor). It is responsible for
parsing through the S_define, finding structures, functions, and ultimately
creating a simulation executable.

```
% cd $HOME/trick_sims/SIM_cannon_analytic
% trick-CP
```

If you typed everything perfectly... Trick is installed properly... there are no
bugs in the tutorial... the stars are aligned... and Trick is in a good mood...
You should, ultimately see :

```
Trick Build Process Complete
```

Now, take a look at the
