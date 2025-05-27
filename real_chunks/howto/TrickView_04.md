### Launching > Automatically Opening Files > TV Files

 in red. Such a variable's value and units cannot be changed, but its name can still be modified for the purpose of adding new variables.

#### Manual Entry Field

The manual entry field provides the user a means by which to directly add a variable of any name. This is useful if a variable's information is not present in the S_sie.resource file or the file itself is not present, or if the variable is a pointer to the beginning of an array. Multiple elements of an arrayed variable can be added by specifying the range within the brackets, such as:

`ball.obj.state.output.position[0-1]`

Note that pointers cannot be dereferenced using the pointer dereference operator (*) in TV. Instead, the user should treat the pointer as a single-element array and append the variable's name with `[0]`.

#### Purge Button

The purge button removes all variables from the variable table that have a value of **\<Invalid Reference\>**.

#### Resolve Button

The resolve button submits a request to the Variable Server to attempt to resolve all invalid references to legal values, which can be useful if a previously null pointer has become valid.

#### Connection Status Bar

The connection panel displays host and port information when TV is connected to a simulation. When disconnected, clicking on the combo box displays a list of available simulations to which to connect. Alternately, the information can be entered directly into the panel in the form of `host:port`.

#### Clearing Logged Data

TV records the value of every variable in the variable table each time the Variable Server sends a report. This allows newly launched strip charts to include data going back all the way to the point at which the variable was first added. This can eventually result in a large amount of memory usage. If performance begins to degrade, you can clear the log of all values via the **Action** menu of either TV or any strip chart. Note that this will erase any data currently being displayed on any strip charts.

#### Settings

The Settings dialog can be accessed via the **File** menu and allows the user to alter the behavior of TV.
See [[Runtime GUIs]] for a detailed description of Application Behavior and Cycle Period options.

![](images/Settings.png)

##### Variable Tree Order

The order in which the variable hierarchy is displayed has three options:

- **None**
  Top-level variables are sorted alphabetically A to Z. Lower-level variables are sorted according to their order of declaration within the simulation.

- **Ascending Alphabetical**
  Variables are sorted alphabetically A to Z.

- **Descending Alphabetical**
  Variables are sorted alphabetically Z to A.

##### Variable Addition

The placement of newly added variables within the variable table is specified via the Position combo box. The available options are **Top**, **Before**, **After**, and **Bottom**. The **Before** and **After** options are relative to the currently selected row.

Character pointers and arrays can be
