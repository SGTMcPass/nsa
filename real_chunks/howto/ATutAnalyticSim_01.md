### Building & Running a Trick-based Simulation > Running The Simulation > Sim Execution

```bash
%  cd $HOME
%  mkdir -p trick_sims/SIM_cannon_analytic
%  mkdir -p trick_sims/SIM_cannon_analytic/models/cannon/src
%  mkdir -p trick_sims/SIM_cannon_analytic/models/cannon/include
```

---

<a id=representing-the-cannonball></a>
### Representing the Cannonball

To represent the cannonball model, we need to create a header file (**cannon.h**)
that will contain:

* A CANNON structure to hold the state of the cannonball, and
* Prototypes for cannonball functions

The CANNON data-type contains the cannonball's initial conditions,
its acceleration, velocity, and position, the model time, whether the cannonball
has impacted the ground, and the time of impact.

The prototypes will declare two functions for initializing our CANNON data-type.
We'll discuss these in the next section.

<a id=listing_2_cannon_h></a>
**Listing 2 - `cannon.h`**

```c
/*************************************************************************
PURPOSE: (Represent the state and initial conditions of a cannonball)
**************************************************************************/
#ifndef CANNON_H
#define CANNON_H

typedef struct {

    double vel0[2] ;    /* *i m Init velocity of cannonball */
    double pos0[2] ;    /* *i m Init position of cannonball */
    double init_speed ; /* *i m/s Init barrel speed */
    double init_angle ; /* *i rad Angle of cannon */

    double acc[2] ;     /* m/s2 xy-acceleration  */
    double vel[2] ;     /* m/s xy-velocity */
    double pos[2] ;     /* m xy-position */

    double time;        /* s Model time */

    int impact ;        /* -- Has impact occured? */
    double impactTime;  /* s Time of Impact */

} CANNON ;

#ifdef __cplusplus
extern "C" {
#endif
    int cannon_default_data(CANNON*) ;
    int cannon_init(CANNON*) ;
    int cannon_shutdown(CANNON*) ;
#ifdef __cplusplus
}
#endif

#endif
```

#### Creating The `cannon.h` Header File

Using your favorite text editor, create and save the file `cannon.h` from
**Listing 2**. We will assume from this point that your favorite text editor
is **vi**. So when you see **vi** following the %, just replace it
with **emacs**, **nedit**, **jot**, **wordpad**, **kate**, **bbedit**, or
whatever you like.

```bash
% cd $HOME/trick_sims/SIM_cannon_analytic/models/cannon/include
% vi cannon.h
```

Type, or cut and paste the contents of
