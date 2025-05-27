### Introduction > Traceability to Parent Requirements

| [Home](/trick/index) → [Documentation Home](../Documentation-Home) → Software Requirements Specification |
|-------------------------------------------------------------------------------------------------|

# Introduction
The Software Requirements Specification defines the functional, performance, and interface requirements for Trick.

## Adaptation Requirements
01. Trick source code shall use a POSIX compliant API when accessing POSIX threads (pthreads), mutual exclusions (mutexes), signals, interrupts, and clock routines. [Trick-151]

## Applicable and Reference Documents
### Applicable Documents
The following documents are reference documents utilized in the development of this SRS. These documents do not form a part of this SRS and are not controlled by their reference herein.

<center>
    <table>
    <tr><th>Document Number</th><th>Revision/ Release Date</th><th>Document Title</th></tr>
    <tr><td></td><td></td><td></td></tr>
    </table>
</center>

### Reference Documents
The following documents are reference documents utilized in the development of this SRS. These documents do not form a part of this SRS and are not controlled by their reference herein.

<center>
    <table>
    <tr><th>Document Number</th><th>Revision/ Release Date</th><th>Document Title</th></tr>
    <tr><td></td><td></td><td></td></tr>
    </table>
</center>

### Order of Precedence
In the event of a conflict between the text of this specification and an applicable document cited herein, the text of this specification takes precedence.

All specifications, standards, exhibits, drawings or other documents that are invoked as "applicable" in this specification are incorporated as cited.  All documents that are referred to by an applicable document are considered to be for guidance and information only, with the exception of Interface Control Documents (ICD) which will have their applicable documents considered to be incorporated as cited.

## Command Line Arguments Requirements
01. Trick shall save the number of command line arguments.
01. Trick shall save all command line arguments.
01. Trick shall determine and save the current directory of the simulation executable.
01. Trick shall determine and save the current name of the simulation executable.
01. Trick shall determine and save the current directory of the run input file.
01. Trick shall use the run input directory as the default output directory.
01. Trick shall allow the user to override the output directory.
01. Trick shall provide the option to create timestamped subdirectories within the output directory.

## Data Recording Requirements
01. Data Recording shall provide the capability to record one or more variables that a user has specified in a log group.
01. Data Recording shall provide the capability to record multiple log groups.
01. Data Recording shall time tag the recorded data with the simulation time.
01. Data Recording shall provide the capability to record each log group at its own user specified frequency
01. Data Recording shall provide the capability to record each log group only when user specified model data changes.
01. Data Recording shall provide the capability to write data to disk without affecting the real-time performance of the simulation.

## Design and Implementation Constraints
01. Trick shall not preclude that which cannot be precluded unless Trick is precluded from not precluding the unprecludable.

## Environment Requirements
01. Trick shall plant a tree for every successful simulation built.
01. Trick shall be dolphin safe.
01. Trick shall recycle.

## Scheduler Requirements
### Simulation Time
01. Trick shall track simulation elapsed time by an integer count of tics/second
01. Trick shall initialize simulation elapsed time after all initialization class jobs have completed.
01. Trick shall increment simulation elapsed time to the next lowest job call time greater than the current simulation time after all jobs at the current simulation time have completed.

### Modes
01. Trick shall provide an initialization mode.
01. Trick shall provide a run mode.
01. Trick shall provide a freeze mode.
01. Trick shall provide an exit mode.
01. Trick shall provide a mode command to transition to Freeze.
01. Trick shall provide a mode command to transition to Run.
01. Trick shall provide a mode command to transition to Shutdown.

### Jobs
01. Trick shall provide a method for adding simulation objects to the scheduler prior to execution.
01. Trick shall order jobs by job_class, then phase, then sim_object id, then job_id.

### Periodic Jobs
01. Trick shall execute periodic scheduled jobs during simulation run mode (all scheduled types).
01. Trick shall execute periodic freeze jobs during simulation freeze mode (freeze).
01. Trick shall execute periodic scheduled jobs during simulation run mode at the end of a settable software_frame  (end_of_frame).
01. Trick shall assign the initial call time for a periodic job to the current simulation time + job offset.
01. Trick shall reschedule subsequent job
