### The API

 is true, so it will work just fine in conditionals.

## Specifying Units
`get_value` has a parameter for that too: `units`.

```python
>>> variable_server.get_value('ball.obj.state.input.mass', units='g', type_=int)
10000
```

You'll get an error if you try an invalid conversion.

```python
>>> variable_server.get_value('ball.obj.state.input.mass', units='m')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "variable_server.py", line 329, in get_value
    _assert_units_conversion(name, units, actualUnits)
  File "variable_server.py", line 927, in _assert_units_conversion
    raise UnitsConversionError(name, expectedUnits)
variable_server.UnitsConversionError: [ball.obj.state.input.mass] cannot be converted to [m]
```

# What About Setting Values?
Of course you can set values! It's even easier than getting them.

```python
>>> variable_server.set_value('ball.obj.state.input.mass', 5)
>>> variable_server.get_value('ball.obj.state.input.mass', type_=int)
5
```

You can specify units when you set variables too.

```python
>>> variable_server.set_value('ball.obj.state.input.mass', 5, units='g')
```

Doing so has no effect on subsequent calls to `get_value`, which continues to use the original units (kg, in this case)

```python
>>> variable_server.get_value('ball.obj.state.input.mass', type_=float)
0.005
```

unless you say otherwise.

```python
>>> variable_server.get_value('ball.obj
