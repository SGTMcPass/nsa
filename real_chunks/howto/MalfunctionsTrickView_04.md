### Events/Malfunctions Trick View > Launching > The MTV GUI (in Edit Mode)

 the need to use many events, you may want to create event "groups" by defining your events in the Run input file using Python classes. For instance, the events `mygroup.this_event` and `mygroup.that_event` shown in the MTV GUI picture above were defined like this :

```python
   class MyGroup:
       this_event = trick.new_event("mygroup.this_event")
       this_event.condition(0, "test.obj.run_status<1")
       this_event.action(0, "trick.freeze()")
       this_event.action(1, "test.obj.run_status=1")
       this_event.activate()
       trick.add_event(this_event)
       that_event = trick.new_event("mygroup.that_event")
       that_event.condition(0, "test.obj.run_status>1")
       that_event.action(0, "trick.run()")
       that_event.activate()
       trick.add_event(that_event)
   mygroup = MyGroup()
```

The Customize Event Display popup will recognize such event groups and allow you to select / deselect events by group name. It will contain a Tab for each  event group labeled with the group name; events that do not belong to any group will be in a Tab labeled "Events".

![MTV Customize](images/mtv_customize.jpg)

You may notice some events named "no_name_specified". These are either events created for `add_read()` statements in the Run input file, or events created by the `new_event()` command when no name string was passed in. By default MTV does not display unnamed events, but you can display them if you want by selecting them in Customize Event Display.

#### Cycle Menu
The Cycle Menu allows you to set how fast the MTV GUI receives updates from the simulation it is connected to. The default cycle update rate is 0.50, but the Cycle Menu lets you pick from 0.05 (fastest) to 1.0 (slowest).

#### Connection Status Bar
At the bottom of the MTV GUI is the Connection Status Bar. At the far left of the bar is an area where status messages are displayed. It normally says "Connected" or "Disconnected" depending on if MTV is connected to a running simulation. When the MTV GUI display updates the events being displayed (at startup or after you selected Customize Event Display), each event name will be briefly displayed in this status message area while loading.

There are two text fields containing the host name and port number of the connected simulation. When not connected, the user can enter the appropriate host name and port number into these text fields and click the Connect button at the right to connect to a running simulation. (The port number is the Trick variable server port number that can be found on the bottom of the "Simulation Control Panel" if it is up.)

### The MTV GUI (in Edit Mode)
MTV has two main screens, one for viewing events in a running simulation (View Mode), and one
