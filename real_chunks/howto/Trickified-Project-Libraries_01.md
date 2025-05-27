### A Real Life Trickified Project

file. I don't recommend setting it in your shell via `export` or `setenv`. All of Trick's environment variables can be specified at compile time, exposed at run time, and limited to the duration of the executable. There's no reason to permanently pollute your environment from your `.cshrc`, `.bashrc`, etc.

For example, say we have a tiny project that looks like this:

<pre><b>${HOME}/myproject/
    include/
        Foo.hh
        Bar.hh
        Baz.hh</b></pre>

To Trickify this project, we'll make a file called `S_source.hh` which includes all three headers:

```c++
#include "Foo.hh"
#include "Bar.hh"
#include "Baz.hh"
```

I recommend putting your `S_source.hh` in its own directory since Trick is going to generate a bunch of files, for some of which you can't yet specify the output directory. Let's call it `trickified`:

<pre>${HOME}/myproject/
    include/
        Foo.hh
        Bar.hh
        Baz.hh
    <b>trickified/
        S_source.hh</b></pre>

In the `trickified` directory, run:

```bash
make -f ${TRICK_HOME}/share/trick/makefiles/trickify.mk TRICKIFY_CXX_FLAGS=-I${HOME}/myproject/include
```

The result should be:

<pre>${HOME}/myproject/
    include/
        Foo.hh
        Bar.hh
        Baz.hh
    trickified/
        S_source.hh
        <b>trickified.o
        python
        build/
        .trick/</b></pre>

`trickified.o` contains all of the compiled `io_*.cpp` and `*_py.cpp` code. The name is configurable via the `TRICKIFY_OBJECT_NAME` variable, which can include directories, which will automatically be created if necessary. `build` contains a lot of ICG and SWIG artifacts. You can't change its name or location at this time, but it's useful to keep around as it will allow you to rebuild only the parts of the project that change in the future, and sims that build against your project will need the `*_py.i` files within. `.trick` includes a bunch of crazily-named Python modules which serve as the input file interface to the content of the header files. Those modules are compiled and zipped into `python`. The zip file name is configurable via the `TRICKIFY_PYTHON_DIR` variable, which can include directories, which will automatically be created if necessary.

Your Trickified library can be produced in three different formats based on the value of `TRICKIFY_BUILD_TYPE`:
1. `STATIC` (.a)
Create a static library. This will require the use of `--whole-archive` (on Linux) or
