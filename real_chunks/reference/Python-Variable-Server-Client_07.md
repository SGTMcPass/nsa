### The API

 use the original units (kg, in this case)

```python
>>> variable_server.get_value('ball.obj.state.input.mass', type_=float)
0.005
```

unless you say otherwise.

```python
>>> variable_server.get_value('ball.obj.state.input.mass', units='g', type_=float)
5.0
```

# Single-Value Fetches are for Chumps. I Want Multiple Values Simultaneously!
To get any fancier, we have to talk about implementation details a bit. Trick's variable server doesn't actually have a "one-shot" value fetching option. Instead, it's designed to periodically send a set of variable values over and over again. If you're familiar with variable server commands, `get_value` actually calls `var_add`, `var_send`, and `var_clear` every time it's called. If we want multiple values, we're better off doing all the `var_adds` together and just calling `var_send` and `var_clear` once. If you don't know what I'm talking about, don't worry about it. All you need to know is that `get_values` is more efficient than calling `get_value` for fetching multiple variables.

It's also a little more complicated. Having a parameter list like `name1, units1, type1, name2, units2, type2` and so on would get ugly fast. So say goodbye to the simple interface! Time to encapsulate that data in a class.

## The `Variable` Class
`Variable` represents a simulation variable. It's constructor takes the same parameters we've been using with `get_value` and `set_value`: `name`, `units`, and
