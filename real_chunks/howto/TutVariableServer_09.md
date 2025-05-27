### Trick Variable Server > Appendix > The Variable Server API

') + b" \n")
            client_socket.send( b"dyn.cannon.init_angle = " + bytes(str(angleScale.get()*(math.pi/180.0)), 'UTF-8') + b" \n")
            # 8.6.2 Command the sim to re-run the cannon_init job.
            client_socket.send( b"trick.cannon_init( dyn.cannon )\n")
            # 8.6.3 Command the sim to RUN mode.
            client_socket.send( b"trick.exec_run()\n")

    # 8.7 Update the Tk graphics.
    tk.update()

# ----------------------------------------------------------------------
# 9.0 Keep the window open, when the data stops.
tk.mainloop()

```

<a id=controlling-the-simulation-mode-from-a-vs-client></a>
### Controlling the Simulation Mode from a VS Client

The current simulation mode is stored in the ```trick_sys.sched.mode``` variable.
So, we request that in addition to our other variables in section 7.0 of the
listing.

The only simulation modes that are available to our client are FREEZE, and RUN.
The variable server isn't available in other modes. The numeric values of these
modes are:

* MODE_FREEZE = 1
* MODE_RUN = 5

To set the simulation mode, we need to use the following functions:

* ```trick.exec_run()``` - commands the sim to RUN mode.
* ```trick.exec_freeze()``` - commands the sim to FREEZE mode.

as in sections 8.5, and 8.6 of the listing.

Don't set ```trick_sys.sched.mode```.

<a id=initializing-the-simulation-from-a-vs-client></a>
### Initializing the Simulation from a VS Client

To set simulation values, we simply create and send Python assignment statements.

```
 client_socket.send( b"dyn.cannon.init_speed = " + str(speedScale.get()) + " \n")
 client_socket.send( b"dyn.cannon.init_angle = " + str(angleScale.get()*(math.pi/180.0)) )
```

Just because the variable server isn't available during INITIALIZATION mode,
doesn't mean we can't initialize our sim. We can just call our initialization
jobs directly.

```
client_socket.send( b"trick.cannon_init( dyn.cannon )\n")
```

<a id=starting-a-client-from-the-input-file></a>
## Starting a Client From The Input File

Rather than having to start a client each and every time from the command line,
we can easily start it from the input file using the function
```trick.var_server_get_port()``` as illustrated in the following input file
script.

```python
#==================================
# Start the variable server client.
#==================================
varServerPort = trick.var_server_get_port();
CannonDisplay
