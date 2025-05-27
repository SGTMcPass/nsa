### The API

 to the input file relative to the simDirectory.
    tag : str
        Simulation tag.
    timeout : positive float or None
        How long to look for the sim before giving up. Pass None to wait
        indefinitely.

    Returns
    -------
    VariableServer
        A VariableServer connected to the sim matching the specified
        parameters.

    Raises
    ------
    socket.timeout
        If a timeout occurs.
```

# Just Tell Me How to Get a Frickin' Value
Looking for the TL;DR version, eh? Alright, here you go:

```python
>>> from variable_server import VariableServer
>>> variable_server = VariableServer('localhost', 7000)
>>> variable_server.get_value('ball.obj.state.input.mass')
'10'
```

## What!? That Returned a String. Mass isn't a String!
Well if you weren't in such a rush, we could talk a bit more about your options. What's that? You suddenly have some time to actually read the documentation? Great! Let's dive in.

## Specifying Type
`get_value` has a parameter called `type_` that is used to convert the string value returned by the sim into something more useful. Want an int? Pass `int`. Want a float? Pass `float`. Want a string? Don't pass anything; `str` is the default. Whatever you pass to `type_` is actually called on the string from the sim, so you can pass any function that accepts one argument. Even a custom lambda!

```python
>>> variable_server.get_value('ball.obj.state.input.mass', type_=int)
10
>>> variable_server.get_value('ball.obj.state.input.mass
