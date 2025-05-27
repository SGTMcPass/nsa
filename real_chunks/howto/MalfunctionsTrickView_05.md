### Events/Malfunctions Trick View > Launching > The MTV GUI (in Edit Mode)

 the user can enter the appropriate host name and port number into these text fields and click the Connect button at the right to connect to a running simulation. (The port number is the Trick variable server port number that can be found on the bottom of the "Simulation Control Panel" if it is up.)

### The MTV GUI (in Edit Mode)
MTV has two main screens, one for viewing events in a running simulation (View Mode), and one for creating / editing events (Edit Mode). The MTV GUI pictured below is in **Edit** Mode.

![MTV Edit](images/mtv_edit.jpg)

#### View/Edit Tab
Click the "Edit" Tab to create / edit an event (Edit Mode). Click the "View" Tab to view the events for a running simulation (View Mode).

#### Event Name Text Field
When you first bring up the Edit Mode screen in MTV, the Event Name string is set to "put_new_event_name_here". You must enter a new Event Name string here before you can begin to edit the event.  Note that you must press the "Enter" key on your keyboard to register the new Event Name and enable the "Event Syntax" and "User Data" areas.

#### Event Syntax Area
Once you've entered an Event Name, MTV will automatically generate a default set of commands to configure your new event. The part of the commands shown under the Event Syntax column on the left is not editable. You can add or delete commands using the "Edit Menu" described below.

#### User Data Area
The part of the event commands shown under the User Data column on the right is editable. You can double click the User Data text you want to change and enter in whatever you want. Note that there is no means of checking your syntax, so if you enter incorrect syntax, you won't find out until you send the event to your simulation and it is evaluated by Trick during execution. A Python syntax error in your event will be printed to the screen and looks something like this:
```
File "<string>", line 1
  trick_ip.ip.return_val = XXX
SyntaxError: unexpected EOF while parsing
```

Where "XXX" is the offending string from your event command.

#### Send To Sim Button
When you have created and edited an event to your satisfaction, you can click the Send To Sim button to the right of the Event Name to send the new event to a connected simulation. Trick will read in the new event and it will be displayed in the MTV View Mode window.

#### File Menu
You can select Save Event from the File Menu if you want to save your newly created event to a file. If you don't do this, it will be lost once you quit MTV or when your connected simulation terminates.

Currently there is no way to Load Event(s) from a file into the MTV editor. It is strictly for creating new events from scratch.

#### Edit Menu
##### Create New Event
If you select
