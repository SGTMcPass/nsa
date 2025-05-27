### Accessing Simulation Parameters > I Just Want to Know How Do I Set this Value...

index>)

# Use a model job as an action
# It is more optimal to use model code as an action, because of the python parsing involved in a normal action()
<event name>.action_job(<index>, "<job name>" [,"<optional comment displayed in mtv>"])
# Turn a model job ON/OFF as an action
<event name>.action_job_on(<index>, "<job name>" [,"<optional comment displayed in mtv>"])
<event name>.action_job_off(<index>, "<job name>" [,"<optional comment displayed in mtv>"])
# Any combination of action(), action_job(), action_job_on(), or action_job_off() can be used for your malfunction action(s).
# NOTE: If the job is something you created just for use in malfunctions (e.g. it is not a scheduled job),
        then it must be specified once and only once in the S_define file as a "malfunction" class job.

# Disable an action from being run (default is enabled)
<event name>.action_disable(<index>)     # the opposite would be <event name>.action_enable(<index>)

# Manually fire the event once now, so that its actions will run once now
# (this event is now in "manual mode" and its conditions will not be evaluated until manual_done commanded)
<event name>.manual_fire()

# Manually set an event as fired and hold on, so that its actions will run each cycle
# (this event is now in "manual mode" and its conditions will not be evaluated until manual_done commanded)
<event name>.manual_on()

# Manually set an event as not fired, so that its actions will not run
# (this event is now in "manual mode" and its conditions will not be evaluated until manual_done commanded)
<event name>.manual_off()

# Exit "manual mode" for this event and return to normal processing of its conditions
<event name>.manual_done()
```

### Setting variables synchronously: Real Time Variable Injector

You can also use `rti_add`/`rti_fire` commands in your event action syntax (or as standalone commands in the input file or
via the variable server) to set variables. See "Real Time Variable Injector".

### Accessing the current Event state

```python
<event name>.condtion_fired(<index>)          # boolean:  test if a particular event condition fired this cycle
<event name>.condition_fired_count(<index>)   # integer:  number of times a particular event condition has fired
<event name>.condtion_fired_time(<index>)     # double:   last sim time a particular event condition has fired
<event name>.action_ran(<index>)              # boolean:  test if a particular event action ran this cycle
<event name>.action_ran_count(<index>)        # integer:
