### Executive Flow > Debugging Help > Getting Build Information

 calls to set the simulation time.

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

A time tic is a fraction of a second equal to 1s/<number_of_tics_per_second>.  The time tic default is 1us.  Scheduled job cycles are converted to numbers of tics.  For instance a 1ms cycle job will be run every 1000 tics.  All job cycles should be a multiple of the time tic value.  If they are not the number of time tics is rounded down to the nearest number of tics.  The time tic value can be changed with the exec_set_time_tic_value() call.

Example 1:  A job is set to run at 128Hz or at 0.0078125 seconds.  This is converted to 7812.5 tics using the default tic value.  The job will end up running incorrectly every 7812 tics.  To correct this we call exec_set_time_tic_value(10000000) to set the time tic value to 100ns.  With a 100ns time tic value the job will be called every 78125 tics, which is (10000000/78125) = 128Hz.

Example 2:  Job 1 is set to run at 300Hz, 0.003333 seconds.  This is converted to 3333 tics and will not run at exactly 300Hz using the default 1us time tic.  Job 2 is set to run at 100Hz. To run both jobs at their correct rates, we call exec_set_time_tic_value(3000000).  Job 1 will run every 10000 tics.  Job 2 will run every 30000 tics.

## Software Frame

The software frame sets the cycle rates of the top_of_frame and end_of_frame class jobs.  Jobs run at the software frame are used to synchronize to real-time, synchronize multiple simulations together, and inject variables values.  The scheduled loop and the freeze loop have separate software frame values.  They are read and written with the following commands.

```c
int exec_set_software_frame(double) ;
double exec_get_software_frame() ;
long long exec_get_software_frame_tics() ;

int exec_set_freeze_frame(double) ;
double exec_get_freeze_frame() ;
long long exec_get_freeze_frame_tics() ;
```

exec_set_software_frame(double) and exec_set_freeze_frame(double) both take frame values in seconds.
exec_get_software_frame() and exec_get_freeze_frame() return the frame values in seconds.
exec_get_software_frame_tics() and exec_get_freeze_frame_tics() return the frame values in number of tics.

## User Mode Control

Users may toggle the Executive mode between Freeze and Run as well as command simulation Shutdown.

### Getting the current mode

```python
# Python code
SIM_MODE trick.exec_get_mode()
```

exec_get_mode returns the current mode of the simulation.  See the SIM_MODE definition for the enumeration values.

### Commanding to Freeze

```c
// C/C++ code
#include "sim_services/Executive/include/exec_proto.h"
exec_freeze()
```

```python
# Python code
trick.freeze()
trick.freeze(<double freeze_time>)
```

Users may command freeze in model code by calling exec_freeze().  Inside the input file users may call freeze with an optional time argument.  Calling trick.freeze() without an argument will freeze the simulation when all jobs at the current time step are complete.  Using a freeze_time argument will freeze the simulation in the future.  The freeze_time argument must be greater than the current time.  The freeze_time argument is elapsed simulation seconds.

```python
# Python code
trick.exec_set_freeze_command(int on_off)
```

Calling exec_set_freeze_command() with a non-zero argument will start the simulation in freeze.  This is here to replicate a call from previous versions of Trick.  A call to trick.freeze() in the input file will accomplish the same result.  A call to trick.freeze(0.0) will not work.  This is because freeze times must be greater than the current sim time.

```python
# Python
