### Adding ${TRICK_HOME}/bin to PATH > TRICK_CFLAGS and TRICK_CXXFLAGS > MAKEFLAGS

| [Home](/trick) → [Documentation Home](../Documentation-Home) → [Building a Simulation](Building-a-Simulation) → Environment Variables |
|------------------------------------------------------------------|

Trick uses a list of variables for building sims e.g. TRICK_CFLAGS and TRICK_CXXFLAGS.  Each variable has a default value that may be overridden by setting the value in the environment. Trick resolves these variables by a call to a function called "trick-gte". Type in "${TRICK_HOME}/bin/trick-gte" on the command line to see what the "Trick environment" is.

### Adding ${TRICK_HOME}/bin to PATH

${TRICK_HOME}/bin can be added to the PATH environment variable for convenience. It is not necessary for compiling or running sims but allows you to call Trick's functions without using the full path of Trick's executables.

```
# bash
PATH="${PATH}:/path/to/trick"

# [t]csh
setenv PATH "${PATH}:/path/to/trick"
```

### TRICK_CFLAGS and TRICK_CXXFLAGS

The contents of TRICK_CFLAGS is included on the command line with each C file compilation. Similarly, TRICK_CXXFLAGS is included for each C++ file. Each contain header file search directories, macro define variables, and compiler flags.

For building a simulation, a user must be proficient at tweaking TRICK_CFLAGS and TRICK_CXXFLAGS. There are a several ways to do this.

TRICK_CXXFLAGS works exactly like TRICK_CFLAGS.

Example 1: Add "-I/user/mooo/trick_models" to the environment variable. TRICK_CFLAGS is currently...

```
UNIX Prompt> echo $TRICK_CFLAGS
-Wall
```

Now we need to edit the shell startup file where TRICK_CFLAGS is defined.

Add the following line for bash.

```
TRICK_CFLAGS="$TRICK_CFLAGS -I/user/mooo/trick_models"
```

Add the following line for [t]csh.

```
setenv TRICK_CFLAGS "$TRICK_CFLAGS -I/user/mooo/trick_models"
```

Now source your shell startup file and voila!...

For bash:
```
UNIX Prompt> . ~/.bash_profile
UNIX Prompt> echo $TRICK_CFLAGS
-Wall -I/user/mooo/trick_models
```

For [t]csh:
```
UNIX Prompt> source ~/.cshrc
UNIX Prompt> echo $TRICK_CFLAGS
-Wall -I/user/mooo/trick_models
```

Example 2: Add "-I/user/mooo/trick_models" through the simulation S_overrides.mk file

We need to edit the S_overrides.mk file in the simulation to be built.

Add the following line.

```
TRICK_CFLAGS="$TRICK_CFLAGS -I/user/mooo/trick_models"
