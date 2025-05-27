### Integrator Control Inputs

| [Home](/trick) → [Documentation Home](../Documentation-Home) → [Simulation Capabilities](Simulation-Capabilities) → Integrator |
|------------------------------------------------------------------|

Trick provides a state integration capability described by the inputs below.
To use these options a developer must develop application code which interfaces the application states with
the Trick integration services.
The integration job class is designed to accommodate the application state to Trick integration service interface.

All integration class jobs must return an integer value which represents the current integration pass identifier.
If all integration passes are complete, the job must return a zero.

The code below represents a simple integration job implementation.

```
/*********** TRICK HEADER **************
PURPOSE:   (State Integration Job)
...
CLASS:     (integration)
...
*/
#include "ip_state.h"
#include "sim_services/Integrator/include/integrator_c_intf.h"

int integration_test( IP_STATE* s)
{
    int ipass;

    /* LOAD THE POSITION AND VELOCITY STATES */
    load_state(
        &s->pos[0],
        &s->pos[1],
        &s->vel[0],
        &s->vel[1],
        NULL
    );

    /* LOAD THE POSITION AND VELOCITY STATE DERIVATIVES */
    load_deriv(
        &s->vel[0],
        &s->vel[1],
        &s->acc[0],
        &s->acc[1],
        NULL
    );

    /* CALL THE TRICK INTEGRATION SERVICE */
    ipass = integrate();

    /* UNLOAD THE NEW POSITION AND VELOCITY STATES */
    unload_state(
        &s->pos[0],
        &s->pos[1],
        &s->vel[0],
        &s->vel[1],
        NULL
    );

    /* RETURN */
    return(ipass);
}
```

The <i> integrate() </i> function, declared externally, is the function which physically integrates the states.
This function uses the input parameters defined in Table 18 and 19 to integrate any set of states and derivatives.

First, the states must be loaded,<i> load_state() </i>.
Notice in the example code that both position and velocity are loaded into the state array.
This is because the integrators are primarily 1st order differential equation integrators, which means that
velocities are integrated to positions independently from the accelerations being integrated to velocities.
Hence, the velocity is a state and the acceleration is its derivative,
just as the position is a state and velocity is its derivative.
From the 2 degree of freedom code example, there are four states: two position and two velocity.

Next, the derivative of the position (velocity) and the derivative of the velocity (acceleration) must be loaded,
<i> load_deriv() </i>.  The integration job class is designed to be called once for each intermediate
pass of a multi-pass integrator.  For example the Runge_Kutta_4 integrator will make 4 separate derivative
evaluations and stores the resulting state from each intermediate pass separately so that they may be
combined and weighted to create a "true" state for the specified time step.  The intermediate_step parameter
defines the current intermediate step ID for the integrator.  This parameter is initialized to zero by the
executive and managed by the <i> integrate() </i> function.

With the states and derivatives loaded into the appropriate integrator arrays, the <i> integrate() </i> function
must be called to integrate the states through a single intermediate step of the selected integration scheme.
The integrated states must then be unloaded, <i> unload_state() </i>.

If a developer wishes to use their own integration scheme, then the <i> integrate() </i> function source code
should be reviewed so that the proper interfaces can be maintained.  The <i> integrate() </i> source code is
located in the ${TRICK_HOME}/trick_source/sim_services/integ/integrate.c file.

## Integrator Control Inputs

There can be any number of <i> integration </i> class jobs listed within the S_define file;
each integration job should have an associated <i> IntegLoop </i> declaration.
The available inputs for state integration control are listed in Table 18.

Table 18 State Integration Control Inputs
<table>
 <tr>
  <th width=375>Name</th>
  <th>Default</th>
  <th>Description</th>
 </tr>
 <tr>
  <td>getIntegrator(Integrator_type, unsigned int, double)</td>
  <td>No default value</td>
  <td>Tell Trick the Integrator scheme and the number of state variables.
      A call to this function is required otherwise a runtime error is generated.</td>
 </tr>
 <tr>
  <td
