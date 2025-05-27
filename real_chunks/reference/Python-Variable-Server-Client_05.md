### The API

 from the sim, so you can pass any function that accepts one argument. Even a custom lambda!

```python
>>> variable_server.get_value('ball.obj.state.input.mass', type_=int)
10
>>> variable_server.get_value('ball.obj.state.input.mass', type_=float)
10.0
>>> variable_server.get_value('ball.obj.state.input.mass', type_=lambda x: int(x) * 2)
20
```

You'll get an error if you try an invalid conversion.

```python
>>> variable_server.get_value('ball.obj.state.input.mass', type_=dict)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "variable_server.py", line 331, in get_value
    return type_(value)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
```

### A Special Note for Booleans
All values from the variable server are strings, and in Python, the only string that converts to `False` is the empty string.

```python
>>> bool("0")
True
>>> bool("False")
True
>>> bool("")
False
```

Booleans come over the variable server as either “0” or “1”, so passing `type_=bool` will restult in the value always being `True`. Instead, just use `int`. In Python, an int with value 0 is false, and anything else is true, so it will work just fine in conditionals.

## Specifying Units
`get_value` has a parameter for that too: `units`.

```python
>>> variable_server.get_value('ball.obj.state.input.mass', units='g', type
