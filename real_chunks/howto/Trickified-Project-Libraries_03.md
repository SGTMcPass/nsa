### A Real Life Trickified Project

XX_FLAGS := -I$(HOME)/myproject/include

all:
        @$(MAKE) -s -f $(TRICKIFY)

clean:
        @rm -rf build python .trick $(TRICKIFY_OBJECT_NAME)
```

Now just type `make` in `trickified` and everything is taken care of. I even added a check to make sure you're using a recent enough version of Trick. I've silenced a lot of make's output because I prefer to see echoed commands only when debugging, but you're welcome to get rid of the `@` and `-s` if you enjoy such verbosity. Note that I've used `TRICKIFY_OBJECT_NAME` to rename the default `trickified.o` to something a little less generic. If you're following along, you can remove the `trickified.o` we built earlier.

## Don't Version Control Build Artifacts!
The only Trickification-related files you want under version control are `S_source.hh` and `Makefile`. You should ignore all of the generated files. For instance, the appropriate `.gitignore` for the `trickified` directory when using default values for the Trickification variables is:

```git
build/
.trick/
python
*.o
```

The generated Python modules can be particularly problematic if they are accidentally version controlled. The names are created by hashing the full file path, both during Trickification and again when the sim is built. If the paths change between Trickification and sim compilation, the names won't match, and you'll get confusing linker errors.

# Using a Trickified Project
Using a project that's been Trickified is a lot like using an external library, but there are a couple of extra things to take care of. Continuing with the example above, we would need to add the following to our sim's `S_overrides.mk`:

``` make
TRICK_LDFLAGS += $(HOME)/myproject/trickified/trickified_myproject.o
```

This line links in the Trickified object. Note that you may need additional flags if you used `TRICKIFY_BUILD_TYPE` to build a static library or shared object.

```make
TRICK_EXT_LIB_DIRS += :$(HOME)/myproject
```

This line tells Trick to expect `io_*` and `*_py` code for the headers in the specified directory (and all directories below it), but not to generate it itself. This is different than `TRICK_ICG_EXCLUDE` and `TRICK_EXCLUDE`, which cause ICG to ignore the headers entirely. It also tells Trick not to compile any source files in the specified directory (and all directories below it) that may be referenced as `LIBRARY_DEPENDENCIES` in user files. Note that it is a colon-delimited list of paths.

You'll need to be more selective if the sim itself or additional non-Trickified headers or source are under
