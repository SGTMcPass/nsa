### User accessible routines > Variable Server Broadcast Channel

| [Home](/trick) → [Documentation Home](../Documentation-Home) → [Simulation Capabilities](Simulation-Capabilities) → Variable Server |
|------------------------------------------------------------------|

When running a Trick simulation, unless specifically turned off, a server called the
"variable server" is always up and listening in a separate thread of execution. The
variable server is privy to simulation parameters and their values since it resides
in an asynchronous simulation thread. Threads share the same address space as their
siblings and parent. Clients connect to the variable server in order to set/get
values of Trick processed variables. You may already be familiar with the Trick
applications that use the variable server: the simulation control panel, Trick
View (TV) , [Event/Malfunction Trick View](/trick/documentation/running_a_simulation/runtime_guis/MalfunctionsTrickView) (MTV) , and the stripchart.

The variable server is a convenient way for external applications to interact with
the simulation. Any application that needs to set or get simulation parameters may
do so through the variable server. The external application need not be on the same
machine since the connection to the variable server is via a Trick communication
TCP/IP socket.

## User accessible routines

These commands are for enabling/disabling the variable server, and for getting its status.
The variable server is enabled by default.

```c
int var_server_set_enabled(int on_off);
int var_server_get_enabled();
```

<b>Disabling the variable server will disable all Trick runtime GUIs: simulation
control panel, TV, MTV, and stripchart.</b>

These commands are for toggling information messages from the variable server (i.e., commands received from <i>ALL</i> clients).
The messages go to the terminal, the simulation control panel, and the "send_hs" file in the RUN directory.
The variable server information message capability is off by default.

```c
int set_var_server_info_msg_off();
int set_var_server_info_msg_on();
```

These commands are also for toggling information messages from the variable server (i.e., commands received from <i>ALL</i> clients).
The messages only go to a dedicated `varserver_log` file in the RUN directory.
The variable server log capability is off by default.

```c
int set_var_server_log_off();
int set_var_server_log_on();
```

These commands are also for toggling individual variable server session logs.
Each log records the IP and port number of the client that connected and every message received.
These logs go into a subdirectory under the RUN direcory called `sesssion_logs`, and the files are named `VSSession<num>.log`
The variable server session log capability is off by default.

```c
int set_var_server_session_log_off();
int set_var_server_session_log_on();
```

### Getting and Setting the Variable Server Port Information

To set the variable server port to a fixed number in the input file use var_server_set_port()

```python
trick.var_server_set_port( unsigned int port )
```

To get the variable server host and port information in the input file use var_server_get_hostname() and
var_server_get_port().

```python
trick.var_server_get_hostname()
trick.var_server_get_port()
```

Additional TCP or UDP sockets can be opened as well. Additional TCP sockets operate the same way as the original variable server socket. A UDP socket will only host 1 variable server session, and the responses will be sent to the latest address that sends commands to it.

Note that this is not necessary to allow multiple variable server clients - any number of clients can connect to the original variable server port.

```python
trick.var_server_create_udp_socket( const char * source_address, unsigned short port )
trick.var_server_create_tcp_socket( const char * source_address, unsigned short port )
```


## Commands

The variable server accepts commands in the form of strings. The variable server parses
these commands using the Python input processor. So in theory, any Python valid syntax
is acceptable to the variable server. This section lists the commands that are specific
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
client at a specified frequency.  An optional units parameter may be attached
