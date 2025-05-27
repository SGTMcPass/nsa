### The API

1]')
>>> print 'The ball is at position ({0}, {1})'.format(*variable_server.get_values(x, y))
The ball is at position (3.069993744436219, -11.04439115432281)
```

Or if you don't want to save the values at all!

```python
>>> print 'The ball is at position ({0}, {1})'.format(*variable_server.get_values(
... Variable('ball.obj.state.output.position[0]'),
... Variable('ball.obj.state.output.position[1]')))
The ball is at position (3.069993744436219, -11.04439115432281)
```

Which are both equivalent to, but more compact than:

```python
>>> x = Variable('ball.obj.state.output.position[0]')
>>> y = Variable('ball.obj.state.output.position[1]')
>>> variable_server.get_values(x, y)
['3.069993744436219', '-11.04439115432281']
>>> print 'The ball is at position ({0}, {1})'.format(x.value, y.value)
The ball is at position (3.069993744436219, -11.04439115432281)
```

### Don't Mess With `Variable` Attributes
You should consider `Variable` read-only. This module ensures that each `Variable`'s state remains consistent. Once you've constructed one, you should not directly set any of its fields, and you shouldn't need to. Of course, this is Python, so there's nothing to stop you from doing:

```python
>>> mass.value = 1337
```

But that's certainly not going to affect the corresponding variable
