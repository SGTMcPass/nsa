### Trick Header Comment > Create Connections

="#e6ceff">freeze_init</td><td>Module executes only once upon entering FREEZE mode.</td></tr>
<tr bgcolor="e6ceff"><td colspan="2" align="center">BEGIN FREEZE FRAME</td></tr>
<tr bgcolor="e6ceff"><td colspan="2" align="center">BEGIN FREEZE LOOP</td></tr>
<tr><td bgcolor="#e6ceff">freeze_scheduled</td><td>Module executes cyclically during simulation FREEZE mode according to its specified cycle time.</td></tr>
<tr bgcolor="e6ceff"><td colspan="2" align="center">END FREEZE LOOP</td></tr>
<tr><td bgcolor="#e6ceff">freeze</td><td>Module runs at end of every freeze frame, after the freeze loop completes.</td></tr>
<tr bgcolor="e6ceff"><td colspan="2" align="center">END FREEZE FRAME</td></tr>
<tr><td bgcolor="#e6ceff">unfreeze</td><td>Module executes only once upon leaving FREEZE mode before returning to RUN mode.</td></tr>
<tr><td bgcolor="#ffc285">checkpoint</td><td>Module executes only once before a checkpoint is dumped.</td></tr>
<tr><td bgcolor="#ffc285">post_checkpoint</td><td>Module executes only once after a checkpoint is dumped.</td></tr>
<tr><td bgcolor="#ffc285">preload_checkpoint</td><td>Module executes only once before a checkpoint is loaded.</td></tr>
<tr><td bgcolor="#ffc285">restart</td><td>Module executes only once after a checkpoint is loaded.</td></tr>
<tr><td bgcolor="#ff8080">shutdown</td><td>Module executes only once at simulation termination to allow a
    graceful shutdown.</td></tr>
</table>
</center>

#### Job Return Type

All integration class jobs must return an integer value which represents the current integration
pass identifier. If all integration passes are complete, the job must return a zero.

All dynamic_event class jobs must return a double precision value representing the estimated time
to go to the defined event, in seconds.

All other jobs managed by the Trick executive, not integration or dynamic_event, may return any
type. If a function is declared with an integer return value, the job must return a non-negative
integer or else the executive will assume an error occurred an immediately terminate the simulation.
If the job does not return an integer, Trick will not take any action based on a return value. Note
that initialization job return values are NOT checked by the executive.

#### Job Name

This field specifies the job name of the job as defined in the job’s source code.

C function and C++ member functions can be called as a jobs. Here is a quick example of a C and C++
calls.

```C
