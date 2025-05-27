### A Simple (non-Trick) Simulation > Cannonball Problem Statement > Limitations of the Simulation

images/equation_init_v.png)

The position of the cannon ball [ p(t) ] is likewise found by anti-differentiating
v(t).

![equation_analytic_p_of_t](images/equation_analytic_p_of_t.png)

Once we specify our initial conditions, we can calculate the position and
velocity of the cannon ball for any time t.

Impact is when the cannon ball hits the ground, that is when the cannonball’s
y-coordinate again reaches 0.

![equation_analytic_y_of_t_impact](images/equation_analytic_y_of_t_impact.png)

Solving for t (using the quadratic formula), we get the time of impact:

![equation_analytic_t_impact](images/equation_analytic_t_impact.png)

---
<a id=a-cannonball-simulation-without-trick></a>
### Code For a non-Trick Cannonball Simulation

<a id=listing_1_cannon.c></a>
**Listing 1 - cannon.c**

```c
/* Cannonball without Trick */

#include <stdio.h>
#include <math.h>

int main (int argc, char * argv[]) {

    /* Declare variables used in the simulation */
    double pos[2]; double pos_orig[2] ;
    double vel[2]; double vel_orig[2] ;
    double acc[2];
    double init_angle ;
    double init_speed ;
    double time ;
    int impact;
    double impactTime;

    /* Initialize data */
    pos[0] = 0.0 ; pos[1] = 0.0 ;
    vel[0] = 0.0 ; vel[1] = 0.0 ;
    acc[0] = 0.0 ; acc[1] = -9.81 ;
    time = 0.0 ;
    init_angle = M_PI/6.0 ;
    init_speed = 50.0 ;
    impact = 0;

    /* Do initial calculations */
    pos_orig[0] = pos[0] ;
    pos_orig[1] = pos[1] ;
    vel_orig[0] = cos(init_angle)*init_speed ;
    vel_orig[1] = sin(init_angle)*init_speed ;

    /* Run simulation */
    printf("time, pos[0], pos[1], vel[0], vel[1]\n" );
    while ( !impact ) {
        vel[0] = vel_orig[0] + acc[0] * time ;
        vel[1] = vel_orig[1] + acc[1] * time ;
        pos[0] = pos_orig[0] + (vel_orig[0] + 0.5 * acc[0] * time) * time ;
        pos[1] = pos_orig[1] + (vel_orig[1] + 0.5 *
