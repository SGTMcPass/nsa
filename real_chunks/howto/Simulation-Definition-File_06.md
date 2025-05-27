### Trick Header Comment > Create Connections

 Job Classes</b>
<table>
<tr bgcolor="#c0c0c0"><th>Job Class Name</th><th>Description</th></tr>
<tr><td bgcolor="#ff8080">default_data</td><td>Module executes only once at simulation time = zero.
    Called before input file is read.</td></tr>
<tr><td bgcolor="#ff8080">initialization</td><td>Module executes only once at simulation time = zero.
    Called after input file is read.</td></tr>
<tr bgcolor="add8e6"><td colspan="2" align="center">BEGIN EXECUTION FRAME</td></tr>
<tr><td bgcolor="add8e6">top_of_frame</td><td>Module runs at the beginning of every execution frame, before the scheduled job loop,
    even before any child threads are started for the frame.</td></tr>
<tr bgcolor="ccffcc"><td colspan="2" align="center">BEGIN SCHEDULED JOB LOOP</td></tr>
<tr><td bgcolor="#ccffff">pre_integration</td><td>Runs only once before the integration loop.
    For example, in the case of a Runge Kutta 4, the derivative and integration jobs will be called
    four times during the integration steps.  A pre_integration job will execute a
    single time before this four step integration process has occurred.</td></tr>
<tr bgcolor="ccffff"><td colspan="2" align="center">BEGIN INTEGRATION LOOP</td></tr>
<tr><td bgcolor="#ccffff">derivative</td><td>Equations of motion (EOM) derivative function.</td></tr>
<tr><td bgcolor="#ccffff">integration</td><td>Equations of motion state integration function.</td></tr>
<tr bgcolor="ccffff"><td colspan="2" align="center">END INTEGRATION LOOP</td></tr>
<tr><td bgcolor="#ccffff">post_integration</td><td>Runs only once after the integration loop.</td></tr>
<tr><td bgcolor="#ccffff">dynamic_event</td><td>Runs after the integration loop
    (after any post_integration jobs). Provides a continuous time dependent equation whose root
    defines a discontinuous event in the system EOM, evaluation of function returns an
    estimated delta time to reach the root.</td></tr>
<tr><td bgcolor="ffff99">automatic</td><td>Module which reschedules its own next call time, and will run before other CYCLIC jobs in the frame.</td></tr>
<tr><td bgcolor="#ccffcc">environment</td><td>Time dependent boundary conditions (mother nature).</td></tr>
<tr><td bgcolor="#ccffcc">sensor</td><td> Simulated interface between dynamics and control simulation components.</td></tr>
<tr><td bgcolor="#ccffcc">
