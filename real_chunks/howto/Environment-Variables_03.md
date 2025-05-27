### Adding ${TRICK_HOME}/bin to PATH > TRICK_CFLAGS and TRICK_CXXFLAGS > MAKEFLAGS

 variable that `make` sees when it starts up is transformed into a `make` variable with the same name and value. However, an explicit assignment in a makefile, or with a command argument, overrides the environment.

**[Exporting Variables](https://www.gnu.org/software/make/manual/html_node/Variables_002fRecursion.html)**
`make` exports a variable if any of the following are true:

1. it is defined in the environment initially
1. it is set on the command line
1. it is preceded by the `export` keyword in a makefile

In all cases, the name must consist only of letters, numbers, and underscores.

```make
export VAR1 = potato
export VAR2 = flapjack
VAR3 = banana

TRICK_GTE_EXT += VAR1 VAR3 VAR4

```

At run time:
* `VAR1` will default to `potato`.
* `VAR2` will be undefined by default, as it was not added to `TRICK_GTE_EXT`.
* `VAR3` will be undefined by default if it was not present in the environment at compile time, as it was not explicitly `export`ed in the makefile. If it *was* present in the environment at compile time, it will default to `banana`, as such variables are automatically exported, and explicit assignments override environment values in `make`.
* `VAR4` will default to its compile-time environment value, if any.
* For each variable, the default value will only be used if that variable is not present in the environment at run time.

### MAKEFLAGS

MAKEFLAGS is not a Trick environment variable. It is used with the GNU make utility. Invoking make with the -j flag allows make to compile more than one file simultaneously. Dramatic speedups in compiling can be achieved when using multiple processors.

```
UNIX Prompt> setenv MAKEFLAGS –j10
```

[Continue to Simulation Definition File](Simulation-Definition-File)
