### Events/Malfunctions Trick View > Launching > The MTV GUI (in Edit Mode)

 then click Added to add it later, MTV will remember where it was and will add the event back in the same position before or after the model job you removed it from.

So when you click on the Added Toggle to check it, the event is added using either `add_event()`, `add_event_before()`, or  `add_event_after()`.

#### Colors Used in MTV
1. **Black font** An event in Normal mode that is both Active and Added, having been added using the `add_event()` command.
1. **Brown font** An event in Normal mode that is both Active and Added, having been added using the `add_event_before()` or `add_event_after()` command.
1. **Gray font** An event that is either not Active or not Added, or a condition/action that is not Active (this color overrides the previous two colors).
1. **Blue font** An event in Manual mode (this color overrides the previous three colors, except that actions can be inactive in Manual mode, so inactive actions will be gray).
1. **Red background** An event's Fired Time column is highlighted in red when it fires.
1. **Green background** An event's Ran Time column is highlighted in green when it runs.

#### File Menu
You can select Load Event(s) from the File menu to have Trick read in a file containing one or more events when MTV is connected to a simulation. MTV will then add the newly loaded events to the View Mode window.

#### View Menu
##### Delete Event
If you select an event row in the MTV display, then select Delete Event from the View Menu, you can delete an event permanently from the simulation you are connected to. MTV will remove the event from the display and you can no longer reference that event during the simulation. This will NOT delete any file where the event was loaded from.  The event object itself will be deleted from memory in the running simulation.

##### Customize Event Display
Selecting Customize Event Display from the File Menu will pop up a window where you can select which events you want MTV to display. This is handy when your simulation contains many events and the display window cannot display them all without scrolling. The default is for MTV to display all events contained in the running simulation, up to a maximum of 500. If your simulation has more than 500 events, you must use Customize Event Display to choose a set of 500 or fewer events to display (only the first 500 loaded will initially be shown).

If you have the need to use many events, you may want to create event "groups" by defining your events in the Run input file using Python classes. For instance, the events `mygroup.this_event` and `mygroup.that_event` shown in the MTV GUI picture above were defined like this :

```python
   class MyGroup:
       this_event = trick.new_event("mygroup.this_event")
       this_event.condition(0, "test
