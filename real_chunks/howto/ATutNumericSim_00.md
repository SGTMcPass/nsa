### State Propagation with Numerical Integration > Numeric Versus Analytical

| [Home](/trick) → [Tutorial Home](Tutorial) → Numerical Integration |
|------------------------------------------------------------------|

<!-- Section -->
<a id=state-Propagation-with-numerical-integration></a>
# State Propagation with Numerical Integration

**Contents**

   * [How Trick Does Numerical Integration](#how-trick-does-numerical-integration)
   * [Derivative Class Jobs](#derivative-class-jobs)
   * [Integration Class Jobs](#integration-class-jobs)
   * [Configuring The Integration Scheduler](#configuring-the-integration-scheduler)
   * [Updating the Cannonball Sim to use Numerical Integration](#updating-the-cannonball-sim-to-use-numerical-integration)
      - [Listing - **cannon_numeric.h**](#listing_cannon_numeric_h)
   * [Creating a Derivative Class Job](creating-a-derivative-class-job)
      - [Listing - **cannon_deriv()**](#listing_cannon_deriv_func)
   * [Creating an Integration Class Job](#creating-an-integration-class-job)
      - [Listing - **cannon_integ()**](#listing_cannon_integ_func)
   * [Updating the S_define File](#updating-the-s_define-file)
      - [Listing - **S_define**](#listing_s_define)
   * [Running The Cannonball With Trick Integration](#running-the-cannonball-with-trick-integration)
   * [Numeric Versus Analytical](#numeric_vs_analytical)

***

<a id=how-trick-does-numerical-integration></a>
## How Trick Does Numerical Integration
The type of model that we created in the last section relied on the fact that
the cannon ball problem has a closed-form solution from which we can
immediately calculate the cannon ball state [position, velocity] at any
arbitrary time. In real-world simulation problems, this will almost never
be the case.

In this section we will model the cannon ball using **numeric integration**,
a technique that can be used when no closed-form solution exists. Instead of
calculating state(n) by simply evaluating a function, it will be calculated by
integrating the state time derivatives [velocity, acceleration] over the
simulation time step from t(n-1) to t(n); adding that to the previous state(n-1).

The Trick integration scheme allows one to choose from amongst several
well-known integration algorithms, such as **Euler**, **Runge Kutta 2**, **Runge
Kutta 4**, and others. To provide simulation developers with a means of getting
data into and out of these algorithms, Trick defines the following two job
classes:

1. **derivative** class jobs - for calculating the state time derivatives.
2. **integration** class jobs - for integrating the state time derivatives
from time t(n-1)
