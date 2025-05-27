### Building & Running a Trick-based Simulation > Running The Simulation > Sim Execution

" as the unit specification.

---

<a id=initializing-the-cannonball-simulation></a>
### Initializing the Cannonball Simulation

The Trickless simulation performed a two-part initialization of the
simulation variables. The first part assigned default values to the simulation
parameters. The second part performed calculations necessary to initialize the
remaining simulation variables.

Trick based simulations perform a three-part initialization of simulation
variables. The first part runs "**default-data**" jobs, that is, it calls one or
more user-provided C functions, whose purpose is to set default values for the
simulation's variables. In the second initialization step, Trick executes the
simulation's Python "**input file**". Variable assignments can be made in the input file.
If a parameter value isn't set in the input file, its default value is used. In the third and final
initialization step, Trick runs "**initialization**" jobs. These perform any
final initialization calculations, needed prior to running the sim.

The two functions in the listing below will serve as the default-data and
initialization jobs for our cannonball simulation. These are the functions for
which we created the prototypes in the cannon.h header file.

We'll create the python input file in a later section.

<a id=listing_3_cannon_init_c></a>
**Listing 3 - `cannon_init.c`**

```c
/******************************* TRICK HEADER ****************************
PURPOSE: (Set the initial data values)
*************************************************************************/

/* Model Include files */
#include <math.h>
#include "../include/cannon.h"

/* default data job */
int cannon_default_data( CANNON* C ) {

    C->acc[0] = 0.0;
    C->acc[1] = -9.81;
    C->init_angle = M_PI/6 ;
    C->init_speed  = 50.0 ;
    C->pos0[0] = 0.0 ;
    C->pos0[1] = 0.0 ;

    C->time = 0.0 ;

    C->impact = 0 ;
    C->impactTime = 0.0 ;

    return 0 ;
}

/* initialization job */
int cannon_init( CANNON* C) {

    C->vel0[0] = C->init_speed*cos(C->init_angle);
    C->vel0[1] = C->init_speed*sin(C->init_angle);

    C->vel[0] = C->vel0[0] ;
    C->vel[1] = C->vel0[1] ;

    C->impactTime = 0.0;
    C->impact = 0.0;

    return 0 ;
}
```

Some important things to note:

* These are just C functions. Trick will have them compiled, and linked into the simulation
executable.

*
