### Executive Flow > Debugging Help > Getting Build Information

| [Home](/trick) → [Documentation Home](../Documentation-Home) → [Simulation Capabilities](Simulation-Capabilities) → Executive Scheduler |
|------------------------------------------------------------------|

This scheduler or derivative of this class is required for Trick simulations to run.

The scheduler is in charge of simulation execution.  The scheduler maintains simulation elapsed time.  The scheduler has 4 modes of operation, Initialization, Run, Freeze, and Shutdown.  The scheduler maintains the simulation mode.  Within each mode of operation the executive/scheduler calls different sets of user and system jobs.

The scheduler is implemented by the Trick::Executive class.

## Executive Flow

The next set of flowcharts details how the Trick main executable runs.

![Executive Initialization](images/initialization.png)

**Figure 1 Executive Initialization**

During the Initialization phase three job classes are called, default data, input_processor, and initialization.  All jobs of these classes are executed in the main thread.  Not shown in the picture is any job returning a non-zero value to "trick_ret" will cause the simulation immediately to go to shutdown.  Execution continues to the Scheduled loop.

![Scheduled Loop](images/scheduled_loop.png)

**Figure 2 Scheduled Loop**

Run mode is also called the Scheduled loop.  The Scheduled loop calls the top_of_frame, the scheduled jobs, and the end_of_frame jobs.  Both the top_of_frame and end_of_frame jobs are called at the software_frame cycle rate.  The scheduled jobs include these job classes:

- integ_loop.  The integ_loop includes derivative, integration, dynamic_event, and post_integration.
- automatic
- environment
- sensor
- sensor_receiver
- scheduled, effector
- effector_emitter
- effector_receiver
- automatic_last
- logging
- advance_sim_time

Receiving a freeze command diverts execution to the Freeze loop.  Execution is resumed in the scheduled loop when returning to run mode.

The loop is run until an exit condition is met.  The exit conditions include receiving an exit command, reaching the termination time, or a job returning a non-zero value to "trick_ret".  Upon meeting an exit condition, execution continues to the Shutdown phase.

![Freeze Loop](images/freeze_loop.png)

**Figure 3 Freeze Loop**

Execution is diverted to the Freeze loop when the Freeze command is set in the Scheduled loop.  When entering freeze the freeze_init jobs are called. The freeze loop cyclically calls the freeze scheduled jobs, freeze_automatic, and freeze jobs.  Elapsed freeze time is kept and cycle times for the freeze_scheduled jobs are followed.  freeze_automatic jobs are assumed to set their own next call time.  Freeze jobs are called at the end of the freeze_software_frame.  The loop is run until a run command is received or an exit condition is met.  Upon receiving a run command, execution is returned to the Scheduled loop.  The exit conditions include receiving an exit command or a job returning a non-zero value to "trick_ret". Upon meeting an exit condition, execution continues to the Shutdown phase.

![Shutdown](images/shutdown.png)

**Figure 4 Shutdown**

The shutdown phase calls the shutdown phase jobs and exits.  Easy peasy.

## Executive Time

Accessing the simulation time is one of the more common user interactions with the executive.  The executive keeps track of only simulation time.  The executive does not keep track of realtime.  That is the job of Trick::RealtimeSync.  The executive also does not keep track of other times including mission elapsed time, universal time, or other model generated time.

### Reading the Time

The executive provides 2 calls to get the simulation time.

```
double exec_get_sim_time() ;
long long exec_get_time_tics() ;
```

exec_get_sim_time() is a returns a double representing simulation elapsed seconds.  exec_get_sim_time() will not return an exact value when time values are large due to roundoff error.

exec_get_time_tics() returns the number of elapsed time tics.  The time tic is explained below.

### Setting the Time

Trick provides 2 calls to set the simulation time.

```c
int exec_set_time( double in_time ) ;
int exec_set_time_tics( long long in_time_tics ) ;
```

exec_set_time() sets the current simulation time to the incoming value.  This should normally be done at initialization.  Doing this while running is not defined.

exec_set_time_tics() sets the simulation time based on time tics.  The time tic is explained below.

### Time tic

```c
int exec_get_time_tic_value( void ) ;
int exec_set_time_tic_value( int num_of_tics_per_second ) ;
```

A time tic is a fraction of a second equal to 1s/<number_of_tics_per
