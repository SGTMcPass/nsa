### Dynamic Events - Making Contact > Updating Our Cannonball Simulation > Step 6 - Run the Simulation

| [Home](/trick) → [Tutorial Home](Tutorial) → Dynamic Events |
|-----------------------------------------------------------|

<!-- Section -->
<a id=dynamic-events-making-contact></a>
# Dynamic Events - Making Contact

**Contents**

* [What are Dynamic Events?](#what-are-dynamic-events)
* [Dynamic Event Jobs](#dynamic-event-jobs)
  - [Finding Events with *regula_falsi()*](#finding-events-with-regula-falsi)
  - [Listing - **cannon_impact()**](listing_cannon_impact)
* [Specifying an Event Boundary](#specifying-an-event-boundary)
* [Calling **regula_falsi()**](#calling-regula-falsi)
* [Updating Our Cannonball Simulation](#updating-our-cannonball-simulation)

***

<a id=what-are-dynamic-events></a>
## What are Dynamic Events?

Our numerical cannon ball simulation still needs to determine the precise time
of impact, *t* when *y(t)=0*.

Remember that the reason for using numerical methods is that simulations often
don't have analytical solutions. So, even though we do have an expression that
will immediately tell us the time of impact of our cannon ball, we're going to
pretend, for now, and for the sake of this tutorial, that we don't.

Let's take a look at the plot of the cannon ball trajectory near *y(t)=0*, in
the figure below. Each blue point represents the state of the cannon ball at the
indicated time step.

Notice that the ball's trajectory crosses *y(t)=0* (the ground) in between our
time steps, somewhere between 5.09 seconds, and 5.10 seconds. So, the question
is, how do we find the exact time that it crosses the y-axis? In Trick, we call
this type of occurrence, when our simulation state is at some boundary that
we've defined, a **dynamic-event**. To find dynamic-events, we use
**dynamic-event** jobs.

**Figure - Cannon Ball Trajectory Near y(t) = 0**
![IntegStepCrossesZero](images/IntegStepCrossesZero.png)

<a id=dynamic-event-jobs></a>
## Dynamic Event Jobs

A dynamic-event job is called periodically, after each integration step.
Its job is to detect when the simulation state crosses a user-defined
event boundary, to take control of integration to find the exact event state
and time, and finally to perform some action as a result. It does
this using the Trick's ```regula_falsi()``` function and ```REGULA_FALSI```
data-type to implement the
[False position method](https://en.wikipedia.org/wiki/False_position_method).

<a id=finding-events-with-regula-falsi></a>
### Finding
