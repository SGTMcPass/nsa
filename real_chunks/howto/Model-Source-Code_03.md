### Programming Language Support > Source Files > Trick Version Compatibility

 Library Dependencies Within Model Source Files:</b><br>
If you find it more intuitive to instead list library dependencies for each
model source file, it is possible to do so. In each model source file, list the
object files and libraries that the current model source file depends on.
Self-references are allowed, but not necessary. For a file `this.c` which calls
* a function within the file `that.c`
* a function in a user object `library my_library/libdog.a`
* a function in a shared library `libcow.so`
* a function `foo.c`

The `LIBRARY DEPENDENCY` field might look like this:<br>
```
LIBRARY DEPENDENCY:
    ((this.o)
     (that.o)
     (my_library/libdog.a)
     (libcow.so)
     (${FOO_ENV_VAR}/foo.o))
```

For references to objects outside the current source directory, the directory paths must be specified relative to the bin_${TRICK_HOST_CPU} directory. In this example, the that.c function might also have its own library dependency list, but the that.c dependencies do not need to appear in the this.c dependency list. The CP will automatically search and sort all the object code dependencies; the developer just has to make sure all dependencies are listed in the appropriate files.

There are two ways to specify dependencies to actual libraries, i.e. lib\*.a files:

`* <relative path>="">/<library name>.a`

If you use a relative path to the library, Trick will search the TRICK_CFLAGS for a directory that contains source code for the library. Once Trick locates the source code, it will automatically build the library and link it in the simulation.

`* <library name>.a`

If you do NOT specify a relative path, Trick will NOT build the library for you. It will simply search your -L paths in your `TRICK_USER_LINK_LIBS` for the library. If found, it will link the library into the simulation.

You may also have Trick link in a shared (`lib*.so`) library. You must supply the `*.so` extension. Trick will not automatically build a shared library, but it is smart enough to use it during link time.

The LIBRARY DEPENDENCY field also handles the `#ifdef`, `#else` and `#endif` statements such that different object files and libraries may be linked for different cases. The previous example might look like this:

```
LIBRARY DEPENDENCY:
    ((this.o)
     (that.o)
#ifdef __animals
     (my_library/libdog.a)
     (libcow.so)
#else
     (my_library/lib.a)
#endif
     (${FOO_ENV_VAR}/foo.o))
```

<b>Listing Library Dependencies Within the `S_define`:</b><br>
Listing library dependencies within the `S_define` is just like listing them
within
