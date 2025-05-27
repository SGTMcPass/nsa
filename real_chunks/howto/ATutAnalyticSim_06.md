### Building & Running a Trick-based Simulation > Running The Simulation > Sim Execution

->vel[0] = C->vel0[0] ;
    C->vel[1] = C->vel0[1] ;

    C->impactTime = 0.0;
    C->impact = 0.0;

    return 0 ;
}
```

Some important things to note:

* These are just C functions. Trick will have them compiled, and linked into the simulation
executable.

* Both functions' arguments have a pointer to the CANNON data-type which was defined in `cannon.h`.

* Both functions return an **int**. Returning 0 indicates success. Non-zero indicates failure.
The return values can optionally be used (by setting trick\_ret in the S\_define) to terminate the simulation.

```bash
% cd $HOME/trick_sims/SIM_cannon_analytic/models/cannon/src
% vi cannon_init.c
```

Type in the contents of **Listing 3** and save.

<a id=updating-the-cannonball-state-over-time></a>
### Updating The Cannonball State Over Time

Trick's job scheduler provides a **"Scheduled"** job type for periodically calling functions when the sim is in RUN (cyclic) mode.

In the case of our cannonball simulation, where there is an analytical solution, we can
calculate the the cannonball state by evaluating a function at each time step.

<a id=listing_4_cannon_analytic_h></a>
**Listing 4 - `cannon_analytic.h`**

```c
/*************************************************************************
PURPOSE: ( Cannon Analytic Model )
**************************************************************************/
#ifndef CANNON_ANALYTIC_H
#define CANNON_ANALYTIC_H
#include "cannon.h"
#ifdef __cplusplus
extern "C" {
#endif
int cannon_analytic(CANNON*) ;
#ifdef __cplusplus
}
#endif
#endif
```

```bash
% cd $HOME/trick_sims/SIM_cannon_analytic/models/cannon/include
% vi cannon_analytic.h
```

Type in the contents of **Listing 4** and save.

<a id=listing_5_cannon_analytic_c></a>
**Listing 5 - `cannon_analytic.c`**

```c
/*****************************************************************************
PURPOSE:    ( Analytical Cannon )
*****************************************************************************/
#include <stdio.h>
#include <math.h>
#include "../include/cannon_analytic.h"

int cannon_analytic( CANNON* C ) {

    C->acc[0] =  0.00;
    C->acc[1] = -9.81 ;
    C->vel[0] = C->vel0[0] + C->acc[0] * C->time ;
    C->vel[1] = C->vel0[1] + C->acc[1] * C->time ;
    C->pos
