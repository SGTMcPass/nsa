### Events/Malfunctions Trick View > Launching > The MTV GUI (in Edit Mode)

| [Home](/trick) → [Documentation Home](../../Documentation-Home) → [Running a Simulation](../Running-a-Simulation) → [Runtime GUIs](Runtime-GUIs) → Malfunctions |
|------------------------------------------------------------------|

## Events/Malfunctions Trick View
Events/Malfunctions Trick View (hereafter referred to as MTV) is a graphical user interface that has two main functions:

1. to view/control Trick-managed event activity while the simulation is running, and
1. to create/edit Trick-managed events for saving to a file or for sending directly to a running simulation.

"Malfunctions" is a legacy term from when events and malfunctions were separate entities in a previous version of Trick. The functionality of both malfunctions and events have been combined and simply called "Events".

### Launching
Typically MTV is launched via the Actions menu in the @ref SimControlPanel "Simulation Control Panel". MTV will then load and display any events you've defined in your Run input file:

![MTV Launch](images/mtv_launch.jpg)

If you want MTV to launch every time you run a simulation, you can automatically launch MTV each run by coding the following in your Run input file:
```
trick.malfunctions_trick_view_set_enabled(1)
```
MTV can also be launched from the command line via:
```
mtv <hostname> <port>
```
The mtv launch script is located in $TRICK_HOME/bin. If you only want to use MTV to create/edit a new event, you can simply type:
```
mtv
```
on the command line in your simulation directory (without the <hostname> or <port> arguments). You can save your newly created event to a file but you of course can't send it to a running simulation in this mode (See @ref MTV_send_to_sim "Send To Sim Button" below).

For additional launching options, see  "Automatically Launching Applications".

### The MTV GUI (in View Mode)
MTV has two main screens, one for viewing events in a running simulation (View Mode), and one for creating / editing events (Edit Mode). The MTV GUI pictured below is in **View** Mode. It may have a different look and feel based on the architecture of the machine on which it is running,
but the functionality will remain the same.

![MTV View](images/mtv_view.jpg)

#### View/Edit Tab
Click the "View" Tab to view the events for a running simulation (View Mode). Click the "Edit" Tab to create / edit an event (Edit Mode).

#### Some Background on Event Processing
There is a Trick job called process_event() that is run near the top of the execution frame to evaluate all "Added" events. See @ref Event_Processing "Event Processing" for more details.

#### Event / Condition / Action Active Toggle
The 1st column in View Mode
