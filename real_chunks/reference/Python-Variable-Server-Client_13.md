### The API

 with the above approach is that there's no synchronization between when the updates occur and when our sleep happens to return. Sure, we could use `set_period` to tell the sim to send data at the same rate that we're sleeping, but we're bound to drift apart over time, and we can't ensure that we start a new cycle at the same time the sim does. Plus, there's network latency. And what if we ask the sim to send as fast as possible? Then we don't even know what the rate _is_!

But wait, it gets worse! If your processing cycle is faster than the sim's update cycle, you'll needlessly reprocess values that haven't been updated since the last time you processed them, which is wasteful. But if your cycle is slower, you'll miss some updates entirely.

For some applications, these issues may truly not matter, and using a simple `while` loop might be sufficient. For the rest of us, there's `register_callback`.

```python
>>> def foo():
...     print position.value
>>> variable_server.register_callback(foo)
0.632962631449
0.598808711027
0.564218072538
```

Now `foo` will be called each and every time there's an update, as soon as it arrives. Huzzah! You can set the period at which updates are sent via `set_period`, which applies to _all_ variables that this instance is tracking, regardless of when they're added. If you want to receive another set at a different rate, you should create another `VariableServer`.

## Concurrency Concerns
Callback functions are executed on the variable sampling thread, which is started when you
