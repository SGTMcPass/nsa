### Trick Variable Server > Appendix > The Variable Server API

 position data, which changes over time.

For this situation, we can take one of several approaches. The most straightforward
is the [**var_send_once**](#api-var-send-once) command, which tells the variable
server to send the values sent as arguments immediately, regardless of whether
[**var_pause**](#api-var-pause) was previously commanded.

To demonstrate how this works, let's add the following code to our script, right
after the line where we sent the **var_ascii** command.

```python
client_socket.send( b"trick.var_send_once(\"dyn.cannon.init_angle\")\n")
line = insock.readline()
print(line)
```

In this code, we simply ask the variable server to immediately send the value of ```dyn.cannon.init_angle```,
call ```insock.readline()``` to wait for a response, and print the response when it is received.
[**var_send_once**](#api-var-send-once) does not alter the session variable list in any way.

When we run the client, the first few lines of output should look something like:

```
5	0.5235987755982988

0	0	0

0	0	0
```

The [**var_send_once**](#api-var-send-once) command uses a [message type](#variable-server-message-types) of 5
to allow a programmer to differentiate between normal session variables and var_send_once variables. var_send_once
does not alter or interfere with the session variable list, which would allow both of these features to be
used simultaneously in a sim.

The [**var_send_once**](#api-var-send-once) also allows a user to request multiple variables in a single
command. [**var_send_once**](#api-var-send-once) can accept a comma-separated list of variables as the
first argument and the number of variables in the list as the second argument.
In our example, suppose we also wanted to retrieve the initial speed of the cannonball.
We could retrieve both variables with a single command:

```python
client_socket.send( b"trick.var_send_once(\"dyn.cannon.init_angle, dyn.cannon.init_speed\", 2)\n")
```

Now, when we run the client, we get both the init_angle and the init_speed with the first message.

```
5	0.5235987755982988	50

0	0	0

0	0	0
```

Another commonly used pattern to retrieve variables only once is to use the [**var_add**](#api-var-add),
[**var_send**](#api-var-send), and [**var_clear**](#api-var-clear) commands. [**var_send**](#api-var-send) tells
the variable server to send all **session** variables immediately regardless of whether [
