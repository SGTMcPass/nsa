### Simulation Compilation Environment Variables > Cleaning Up

 to compile.

### Example Of How To Add a Pre-compiled Library to the Simulation

Go to simulation dir.

```
UNIX Prompt> cd /user/me/trick_sims/SIM_ball_L1
```

Edit a file called "S_overrides.mk". Append to the TRICK_USER_LINK_LIBS variable.

```
TRICK_USER_LINK_LIBS = -L/path/to/library -lmy_lib
```
### Example Of How To Exclude a Directory from ICG during CP

Go to simulation dir.

```
UNIX Prompt> cd /user/me/trick_sims/SIM_ball_L1
```

Edit a file called "S_overrides.mk". Append to the TRICK_ICG_EXCLUDE variable.

TRICK_ICG_EXCLUDE += /path/to/exclude:/another/path/to/exclude

### Example Of How To Exclude a Directory from most CP processing

Edit a file called "S_overrides.mk". Append to the TRICK_EXCLUDE variable.

```
TRICK_EXCLUDE += /path/to/exclude:/another/path/to/exclude
```

### Example how to set a C++ standard for ICG parsing

Edit a file called "S_overrides.mk". Append to the TRICK_ICGFLAGS variable.

```
TRICK_ICGFLAGS += -icg-std=c++11
```

Valid options are c++11, c++14, c++17, or c++20. ICG will parse to c++17 by default, or the newest supported version if c++17 is not availible.

## Cleaning Up

There are several levels of clean.

```
UNIX Prompt> make clean
```

Clean tries to remove only object files directly related to the current simulation. It will remove all of the generated files in the simulation directory. Clean also selectively removes model object files used to link this simulation.

```
UNIX Prompt> make spotless
```

Spotless is less discriminate in the files it removes. In addition to all of the files that clean removes, spotless will remove complete model object directories where any file included in the simulation was found.

```
UNIX Prompt> make apocalypse
```

Apocalypse is a special case rule when simulation libraries are used to build a simulation. See section Simulation_Libraries for more information about. In addition to all of files that spotless removes, apocalypse will run the spotless rule on any simulation directory the current simulation includes.

[Continue to Trickified Project Libraries](Trickified-Project-Libraries)
