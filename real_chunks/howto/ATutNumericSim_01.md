### State Propagation with Numerical Integration > Numeric Versus Analytical

 as **Euler**, **Runge Kutta 2**, **Runge
Kutta 4**, and others. To provide simulation developers with a means of getting
data into and out of these algorithms, Trick defines the following two job
classes:

1. **derivative** class jobs - for calculating the state time derivatives.
2. **integration** class jobs - for integrating the state time derivatives
from time t(n-1) to t(n), to produce the next state.

A special **integ_loop** job scheduler coordinates the calls to these jobs.
Depending on the chosen integration algorithm, these jobs are called one or more
times per integration time step. For the Euler integration algorithm, they are
each only called once. For Runge Kutta 4 integration algorithm they are each
called 4 times per integration time step.

<a id=derivative-class-jobs></a>
## Derivative Class Jobs

The purpose of a derivative class job is to generate model time derivatives
when it is called by the integration loop scheduler. If these derivatives are
dependent on the results of the corresponding integration, then they and the
time dependent quantities on which they depend should be calculated in the
derivative job.

For "F=ma" type models, derivative jobs calculate acceleration, by dividing the
sum of the forces applied to the object, whose state we are propagating, at a
given time, by its mass.

If acceleration is constant, then it does not really need to be calculated in a
derivative job. But if acceleration is a function of time, as when it is a
function of one or more of the model state variables, then it needs to be
calculated in a derivative job. Note that the time dependent quantities from
which acceleration is calculated should also be calculated in the derivative
job.

In the corresponding integration class job, the acceleration is then integrated
to produce velocity, and velocity is integrated to produce position.

### Example: A Skydiver

Suppose we want to model a skydiver plummeting to Earth. In our model we decide
to account for two forces that are acting on the skydiver:

1. The force of gravity.
2. The atmospheric drag force.

The force of gravity can be calculated using Newton's Law of Gravitation:

![Figure 1 - Newton's Law of Gravitation](images/NewtonsLawOfGravitation.png)

and the drag force can be calculated using the drag equation:

![Figure 2 - Drag Equation](images/DragEquation.png)

Notice that the force of gravity is dependent upon the skydiver position,
which is an integration result. Therefore the force of gravity needs to be
calculated in the derivative class job, prior to summing the forces.

Similarly, the drag force has state variable dependencies. It is obviously
dependent on velocity, but also notice that the atmospheric air density is a
function of
