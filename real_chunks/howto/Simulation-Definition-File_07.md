### Trick Header Comment > Create Connections

 reschedules its own next call time, and will run before other CYCLIC jobs in the frame.</td></tr>
<tr><td bgcolor="#ccffcc">environment</td><td>Time dependent boundary conditions (mother nature).</td></tr>
<tr><td bgcolor="#ccffcc">sensor</td><td> Simulated interface between dynamics and control simulation components.</td></tr>
<tr><td bgcolor="#ccffcc">sensor_emitter</td><td>Same as sensor, but for the emitter portion of an integrated
    multi-component sensor system.</td></tr>
<tr><td bgcolor="#ccffcc">sensor_reflector</td><td>Same as sensor, but for the reflector portion of an
    integrated multi-component sensor system.</td></tr>
<tr><td bgcolor="#ccffcc">sensor_receiver</td><td>Same as sensor, but for the receiver portion of an
    integrated multi-component sensor system.</td></tr>
<tr><td bgcolor="#ccffcc">scheduled</td><td>Typical flight software and hardware subsystems.</td></tr>
<tr><td bgcolor="#ccffcc">effector</td><td>Simulated interface between control and force generator
    simulation components.</td></tr>
<tr><td bgcolor="#ccffcc">effector_emitter</td><td>Same as effector, but for the action portion of an
    action-reaction effector system.</td></tr>
<tr><td bgcolor="#ccffcc">effector_receiver</td><td>Same as effector, but for the reaction portion of an
    action-reaction effector system.</td></tr>
<tr><td bgcolor="#ccffcc">logging</td><td>Simulation data recording or displaying.</td></tr>
<tr><td bgcolor="#ffff99">automatic_last</td><td>Module which reschedules its own next call time, and will run after other CYCLIC jobs in the frame.</td></tr>
<tr bgcolor="ccffcc"><td colspan="2" align="center">END SCHEDULED JOB LOOP</td></tr>
<tr><td bgcolor="add8e6">end_of_frame</td><td>Module runs at the end of every execution frame, after the scheduled job loop completes.</td></tr>
<tr bgcolor="add8e6"><td colspan="2" align="center">END EXECUTION FRAME</td></tr>
<tr><td bgcolor="#e6ceff">freeze_init</td><td>Module executes only once upon entering FREEZE mode.</td></tr>
<tr bgcolor="e6ceff"><td colspan="2" align="center">BEGIN FREEZE FRAME</td></tr>
<tr bgcolor="e6ceff"><td colspan="2" align="center">BEGIN FREEZE LOOP</td></tr>
<tr><td bgcolor="#e6ceff">freeze
