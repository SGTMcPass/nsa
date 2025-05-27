### Executive Flow > Debugging Help > Getting Build Information

iously spins waiting for them to finish.  Calling exec_set_rt_nap() with a non-zero argument will tell the main thread to momentarily give up the CPU if it needs to wait for child threads to finish.

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

exec_set_thread_priority() will set the thread's priority.  The main thread is thread_id=0, 1-n are the child threads. for req_priority, 1 is the highest priority.  This number is converted internally to the highest priority of the system automatically.

Setting a simulation to run as priority 1 may lock out keyboard and mouse processing.

```python
# Python code
trick.exec_set_thread_cpu_affinity(unsigned int thread_id , int cpu_num) ;
```

exec_set_thread_cpu_affinity assigns a thread to a specific CPU. If called multiple times, you can add multiple CPUs to a thread and the OS scheduler will choose one of those CPUs for the thread. The main thread is thread_id=0. 1-n are the child threads.  Setting a thread to run on a CPU does not exclude other processes to continue to run on the same CPU.

### Thread Priorities

```python
# Python code
trick.exec_set_lock_memory(int yes_no) ;
```

Lock all of the process memory for best real-time performance.  This prevents process memory to be swapped out to virtual memory on disk. This option may move to the Trick::RealtimeSync class in the future.

### Thread Job Dependencies

```python
# Python code
trick.exec_add_depends_on_job(char * target_job_string , unsigned int t_instance ,
                              char * depend_job_string , unsigned int d_instance )
```

Jobs in different threads may need other jobs in other threads to run first before executing.  Trick provides a depends_on feature.  Jobs that depend on other jobs will not execute until all dependencies have finished.  The instance value in the above call to take care of the case where the same job name is called multiple times in a sim_object.  Instance values start at 1.

### Getting Thread ID

```c
unsigned int exec_get_process_id() ;
unsigned int exec_get_num_threads() ;
```

exec_get_process_id() will return the current thread the caller is on.  0 = main thread, 1-n are the child threads.  If this call is issued through a variable server client, or a thread that was not spawned by the executive, a -1 error code is returned.

exec_get_num_threads() returns the number of child threads spawned by the main thread.

## Debugging Help

The Executive provides several parameters that can help a model developer debug a simulation.

### Trapping signals

```python
# Python code
trick.exec_set_trap_sigbus(int on_off)
trick.exec_set_trap_sigfpe(int on_off)
trick.exec_set_trap_sigsegv(int on_off)
trick.exec_set_trap_sigchld(int on_off)
trick.exec_get_trap_sigbus()
trick.exec_get_trap_sigfpe()
trick.exec_get_trap_sigsegv()
trick.exec_get_trap_sigchld()
```

The set_trap routines listed above set a signal handler for the SIGBUS, SIGFPE, SIGSEGV, and SIGCHLD signals respectively.  The get_trap routines return the on/off status of the trap.  Trapping the signals allows the Trick to gracefully shutdown the simulation and to possibly write important information about the signal before exiting execution.  Turning off the traps will revert signal handling to the default system signal handler.  By default the traps for SIGBUS, SIGSEGV, and SIGCHLD are true.  SIGFPE is not trapped by default.

### Printing a Stack (Call) Trace on Signal

```python
# Python code
trick.exec_set_stack_trace(int on_off)
```

This is a Linux only option.  By default, printing a stack trace when a signal is trapped is enabled.  When a signal is trapped a debugger is automatically connected to the running simulation and a printout of the calling stack is printed before the simulation exits.

### Attaching a debugger on Signal

```python
# Python code
trick.exec_set_attach_debugger(int on_off)
```

This is a Linux only option.  By default, this option is off.  If enabled, when a signal is trapped a debugger is automatically connected to the running simulation and
