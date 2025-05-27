### Trick DP - Data Products Application > Viewing Data > Using External Program

.
- <b>Contrast Plot...</b>
    - Displays a comparison plot and a delta plot on the same page.
- <b>Table...</b>
    - Displays selected variable data in a table.
- <b>Table Error...</b>
    - TBD.
- <b>GNUplot Postscript Single Plot...</b>
    - TBD.
- <b>GNUplot Postscript Comparison Plot...</b>
    - TBD.
- <b>GNUplot Postscript Error Plot...</b>
    - TBD.
- <b>Quickplot</b>
    - Launches the Quickplot application.
- <b>Create PDF Booklet...</b>
    - Allows users to view, merge, or create a PDF file for the selected postscript file(s).

#### Trick DP Help Menu

![trick_dp_help_menu](images/trick_dp_help_menu.jpg)

- <b>Help Contents</b>
    - Brings up on-line help.
- <b>About...</b>
    - Shows the information about this application.

### Toolbar

![trick_dp_toolbar](images/trick_dp_toolbar.jpg)

These icon buttons eables easier access to those commonly used functions. The functionality of each button is the same as
the menu item that shares the same icon. A tooltip of the button will be displayed if moving the mouse pointer over any
of these buttons.

### Display areas

There are 5 display areas that are Sims/Runs Tree (upper left), DP Tree (upper right),
Run Selections (middle left), DP Selections (middle right) and the bottom is
a message display area.

Please note that all sim directories start with <b>SIM</b>, all run directories starts with <b>RUN</b> or <b>MONTE_RUN</b>, and
all data product files start with <b>DP</b> and are placed in <b>DP_Product</b> directory within a <b>SIM</b> directory.

#### Sims/Runs Tree

Launching trick_dp in a directory that contains SIM directories will cause those SIM directories to be displayed
in this area as shown below. If no SIM directories exist in the launch directory, trick_dp will display SIMs from
$TRICK_USER_HOME by default. If $TRICK_USER_HOME is not defined, SIMs from $HOME will be displayed. If this is not
the first time to run trick_dp on this machine, all previously imported SIMs will be displayed also.

SIMs initially appear unexpanded in the Sims/Runs Tree. Double clicking a SIM node or
single clicking the node icon on the left will show runs contained in that SIM. Runs in black contain data and
in grey contain no data.

<b>Trick DP - Sims/Runs Tree</b>

![trick_dp_simrun_area](images/trick_dp_simrun_area.jpg)

#### Sims/Runs Tree Popup Menus

![trick_dp_simrun_popup1](images/trick_dp_simrun_popup1.jpg)

- <b>Refresh</b>
    - Refreshes the highlighted directory.
- <b>Opentree</b>
    - Expands the highlighted directory.
- <b>Closetree</b>
    - Collapses the highlighted directory.
- <b>Remove</b>
    - Removes the highlighted directory from the tree. It does not physically remove the directory from your file system.

#### Sims/Runs Tree Popup Menus

![trick_dp_simrun_popup2](images/trick_dp_simrun_popup2.jpg)

- <b>Add run(s)</b>
    - Adds all RUN directories that contains data in all highlighted SIM directories to the "Run Selections" area.
- <b>Read DP List</b>
    - Adds all DP files in that SIM directory to the DP Tree area if any of RUN directories in that
      SIM directory contains data.
- <b>Refresh</b>
    - Refreshes the highlighted directory.
- <b>Opentree</b>
    - Expands the highlighted directory.
- <b>Closetree</b>
    - Collapses the highlighted directory.
- <b>Remove</b>
    - Removes the selected directory from the tree. It does not physically remove the directory from your file system.

##### Sims/Runs Tree Popup Menus

![trick_dp_simrun_popup3](images/trick_dp_simrun_popup3.jpg)

- <b>Add run(s)</b>
    - Adds all highlighted RUN directories that contains data to the "Run Selections" area.
- <b>Quickplot...</b>
    - Launches the Quickplot application.
- <b>Run Sim</b>
    - Runs the sim from each sim directory using the input.py from the corresponding highlighted RUN directory.

##### DP Tree

DP files in DP_Product of SIM directories are displayed here in a
