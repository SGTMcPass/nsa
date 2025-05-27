### User accessible routines > Variable Server Broadcast Channel

 done in the main thread of execution.  This
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

### Sending the Return Values Immediately

```python
trick.var_send()
```

The var_send command forces the variable server to return the list of values to the
client immediately.

### Sending variables only once and immediately

```python
trick.var_send_once( string var_name)
```

The var_send_once command forces the variable server to return the value of the given
variable to the client immediately.

```python
trick.var_send_once( string var_list, int num_vars)
```

var_send_once can also accept a comma separated list of variables. The number of variables
in this list must match num_vars, or it will not be processed.

### Changing the Units

```python
trick.var_units( string var_name , string units )
```

The returned values can be converted to other units of measurments. The var_units command
tells the variable server what units to use.  If the units are changed, then the units
are included in the returned string to the client.

### Removing a Variable

```python
trick.var_remove( string var_name )
```

Removing a variable removes the variable from the list returned to the client.

### Clearing the List of Variables

```python
trick.var_clear()
```

To clear the whole list of variables sent to the client.

### Exiting the Variable Server

```python
trick.var_exit()
```

Disconnects the current client from the variable server.

### Checking for existence of a variable

```python
trick.var_exists( string var_name )
```

To test if a variable name exists.  A special response is sent to the client when
this command is processed.

In **var_binary** mode, the (4 byte) message indicator of the response will be 1,
followed by a (1 byte) value of 0 or 1 to indicate the existence of the variable.

In **var_ascii** mode: the message indicator of the response will be "1" followed
by a tab, then an ASCII "0" or "1" to indicate the existence of the variable.

### Changing the Return Value Cycle Rate

```python
trick.var_cycle( double cycle_rate )
```

Changes the rate of the return messages to the client.  This rate is estimated and may not
perfectly match the requested rate.

### Pause the Variable Server

```python
trick.var_pause()
```

Pauses the return values sent to the client.  Even when paused, the variable server will
accept new commands.

### Unpause the Variable Server

```python
trick.var_unpause()
```

Resumes sending the return values to the client.

### Setting Ascii Return Format

```python
trick.var_ascii()
```

Sets the return message format to ASCII. See below for the format of the message.

### Setting Binary Return Format

```python
trick.var_binary()
```

Sets the return message format to Binary. See below for the format of the message.

```python
trick.var_binary_nonames()
```

This variation of the binary format reduces the amount of data that is sent to the client.
See below for the exact format.

### Sending stdout and stderr to client

```python
trick.var_set_send_stdio(bool on_off)
```

If var_set_send_stdio is called with a true value, then all python stdout and stderr
output will be redirected to the client instead of printing to the simulation stdout/stderr
location.  Note: output from C/C++ code called from python will direct it's output to
the simulation stdout/stderr location.  See the return message format for Stdio.

This is useful to get output from the simulation such as the return values of a function.

```
# Example in a variable server client to get the Trick version used to compile a sim
# The C prototype is "const char *exec_get_current_version(void) ;"
trick.var_set_send_stdio(True)
sys.stdout.write(trick.exec_get_current_version())

# The returned text will look like this. See the return message format below
4  1       10
10.7.dev-1
