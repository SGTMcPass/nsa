### The API

 7000) as variable_server:
    # Hmmm, this syntax is a little strange, but I'll go with it.
    # Actually, the more I look at it, the more I like it.
    # Python is pretty cool!
    # Oh yeah, I'm supposed to be using variable_server here.
    # Ok, I'm done.
# Look, ma! No need to call close!
```

`close` is automatically called when the `with` block exits, no matter how that occurs: normally, via exception, ~~even if you pull the power cord from your computer!~~

# How do I Make One of These `VariableServer` Thingies?
If you know the host and port of the simulation you want to connect to, you can call `VariableServer`'s constructor directly.

```python
>>> from variable_server import VariableServer
>>> variable_server = VariableServer('localhost', 7000)
```

If no one's listening, you'll get an error.

```python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "variable_server.py", line 216, in __init__
    self._synchronous_socket = socket.create_connection((hostname, port))
  File "/usr/lib64/python2.7/socket.py", line 571, in create_connection
    raise err
socket.error: [Errno 111] Connection refused
```

If you don't know the host and port (sims select a random available port by default), look no further than `find_simulation`, which will create a `VariableServer` for you from all sorts of simulation parameters.

```python
>>>
