### The API

 familiar with the core data structure: our old friend `Variable`.

## Adding `Variable`s
Periodic sampling uses the same `Variable`s we used with `get_values`. To get started, just call `add_variables`!

```python
>>> position = Variable('ball.obj.state.output.position[0]', type_=float)
>>> variable_server.add_variables(position)
```

After checking for units and type_ conversion errors, this causes the sim to periodically send the value of `ball.obj.state.output.position[0]` to us, which is used to automatically update `position`.

```python
>>> position.value
-7.24269488786
>>> position.value
-9.0757620175
>>> position.value
-9.751339991
```

Look at that! `position` is updating all on its own. Now you can stick your periodic logic in a nice `while` loop and run forever!

```python
>>> import time
>>> while True:
...     position.value
...     time.sleep(1)
-2.065295422179974
1.5358082417288299
4.8450427189593777
```

## Triggering Callbacks
Using a `while` loop with a `sleep` might work for applications that don't care about the "staleness" of the data when it arrives, but we write real-time code around here; I can't suffer unnecessary delays! The problem with the above approach is that there's no synchronization between when the updates occur and when our sleep happens to return. Sure, we could use `set_period` to tell the sim to send data at the same rate that we're sleeping, but we're bound
