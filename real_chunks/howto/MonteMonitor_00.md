### Monte Monitor > Launching > Starting and Stopping

| [Home](/trick) → [Documentation Home](../../Documentation-Home) → [Running a Simulation](../Running-a-Simulation) → [Runtime GUIs](Runtime-GUIs) → Monte Monitor |
|------------------------------------------------------------------|

## Monte Monitor

Monte Monitor (hereafter referred to as MM) is a graphical user interface that allows users to view and modify the states
of slaves in a Monte Carlo simulation.

### Launching

MM can be launched from the command line via:

'''
${TRICK_HOME}/bin/mm [options]
'''

Pass <code>--help</code> for a description of available options. For additional launching options, see
"Automatically Launching Applications".

### The GUI

The GUI pictured below may have a different look and feel based on the architecture of the machine on which it is running,
but the functionality will remain the same.

![Monte Monitor](images/MonteMonitor.jpg)

#### Progress Bar

The progress bar displays a visual and textual representation of how far the Monte Carlo has progressed. The format is
<code>\<resolved runs\> / \<total runs\> (\<percent resolved\>)</code>.

#### Slave Table

The slave table displays information on each of the slaves. From left to right, this information is:

<ul><li><b>ID</b><br>
  The unique ID of the slave.

<li><b>Status</b><br>
  The current status of the slave. It can be one of:

  <ul><li><b>Unitialized</b><br>
    The slave has yet to be spawned.

  <li><b>Initializing</b><br>
    The slave has been spawned, and the master is waiting for initialization information from it. Once initialized, the
    slave will be in the <code>Ready</code> state. Since Monte Carlo cannot determine if slaves spawn correctly, slaves
    that fail to spawn will remain in this state for the duration of the Monte Carlo.

  <li><b>Ready</b><br>
    The slave is awaiting a dispatch.

  <li><b>Running</b><br>
    The slave is processing a run. Once completed, the slave will be in the <code>Ready</code> state.

  <li><b>Stopping</b><br>
    The slave is processing a run. Once completed, the slave will be in the <code>Stopped</code> state.

  <li><b>Stopped</b><br>
    The slave is not accepting dispatches.
  <li><b>Finished</b><br>
    No runs remain to dispatch to the slave.

  <li><b>Unresponsive - Running</b><br>
    The slave has timed out and is also in the <code>Running</code> state.

  <li><b>Unresponsive - Stopping</b><br>
    The slave
