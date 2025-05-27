### Monte Carlo > Optimization > Modifications to S_Define

-value-list></a>
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
This text file will be used to assign the cannon's initial angle. Remember that this angle is in radians.

### Updating our Input File
The simulation input file must be adjusted to run the simulation using Monte Carlo techniques.

```
% cd $HOME/trick_sims/SIM_cannon_analytic/RUN_test
% vi input.py
```

The simulation must be told to enable Monte Carlo, recognize a Monte Carlo variable, and use the angle_value_list file created above. To accomplish this, change the input file to include the following:

<a id=listing-input_1></a>
**Listing - input.py**

```python

exec(open("Modified_data/cannon.dr").read())

# Enable Monte Carlo.
trick.mc_set_enabled(1)

# Sets the number of runs to perform to 15. Trick will not exceed the number of values in an input file.
trick.mc_set_num_runs(15)

# Create and add a new Monte Carlo File variable to the simulation.
mcvar_launch_angle = trick.MonteVarFile("dyn.cannon.init_angle", "angle_value_list", 1, "rad")
trick.mc_add_variable(mcvar_launch_angle)

# Stop Monte Carlo runs after 25 seconds of simulation time
trick.stop(25)

# Stop Monte Carlo runs if they take longer than 1 second of real time
trick.mc_set_timeout(1)
```

After the file has been adjusted, save it and run the simulation.

```
% cd ..
% ./S_main*.exe RUN_test/input.py
```

The terminal will display a fairly verbose Monte Carlo process detailing each run. After completion, information about each run will be put into a MONTE_RUN_test directory.

In order to complete our task of finding the optimal launch angle, it will be necessary to plot each run to compare the distance achieved by each cannon. Open up the Trick Data Product application with the following command.

```
trick-dp &
```

<p align="center">
	<img src="images/Trick-DP.png" width=750px/>
</p>

Right click the MONTE_RUN_test directory and select **Add run(s)**. Then open quick plot by clicking the blue lightning bolt. Expand the dyn.cannon.pos[0-1] variable in the left pane and create a curve with pos[1] as the Y axis and pos[0] as the X axis. Finally, click the **comparison plot** button in the actions menu.

<p align="center">
	<img src="images/MONTE_list_plot.png" width
