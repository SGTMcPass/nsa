### Trick DP - Data Products Application > Viewing Data > Using External Program

.time

![trick_run_selections_input_timename](images/trick_run_selections_input_timename.jpg)

##### DP Selections

All selected DP files that tell data products how and what to display in plots and tables are listed here.
<b>Trick DP - DP Selections</b>
![trick_dp_dpselections_area](images/trick_dp_dpselections_area.jpg)

##### DP Selections Popup Menus

Right clicking on a DP file from the list brings up a popup menu.

![trick_dp_selections_popup1](images/trick_dp_selections_popup1.jpg)

- <b>Edit DP...</b>
    - Opens the selected DP file with Quickplot application for editing.
- <b>Remove</b>
    - Removes all of highlighted DP files from the list.
- <b>Remove All</b>
    - Removes all DP files from the list.

##### Message Display

This display redirects all screen printout to here to let users know what it is been doing or what has gone wrong.
<b>Trick DP - Message Display</b>
![trick_dp_msg_area](images/trick_dp_msg_area.jpg)

## Trick QP - Quickplot Application

The trick_qp is designed for a quick peek at data in a particular RUN. It is also designed to create the DP specification
files that the trick_dp uses. Quickplot usage can be abused. It is best to take time to make a DP specification file using
Quickplot, then use the trick_dp for plotting. To launch the quickplot program:

```
<b>UNIX Prompt></b> trick_dp
```

Select a RUN directory (or multiple RUN directories if comparing data sets).
Click the blue lightning bolt icon to launch Quickplot.

OR

```
<b>UNIX Prompt></b> trick_qp RUN<name> &
```

### Trick QP GUI

![trick_qp](images/trick_qp.jpg)

Similar to Trick DP, the graphical user interface of Trick QP also contains the menu bar, toolbar and five display areas
as shown in the above image. The interface is explained with further details in the following sections:

- Menu bar
- Toolbar
- Display areas

#### Menu bar

This table shows all of the menus along with their menu items and functionalities related to the Trick QP menu bar:

#### Trick QP File Menu

![trick_qp_file_menu](images/trick_qp_file_menu.jpg)

- <b>New DP...</b>
    - Starts a new DP file.
- <b>Open DP...</b>
    - Brings up the Open File dialog box to let the user to open a DP file.
- <b>Refresh...</b>
    - Refreshes all variables in "Vars" area.
- <b>Save...</b>
    - Saves to the currently opened DP file if available, otherwise, users can sepecify a file to save to.
- <b>Save As...</b>
    - Brings up the Save File dialog box to let the use to save to a specified DP file.
- <b>Look and Feel</b>
    - Changes the Look and Feel for the GUI.
- <b>Show Exit Confirmation Prompt</b>
    - Toggles whether to show the Confirm Exit dialog box before exiting the GUI.
- <b>Exit</b>
    - Exits the GUI. If Show Exit Confirmation Prompt is checked, Confirm Exit dialog box would be displayed. Otherwise, exits immediately.

#### Trick QP Vars Menu

![trick_qp_vars_menu](images/trick_qp_vars_menu.jpg)

- <b>Add Var</b>
    - Adds the Vars highlighted variables to DP Content on the right.
        - If nothing is highlighted or if "Plots" is highlighted:
            - One plot per page for each selected variable will be created.
        - If "Tables" is highlighted:
            - One table with each variable representing one column will be created.
        - If "Programs" is highlighted :
            - Nothing will happen.
        - If any sub node of "Plots", "Tables", or "Programs" is highlighted:
            - Variables will be added to the corresponding node if possible.
- <b>Expand Var</b>
    - Expands the Vars highlighted variables.
- <b>Contract Var</b>
    - Collaps the Vars highlighted variables.
- <b>Change Units...</b>
    - Prompts for changing highlighted variables (first one if multiple variables selected) units.

#### Trick QP Runs Menu

![trick_qp_runs_menu](images/trick_qp_runs_menu.jpg)

- <b>Add Run...</b>
    - Adds the highlighted RUN directory to "Runs" area.
- <b>Remove Run</b>
    - Removes all highlighted RUN directories from "Runs" area.

#### Trick QP Plots Menu

![tr
