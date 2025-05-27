### The API

 instance is tracking, regardless of when they're added. If you want to receive another set at a different rate, you should create another `VariableServer`.

## Concurrency Concerns
Callback functions are executed on the variable sampling thread, which is started when you instantiate `VariableServer` and runs until you call `close` (either explicitly or via a `with` statement). This means that new updates can't be processed until all callback functions have returned. The variable sampling thread spends most of its time blocked, waiting for new updates to arrive, so time consumed by callback functions usually isn't an issue. But if your callback performs a long-running task, you should probably do it in another thread so it doesn't cause the variable sampling thread to fall behind.

# The API
Wikis are great for how-tos and high-level discussions, but if you want to get down to the nuts and bolts, you need to look at the API. You can do so by running `pydoc variable_server` in the directory containing `variable_server.py` or programmatically by calling `help` on the feature in which you're interested.

```python
>>> import variable_server
>>> help(variable_server.Variable)
Help on class Variable in module variable_server:

class Variable(__builtin__.object)
 |  A variable whose value and units will be updated from the sim. You
 |  should not directly change any part of this class.
```

[Continue to Trick Ops](TrickOps)
