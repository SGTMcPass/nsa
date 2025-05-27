### Viewing Real-Time Data with Trick View (TV) > TV Without An Input File > TV With An Input File

| [Home](/trick) → [Tutorial Home](Tutorial) → Viewing Real-Time Data |
|-------------------------------------------------------------------|

<!-- Section -->
<a id=viewing-real-time-data-with-trick-view></a>
## Viewing Real-Time Data with Trick View (TV)

Trick View (TV) is an application for viewing/setting simulation variables in
real-time. TV can be launched from the input file, or may be launched directly
from the sim control panel. You can also leave TV running between simulation
runs. In this case You will need to click the "Connect" button in the lower right
corner of the TV GUI to re-connect to the simulation.

#### TV Without An Input File
1. Fire up the simulation:

   ```bash
   % cd $HOME/trick_sims/SIM_cannon_analytic
   % ./S_main*exe RUN_test/input.py &
   ```

1. Start TV by either clicking the blue TV icon button or choosing
the sim control panel menu option: **Actions->Start TrickView**. The TV
GUI should pop up.

1. In the **Variable Hierarchy Tree** pane, on the left side of the
GUI, double-click `dyn`, and then double-click `cannon`.

1. Choose some variables to view. Double-click on `pos[2]`, and
`vel[2]`. These variables will be added to the **Variable Table** pane on the
right.

1. Since we have gone to the trouble, go ahead and save these
selections.

    * Click the **Save** button on the TV toolbar, or select **File->Save** from
    the main menu.
    * Save to the `SIM_cannon_analytic` directory, and name the file "TV_cannon".

1. On the sim control panel, choose **Actions->FreezeAt**. Enter in a
time of 2.0 seconds. Click **OK**.

1. On the sim control panel, click the **Start** button to put the
simulation into action. Notice that TV parameter values have changed. When the
simulation time reaches 2.0 seconds, the cannon ball position will be [86.17, 30.33].

1. In the Trick View variable table, select `dyn.cannon.pos[0]` and
`dyn.cannon.pos[1]`. You can use SHIFT-click to select both. With these
variables high-lighted, select **Actions->Strip Chart** on the menu bar. The
Strip Chart GUI should then appear, and represent each of the two variables as a
squiggly line, and unique color of its own. Also verify that the two values of
dyn.cannon.pos as represented in TV, and Stripchart agree.

1. Now force the Y position of the cannonball to drop to 10
meters. To do this, click on the
