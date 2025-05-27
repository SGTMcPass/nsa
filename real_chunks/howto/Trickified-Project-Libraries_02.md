### A Real Life Trickified Project

ipped into `python`. The zip file name is configurable via the `TRICKIFY_PYTHON_DIR` variable, which can include directories, which will automatically be created if necessary.

Your Trickified library can be produced in three different formats based on the value of `TRICKIFY_BUILD_TYPE`:
1. `STATIC` (.a)
Create a static library. This will require the use of `--whole-archive` (on Linux) or `-all_load`/`-force_load` (on Mac) when linking the sim executable. Trick uses `dlsym` to dynamically load symbols at run time, but the linker, by default, will not include symbols from static libraries that are not known to be needed at compile time.
2. `SHARED` (.so)
Create a shared object (dynamically linked library). This may require the use of `-rpath` to ensure the linker can find the shared object at runtime unless you explicitly link against it (as opposed to using `-L` and `-l`) during compilation.
3. `PLO` (.o)
Create a partially-linked object (see the `--relocatable` option of `ld`). No special linker options are required. This is the default build type.

Note that Trick does not automatically append file extensions and will use the value of `TRICKIFY_OBJECT_NAME` regardless of the value of `TRICKIFY_BUILD_TYPE`.

## Simplify with a Makefile
Let's be honest. You're not going to remember that command line. And who wants to type all that stuff every time? Let's do it once in our own makefile and just call `make` on that. It seems sensible to put this in the `trickified` directory right next to `S_source.hh`.

<pre>${HOME}/myproject/
    include/
        Foo.hh
        Bar.hh
        Baz.hh
    trickified/
        <b>Makefile</b>
        S_source.hh
        trickified.o
        python
        build/
        .trick/</pre>

```make
ifndef TRICK_HOME
    $(error TRICK_HOME must be set)
endif

TRICKIFY := $(TRICK_HOME)/share/trick/makefiles/trickify.mk

ifeq ($(wildcard $(TRICKIFY)),)
    $(error This makefile requires at least Trick 17.1)
endif

export TRICKIFY_OBJECT_NAME := trickified_myproject.o
export TRICKIFY_CXX_FLAGS := -I$(HOME)/myproject/include

all:
        @$(MAKE) -s -f $(TRICKIFY)

clean:
        @rm -rf build python .trick $(TRICKIFY_OBJECT_NAME)
```

Now just type `make` in `trickified` and everything is taken care of. I even added a check to make sure you're using a recent enough version of Trick. I've silenced a
