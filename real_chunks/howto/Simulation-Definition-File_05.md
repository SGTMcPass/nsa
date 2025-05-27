### Trick Header Comment > Create Connections

 spec because they run only once.
- FRAME-BOUNDARY (blue color) are tied to each execution frame and not a cycle time.
- INTEGRATOR (cyan color) are specified via the state integration specifications for the simulation (see Section 4.4.7).ME-BOUNDARY (blue color) are tied to each execution frame and not a cycle time.
- INTEGRATOR (cyan color) are specified via the state integration specifications for the simulation (see Section 4.4.7).
- SELF-SCHEDULING (yellow color) are responsible for scheduling themselves.
- FREEZE (purple color) are tied to the freeze frame (EXCEPT for freeze_scheduled class jobs which DO need the spec.)
- CHECKPOINT (orange color) are tied to checkpointing and run only once.

#### Job Class
The job class determines where in the simulation a job is run.  Each job in the S_define file
requires a job class.

<center>
<b>KEY: Job Class Category Colors used in Table SD_1</b>
<table>
<tr bgcolor="#c0c0c0"><th>Category Color</th><th>The job classes in Table SD_1 are categorized as one of the following:</th></tr>
<tr><td bgcolor="#ff8080">NON-CYCLIC</td><td>jobs that run once either at simulation startup or termination</td></tr>
<tr><td bgcolor="#add8e6">FRAME-BOUNDARY</td><td>jobs that run cyclically before/after the scheduled job loop</td></tr>
<tr><td bgcolor="#ccffff">INTEGRATOR</td><td>jobs that run first in the scheduled job loop for Trick state integration</td></tr>
<tr><td bgcolor="#ffff99">SELF-SCHEDULING</td><td>jobs in the scheduled job loop that must schedule themselves when to run</td></tr>
<tr><td bgcolor="#ccffcc">CYCLIC</td><td>jobs in the scheduled job loop that run cyclically according to their specified cycle time</td></tr>
<tr><td bgcolor="#e6ceff">FREEZE</td><td>jobs that are run during the freeze execution mode</td></tr>
<tr><td bgcolor="#ffc285">CHECKPOINT</td><td>jobs that are run when a checkpoint is dumpded or loaded</td></tr>
</table>

<b>Table SD_1 Trick-Provided Job Classes</b>
<table>
<tr bgcolor="#c0c0c0"><th>Job Class Name</th><th>Description</th></tr>
<tr><td bgcolor="#ff8080">default_data</td><td>Module executes only once at simulation time = zero.
    Called before input file is read.</td></tr>
<tr><td bgcolor="#ff8080">initialization</td><td>Module executes only once
