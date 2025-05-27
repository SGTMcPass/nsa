### Building & Running a Trick-based Simulation > Running The Simulation > Sim Execution

, and ultimately
creating a simulation executable.

```
% cd $HOME/trick_sims/SIM_cannon_analytic
% trick-CP
```

If you typed everything perfectly... Trick is installed properly... there are no
bugs in the tutorial... the stars are aligned... and Trick is in a good mood...
You should, ultimately see :

```
Trick Build Process Complete
```

Now, take a look at the sim directory. Is there an `S_main*.exe` file?? (* is a wildcard, instead of * you will see the name of your platform). If so, cool deal. If not, scream!, then take a look at the next section "Troubleshooting A Bad Build". If all went well, you will notice several other files now resident in the `SIM_cannon_analytic` directory.

```bash
% ls
S_overrides.mk                        makefile
S_sie.resource                        trick.zip
S_define                              S_source.hh
S_main_<your_platform_name_here>.exe	build
```

#### Troubleshooting A Bad Build

Here are some common problems.

* Trick cannot seem to find a function or structure that you have in your
S_define.
    * Make sure that your TRICK_CFLAGS are set.
    * You have a misspelling.
    * In order for Trick to find a job, argument types must match exactly.
* Trick barfs when building the simulation
    * One of your C routines may not compile because of a C syntax error.
    * Trick was not installed properly on your system.
* trick-CP croaks - You may have a syntax error in your S_define.


<a id=running-the-simulation></a>
## Running The Simulation

You've done a lot of work to get to this point. You've created a header, a
default data job, an initialization job, a scheduled job, and an S_define.
You've also had to set up an environment and trudge through trick-CP errors. The
tiny Trickless main() program may be looking short-n-sweet at this point! There
can't be anything more to do!?!  There is one more file to create to get the
cannonball out of the barrel and into the air.

### Simulation Input File
Every Trick simulation needs an input file. This input file will be simple (only
one line). In practice, input files can get ridiculously complex. The input file
is processed by Python. There is no need to recompile the simulation after
changing the input file. The file is interpreted.

<a id=listing_9_input_py></a>
**Listing 9 - input.py**

```python
trick.stop(5.2)
```

By convention, the input file is placed in a `RUN_*` directory.

```bash
% cd $HOME/trick_sims/SIM_cannon_analytic
%
