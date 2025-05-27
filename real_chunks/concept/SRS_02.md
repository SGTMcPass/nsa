### Introduction > Traceability to Parent Requirements

 synchronizing simulation time to a real-time clock.
01. Trick shall be capable of running non-real-time.
01. Trick shall provide the capability to switch between real-time and non-real-time execution.
01. Trick shall detect when the current simulation job execution frame takes longer than the real-time frame (overrun).
01. Trick shall provide the option to respond to simulation overruns by continuing to next frame of execution.
01. Trick shall provide the option to respond to simulation overruns by freezing.
01. Trick shall provide the option to respond to simulation overruns by terminating.
01. The overrun criteria to cause a response shall be either a single large overrun of a user specified size (in seconds), or a user specified number of overruns is detected.
01. Trick shall detect when the current simulation job execution frame is equal to or shorter than the real-time frame (underrun).
01. Trick shall wait for real-time to catch up to the simulation time before starting the next frame of execution during an underrun.
01. Trick shall provide the option to release the processor (sleep) during an underrun.

## Safety Requirements
There are no safety requirements for this software.  Any simulations that use trick functions to control hazards are responsible for maintaining their safety requirements.

## Scheduled Job Queue Requirements.
The ScheduledJobQueue is a helper object to the Scheduler. This object keeps an ordered queue of the jobs for a particular job class. The Scheduler adds and removes jobs from the queue. The Scheduler asks for the top job of the queue, or the next job that has an execution time that matches the current simulation time. Finally, the Scheduler asks the ScheduledJobQueue to insert an instrumentation job where the job is attached before or after a specific job in the queue, or attached before or after all jobs in the simulation.

### Jobs
01. Trick shall store an ordered queue of jobs of the same scheduling class.  The order shall be based on job class, phase number, sim_object order, and finally order of jobs within the simulation object.
01. Trick shall provide a method to add simulation objects to the queue.
01. Trick shall provide a method to add simulation objects to the queue that ignores the sim_object and job order.
01. Trick shall provide a method to clear the job queue.
01. Trick shall provide a method to get the next job on the list.
01. Trick shall provide a method to search for the next job on the list whose next job call time matches the current simulation time.
01. Trick shall provide a method to reset the search index to the top of the list.

### Job Call Time
01. Trick shall track the lowest next job call time greater than the current call time.
01. Trick shall provide a method to retrieve the next job call time.

### Instrumentation Jobs
01. Trick shall provide a method to insert a job before each job in the queue.
01. Trick shall provide a method to insert a job before a single job in the queue.
01. Trick shall provide a method to insert a job after each job in the queue.
01. Trick shall provide a method to insert a job after a single job in the queue.

## Sleep Timer Requirements
01. Trick shall provide a framework to use a sleep timer.
01. The framework shall provide a base timer class that provides an interface to initialize the timer.
01. The framework shall provide a base timer class that provides an interface to start the timer.
01. The framework shall provide a base timer class that provides an interface to reset the timer.
01. The framework shall provide a base timer class that provides an interface to wait on the timer to expire.
01. The framework shall provide a base timer class that provides an interface to stop the timer.
01. The framework shall provide a base timer class that provides an interface to shutdown the timer.
01. Trick shall provide a sleep timer based on the system itimer (ITimer timer).

## Traceability to Parent Requirements
01. There are no formal parent requirements that flow into this SRS.
