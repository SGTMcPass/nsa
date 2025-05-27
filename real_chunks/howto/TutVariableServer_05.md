### Trick Variable Server > Appendix > The Variable Server API

0	0

0	0	0
```

Another commonly used pattern to retrieve variables only once is to use the [**var_add**](#api-var-add),
[**var_send**](#api-var-send), and [**var_clear**](#api-var-clear) commands. [**var_send**](#api-var-send) tells
the variable server to send all **session** variables immediately regardless of whether [**var_pause**](#api-var-pause)
was previously commanded.

To demonstrate how this works, replace the code in the previous listing with the snippet below, right
after the line where we sent the **var_ascii** command.

```python
client_socket.send( b"trick.var_add(\"dyn.cannon.init_angle\")\n")
client_socket.send( b"trick.var_send()\n" )
line = insock.readline()
print(line)
client_socket.send( b"trick.var_clear()\n" )
```

In this snippet of code, we add  ```dyn.cannon.init_angle``` to the session
variable list. Then we call [**var_send**](#api-var-send) to tell the variable
server to send us the value, and wait for the response by calling
```insock.readline()```. When it arrives, we print it. Before the script adds
the cannon position variables, we need to remove ```dyn.cannon.init_angle```,
otherwise we'll be getting this in our messages too. We can do this in one of
two ways. We can 1) call [**var_clear**](#api-var-clear) to clear the the list,
or 2) we can call [**var_remove**](#api-var-remove). Specifically we could do
the following:

```python
client_socket.send( b"trick.var_remove(\"dyn.cannon.init_angle\")\n" )
```

So, when we run the modified client, the first three lines of the output should
look something like the following.

```
0	0.5235987755982988

0	0	0

0	0	0
```

The first line contains the message type (which is zero), followed by the value
of  ```dyn.cannon.init_angle```. Subsequent lines contain the position data like
before.

<a id=a-more-realistic-example></a>
## A More Realistic Example

In the previous example we only called variable server API functions, like
```trick.var_add```, ```trick.var_send```, and so forth. But, we're not
just limited to variable server API calls. The variable server's Python
interpreter is bound to our simulation's variables and many other functions,
including those that we've written ourselves. In this example we'll create a
more interactive client, to initialize our simulation, and to control the
simulation modes.

The listing below implements
