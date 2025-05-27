### Building & Running a Trick-based Simulation > Running The Simulation > Sim Execution

default_data")`
This assigns cannon\_default\_data() a job classification of *default_data*.


### Scheduled Job
The next job needs to be called at a regular frequency while the cannonball is
flying in the air. A *scheduled* class job is one of many jobs that can be
called at a given frequency. The only thing new about the declaration for
cannon\_analytic is the additional specification of 0.01.

`(0.01, "scheduled") cannon_analytic(&cannon) ;`


* `(0.01, "scheduled")`
The 0.01 specification tells Trick to run this job every 0.01 seconds (starting
at time=0.0). "scheduled" is the job classification.

### Create The S\_define

```
% cd $HOME/trick_sims/SIM_cannon_analytic
% vi S_define
```

Type in the contents of **Listing 7** and save.

<a id=compiling-and-building-the-simulation></a>
## Compiling, and Building the Simulation

The pieces are in order. The simulation is ready to be built!

### Setting `$TRICK_CFLAGS` and `$TRICK_CXXFLAGS`

![TRICK_CFLAGS WARNING](images/Warning_TRICK_CFLAGS.png)

Before we continue with the magical building of the cannonball, **PLEASE** take
the time to understand this section. It will save you much heartache and time.

The environment variables **`$TRICK_CFLAGS`** and **`$TRICK_CXXFLAGS`** are used
to provide TRICK, and the compilers that it uses with information that is
necessary to build your sim. Most importantly, they will tell TRICK where to
find your model files. They also provide a way for you to invoke some very useful
compiler options.

* `$TRICK_CFLAGS` is used by the C compiler and by the Trick Interface Code Generator.
* `$TRICK_CXXFLAGS` is for C++ compiler

#### Resolving Relative Paths

In the files that we have created so far, the file paths in `#include` directives
and in the `LIBRARY_DEPENDENCY` sections, are **relative** paths. These paths
are relative to a **base-path**, that we still need to specify.

For example, the `S_define` file listed above `#includes` the relative path:
`cannon/include/cannon_analytic.h`. We intend for this path to be relative to the
`models` directory that we created in our `SIM_cannon_analytic` directory. The complete
path to our cannon.h header file should be:

```
${HOME}/trick_sims/SIM_cannon_analytic/models/cannon/include/cannon_analytic.h
```

We need to specify either the absolute path to the `models` directory, or the
