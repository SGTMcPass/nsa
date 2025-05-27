### User accessible routines > Variable Server Broadcast Channel

 specific
for the variable server. Commands are sent over a Trick communication TCP/IP socket to
the variable server. Multiple commands (newline separated) can be sent in the string
over the socket. The variable server will send back information to the requesting client.

If the command contains a syntax error, Python will print an error message to the screen,
but nothing will be returned to the client.

### Adding a Variable

```python
trick.var_add( string var_name )
```
or
```python
trick.var_add( string var_name , string units )
```

Adding a variable will tell the variable server to send the variable's value back to the
client at a specified frequency.  An optional units parameter may be attached to the
variable as the desired return units.  Multiple variables may be added to the list to be sent
back to the client.  The format of the returned values are described below, Ascii Format
or binary format.

Simulation time as a decimal number in "seconds" is available through a special var_add command.  This time marks the simulation time at the start of the variable server's task to copy variables.

```python
trick.var_add("time")
```

### Time Homogeneous or Synchronous Data

#### Copying Data Out of Simulation.

```python
trick.var_set_copy_mode(int mode)
```

There are 3 options to when the variable server will copy data out from the simulation.
Each option has unique capabilites.

##### Asynchronous Copy (mode = trick.VS_COPY_ASYNC or 0)

This is the default. Values are copied out of the sim asynchronously.  Copies are done
approximately at the var_cycle() rate during run and freeze mode.  A separate thread
is used to copy the data.  The data is not guaranteed to be time homogenous.  This mode
does not affect the main thread real-time performance.

##### End of Main Thread Execution Copy (mode = trick.VS_COPY_SCHEDULED or 1)

This mode copies data at the end of execution frame.  Copies are done exactly at the
var_cycle() rate after the main thread has finished all of it's jobs scheduled to run
at that time step both in run and freeze mode.  All variables solely calculated in the
main thread are guaranteed to be time homogenous.  Variables calculated in child
threads are not guaranteed to be time homogenous.  Copying data may very slightly
affect the main thread real-time performance.

##### Top of Frame Copy (mode = trick.VS_COPY_TOP_OF_FRAME or 2)

This mode copies data at the top of frame.  Copies are done at a multiple and offset of
the Executive software frame.  During freeze mode copies are made at a multiple and offset
of the freeze frame.  With careful planning, all variables from all threads can be
guaranteed to be time homogenous. Copying data may very slightly affect the main thread
real-time performance.

To set the frame multiplier and frame offset between copies use the following commands.
The frame refers to the software frame in the Executive.  In freeze mode a different
multiplier and offset are used.

```python
trick.var_set_frame_multiple(int mult)
trick.var_set_frame_offset(int offset)

trick.var_set_freeze_frame_multiple(int mult)
trick.var_set_freeze_frame_offset(int offset)
```

#### Writing Data Out of Simulation.

```python
trick.var_set_write_mode(int mode)
```

There are 2 options when the variable server writes the data.

##### Asynchronous Write ( mode = trick.VS_WRITE_ASYNC or 0 )

This is the default. Values are written onto the socket asynchronously.  Writes are done
approximately at the var_cycle() rate during run and freeze mode.  A separate thread
is used to copy write data.  This mode does not affect the main thread real-time performance.

##### Write When Copied ( mode = trick.VS_WRITE_WHEN_COPIED or 1 )

Values are written onto the socket as soon as they are copied from the simulation. The
write rate depends on the copy. Writes are done in the main thread of execution.  This
can greatly affect real-tim performance if a large amount of data is requested.

#### Old Style var_sync() Command

```python
trick.var_sync(bool mode)
```

var_sync() was previously used to control the copies and writes from the simulation.
The number of options has outgrown what a single var_sync command can configure.  It
may still be used to configure a subset of the copy/write combinations.

```python
trick.var_sync(0) # asynchronous copy and asynchronous write.
trick.var_sync(1) # end of main thread copy and asynchronous write.
trick.var_sync(2) # end of main thread copy and write when copied.
```
