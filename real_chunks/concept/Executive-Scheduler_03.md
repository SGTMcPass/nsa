### Executive Flow > Debugging Help > Getting Build Information

 a sim_object on or off, but does not change the overall sim object's disabled status.


### Job Cycle Time

```python
# Python code
trick.exec_set_job_cycle(char * job_name, int instance_num, double in_cycle)
double trick.exec_get_job_cycle(char * job_name)
```

Each job cycle time is available to read and to set.  Some job classes ignore cycle times, i.e. initialization and shutdown.  The user may change the cycle time set in the S_define file with the exec_set_job_cycle() call.  The instance_num argument is used when jobs have the same name (see exec_set_job_onoff above).

If there is a job tag specified for one of more jobs in the S_define file, you can set the cycle for all jobs with that tag by specifying the tag as the job_name argument.

## Thread Control

Jobs may be assigned to specific threads.  See the Simulation Definition File -> Child Thread Specification section for information about assigning jobs to threads.

Trick provides 3 types of threads.  Each thread type synchronizes to the main threads differently.  Setting the thread process type determines how the executive synchronizes child threads to run.

```python
# Python code
trick.exec_set_thread_process_type( unsigned int thread_id , int process_type )
```

Sets the synchronization type of a child thread. There are three synchronization types, PROCESS_TYPE_SCHEDULED, PROCESS_TYPE_ASYNC_CHILD, and PROCESS_TYPE_AMF_CHILD.  See the Trick::ProcessType.

### PROCESS_TYPE_SCHEDULED Threads

Jobs in scheduled threads run in step with the main thread.  The main thread will wait for jobs in scheduled threads to finish before advancing to the simulation time step.  Scheduled thread simulation time always matches the main thread.

### PROCESS_TYPE_ASYNC_CHILD Threads

Asynchronous threads have 2 modes of operation depending on if a synchronization time is specified. A cycle synchronization time is set through the exec_set_thread_async_cycle_time call.

```python
# Python code
trick.exec_set_thread_async_cycle_time( unsigned int thread_id , double cycle_time ) ;
```

If the synchronization cycle time is set to zero, then the asynchronous threads do not synchronize to the main thread.  Asynchronous jobs are often infinite loops.  If all jobs in an asynchronous thread finish, the thread is immediately restarted.  Execution frequencies for jobs in asynchronous threads are ignored.  All jobs are run each time an asynchronous thread is executed.  Asynchronous thread simulation time is set to the thread start time and is not updated while the thread is executing.

If the synchronization cycle time is non zero, then the asynchronous thread attempts to synchronize to the main thread.  At the end of the synchronization cycle if the asynchronous thread has completed, then it will be triggered to run its next frame of jobs.  If the asynchronous thread has not completed, then it will not be triggered to run the next frame of jobs.  This condition is not considered an overrun and is not logged as one.  The non completed thread will be checked at the next synchronization cycle time for completion.  Between synchronization times, async threads maintain their own simulation time.  The simulation time on the thread may not match the main thread.

### PROCESS_TYPE_AMF_CHILD Threads

AMF stands for Asynchronous Must Finish.  Threads of this type synchronize to the main thread at regular intervals set by exec_set_thread_amf_cycle_time().  Between synchronizations, AMF threads maintain their own simulation time.  Jobs in AMF threads are run as fast as possible.  The AMF thread simulation time may not match the main thread

When using an AMF thread the executive needs to know how often to synchronize with the child thread.

```python
# Python code
trick.exec_set_thread_amf_cycle_time( unsigned int thread_id , double cycle_time ) ;
```

exec_set_thread_amf_cycle_time sets the synchronization cycle rate with the main thread.

### Main Thread CPU release.

```python
# Python code
trick.exec_set_rt_nap(int on_off)
trick.exec_get_rt_nap()
```

While the main thread is waiting for child threads to finish execution, it furiously spins waiting for them to finish.  Calling exec_set_rt_nap() with a non-zero argument will tell the main thread to momentarily give up the CPU if it needs to wait for child threads to finish.

### Asynchronous Threads at Shutdown

```python
# Python code
trick.exec_set_thread_async_wait( unsigned int thread_id , int yes_no ) ;
```

By default the executive does not wait for asynchronous or AMF threads during shutdown.  Calling exec_set_thread_async_wait() will tell the executive to wait for a thread before calling shutdown routines and exiting.

### Thread Priorities

```python
# Python code
trick.exec_set_thread_priority(unsigned int thread_id , unsigned int req_priority)
```

exec_set_thread
