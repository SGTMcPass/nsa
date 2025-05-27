### Trick Variable Server > Appendix > The Variable Server API

 are to be sent in messages to
the client.
* The rate at which messages are transmitted to the client.
* How messages are encoded. (ASCII or binary).
* Whether messages are guaranteed to be time homogenous.
* Whether message transmission is synchronous with the main simulation thread.
* Whether data transmission is paused (inactive), or unpaused (active).
* The debug state of the connection.
* An optional name, to identify the connection when debug messages are enabled.

![VarServerSessions](images/VarServerSessions.png)

The primary purpose of the [**variable server API**](#the-variable-server-api)
is to configure the sessions.

## Approach

Calling functions and setting simulation variables with the variable server client is a similar process to doing the same with the input file. The client sends Python code to the variable
server, where it's executed to call functions, set variables, or both. In the
following sections, we'll see examples of these. We'll also learn how to use the
variable server API to get data back to the client.

<a id=a-simple-variable-server-client></a>
## A Simple Variable Server Client

The listing below implements a very simple variable server client for our
cannonball simulation. It connects to the simulation, requests cannonball
position data, and prints the periodic responses to the screen.

<a id=listing-CannonDisplay_Rev1-py></a>
**Listing - CannonDisplay_Rev1.py**

```python
#!/usr/bin/python3
import sys
import socket

# 1.0 Process the command line arguments.
if ( len(sys.argv) == 2) :
    trick_varserver_port = int(sys.argv[1])
else :
    print( "Usage: python<version_number> CannonDisplay_Rev1.py <port_number>")
    sys.exit()

# 2.0 Connect to the variable server.
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect( ("localhost", trick_varserver_port) )
insock = client_socket.makefile("r")

# 3.0 Request the cannon ball position.
client_socket.send( b"trick.var_pause()\n" )
client_socket.send( b"trick.var_ascii()\n" )
client_socket.send( b"trick.var_add(\"dyn.cannon.pos[0]\") \n" +
                    b"trick.var_add(\"dyn.cannon.pos[1]\") \n"
                  )
client_socket.send( b"trick.var_unpause()\n" )

# 4.0 Repeatedly read and process the responses from the variable server.
while(True):
    line = insock.readline()
    if line == '':
        break

    print(line)
```

<a id=running-the-client></a>
### Running the Client

To run the variable server client :

* Create a new file called *CannonDisplay_Rev1.py* in your home
