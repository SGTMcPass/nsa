### Introduction > Traceability to Parent Requirements

01. Trick shall provide a mode command to transition to Shutdown.

### Jobs
01. Trick shall provide a method for adding simulation objects to the scheduler prior to execution.
01. Trick shall order jobs by job_class, then phase, then sim_object id, then job_id.

### Periodic Jobs
01. Trick shall execute periodic scheduled jobs during simulation run mode (all scheduled types).
01. Trick shall execute periodic freeze jobs during simulation freeze mode (freeze).
01. Trick shall execute periodic scheduled jobs during simulation run mode at the end of a settable software_frame  (end_of_frame).
01. Trick shall assign the initial call time for a periodic job to the current simulation time + job offset.
01. Trick shall reschedule subsequent job call times for a periodic job to the current simulation time + job cycle.

### Discrete Jobs
01. Trick shall execute discrete job execution scheduling on simulation startup (default_data).
01. Trick shall execute discrete job execution scheduling during simulation initialization (initialization).
01. Trick shall execute of discrete job execution scheduling upon entering simulation freeze (freeze_init).
01. Trick shall execute of discrete job execution scheduling upon exiting simulation freeze (unfreeze).
01. Trick shall execute discrete job execution scheduling during simulation termination (shutdown).

### Instrumentation Jobs
01. Trick shall provide a method for inserting a job before each initialization and each scheduled job within a simulation.
01. Trick shall provide a method for inserting a job before a single initialization or scheduled job within a simulation.
01. Trick shall provide a method for inserting a job after each initialization and each scheduled job within a simulation.
01. Trick shall provide a method for inserting a job after a single initialization or scheduled job within a simulation.
01. Trick shall provide a method for removing instrumentation job(s).

### Threads
01. Trick shall support single threaded execution during all modes of operation.
01. Trick shall support multiple threads of execution during run mode.
01. Trick shall support child threads that synchronize execution with each time step of the parent thread (synchronous thread).
01. Trick shall support child threads that does not synchronize execution with the parent thread. Thread jobs are restarted at next available time step from the master thread.  (asynchronous thread)
01. Trick shall support child threads that does synchronizes execution with the parent thread at a specified interval. This interval may be greater than a time step in the parent thread (asynchronous must finish (AMF) thread).
01. Trick shall spawn enough threads to accomodate jobs listed within the S_define file.
01. Trick shall provide inter-thread job dependencies. This ensures pre-requesite jobs are completed before current job execution.
01. Trick shall terminate simulation execution if a child thread exits.

### Signals
01. Trick shall assign signal handlers to attempt a graceful shutdown of the simulation when the following signals occur: SIGINT, SIGTERM, SIGBUS, SIGSEGV, SIGFPE.
01. Trick shall assign signal handlers to handle the SIGCHLD signal.
01. Trick shall attempt to terminate the simulation gracefully when a SIGTERM, SIGBUS, or SIGSEGV signal is caught. Program corruption at this point may be too great to complete this requirement, hence "attempt".
01. Trick shall allow the user to assign the system default signal handlers for the signals SIGBUS, SIGSEGV, or SIGFPE signals.

## Realtime Clock Requirements
01. Trick shall provide a framework to use a real-time clock source.
01. The framework shall provide a base real-time clock class that provides an interface to initialize the clock.
01. The framework shall provide a base real-time clock class that provides an interface to return the current time.
01. The framework shall provide a base real-time clock class that provides an interface to reset the clock.
01. The framework shall provide a base real-time clock class that provides an interface to wait/spin on the clock to reach a requested time.
01. The framework shall provide a base real-time clock class that provides an interface to stop the clock.
01. Trick shall provide a real-time clock based on the system gettimeofday clock (GetTimeofDay Clock).

## Realtime Synchronization Requirements
01. Trick shall be capable of synchronizing simulation time to a real-time clock.
01. Trick shall be capable of running non-real-time.
01. Trick shall provide the capability to switch between real-time and non-real-time execution.
01. Trick shall detect when the current simulation job execution frame takes longer than the real-time frame (overrun).
01. Trick shall provide the option to respond to simulation overruns by continuing to next frame of execution.
01. Trick shall provide the option to respond to simulation overruns by freezing.
01. Trick shall provide the option to respond to simulation overruns by terminating.
01. The overrun criteria to cause a response shall be either a single large overrun of a user specified size (in seconds), or a user specified number of overruns is
