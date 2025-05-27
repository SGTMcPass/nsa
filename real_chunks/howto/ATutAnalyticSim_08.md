### Building & Running a Trick-based Simulation > Running The Simulation > Sim Execution

 object, and later, linked
with a number of libraries to create a simulation executable.

```bash
% cd $HOME/trick_sims/SIM_cannon_analytic/models/cannon/src
% vi cannon_analytic.c
```

Type in the contents of **Listing 5** and save.

<a id=cannonball_cleanup_and_shutdown></a>
### Cannonball Cleanup And Shutdown

**shutdown** job types are called by Trick's job scheduler when the simulation ends.
These types of jobs are for doing anything that one might want to do at the end of a simulation, like releasing resources, or doing some final result calculation, or maybe just printing a message.

In our case we're just going to print the final cannon ball state.

<a id=listing_6_cannon_shutdown_c></a>
**Listing 6 - `cannon_shutdown.c `**

```c
/************************************************************************
PURPOSE: (Print the final cannon ball state.)
*************************************************************************/
#include <stdio.h>
#include "../include/cannon.h"
#include "trick/exec_proto.h"

int cannon_shutdown( CANNON* C) {
    double t = exec_get_sim_time();
    printf( "========================================\n");
    printf( "      Cannon Ball State at Shutdown     \n");
    printf( "t = %g\n", t);
    printf( "pos = [%.9f, %.9f]\n", C->pos[0], C->pos[1]);
    printf( "vel = [%.9f, %.9f]\n", C->vel[0], C->vel[1]);
    printf( "========================================\n");
    return 0 ;
}
```

```bash
% cd $HOME/trick_sims/SIM_cannon_analytic/models/cannon/src
% vi cannon_shutdown.c
```

<a id=simulation-definition-file></a>
## The Simulation Definition File (S_define)

To automate the build process of a Trick based simulation, Trick needs to
know user source code locations, data types, functions, variables and scheduling
requirements of a simulations models. This starts with the simulation
definition file (**S_define**), an example of which, that we will use to define
our Cannonball simulation is shown in Listing 7, below.

<a id=listing_7_s_define></a>
**Listing 7 - `S_define`**

```c++
/************************TRICK HEADER*************************
PURPOSE:
    (S_define file for SIM_cannon_analytic)
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
        CANN
