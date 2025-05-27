### The API

(name, expectedUnits)
variable_server.UnitsConversionError: [ball.obj.state.input.mass] cannot be converted to [m]

>>> variable_server.get_values(Variable('ball.obj.state.input.mass', type_=dict))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "variable_server.py", line 438, in get_values
    return [variable.value for variable in variables]
  File "variable_server.py", line 145, in value
    return self._type(self._value)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
```

But wait, there's more! Each `Variable` is also updated in place, so you can ignore the returned list and use each `Variable`'s `value` property instead if that's more convenient.

```python
>>> position.value
5
```

Units are also available and are automatically filled in if you didn't specify them when creating the `Variable`.

```python
>>> position.units
'm'
```

You were probably going to save the returned values somewhere anyway, right? Might as well save them with the `Variable`s themselves! However, the returned list can be useful if you want to use the values in the same expression in which they're fetched.

```python
>>> x = Variable('ball.obj.state.output.position[0]')
>>> y = Variable('ball.obj.state.output.position[1]')
>>> print 'The ball is at position ({0}, {1})'.format(*variable_server.get_values(x, y))
The ball is at position (3.069993744436219, -11.04439115432281)
```
