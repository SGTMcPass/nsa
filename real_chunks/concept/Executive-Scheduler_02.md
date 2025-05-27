### Executive Flow > Debugging Help > Getting Build Information

 at the current time step are complete.  Using a freeze_time argument will freeze the simulation in the future.  The freeze_time argument must be greater than the current time.  The freeze_time argument is elapsed simulation seconds.

```python
# Python code
trick.exec_set_freeze_command(int on_off)
```

Calling exec_set_freeze_command() with a non-zero argument will start the simulation in freeze.  This is here to replicate a call from previous versions of Trick.  A call to trick.freeze() in the input file will accomplish the same result.  A call to trick.freeze(0.0) will not work.  This is because freeze times must be greater than the current sim time.

```python
# Python code
trick.exec_set_freeze_on_frame_boundary(int on_off)
```

Calling exec_set_freeze_on_frame_boundary() with a non-zero argument will force all freezes to synchronize with the software frame.  Freeze commands received in the middle of the frame will be saved and executed at the next available frame boundary.

```python
# Python code
trick.exec_set_enable_freeze( int on_off )
int trick.exec_get_enable_freeze() ;
```

Calling exec_set_enable_freeze() with a non-zero argument will enable the CTRL-C keyboard interrupt signal to freeze/unfreeze the simulation.  The default is off.  When enable_freeze is off, a CTRL-C keystroke will terminate the simulation.

### Commanding to Run

```python
exec_run()
```

exec_run() is called when the Run button on an attached sim_control panel is pressed.  It is rare that a user job calls exec_run.

### Commanding to Shutdown

```python
# Python code
trick.exec_set_terminate_time(double time_value)
double trick.exec_get_terminate_time() ;
```

The most common way to shutdown a simulation is setting a terminate time.  When simulation elapsed time reaches the terminate time, the shutdown jobs are executed and the program terminates.

```c
exec_terminate(const char *file_name, const char *error)
exec_terminate_with_return(int ret_code, const char *file_name, int line, const char *error)
```

Users may terminate simulation execution at any time by calling one of the exec_terminate varieties.  Both versions set the the Executive mode to shutdown.  The exec_terminate routine The exec_terminate_with_return allows users to set the simulation exit code as well as include a line number in the error message.

## Job Control

The executive provides routines to control job execution.

### Turning Jobs On/Off

```python
# Python code
trick.exec_set_job_onoff(char * job_name , int instance_num , int on) ;
```

The exec_set_job_onoff() routine allows users to turn individual jobs on and off.  The job name is the concatenation of the sim_object name and the job name.  The instance_num argument is used when jobs have the same name.  Jobs with unique names are always instance_num 1.  Jobs with identical names start at instance_num 1 and increment for each job as they appear in the sim object.

If there is a job tag specified for one of more jobs in the S_define file, you can turn all jobs with that tag on/off by specifying the tag as the job_name argument.

```python
# Python code
trick.exec_set_sim_object_onoff(char * sim_object_name , int on) ;
```

The exec_set_sim_object_onoff routine allows users to turn individual whole sim_objects on and off. If individiual jobs were disabled before the sim object is disabled, they will retain their disabled status when the sim object is turned back on.

```
# Python code
trick.exec_get_sim_object_onoff(char * sim_object_name) ;
```

The exec_get_sim_object_onoff routine allows users to determine if the sim_object is currently on or off.


```
# Python code
trick.exec_set_sim_object_jobs_onoff(char * sim_object_name , int on) ;
```

The exec_set_sim_object_jobs_onoff allows users to turn all of the jobs in a sim_object on or off, but does not change the overall sim object's disabled status.


### Job Cycle Time

```python
# Python code
trick.exec_set_job_cycle(char * job_name, int instance_num, double in_cycle)
double trick.exec_get_job_cycle(char * job_name)
```

Each job cycle time is available to read and to set.  Some job classes ignore cycle times, i.e. initialization and shutdown.  The user may change the cycle time set in the S_define file with the exec_set_job_cycle() call.  The instance_num argument is used when jobs have the same name (see exec_set_job_onoff above).

If there is a job tag specified for one of more jobs in the S
