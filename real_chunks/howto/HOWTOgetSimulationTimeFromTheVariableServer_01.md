### How to Get Simulation Time from the Variable Server > Example (SimTimeExample.py)

 variable server.
client_socket.send( b"trick.var_unpause()\n" )

# Repeatedly read and process the responses from the variable server.
while(True):
    line = insock.readline()
    if line == '':
        break

    field = line.split("\t")
    time_tics = int(field[1]);

    # Calculate sim_time
    sim_time = float(time_tics) / tics_per_second

    print(f'sim_time = {sim_time}')
```

If you are unfamiliar or rusty on how to use the Trick variable server, please see
the [Variable Server](/trick/tutorial/TutVariableServer) section of the [Trick Tutorial](/trick/tutorial/Tutorial).
