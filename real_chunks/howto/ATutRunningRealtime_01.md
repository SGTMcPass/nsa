### Running Real-Time > Making A Real-time Input File > Using The Sim Control Panel

(simControlPanel)` -
brings up the simulation control panel GUI.

The `realtime.py` file must be included in the RUN_test/input.py file. When
finished, the latest version of the input file should look like the following:

```python
exec(open("Modified_data/realtime.py").read())
exec(open("Modified_data/cannon.dr").read())
trick.stop(5.2)
```

```bash
% cd $HOME/trick_sims/SIM_cannon_analytic/RUN_test
% vi input.py <edit and save>
```

### Using The Sim Control Panel

Fire up the cannonball again.

```bash
% cd $HOME/trick_sims/SIM_cannon_analytic
% ./S_main*.exe RUN_test/input.py &
```

The **simulation control panel** should popup now. In the `realtime.py` file, we
instructed Trick to start in a **freeze** state. Currently, the ball is sitting
in the base of the barrel. To fire it, the **Start** button must be clicked on
the simulation control panel in the **Commands** box.

1. Click **Start** on simulation control panel. The simulation will
run in sync with real-time.

1. Once the simulation is finished, click the **Exit** button.
Some items to note about the simulation control panel for your future use:
    * You may freeze the simulation at any point, and then restart.
    * You may freeze the simulation, then "dump a checkpoint" of the current
    state. This state is reloadable (i.e., you may jump to a previous/future
    point in the sim by loading the appropriate checkpoint).
    * You may toggle between real-time and non-real-time.
    * If the simulation lags behind real-time, it will log these as overruns
    (does not complete all jobs during the software frame) and display them in
    the tiny box next to the simulation name. If the simulation overruns, the
    sim will run as fast as it can "to catch up" to where it should be.
    * Using the Actions menu at the top, you may set a freeze point in the future.

---

[Next Page](ATutTrickView)
