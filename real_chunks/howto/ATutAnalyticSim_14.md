### Building & Running a Trick-based Simulation > Running The Simulation > Sim Execution

. There is no need to recompile the simulation after
changing the input file. The file is interpreted.

<a id=listing_9_input_py></a>
**Listing 9 - input.py**

```python
trick.stop(5.2)
```

By convention, the input file is placed in a `RUN_*` directory.

```bash
% cd $HOME/trick_sims/SIM_cannon_analytic
% mkdir RUN_test
% cd RUN_test
% vi input.py <edit and save>
```

### Sim Execution
To run the simulation, simply execute the `S_main*exe`:

```bash
% cd $HOME/trick_sims/SIM_cannon_analytic
% ./S_main_*.exe RUN_test/input.py
```

If all is well, something similar to the following sample output will be
displayed on the terminal.

```
IMPACT: t = 5.096839959, pos[0] = 220.699644186

========================================
      Cannon Ball State at Shutdown
t = 5.2
pos = [220.699644186, 0.000000000]
vel = [0.000000000, 0.000000000]
========================================
     REALTIME SHUTDOWN STATS:
     REALTIME TOTAL OVERRUNS:            0
            ACTUAL INIT TIME:        0.203
         ACTUAL ELAPSED TIME:       12.434
SIMULATION TERMINATED IN
  PROCESS: 0
  ROUTINE: Executive_loop_single_thread.cpp:98
  DIAGNOSTIC: Reached termination time

       SIMULATION START TIME:        0.000
        SIMULATION STOP TIME:        5.200
     SIMULATION ELAPSED TIME:        5.200
        ACTUAL CPU TIME USED:        0.198
       SIMULATION / CPU TIME:       26.264
     INITIALIZATION CPU TIME:        0.144
```

We got the same answer! But, what about the trajectory? In the next section, we’ll see how to record our simulation variables to a file, so we can plot them.

---

[Next Page](ATutRecordingData)
