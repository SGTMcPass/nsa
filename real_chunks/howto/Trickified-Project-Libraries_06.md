### A Real Life Trickified Project

 SWIG where to find *_py.i files
    TRICK_SWIG_FLAGS += -I$(MYPROJECT_HOME)/trickified

    # Link in the Trickified object
    TRICK_LDFLAGS += $(MYPROJECT_TRICK)

    # Append a prerequisite to the $(SWIG_SRC) target. This will build the
    # Trickified library along with the sim if it does not already exist. Using
    # $(SWIG_SRC) ensures that all Trickified .i files are created before SWIG is
    # run on any simulation .i files, which may %import them. Note that this does
    # NOT cause the Trickified library to be rebuilt if it already exists, even if
    # the Trickified source code has changed.
    $(SWIG_SRC): $(MYPROJECT_TRICK)

endif

$(MYPROJECT_TRICK):
        @$(MAKE) -s -C $(MYPROJECT_HOME)/trickified
```

Now to use your project, all the user has to do is add one line to his `S_overrides.mk`:

```make
include <myproject>/trickified/myproject.mk
```

They'll have to replace `<myproject>` with the location to which they installed your project, of course. They might choose to hardcode the path or use a variable, but that's up to them.

# You Still Need a Core Library
Trickification is great and all, but it only builds the `io_*` and `*_py` code into an object. And because your project's headers and source are now under `TRICK_EXT_LIB_DIRS`, Trick won't be determining dependencies or compiling source code. Trickification thus necessitates that you build all of your source code into a library. There are plenty of internet tutorials available on that topic, so I won't be suggesting anything here. But once you've got that taken care of, you should incorporate it into your user-facing makefile by adding it to `TRICK_LDFLAGS`. You can also create a rule to call its build system and add the library as a prerequisite to `$(S_MAIN)` to have it built along with the sim if necessary.

# A Real Life Trickified Project
Here's a real project we used as the guinea pig for Trickification. It provides a makefile that a user can include from his `S_overrides.mk` that causes both a core library and Trickified object to be built if they don't already exist whenever the sim is compiled. The makefile is located at `3rdParty/trick/makefiles/trickified.mk`. The Trickified stuff is at `3rdParty/trick/lib`.

https://github.com/nasa/IDF

[Continue to Running A Simulation](../running_a_simulation/Running-a-Simulation)
