### User accessible routines > Variable Server Broadcast Channel

 below.

| Name              | Value | Meaning |
|-------------------|-------|---------|
| VS\_IP\_ERROR     | -1    | Protocol Error|
| VS\_VAR\_LIST     |  0    | A list of variable values. |
| VS\_VAR\_EXISTS   |  1    | Response to var\_exists( variable_name )|
| VS\_SIE\_RESOURCE |  2    | Response to send_sie_resource|
| VS\_LIST\_SIZE    |  3    | Response to var_send_list_size or send_event_data|
| VS\_STDIO         |  4    | Values Redirected from stdio if var_set_send_stdio is enabled|
| VS\_SEND\_ONCE    |  5    | Response to var\_send\_once|

If the variable units are also specified along with the variable name in a var_add or
var_units command, then that variable will also have its units specification returned following
its associated value separated by a single blank. For example, if the 2nd of N variables was
specified with {<units>} in either a var_add or var_units command, the returned string would
be in the following format:

```
0\t<variable1 value>\t<variable2 value> {<variable2 units>}. . .\t<variableN value>
```

Note that the maximum message size that the variable server sends to the client is 8192 bytes.
If the amount of data requested is larger than that, the ASCII message will be split into
multiple messages.  The client is responsible for concatenating the multiple messages back
together.  (Hint: look for the "\n" delimter)

If a syntax error occurs when processing the variable server client command, Python will print
an error message to the screen, but nothing will be returned to the client.

If a var_add command was issued for a non-existent variable, there will be a one time Trick error
message printed to the screen, but the resulting data sent to the client is still ok. The value
returned for the non-existent variable is the string "BAD_REF".

## Binary Format

By specifying the var_binary or var_binary_nonames command, the variable server will return
values in a binary message formatted as follows:

```
<message_indicator><message_size><N>
<variable1_namelength><variable1_name><variable1_type><variable1_size><variable1_value>
<variable2_namelength><variable2_name><variable2_type><variable2_size><variable2_value>
. . .
<variableN_namelength><variableN_name><variableN_type><variableN_size><variableN_value>
```

Where the first 12 bytes are the message header:
- message_indicator is the same possible values as in var_ascii shown above : a 4 byte integer
- message_size is the total size of the message in bytes (NOT including message_indicator) : a 4 byte integer
- N is the number of variables registered via the var_add command(s) : a 4 byte integer
.
and the remaining bytes of the message contain the variable data:
- variable_namelength is the string length of the variable name : a 4 byte integer (NOT present for var_binary_nonames)
- variable_name is the ASCII variable name string : @e variable_namelength bytes of string (NOT present for var_binary_nonames)
- variable_type is Trick data type of the variable : a 4 byte integer (see Trick::MemoryManager::TRICK_TYPE)
- variable_size is number of bytes the variable occupies in memory : a 4 byte integer
- variable_value is the variable's current value : @e variable_size bytes of @e variable_type

When the client has requested a very large amount of data, it is possible that it may require
more than one message to be returned.  The maximum message size is 8192 bytes, so if the data
returned by the variable server requires more space than that (once formatted into the above
message format), then the variable server sends more than one message.  This is indicated by
the @e N field.  For example, if the client has requested 15 variables, and @e N = 15, then
everything is contained in that one message.  However if @e N < 15, then the client should
continue reading messages until all @e N received add up to 15.

If a syntax error occurs when processing the variable server client command, Python will print
an error message to the screen, but nothing will be returned to the client.

If a var_add command was issued for a non-existent variable, there will be a one time Trick error
message printed to the screen, but the resulting data sent to the client is still ok. The message
returned
