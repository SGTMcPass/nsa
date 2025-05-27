### State Propagation with Numerical Integration > Numeric Versus Analytical

 with a declaration
of the following form:

```c++
IntegLoop integLoopName ( integrationTimeStep ) listOfSimObjectNames ;
```

* Jobs within a simObject that are tagged "derivative" or "integration" will be
dispatched to the associated integration scheduler.

Then, in the input file, call the IntegLoop **getIntegrator()** method to specify
the integration algorithm of choice and the number of state variables to be
integrated.

```py
integLoopName.getIntegrator( algorithm, N );
```

* *algorithm* is a enumeration value that indicates the numerical integration
algorithm to be used, such as: `trick.Euler`, `trick.Runge_Kutta_2`,
`trick.Runge_Kutta_4`. A complete list is visible in Integrator.hh, in
`${TRICK_HOME}/include/trick/Integrator.hh`.

* N is the number of state variables to be integrated.

<a id=updating-the-cannonball-sim-to-use-numerical-integration></a>
## Updating the Cannonball Sim to use Numerical Integration

Rather than type everything again, we will first "tidy up" and then copy the
simulation.  When trick-CP builds a simulation, it creates a makefile, that
directs the build process. The generated makefile also contains a procedure
("target" in Make parlance) called "spotless" for removing all of the
intermediate files that were produced during the build but that are not longer
needed.

So, to tidy up, execute the following:

```bash
% cd $HOME/trick_sims/SIM_cannon_analytic
% make spotless
```

And then copy the sim directory.

```bash
% cd ..
% cp -r SIM_cannon_analytic SIM_cannon_numeric
```

### Create **cannon_numeric.h.**
In this new simulation, we're going to create two new functions, 1)
`cannon_deriv()` [our derivative job], and 2) `cannon_integ ()` [our integration job].
We'll put prototypes for each these functions into `cannon_numeric.h`. This new
header file which will replace `cannon_analytic.h`.

<a id=listing_cannon_numeric_h></a>
**Listing - `cannon_numeric.h `**

```c
/*************************************************************************
PURPOSE: ( Cannonball Numeric Model )
**************************************************************************/

#ifndef CANNON_NUMERIC_H
#define CANNON_NUMERIC_H

#include "cannon.h"

#ifdef __cplusplus
extern "C" {
#endif
int cannon_integ(CANNON*) ;
int cannon_deriv(CANNON*) ;
#ifdef __cplusplus
}
#endif
#endif
```
```bash
% cd SIM_cannon_numeric/models/cannon/include
% vi cannon_numeric.h <edit and save>
```

### Create **cannon_numeric.c.**

**Header and
