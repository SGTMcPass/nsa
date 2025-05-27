### Accessing Simulation Parameters > I Just Want to Know How Do I Set this Value...

trick.freeze()` called with no
arguments will freeze immediately.  An optional freeze time may be provided to freeze some time
in the future.

```python
# Freezes immediately
trick.freeze()

# Freezes at an absolute time
trick.freeze(100.0)

# Freezes 5 seconds relative from the current sim_time
trick.freeze(trick.exec_get_sim_time() + 5.0)

```

## Checkpoint the Simulation

To checkpoint a simulation call `trick.checkpoint([<checkpoint_time>])`.  `trick.checkpoint()` called with no
arguments will checkpoint immediately.  An optional checkpoint time may be provided to checkpoint some time
in the future.

```python
# Checkpoints immediately
trick.checkpoint()

# Checkpoints at an absolute time
trick.checkpoint(100.0)

# Checkpoints 5 seconds relative from the current sim_time
trick.checkpoint(trick.exec_get_sim_time() + 5.0)
```

## Stopping the Simulation

To shutdown a simulation call trick.stop([<stop_time>]).  trick.stop() called with no
arguments will shutdown immediately.  An optional stop time may be provided to shutdown some time
in the future.

```python
# Stop immediately
trick.stop()

# Stop at an absolute time
trick.stop(100.0)

# Stop 5 seconds relative from the current sim_time
trick.stop(trick.exec_get_sim_time() + 5.0)
```

## Events and Malfunctions

Trick 10 events are a hybrid of Trick 07 events and malfunctions. A Trick 07 event has one or more conditions, one action, and is evaluated by the input processor. A Trick 07 malfunction also has one or more conditions (called triggers) that you can disable/enable, multiple actions, manual mode, and is evaluated before/after a specified job. Multiple conditions in malfunctions are ORed in 07, while multiple conditions in events can be specified by the user as being ORed or ANDed.  Here is the Python syntax showing how Trick 10 events implement all of this functionality.

For information on how Trick processes events during runtime, see [Event Processing](/trick/documentation/simulation_capabilities/Event-Manager).

### Basic Event Usage

```python
# Create an event that can be viewed and manipulated in MTV, and can be checkpointed
<event name> =  trick.new_event("<event name>")
# Alternatively, you can create an unnamed event (hidden in MTV and not checkpointable)
<event name> =  trick.new_event()

# Set the event condition
# (note that because there can be multiple conditions, you must specify a condition index starting at 0)
# The number of conditions an event can have is unlimited 0...n
# When an (enabled) event condition is true, we say it has "f
