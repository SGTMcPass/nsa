### The API

 of its fields, and you shouldn't need to. Of course, this is Python, so there's nothing to stop you from doing:

```python
>>> mass.value = 1337
```

But that's certainly not going to affect the corresponding variable in the sim.

```python
>>> variable_server.get_value('ball.obj.state.input.mass', type_=float)
5.0
```

And changing a `Variable`'s units

```python
>>> mass.units = 'g'
```

is not going to automagically perform a conversion.

```python
>>> mass
ball.obj.state.input.mass = 1337.0 g
```

A `Variable` only reflects the state of its corresponding variable in the sim. It does not manipulate it. Always use  `set_value` to change the value. The units can be specified in `Variable`'s constructor. They can also be changed via `set_units`, but only for `Variable`s that are being periodically sampled.

# Periodic Sampling
Ah, now we're _really_ cooking! This is what the variable server was made for: sending sets of variable values at a specified rate. If you find yourself calling `get_values` over and over again on the same set of variables, perhaps you'd like to step up to the big leagues and take a crack at asynchronous periodic sampling. Don't worry, it's not as scary as it sounds. In fact, we're already familiar with the core data structure: our old friend `Variable`.

## Adding `Variable`s
Periodic sampling uses the same `Variable`s we used with `get_values`. To get started, just call `add_variables`!

```python
>>> position =
