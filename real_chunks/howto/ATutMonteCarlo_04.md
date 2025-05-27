### Monte Carlo > Optimization > Modifications to S_Define

 increment *= -1;
    }

    C->init_angle += increment;
    previous_distance = run_cannon.pos[0];
    return 0;
}
```

### Modifications to input.py

<a id=listing-input-3></a>
**Listing - input.py**

```python
exec(open("Modified_data/cannon.dr").read())

# Enable Monte Carlo.
trick.mc_set_enabled(1)

# Run 25 optimizations.
# The more runs, the more precise your variable will end up assuming you wrote your optimization logic correctly.
trick.mc_set_num_runs(25)

# Create a calculated variable and add it to Monte Carlo.
mcvar_launch_angle = trick.MonteVarCalculated("dyn.cannon.init_angle", "rad")
trick.mc_add_variable(mcvar_launch_angle)

# Stop Monte Carlo runs after 25 seconds of simulation time
trick.stop(25)

# Stop Monte Carlo runs if they take longer than 1 second of real time
trick.mc_set_timeout(1)
```

### Modifications to S_Define
The last thing that we need to do is modify our simulation definition file and add the two new Trick jobs. As you can see, we have added a new library dependency, a new ## inclusion, and two new constructor jobs.

<a id=listing-s-define></a>
**Listing - S_Define**

```C++

/************************TRICK HEADER*************************
PURPOSE:
    (S_define file for SIM_cannon_numeric)
LIBRARY DEPENDENCIES:
    (
      (cannon/src/cannon_init.c)
      (cannon/src/cannon_numeric.c)
      (cannon/src/cannon_shutdown.c)
      (cannon/src/optimization.c)
    )
*************************************************************/

#include "sim_objects/default_trick_sys.sm"
##include "cannon/include/cannon_numeric.h"
##include "cannon/include/optimization.h"

class CannonSimObject : public Trick::SimObject {

    public:
        CANNON cannon;

        CannonSimObject() {
            ("default_data") cannon_default_data( &cannon ) ;
            ("initialization") cannon_init( &cannon ) ;
            ("derivative") cannon_deriv( &cannon ) ;
            ("integration") trick_ret= cannon_integ( & cannon ) ;
            ("dynamic_event") cannon_impact( &cannon ) ;
            ("monte_slave_post") cannon_slave_post( &cannon ) ;
            ("monte_master_post") cannon_master_post( &cannon ) ;
            ("shutdown") cannon_shutdown( &cannon ) ;
        }
} ;

CannonSimObject dyn ;
IntegLoop dyn_integloop (0.01) dyn ;
void create_connections() {
    dyn_integloop.getIntegrator(Runge_Kutta_4, 4);
}
```

Run the script and plot the curves.

```
% trick-CP
...
% ./S_main*.exe RUN_test
