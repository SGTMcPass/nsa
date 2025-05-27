### Building & Running a Trick-based Simulation > Running The Simulation > Sim Execution

annon_analytic)
LIBRARY DEPENDENCIES:
    (
      (cannon/src/cannon_init.c)
      (cannon/src/cannon_analytic.c)
      (cannon/src/cannon_shutdown.c)
    )
*************************************************************/

#include "sim_objects/default_trick_sys.sm"
##include "cannon/include/cannon_analytic.h"

class CannonSimObject : public Trick::SimObject {

    public:
        CANNON cannon;

        CannonSimObject() {
            ("default_data") cannon_default_data( &cannon ) ;
            ("initialization") cannon_init( &cannon ) ;
            (0.01, "scheduled") cannon_analytic( &cannon ) ;
            ("shutdown") cannon_shutdown( &cannon ) ;
        }
} ;

CannonSimObject dyn ;
```

The `S_define` file syntax is C++ with a couple of Trick specific constructs.
Let us dissect this S_define file to see what makes it tick.

### Trick Header

* `PURPOSE:` keyword tells Trick to scan the remainder of the file for data
types, variable definitions, job scheduling specifications and compilation unit
dependencies.

* `LIBRARY_DEPENDENCY: ((cannon/src/cannon_analytic.c) ...` Lists the

*compilation units* (the .c source files), upon which this S_define depends. The
specified source files are the starting point for the recursive determination of
the list of files that need to be compiled and linked to build the simulation.
Trick headers that are included within each of these files may specify additional
source code dependencies, and so forth. Libraries may also be specified for
linking into the final executable.

Trick uses your `$TRICK_CFLAGS` environment variable ([see section 3.2 of the Trick User Guide](/trick/documentation/building_a_simulation/Environment-Variables)) in
conjunction with `cannon/src` to find the listed files. The entire path
name following the `$TRICK_CFLAGS` path must be included.

### Included Files

* `#include "sim_objects/default_trick_sys.sm"` This line is mandatory in an
S_define. It includes predefined data types, variable definitions, and jobs the
that provide standard Trick Simulation functionality.

* `##include "cannon/include/cannon_analytic.h"` The S_define must `##include`
type definitions for all of the classes and structures that it uses. It also
needs to include prototypes for all of the functions that it calls. You may also
put the prototypes in the `S_define` block using ([user code blocks](/trick/documentation/building_a_simulation/Simulation-Definition-File#user-code-block)), but if you need to call any of the C functions from the input file then you must include the
prototypes in a header file (the preferred method).

### Data Lines

`Class CannonSimObject : public
