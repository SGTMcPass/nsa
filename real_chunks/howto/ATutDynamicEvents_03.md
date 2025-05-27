### Dynamic Events - Making Contact > Updating Our Cannonball Simulation > Step 6 - Run the Simulation

rf.mode``` to
```Decreasing``` to explicitly indicate that the only events we care about are
positive to negative boundary crossings. Or, we could just let the mode default
to ```Any```, because the cannonball doesn't start below the ground.

* ```REGULA_FALSI.error_tol```

To specify the how small the error should be before declaring success, set
```REGULA_FALSI.error_tol```. The default error tolerance is 1.0e-15.

<a id=calling-regula-falsi></a>
### Calling regula_falsi()

Given the current integration time, from ```get_integ_time()```, and a pointer
to the ```REGULA_FALSI``` variable, ```regula_falsi()``` returns an estimate
of amount of integration time necessary to reach the event.

When the estimate (tgo in our example) is equal to 0.0, we've found the event.
At this point, the actions meant to result from the event should be performed.

In the action block, the first thing you'll want to do is the get the current
simulation time. This is the event time. Then you'll want to reset the
```REGULA_FALSI``` object to it's default state with ```reset_regula_falsi()```.
After do whatever needs to happen as a result of the event. In
our cannon ball simulation, we want the ball to stop moving when it hits the
ground. So, we set its state-derivatives to zero.

If we had wanted our ball to bounce instead of just stopping, we
could instead have changed the balls velocity vector to account for the rebound,
and energy loss.

Regardless of its value, the time estimate is returned by the dynamic event job,
to the Trick integration scheduler to let it know what its next integration step
size should be.

When the dynamic event job returns 0.0, the integration scheduler will return to
its normal behavior of integrating from the current state to the next integer
multiple of the integloop time step.

<a id=updating-our-cannonball-simulation></a>
## Updating Our Cannonball Simulation

### Step 1 - Modifications to ```cannon.h```

To the #include directives near the top of the file, add:

```
#include "trick/regula_falsi.h"
```

then add the following new member to the CANNON struct :

```REGULA_FALSI rf ; ```

### Step 2 - Modifications to ```cannon_numeric.h```

Add the following prototype for our new dynamic event job function, **cannon_impact**
below the existing **cannon_deriv** prototype.

```c++
double cannon_impact(CANNON*) ;
```

### Step 3 - Modifications to ```cannon_numeric.c```

Add the [cannon_impact](#listing_cannon_impact
