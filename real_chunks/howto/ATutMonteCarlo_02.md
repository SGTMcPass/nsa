### Monte Carlo > Optimization > Modifications to S_Define

 and select **Add run(s)**. Then open quick plot by clicking the blue lightning bolt. Expand the dyn.cannon.pos[0-1] variable in the left pane and create a curve with pos[1] as the Y axis and pos[0] as the X axis. Finally, click the **comparison plot** button in the actions menu.

<p align="center">
	<img src="images/MONTE_list_plot.png" width=750px/>
</p>

The various curves show the trajectories of each cannon run. It may be necessary to hide the legend if all the run names cover up the plot.

<a id=random-input-generation></a>
## Random Input Generation
Random Input Generation provides users with the ability to statistically generate input values along a Gaussian or Poisson distribution. Random generation is less precise than an input file, but it is more extensible and much easier to modify. Modify the input file again to use a gaussian distribution to generate launch angles.

<a id=listing-input-2></a>
**Listing - input.py**

```python
exec(open("Modified_data/cannon.dr").read())

# Enable Monte Carlo.
trick.mc_set_enabled(1)

# Run 100 randomly generated variables.
trick.mc_set_num_runs(100)

# Create a Monte Carlo Random variable.
mcvar_launch_angle = trick.MonteVarRandom("dyn.cannon.init_angle", trick.MonteVarRandom.GAUSSIAN, "rad")

# Set the random number generator seed.
mcvar_launch_angle.set_seed(1)

# Set the standard deviation for this bellcurve.
mcvar_launch_angle.set_sigma(30)

# Set the center of the bellcurve.
mcvar_launch_angle.set_mu(3.141592 / 4) # PI/4

# Set the maximum and minimum values to be generated.
mcvar_launch_angle.set_max(3.141592 / 2) # PI/2
mcvar_launch_angle.set_min(3.141592 / 12) #PI/12

# The min and max are absolute values, not relative to mu.
mcvar_launch_angle.set_min_is_relative(False)
mcvar_launch_angle.set_max_is_relative(False)

# Add the variable.
trick.mc_add_variable(mcvar_launch_angle)

# Stop Monte Carlo runs after 25 seconds of simulation time
trick.stop(25)

# Stop Monte Carlo runs if they take longer than 1 second of real time
trick.mc_set_timeout(1)
```

Run the script and plot the curves the same way as before. You will end up with something similar to this:

<p align="center">
	<img src="images/MONTE_gauss_plot.png" width=750px/>
</p>

<a id=optimization></a>
## Optimization
Optimization is the process of evaluating the previous run's data for use in the next run. In essence, you are optimizing each subsequent run and closing in on a specific
