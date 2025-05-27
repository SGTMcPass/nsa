### Accessing Simulation Parameters > I Just Want to Know How Do I Set this Value...

>.condition_fired_count(<index>)   # integer:  number of times a particular event condition has fired
<event name>.condtion_fired_time(<index>)     # double:   last sim time a particular event condition has fired
<event name>.action_ran(<index>)              # boolean:  test if a particular event action ran this cycle
<event name>.action_ran_count(<index>)        # integer:  number of times a particular event action has run
<event name>.action_ran_time(<index>)         # double:   last sim time a particular event action has run
<event name>.fired                            # boolean:  test if the event conditions setup evaluated to true this cycle
<event name>.fired_count                      # integer:  number of times this event has fired
<event name>.fired_time                       # double:   last sim time this event has fired
<event name>.ran                              # boolean:  test if any event action ran this cycle
<event name>.ran_count                        # integer:  number of times this event has run an action
<event name>.ran_time                         # double:   last sim time this event has run an action
<event name>.manual                           # boolean:  test if this event is in "manual mode"
<event name>.manual_fired                     # boolean:  test if this event was fired manually this cycle
```

### Event Example

Hopefully this example shows the various things you can do using events without being too confusing. Even the event components themselves can be queried and changed.

```python
# In this event example:
#    evaluate velocity before integration...
#    if it is over 50, print a message
#    if it is over 100, reset the velocity to 0 after data recording is done for this frame
#    if our sim has gone past 500 seconds, do not reset velocity when it goes over 100,
#       but instead shutdown when velocity goes over 200

vel_event = trick.new_event("vel_event")
vel_event.condition(0, "trick.as_pyfloat(ball.obj.state.output.velocity) > 50.0")
vel_event.condition(1, "trick.as_pyfloat(ball.obj.state.output.velocity) > 100.0")
vel_event.action(0, """
print "VELOCITY = ", ball.obj.state.ouput.velocity
vel_event.activate()
""")
vel_event.activate()

over100_event = trick.new_event("over100_event")
over100_event.condition(0, "vel_event.condition_fired(1)")
over100_event.action(0, "trick.as_pyfloat(ball.obj.state.output.velocity) = 0.0")
over100_event.action(1, "trick.stop()")
over100_event.action(2, "over100_event.activate()")
over100_event.action_disable(1)
over100_event.activate()

change_event = trick.new_event
