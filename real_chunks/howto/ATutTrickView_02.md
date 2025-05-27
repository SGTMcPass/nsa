### Viewing Real-Time Data with Trick View (TV) > TV Without An Input File > TV With An Input File

Set" is chosen for opening a TV file, all saved values are
restored as well. Otherwise, only variables are loaded to the Parameter table.
If only "Set" is selected, corresponding vaiable values are restored without the
Parameter table being changed.
This simulation is simple since we have a limited number of parameters. The
streamlining is more pronounced when the simulation has thousands of variables,
in which the process for selecting variables would become awfully repetitious.

##### Allowing The Simulation To Load A TV Input File
It even gets tiresome clicking the TV input file from TV. The following example
shows how to configure the simulation to automatically launch the TV with the
parameters of interest. The syntax for this file is similar to the stripchart
input file.
Again, we need to incorporate the TV input file into our ever expanding
simulation input file.

```python
exec(open("Modified_data/realtime.py").read())
exec(open("Modified_data/cannon.dr").read())

trick.trick_view_add_auto_load_file("TV_cannon.tv")
trick.stop(5.2)
```
**Listing 9a - Simulation TV Input File - input.py**

```bash
% cd $HOME/trick_sims/SIM_cannon_analytic/RUN_test
% vi input.py <edit and save>
```

You may now run the sim and verify that TV pops up automatically.

[Next Page](ATutNumericSim)
