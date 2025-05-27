### Dynamic Events - Making Contact > Updating Our Cannonball Simulation > Step 6 - Run the Simulation

ALSI rf ; ```

### Step 2 - Modifications to ```cannon_numeric.h```

Add the following prototype for our new dynamic event job function, **cannon_impact**
below the existing **cannon_deriv** prototype.

```c++
double cannon_impact(CANNON*) ;
```

### Step 3 - Modifications to ```cannon_numeric.c```

Add the [cannon_impact](#listing_cannon_impact) function, listed above, to the bottom of **cannon_numeric.c**.

### Step 4 - Modifications to ```SIM_cannon_numeric/S_define```

Add the following job specification, to run our cannon_impact job.

```
("dynamic_event") cannon_impact( &cannon ) ;
```

to the end of the list of jobs in the CannonSimObject.

### Step 5 - Build the Simulation

```cd``` to the ```SIM_cannon_numeric``` directory, and type:

```trick-CP``` to build or re-build the simulation.

If all goes well, you should see:

```Trick Build Process Complete```

### Step 6 - Run the Simulation

Execute the Simulation:

```./S_main_Darwin_16.exe RUN_test/input.py```

You should see:

```
IMPACT: t = 5.096839959, pos[0] = 220.699644186

========================================
      Cannon Ball State at Shutdown
t = 5.2
pos = [220.699644186, 0.000000000]
vel = [0.000000000, 0.000000000]
========================================
```

**It's the same answer we got from our analytic simulation!**

[Next Page](TutVariableServer)
