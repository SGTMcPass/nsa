### Format of Recording Groups > DRHDF5 Recording Format > Interaction with Checkpoints

 disk during
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

## Recording Frequency: Always or Only When Data Changes

Data recording groups have three recording frequency options:

- DR_Always - the group will record the variable value(s) at every recording cycle. (This is the default).
- DR_Changes - the group will record the variable value(s) only when a particular watched parameter (or parameters) value changes.
- DR_Changes_Step - like DR_Changes, except that a before and after value will be recorded for each variable,
creating a stair step effect (instead of point-to-point) when plotted.

To set the recording frequency call the <tt>set_freq(trick.<frequency_option>)</tt> method of the recording group. For example:

```python
drg.set_freq(trick.DR_Changes)
```

For DR_Changes or DR_Changes_Step, to specify parameter(s) to watch that will control when the variables added with <tt>add_variable</tt> are recorded,
call the <tt>add_change_variable(string)</tt> method of the recording group. For example:

```python
drg.add_change_variable("ball.obj.state.output.velocity[0]")
```

So if we assume the <tt>add_variable</tt> statements from the example in @ref S_7_8_3 "7.8.3" combined with the above <tt>add_change_variable</tt> statement,
then <tt>ball.obj.state.output.position[0]</tt> and <tt>ball.obj.state.output.position[1]</tt> will be recorded only when
<tt>ball.obj.state.output.velocity[0]</tt> changes. Multiple parameters may be watched by adding more change variables, in which case
data will be recorded when any of the watched variable values change.

## Turn Off/On and Record Individual Recording Groups

At any time during the simulation, model code or the input processor can turn on/off individual
recording groups as well as record a single point of data.

```c++
/* C code */
dr_enable_group("<group_name>") ;
dr_disable_group("<group_name>") ;
dr_record_now_group("<group_name>") ;
```

This is the Python input file version:

```python
# Python code
trick.dr_enable_group("<group_name>") ;  # same as <group_name>.enable()
trick.dr_disable_group("<group_name>") ; # same as <group_name>.disable()
trick.dr_record_now_group("<group_name>") ;
```

## Changing the thread Data Recording runs on.

To change the thread that the data recording group runs on use the DataRecordGroup::set_thread
method.  The thread number follows the same numbering as the child threads in the S_define file.
This must be done before the add_data_record_group function is called.  Trick does not
provide data locks for data record groups.  It is up to the user to ensure that the data
recorded on *any* thread (including the master) is ready in order for data recording to
record a time homogeneous set of data.

```python
drg.set_thread(<thread_number>)
```

## Changing the Job Class of a Data Record Group

The default job class of a data record group is "data_record".  This job class is run after all
of the cyclic job classes have completed.  The job class of the data record group can be
changed through the set_job_class method.  The data recording job will be added to the end of
the job class queue it is set.

```python
drg.set_job_class(<string class_name>)
```


## Changing the Max File Size of a Data Record Group (Ascii and Binary only)

The default size of a data record is 1 GiB. A new size can be set through the set_max_file_size method. For unlimited size, pass 0.

```python
drg.set_max_file_size(<uint64 file_size_in_bytes>)
```

## Example Data Recording Group

This is an example of a data recording group in the input file

```python
# Data recording HDF5 test
drg0 = trick.DRHDF5("Ball")
drg0.add_variable("
