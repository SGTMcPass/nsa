### Building & Running a Trick-based Simulation > Running The Simulation > Sim Execution

| [Home](/trick) → [Tutorial Home](Tutorial) → Analytical Cannon Simulation |
|-------------------------------------------------------------------------|

<!-- Section -->
<a id=building-and-running-a-trick-based-simulation></a>
# Building & Running a Trick-based Simulation

**Contents**

   * [Organizing the Simulation Code in Directories](#organizing-the-simulation-code-in-directories)<br>
   * [Representing the Cannonball](#representing-the-cannonball)<br>
     - [Listing 2 : **cannon.h**](#listing_2_cannon_h)<br>
     - [The Input/Output (I/O) Specification](#the-input_output-io-specification)<br>
     - [Units Specification](#units-specification)<br>
   * [Initializing the Cannonball Simulation](#initializing-the-cannonball-simulation)<br>
     - [Listing 3 : **cannon_init.c**](#listing_3_cannon_init_c)<br>
   * [Updating the Cannonball State Over Time](#updating-the-cannonball-state-over-time)<br>
     - [listing 4 : **cannon\_analytic.h**](#listing_4_cannon_analytic_h)<br>
     - [listing 5 : **cannon\_analytic.c**](#listing_5_cannon_analytic_c)<br>
   * [Cannonball Cleanup And Shutdown](#cannonball_cleanup_and_shutdown)
     - [listing 6 : **cannon\_shutdown.c**](#listing_6_cannon_shutdown_c)<br>
   * [The Simulation Definition File (S_define)](#simulation-definition-file)<br>
     - [listing 7 : **S_define**](#listing_7_s_define)<br>
   * [Compiling, and Building the Simulation](#compiling-and-building-the-simulation)<br>
     - [Listing 8 : **S_overrides.mk**](#listing_8_s_overrides.mk)
   * [Running the Simulation](#running-the-simulation)<br>
     - [Listing 9 : **input.py**](#listing_9_input_py)

***

In this and subsequent sections, we're going to build and run a Trick-based cannonball simulation.

---

<a id=organizing-the-simulation-code-in-directories></a>
### Organizing the Simulation Code in Directories

We'll begin by creating a directory system to hold our simulation source code:

```bash
%  cd $HOME
%  mkdir -p trick_sims/SIM_cannon_analytic
%  mkdir -p trick_sims/SIM_cannon_analytic/models/cannon/src
%  mkdir -p trick_sims/SIM_cannon_analytic/models/cannon/include
```

---

<a id=representing-the-cannonball></a>
### Representing the Cannonball

To represent
