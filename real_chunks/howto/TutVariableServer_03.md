### Trick Variable Server > Appendix > The Variable Server API

 **trick.var_add("dyn.cannon.pos[1]")**
* **trick.var_unpause()**

The [**var_pause**](#api-var-pause), and [**var_unpause**](#api-var-unpause)
commands are generally used at the beginning, and ending of variable server
session configurations. [**var_pause**](#api-var-pause) tells the variable
server to stop sending data, if it is. [**var_unpause**](#api-var-unpause),
tells the variable server to start sending data.

The [**var_ascii**](#api-var-ascii) command then tells the variable server to
send messages using an ASCII encoding (rather than binary).

The two [**var_add**](#api-var-add) commands add "dyn.cannon.pos[0]"
and "dyn.cannon.pos[1]" to the session variable list.

⚠️ Please notice that the quotes around the variable names must be
escaped with the '\' (backslash) character.

```python
client_socket.send( b"trick.var_add(\"dyn.cannon.pos[0]\") \n" +
                    b"trick.var_add(\"dyn.cannon.pos[1]\") \n"
                  )
```

When the [**var_unpause**](#api-var-unpause) command is executed, messages
containing the values of the variables listed in the session variable list will
be repeatedly created, and sent to the client.

By default, the variable server sends data every 0.1 seconds (that is, 10 hertz).
This is equivalent to commanding: [**var_cycle(0.1)**](#api-var-cycle).

The script then enters a while-loop that repeatedly 1) waits for, 2) reads, and
3) prints the raw responses from the variable server. The responses are encoded
in ASCII, as specified by [**var_ascii**](#api-var-ascii), and are of the
following format:

```
0\t<variable1-value>[\t<variable2-value>...\t <variableN-value> ]\n
```
<a id=getting-values-just-once></a>
## Getting Values Just Once

Suppose we wanted to get the value of the initial angle of our cannon. We don't
need to get it repeatedly, because it doesn't change. We just want to get it
once, and then to repeatedly get the position data, which changes over time.

For this situation, we can take one of several approaches. The most straightforward
is the [**var_send_once**](#api-var-send-once) command, which tells the variable
server to send the values sent as arguments immediately, regardless of whether
[**var_pause**](#api-var-pause) was previously commanded.

To demonstrate how this works, let's add the following code
