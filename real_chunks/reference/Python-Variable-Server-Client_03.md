### The API


```

If you don't know the host and port (sims select a random available port by default), look no further than `find_simulation`, which will create a `VariableServer` for you from all sorts of simulation parameters.

```python
>>> help(variable_server.find_simulation)

find_simulation(host=None, port=None, user=None, pid=None, version=None, sim_directory=None, s_main=None, input_file=None, tag=None, timeout=None)
    Listen for simulations on the multicast channel over which all sims broadcast
    their existence. Connect to the one that matches the provided arguments that
    are not None.

    If there are multiple matches, connect to the first one we happen to find.
    If all arguments are None, connect to the first sim we happen to find.
    Such matches will be non-deterministic.

    Parameters
    ----------
    host : str
        Host name of the machine on which the sim is running as reported by
        Trick.
    port : int
        Variable Server port.
    user : str
        Simulation process user.
    pid : int
        The sim's process ID.
    version : str
        Trick version.
    sim_directory : str
        SIM_* directory. If this starts with /, it will be considered an
        absolute path.
    s_main : str
        Filename of the S_main* executable. Not an absolute path.
    input_file : str
        Path to the input file relative to the simDirectory.
    tag : str
        Simulation tag.
    timeout : positive float or None
        How long to look for the sim before giving up. Pass None to wait
        indefinitely.

    Returns
