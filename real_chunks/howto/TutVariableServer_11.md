### Trick Variable Server > Appendix > The Variable Server API

value\>...**\t** \<variable**N**-value\> ]**\n**

Where:

* **N** is the number of variables in the session variable list.
* **\t** is a tab character.

<a id=api-var-binary></a>
**var\_binary()** -
Set response encoding to binary.

<a id=api-var-cycle></a>
**var\_cycle( period )** -
Set data response message period in seconds. (default = 0.1 seconds, i.e., 10 hertz)

<a id=api-var-pause></a>
**var\_pause()** -
Halt periodic responses.

<a id=api-var-unpause></a>
**var\_unpause()** -
Resume periodic responses.

<a id=api-var-send></a>
**var\_send()** -
Send response immediately.

<a id=api-var-send-once></a>
**var\_send\_once( variable_name )** -
Immediately send the value of variable_name

**var\_send\_once( variable_list, num_variables )** -
Immediately send the value of all variables in the comma separated variable_list, or an error if the number of variables in the list does not match num_variables

<a id=api-var-clear></a>
**var\_clear()** -
Clear the session variable list.

<a id=api-var-exit></a>
**var\_exit()** -
End the connection to the variable server.

<a id=api-var-remove></a>
**var\_remove( variable_name )** -
Remove the given name from the session variable list.

<a id=api-var-set-client-tag></a>
**var\_set\_client\_tag( text )** - Name the current connection, for debugging.

<a id=api-var-debug></a>
**var\_debug( level )** -
Set the debug level. Set level to 3 for all debug messages, and 0 for no debug messages.

<a id=api-var-sync></a>
**var\_sync( mode )**

Set the synchronization mode of the variable server session, where the modes are:

* **0 = fully asynchronous** (default)

  This means that periodic data messages are not guaranteed to
  be time homogeneous. That is, data may not all be associated with
  a the exact same sim time. The variable server data messages are
  written from a thread other than the main thread.

* **1 = sync data gather, async socket write**

  This means that periodic data messages are guaranteed to
  be time homogeneous, but are written from a thread other
  than the main simulation thread.

* **2 = sync data gather, sync socket write**

  This means that periodic data messages are guaranteed to
  be time homogeneous, but are written from the main simulation thread.

[Next Page](ATutMonteCarlo)
