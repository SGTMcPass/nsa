### The API

 to encapsulate that data in a class.

## The `Variable` Class
`Variable` represents a simulation variable. It's constructor takes the same parameters we've been using with `get_value` and `set_value`: `name`, `units`, and `type_`. `Variables` are used with the `get_values` function (note the trailing `s`), which accepts an arbitrary number of them. `get_values` uses the information in each `Variable` in the same way that `get_value` uses its parameters, and the observable behavior is largely the same: you get back a list of values.

```python
>>> from variable_server import Variable
>>> position = Variable('ball.obj.state.input.position[0]', type_=int)
>>> mass = Variable('ball.obj.state.input.mass', units='g', type_=float)
>>> variable_server.get_values(position, mass)
[5, 10000.0]
```

And you get an error if a units or type_ conversion fails.

```python
>>> variable_server.get_values(Variable('ball.obj.state.input.mass', units='m'))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "variable_server.py", line 430, in get_values
    _assert_units_conversion(variable.name, variable.units, units)
  File "variable_server.py", line 941, in _assert_units_conversion
    raise UnitsConversionError(name, expectedUnits)
variable_server.UnitsConversionError: [ball.obj.state.input.mass] cannot be converted to [m]

>>> variable_server.get_values(Variable('ball.obj.state.input.mass', type_=dict))
Traceback (most recent call last):
