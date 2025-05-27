### Events/Malfunctions Trick View > Launching > The MTV GUI (in Edit Mode)

 events for a running simulation (View Mode). Click the "Edit" Tab to create / edit an event (Edit Mode).

#### Some Background on Event Processing
There is a Trick job called process_event() that is run near the top of the execution frame to evaluate all "Added" events. See @ref Event_Processing "Event Processing" for more details.

#### Event / Condition / Action Active Toggle
The 1st column in View Mode is the Active Toggle.
* Clicking an Active toggle button for an **Event** will make that Event active/inactive in Normal mode.
* Clicking the Active toggle for a **Condition** will make that Condition active/inactive in Normal mode.
* Clicking the Active toggle for an **Action** will make that Action active/inactive in both Normal and Manual mode.

#### Event Name, Conditions and Actions
The 2nd column in View Mode is the event name. Each event name is shown on a gray line in the MTV display.
The name is the string that was passed to the `new_event()` command. The event's condition(s) are listed next, followed by the event's action(s). The first 50 characters of each condition/action string are shown, unless the optional comment was passed to the `condition()` or `action()` command. If the comment was specified, it is what will be displayed as the condition or action name. The number in parentheses shown in each condition / action is the index number (from 0..n) used in the `condition()` or `action()` command.

#### Event Fired & Ran Status
Columns 3, 4, 5, and 6 in View Mode show when and how many times the event and its components fired/ran.
* A **Condition** fires when it is Active in Normal mode and is evaluated as true.
* An **Event** fires when it is Active in Normal mode and its condition(s) are evaluated as true, or when it is in Manual mode and the command issued is either `manual_fire()` or `manual_on()`.
* An **Action** runs if it is Active and the event fires. An event runs when at least one of its actions runs.

#### Condition Hold Toggle
The 7th column in View Mode is the Hold toggle, only valid for Conditions. Clicking the Hold toggle on a Condition will turn on/off the Hold status for that condition. If Hold is on, when the condition evaluates to true it will be "held" as true so that the condition will fire each time it is evaluated.

#### Event Mode
The 8th column in View Mode is the Event Mode selector:

1. **Normal** The default, event conditions are evaluated to determine when the event fires (issues a `manual_done()` command).
1. **Manual FIRE** Fire the event once now, remain in manual OFF mode (issues a `manual_fire()` command).
1. **Manual ON
