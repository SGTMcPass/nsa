### Monte Carlo > Optimization > Modifications to S_Define

| [Home](/trick) → [Tutorial Home](Tutorial) → Monte Carlo |
|--------------------------------------------------------|

# Monte Carlo

**Contents**

* [What is Monte Carlo?](#what-is-monte-carlo)
* [Example Task](#example-task)
* [Input Files](#input-files)
  - [Listing - **angle_value_list**](#listing-value-list)
  - [Listing - **input.py**](#listing-input_1)
* [Random Input Generation](#random-input-generation)
  - [Listing - **input.py**](#listing-input-2)
* [Optimization](#optimization)
  - [Listing - **optimization.h**](#listing-optimization-h)
  - [Listing - **optimization.c**](#listing-optimization-c)
  - [Listing - **input.py**](#listing-input-3)
  - [Listing - **S_Define**](#listing-s-define)

***

<a id=what-is-monte-carlo></a>
## What is Monte Carlo?

Monte Carlo is an advanced simulation capability provided by Trick that allows users to repeatedly run copies of a simulation with different input values. Users can vary the input space of a simulation via input file, random value generation, or by calculating values from previous Monte Carlo runs in a process called optimization. This tutorial will show you how to modify the cannon_numeric simulation to take advantage of this capability.

**For a thorough explanation of Monte Carlo and its features, read the [Monte Carlo User Guide](/trick/documentation/simulation_capabilities/UserGuide-Monte-Carlo).**

<a id=example-task></a>
## Example Task
**What would be the optimal launch angle required to ensure our cannonball travels the furthest distance?** Let us assume that we have no conception of physics or trigonometry and that we don't already know the answer.

<p align="center">
	<img src="images/OptimalLaunchAngle.png" width=550px/>
</p>

<a id=input-files></a>
## Input Files
Input files allow you to specify the exact values you want on a particular simulation run. Input files are the most precise implementation, but they require more effort to setup and modify later down the road. Input files can contain multiple (tab or space) delimited columns filled with numerical information.

### Value List
Create the following text file in your simulation directory with the name **angle\_value\_list**:

<a id=listing-value-list></a>
**Listing - angle_value_list**

```
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
1.1
1.2
1.3
1.4
1.5

```
This text file will be used to assign the cannon's initial angle. Remember that
