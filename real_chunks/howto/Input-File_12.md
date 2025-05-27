### Accessing Simulation Parameters > I Just Want to Know How Do I Set this Value...

("over100_event")
over100_event.condition(0, "vel_event.condition_fired(1)")
over100_event.action(0, "trick.as_pyfloat(ball.obj.state.output.velocity) = 0.0")
over100_event.action(1, "trick.stop()")
over100_event.action(2, "over100_event.activate()")
over100_event.action_disable(1)
over100_event.activate()

change_event = trick.new_event("change_event")
change_event.condition(0, "trick.exec_get_sim_time() > 500.0")
change_event.action(0, """
over100_event.action_disable(0)
over100_event.action_enable(1)
vel_event.condition(1, "trick.as_pyfloat(ball.obj.state.output.velocity) > 200.0")
""")
change_event.activate()

trick.add_event_before(vel_event, "ball.obj.state_integ")
trick.add_event_before(change_event, "ball.obj.state_integ")
trick.add_event_after(over100_event, "data_record_group1.Ball")
```

## Trick Specific Python Usage

Many of Trick's functions can be called using Python commands in the input file (or via the variable server)
to perform various operations or to customize/configure Trick.

## I Just Want to Know How Do I Set this Value...

[Continue to Runtime GUIs](runtime_guis/Runtime-GUIs)
