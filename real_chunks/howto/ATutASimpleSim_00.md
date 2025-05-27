### A Simple (non-Trick) Simulation > Cannonball Problem Statement > Limitations of the Simulation

| [Home](/trick) → [Tutorial Home](Tutorial) → A Simple Simulation |
|----------------------------------------------------------------|

<!-- Section -->
<a id=simulating-a-cannonball></a>
## A Simple (non-Trick) Simulation

**Contents**

* [Cannonball Problem Statement](#cannonball-problem-stated)<br>
* [Modeling The Cannonball](#modeling-the-cannonball)<br>
* [A Cannonball Simulation (without Trick)](#a-cannonball-simulation-without-trick)<br>
  - [Listing 1 - **cannon.c**](#listing_1_cannon.c)
* [Limitations Of The Simulation](#limitations-of-the-simulation)<br>

***

In this tutorial, we are going to build a cannonball simulation. We will start out with
a non-Trick-based simulation. Then we will build a Trick-based simulation. Then we
will make incremental improvements to our Trick-based simulation, introducing new
concepts as we go.

The commands following `%` should typed in and executed.

---

<a id=cannonball-problem-stated></a>
### Cannonball Problem Statement

![Cannon](images/CannonInit.png)

**Figure 1 Cannonball**

Determine the trajectory and time of impact of a cannon ball that is fired
with an initial speed and initial angle. Assume a constant acceleration of
gravity (g), and assume no aerodynamic forces.

---
<a id=modeling-the-cannonball></a>
### Modeling the Cannonball

For this particular problem it's possible to write down equations that
will give us the position, and velocity of the cannon ball for any time (t).
We can also write an equation that will give us the cannon ball’s time of impact.

The cannonball’s acceleration over time is constant. It's just the acceleration of gravity:

![equation_acc](images/equation_acc.png)

On earth, at sea-level, g will be approximately -9.81 meters per second squared.
In our problem this will be in the y direction, so:

![equation_init_g](images/equation_init_g.png)

Since acceleration is the derivative of velocity with respect to time, the
velocity [ v(t) ] is found by simply anti-differentiating a(t). That is:

![equation_analytic_v_of_t](images/equation_analytic_v_of_t.png)

where the initial velocity is :

![equation_init_v](images/equation_init_v.png)

The position of the cannon ball [ p(t) ] is likewise found by anti-differentiating
v(t).

![equation_analytic_p_of_t](images/equation_analytic_p_of_t.png)

Once we specify our initial conditions, we can calculate the position and
velocity of the cannon ball for any time t.

Impact is when the cannon ball hits the ground, that is when
