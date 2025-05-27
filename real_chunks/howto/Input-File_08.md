### Accessing Simulation Parameters > I Just Want to Know How Do I Set this Value...

>")
# Alternatively, you can create an unnamed event (hidden in MTV and not checkpointable)
<event name> =  trick.new_event()

# Set the event condition
# (note that because there can be multiple conditions, you must specify a condition index starting at 0)
# The number of conditions an event can have is unlimited 0...n
# When an (enabled) event condition is true, we say it has "fired"
<event name>.condition(<index>, "<input text string>" [,"<optional comment displayed in mtv>"])

# Set the condition evaluation such that ANY fired condition will cause all of this event's (enabled) actions to run
# (conditions are ORed -- this is the default)
<event name>.condition_any()
# Set the condition evaluation such that ALL (enabled) conditions must fire to cause all of event's (enabled) actions to run
# (conditions are ANDed)
<event name>.condition_all()

# Set the frequency that the event condition(s) will be evaluated at
<event name>.set_cycle(<cycle time in seconds>)

# Set the event action to occur when any/all condition(s) have fired
# (again specify an index because there can be multiple actions)
# The number of actions an event can have is unlimited 0...n
<event name>.action(<index>, "<input text string>", [,"<optional comment displayed in mtv>"])

# Set the event active so that it is processed (default is not active, and event is also deactivated when fired)
<event name>.activate()     # the opposite would be <event name>.deactivate()
# Note that your event will be a one-time thing unless you put the activate statement in your action
# This behavior can be overridden using "manual mode" described below

# Add the event to the input processor's list of events (it will be processed at top of frame before scheduled jobs)
trick.add_event(<event name>)

# Tell trick whether to terminate the sim if an error occurs while parsing Python code. Defaults to False
trick.terminate_on_event_parse_error(<True|False>)
```

### Advanced Event (Malfunction) Usage

```python
# Insert the event before/after a "target" job so that it is evaluated then (as opposed to top of frame)
# Note that the event cycle is ignored in this case, the event takes on the cycle time of the target job
# Also note that an event can be inserted before/after multiple target jobs,
# in which case it will be evaluated multiple times per frame
# The job name string is the "sim_object.job_name" from the S_define file.
# The job instance is used to specify which instance of the job to use if identically named jobs are
# multiply defined in a sim object.  If the argument is not specified, the first instance of the is the default
