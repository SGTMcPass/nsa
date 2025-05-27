### Format of Recording Groups > DRHDF5 Recording Format > Interaction with Checkpoints

| [Home](/trick) → [Documentation Home](../Documentation-Home) → [Simulation Capabilities](Simulation-Capabilities) → Data Record |
|------------------------------------------------------------------|

Data Recording provides the capability to specify any number of data recording groups,
each with an unlimited number of parameter references, and with each group recording
at different frequencies to different files in different formats.

All data is written to the simulation output directory.

## Format of Recording Groups

Trick allows recording in three different formats. Each recording group is readable by
different external tools outside of Trick.

- DRAscii - Human readable and compatible with Excel.
- DRBinary - Readable by previous Trick data products.
- DRHDF5 - Readable by Matlab.

DRHDF5 recording support is off by default.  To enable DRHDF5 support Trick must be built with HDF5 support.
Go to http://www.hdf5group.org and download the latest pre-built hdf5 package for your system. Source packages are
available as well.  We recommend getting the static library packages above the shared.  Static packages make
your executable larger, but you will not have to deal with LD_LIBRARY issues.  The HDF5 package may be installed
anywhere on your system.  To tell Trick you have HDF5 run ${TRICK_HOME}/configure --with-hdf5=/path/to/hdf5.
Re-compile Trick to enable HDF5 support.

## Creating a New Recording Group

To create a new recording group, in the Python input file instantiate a new group by format name:
<tt><variable_name> = trick.<data_record_format>() ;</tt>

For example:

```
drg = trick.DRBinary() ;
```

Note: drg is just an example name.  Any name may be used.

## Adding a Variable To Be Recorded

To add variables to the recording group call the <tt>drg.add_variable("<string_of_variable_name>")</tt> method of the recording group.
For example:

```python
drg.add_variable("ball.obj.state.output.position[0]")
drg.add_variable("ball.obj.state.output.position[1]")
```
In this example `position` is an array of floating point numbers. **DO NOT ATTEMPT TO DATA RECORD C OR C++ STRINGS. THIS HAS BEEN OBSERVED TO CREATE MEMORY ISSUES AND TRICK DOES NOT CURRENTLY PROVIDE ERROR CHECKING FOR THIS UNSUPPORTED USE CASE**

An optional alias may also be specified in the method as <tt>drg.add_variable("<string_of_variable_name>" [, "<alias>"])</tt>.
If an alias is present as a second argument, the alias name will be used in the data recording file instead of the actual variable name.
For example:

```python
drg.add_variable("ball.obj.state.output.position[0]", "x_pos")
drg.add_variable("ball.obj.state.output.position[1]", "y_pos")
```

Only individual primitive types can be recorded. Arrays, strings/char *, structured objects, or STL types are not supported.

## Changing the Recording Rate

To change the recording rate call the <tt>set_cycle()</tt> method of the recording group.

```python
drg.set_cycle(0.01)
```

## Buffering Techniques

Data recording groups have three buffering options:

- DR_Buffer - the group will save recorded data to a buffer and use a separate thread to write recorded
data to disk.  This will have little impact to the performance of the simulation.  The downside
is that if the simulation crashes, the most recent recorded points may not be written to disk in time.
DR_Buffer is the default buffering technique. (For backwards compatibility, DR_Buffer can also be called DR_Thread_Buffer).
- DR_No_Buffer - the group will write recorded data straight to disk.  All data is guaranteed to be written
to disk at simulation termination time.  The downside of this method is that it is performed in
the main thread of the simulation and could impact real-time performance.
- DR_Ring_Buffer - the group will save a set number of records in memory and write this data to disk during
a graceful simulation termination.  The advantage of this method is that there is only a set, usually
small, number of records written.  The downside of this method is that if the simulation terminates
ungracefully, all recorded data may be lost.

To set the buffering technique call the <tt>set_buffer_type(trick.<buffering_option>)</tt> method of the recording group.
For example:

```python
drg.set_buffer_type(trick.DR_Buffer)
```

All buffering options (except for DR_No_Buffer) have a maximum amount of memory allocated to
holding data.  See Trick::DataRecordGroup::set_max_buffer_size for buffer size information.

## Recording Frequency: Always or
