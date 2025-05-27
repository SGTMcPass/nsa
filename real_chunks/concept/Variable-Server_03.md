### User accessible routines > Variable Server Broadcast Channel

 of printing to the simulation stdout/stderr
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

# If a "print" is used instead of sys.stdout.write, a second message is sent containing
# a single newline.
print "trick.exec_get_current_version()"

4  1       10
10.7.dev-14  1        1
 <- a single newline is the second message
```

### Debugging Variable Server Messages

```python
trick.var_debug(int level)
```

The level may range from 0-3.  The larger the number the more debugging information is printed to
the screen (for the current client only).

### Logging Messages to file.

These commands are for toggling information messages from the variable server (for this client only).
The messages only go to a dedicated "varserver_log" file in the RUN directory.
The variable server log capability is off by default. (See the global variable server commands
@link Trick::VariableServer::set_var_server_log_on() set_var_server_log_on() @endlink and
@link Trick::VariableServer::set_var_server_log_off() set_var_server_log_off() @endlink for toggling
the logging capability for <i>ALL</i> clients.)

```python
trick.var_server_log_on()
trick.var_server_log_off()
```

### Setting Variable Server Client Tag

```python
trick.var_set_client_tag(string name)
```

This sets an identifying name tag to be associated with the current client that will be printed with each information message
displayed. Information messages are displayed as a result of
@link Trick::VariableServer::set_var_server_info_msg_on() set_var_server_info_msg_on() @endlink,
@c var_server_log_on() or
@c var_debug(). For instance, Trick sets a name tag for each of its variable server clients (simulation control panel is "SimControl",
TV is "TRICK_TV", etc.).

### Byteswapping

```python
trick.var_byteswap(bool on_off)
```

## Returned Values

By default the values retrieved are sent asynchronously to the client. That is, the values
retrieved by the variable server are pulled directly from memory asynchronously and do not
guarantee synchronization from the same simulation execution frames unless the var_sync
command is used. Values will be returned to the client in the same order that they were
issued in the var_add command(s).  Typically the client receives the data from the variable
server in a buffer via the tc_read command (see TrickComm for more information).

## Ascii Format

The default format, or if var_ascii is commanded specifically, causes the variable server
to return a buffer containing a tab delimited character string in the following format:

```
0\t<variable1 value>[\t<variable2 value>. . .\t<variableN value>]
```

where N is the number of variables registered via the var_add command(s). The "\t" represents
a tab character, and the "\n" is the newline character that always ends the string.  Note
that if a value being returned is itself a character string data type, any tab (or other
unprintable character) that occurs within the character string value will appear as an
escaped character, i.e. preceded by a backslash.

The 1st value returned in the list will always be a message indicator. The possible
values of the message indicator listen in the table below.

| Name              | Value | Meaning |
|-------------------|-------|---------|
| VS\_IP\_ERROR     | -1    | Protocol Error|
| VS\_VAR\_LIST     |  0    | A list of variable values. |
| VS\_VAR\_EXISTS   |  1    | Response to var\_exists( variable_name )|
| VS\_SIE\_RESOURCE |  2    | Response to send_sie_resource|
| VS\_LIST\_SIZE    |  3    | Response to var_send_list_size or send_event_data|
| VS\_STDIO         |  4    | Values Redirected from stdio if var_set_send_stdio is enabled|
| VS
