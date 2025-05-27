### Dynamic Events - Making Contact > Updating Our Cannonball Simulation > Step 6 - Run the Simulation

'll discuss the details of how this and other
dynamic event jobs work.

<a id=specifying-an-event-boundary></a>
### Specifying an Event Boundary

* ```REGULA_FALSI.error```

An event boundary is defined by a user-supplied error-function of the simulation
state. After each integration step, the dynamic event job evaluates the error
function at the current state and then assigns the error-value to
```REGULA_FALSI.error```. The ```REGULA_FALSI``` object is then passed into
```regula_falsi()``` as an argument.

The magnitude of the error should indicate how close the given state is to
the event state, and the sign of the error should indicate which side of the
boundary the given state is on. An error-value of 0 should indicate that the
given state is the same as the event state.

In our ```cannon_impact``` function above, the assignment
```C->rf.error = C->pos[1] ;``` defines our cannonball's event boundary, that
is, the surface of the ground. When ```C->pos[1]``` is positive, the ball is
above the surface. When negative, it's below the surface. When zero, it's at
the surface.

* ```REGULA_FALSI.mode```

Notice that a sign change of the error-value, between consecutive states
indicates that the state has crossed the event boundary. In our cannonball
simulation, we only care about the situation in which the error changes from
positive to negative. A situation in which the error crosses from negative
to positive simply won't occur, so we don't really care. But what if we did
care, because, for example, we wanted to detect when the cannon ball hit a
ceiling?

The enumeration member variable ```REGULA_FALSI.mode``` allows us to specify
the crossing directions in which we are interested. Possible are values :

1. **Any** - (default) specifies that an event occurs when the boundary is
crossed from either direction, that is, from positive to negative or from
negative to positive.
2. **Increasing** - specifies that an event occurs only when the boundary is
crossed from negative to positive.
3. **Decreasing** - specifies that an event occurs only when the boundary is
crossed from positive to negative.

So, in our cannon ball simulation, we could set ```C->rf.mode``` to
```Decreasing``` to explicitly indicate that the only events we care about are
positive to negative boundary crossings. Or, we could just let the mode default
to ```Any```, because the cannonball doesn't start below the ground.

* ```REGULA_FALSI.error_tol```

To specify the how small the error should be before declaring success, set
```REGULA_FALSI.error_tol```. The
