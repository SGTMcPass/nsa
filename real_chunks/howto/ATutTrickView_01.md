### Viewing Real-Time Data with Trick View (TV) > TV Without An Input File > TV With An Input File

Actions->Strip Chart** on the menu bar. The
Strip Chart GUI should then appear, and represent each of the two variables as a
squiggly line, and unique color of its own. Also verify that the two values of
dyn.cannon.pos as represented in TV, and Stripchart agree.

1. Now force the Y position of the cannonball to drop to 10
meters. To do this, click on the dyn.cannon.pos[1] variable on the TV Parameter
table. Replace 30.325... with 10.0 as a new position. Hit **Enter** to set the
variable with the new value. The stripchart should show the drop from 30 meters
to 10 meters.

1. Notice that dyn.cannon.vel[0] is 43.30... meters per second. To
view it in feet per second:
    * Left Click on the variable dyn.cannon.vel[0] on the Variable table.
    * Double Click on the "m/s" in the Unit column to edit the field.
    * Type **ft/s**. Notice that the value of dyn.cannon.vel[0] changes to
    142.06... ft/s.

1. Resume the simulation run by clicking the **Start** button on the
sim control panel. Notice that the trajectory assumes its predetermined path.
This is because we are analytically calculating the cannonball position as a
function of time, rather than calculating it from the previous frame data.


#### TV With An Input File
If this simulation were run over and over, it would be laborious to
clickety-click the variables each time. It would be advantageous to use the
TV_cannon file we saved off in the last step. There are two ways to do this.

##### Loading A TV Input File Directly From TV

1. Fire up the cannon.

```bash
% cd $HOME/trick_sims/SIM_cannon_analytic
% ./S_main*exe RUN_test/input.py &
```

1. Choose "Actions->Start Trick View" from sim control panel.

1. Click the file **Open** or **Open** with a blue circle icon button on
the TV toolbar or select File->Open or File->Open & Set from the main menu.

1. Select the TV_cannon file saved off in the last run. The Parameter
table on the right is cleared and replaced with all the saved variables.

1. If "Set" is chosen for opening a TV file, all saved values are
restored as well. Otherwise, only variables are loaded to the Parameter table.
If only "Set" is selected, corresponding vaiable values are restored without the
Parameter table being changed.
This simulation is simple since we have a limited number of parameters. The
streamlining is more pronounced when the simulation has thousands of variables,
in which the process for selecting variables would become
