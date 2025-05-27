### Dynamic Events - Making Contact > Updating Our Cannonball Simulation > Step 6 - Run the Simulation

, to take control of integration to find the exact event state
and time, and finally to perform some action as a result. It does
this using the Trick's ```regula_falsi()``` function and ```REGULA_FALSI```
data-type to implement the
[False position method](https://en.wikipedia.org/wiki/False_position_method).

<a id=finding-events-with-regula-falsi></a>
### Finding Events with *regula_falsi()*

The ```regula_falsi()``` function is the heart of a dynamic event function.
It's job is to:

1. monitor the simulation state produced by each integration step,
2. detect when the state crosses a specified event boundary, and
3. guide Trick's integration scheduler to find that event.

Progress toward finding the event state is recorded in a ```REGULA_FALSI```
variable.

The function ```cannon_impact()```, listed below is the dynamic event job
function that we'll use for our cannonball simulation.

<a id=listing_cannon_impact></a>
**Listing - cannon_impact()**

```c
double cannon_impact( CANNON* C ) {
    double tgo ; /* time-to-go */
    double now ; /* current integration time. */

    C->rf.error = C->pos[1] ;              /* Specify the event boundary. */
    now = get_integ_time() ;               /* Get the current integration time */
    tgo = regula_falsi( now, &(C->rf) ) ;  /* Estimate remaining integration time. */
    if (tgo == 0.0) {                      /* If we are at the event, it's action time! */
        now = get_integ_time() ;
        reset_regula_falsi( now, &(C->rf) ) ;
        C->impact = 1 ;
        C->impactTime = now ;
        C->vel[0] = 0.0 ; C->vel[1] = 0.0 ;
        C->acc[0] = 0.0 ; C->acc[1] = 0.0 ;
        fprintf(stderr, "\n\nIMPACT: t = %.9f, pos[0] = %.9f\n\n", now, C->pos[0] ) ;
    }
    return (tgo) ;
}
```

In the following two sections, we'll discuss the details of how this and other
dynamic event jobs work.

<a id=specifying-an-event-boundary></a>
### Specifying an Event Boundary

* ```REGULA_FALSI.error```

An event boundary is defined by a user-supplied error-function of the simulation
state. After each integration step, the dynamic event job evaluates the error
function at the current state and then assigns the error-value to
```REG
