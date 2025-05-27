### Executive Flow > Debugging Help > Getting Build Information

 trapped by default.

### Printing a Stack (Call) Trace on Signal

```python
# Python code
trick.exec_set_stack_trace(int on_off)
```

This is a Linux only option.  By default, printing a stack trace when a signal is trapped is enabled.  When a signal is trapped a debugger is automatically connected to the running simulation and a printout of the calling stack is printed before the simulation exits.

### Attaching a debugger on Signal

```python
# Python code
trick.exec_set_attach_debugger(int on_off)
```

This is a Linux only option.  By default, this option is off.  If enabled, when a signal is trapped a debugger is automatically connected to the running simulation and an interactive debugging session is presented to the user.

The debugger executable may be set with the following.  The default is "/usr/bin/gdb".

```python
# Python code
trick.exec_set_debugger_command(char * command)
char * trick.exec_get_debugger_command()
```

### Getting Build Information

```python
# Python code
char * trick.exec_get_current_version()
```

The executive stores the Trick version that was used to build the executable.  Use exec_get_current_version() to return the version string.

[Continue to Input Processor](Input-Processor)
