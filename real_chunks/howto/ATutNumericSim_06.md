### State Propagation with Numerical Integration > Numeric Versus Analytical

integration` jobs in the *dyn* SimObject. The integration rate is specified in parentheses.

`create_connections` is a special function-like construct whose code is copied into S_source.cpp and is executed directly after SimObject instantiations. Common uses are to 1) instantiate integrators, and 2) connect data structures between SimObjects.

`dyn_integloop.getIntegrator` configures our integration scheduler. Its first argument specifies the integration algorithm to be used. In the case `Runge_Kutta_4`. The second argument is the number of variables that are to be integrated. There are four variables for this simulation (pos[0], pos[1], vel[0], vel[1]).


The updated S_define is:

<a id=listing_s_define></a>
**Listing - `S_define`**

```c++
/****************************************************************
PURPOSE: (S_define file for SIM_cannon_numeric)
LIBRARY_DEPENDENCY: ((cannon/src/cannon_init.c)
                     (cannon/src/cannon_numeric.c)
                     (cannon/src/cannon_shutdown.c))
****************************************************************/
#include "sim_objects/default_trick_sys.sm"
##include "cannon/include/cannon_numeric.h"

class CannonSimObject : public Trick::SimObject {
    public:
    CANNON cannon ;
    CannonSimObject() {
        ("initialization") cannon_init( &cannon ) ;
        ("default_data") cannon_default_data( &cannon ) ;
        ("derivative") cannon_deriv( &cannon ) ;
        ("integration") trick_ret= cannon_integ( &cannon ) ;
        ("shutdown") cannon_shutdown( &cannon ) ;
    }
};

CannonSimObject dyn ;
IntegLoop dyn_integloop (0.01) dyn ;
void create_connections() {
    dyn_integloop.getIntegrator(Runge_Kutta_4, 4);
}
```

<a id=running-the-cannonball-with-trick-integration></a>
## Running The Cannonball With Trick Integration

There is nothing different about running with Trick integration. We just need to
build the simulation and run it.

```
% cd $HOME/trick_sims/SIM_cannon_numeric
% trick-CP
```

If the sim builds successfully, then run it.

```
% ./S_main*exe RUN_test/input.py &
```

Run the simulation to completion

<a id=numeric_vs_analytical></a>
## Numeric Versus Analytical

Let's compare the analytical "perfect" simulation with latest version using
Trick integration.

1. Start the trick data products: `% trick-dp &`.
There should be the two SIMs in the "Sims/Runs" pane of trick-dp:

    1. `SIM_cannon_analytic`, and
    2. `SIM_cannon_numeric`.

2. Double click `SIM_cannon_analytic->RUN_test`
This will move `SIM
