### State Propagation with Numerical Integration > Numeric Versus Analytical

Figure 2 - Drag Equation](images/DragEquation.png)

Notice that the force of gravity is dependent upon the skydiver position,
which is an integration result. Therefore the force of gravity needs to be
calculated in the derivative class job, prior to summing the forces.

Similarly, the drag force has state variable dependencies. It is obviously
dependent on velocity, but also notice that the atmospheric air density is a
function of altitude (position). So, it too should be calculated in the
derivative job.

Again, if the derivatives are dependent on the results of the corresponding
integration, then those derivatives and the time dependent quantities on which
they depend should be calculated in the derivative job.

<a id=integration-class-jobs></a>
## Integration Class Jobs
The purpose of a integration class job is to integrate the derivatives that were
calculated in the corresponding derivative jobs, producing the next simulation
state from the previous state.

Integration jobs generally look very similar. That is because they are expected
to do the same five things:

1. Load the state into the integrator.
2. Load the state derivatives into the integrator.
3. Call the integrate() function.
4. Unload the updated state from the integrator.
5. Return the value that was returned by the integrate() call.

Using the integration interface functions, `load_state()`, `load_deriv()`,
`integrate()`, and `unload_state()` requires that `integrator_c_intf.h` be
included. And of course the data structure(s) that define the model state will
also have to be included.

The value returned from `integrate()`, and stored in the `ipass` variable below,
tells the Trick integration scheduler the status of the state integration. It
returns the last integration step number until it is finished, when it returns 0.
For example, if the integrator is configured for Runge Kutta 4, a four step
integration algorithm, then `integrate()` will return 1 the first time it is
called, 2 the second time, 3 the third, and 0 the fourth time, indicating that
it is done.

<a id=configuring-the-integration-scheduler></a>
## Configuring The Integration Scheduler
Producing simulation states by numerical integration requires that the derivative
and integration jobs be called at the appropriate rate and times. This requires
a properly configured integration scheduler.

First, instantiate an integration scheduler in the S_define with a declaration
of the following form:

```c++
IntegLoop integLoopName ( integrationTimeStep ) listOfSimObjectNames ;
```

* Jobs within a simObject that are tagged "derivative" or "integration" will be
dispatched to the associated integration scheduler.

Then, in the input file, call the IntegLoop **getIntegrator()** method to specify
the integration algorithm of choice and the number of state variables
