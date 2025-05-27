### Trick DP - Data Products Application > Viewing Data > Using External Program

| [Home](/trick) → [Documentation Home](../Documentation-Home) → [Data Products](Data-Products) → Data Products GUIs |
|------------------------------------------------------------------|

There are two main GUIs for viewing Trick logged data:

- TrickDP
- TrickQP

These two applications work together and allow the user to plot and tabularize Trick data.

- Viewing Data

This section gives various examples of viewing Trick logged data using Trick DP and Trick QP.

## Trick DP - Data Products Application

The trick_dp (data products) is designed to make use of data product specification files (DP files). DP specification
files are input files which tell data products how and what to display in plots and tables. If time is taken to create the DP
specification files, this tool shows its power in perusing large sets of data. The "Help" menu option on the GUI also gives
detailed information on its use. To launch the program:

- <b>UNIX Prompt></b> trick_dp&


## Trick DP GUI

![trick_dp](images/trick_dp.jpg)

The graphical user interface of trick_dp contains the menu bar, toolbar and five display areas
as shown in the above image. The interface is explained with further details in the following sections:

- Menu bar
- Toolbar
- Display areas


### Trick DP Menu bar

#### Trick DP Session Menu

![trick_dp_session_menu](images/trick_dp_session_menu.jpg)

- <b>New...</b>
    - Starts a new session.
- <b>Open...</b>
    - Brings up the Open File dialog box to let the user to open a session file.
- <b>Save...</b>
    - Brings up the Save File dialog box to let the user to save the current session to a file.
- <b>Refresh...</b>
    - Refreshes the Sims/Runs Tree.
- <b>Look and Feel</b>
    - Changes the Look and Feel for the GUI.
- <b>Show Exit Confirmation Prompt</b>
    - Toggles whether to show the Confirm Exit dialog box before exiting the GUI.
- <b>Exit</b>
    - Exits the GUI. If Show Exit Confirmation Prompt is checked, Confirm Exit dialog box would be displayed. Otherwise, exits immediately.

#### Trick DP Simrun Menu

![trick_dp_simrun_menu](images/trick_dp_simrun_menu.jpg)

- <b>Import Sim Dir...</b>
    - Imports a SIM dir that will be added to the Sims/Runs Tree area.
- <b>Add Run Dir...</b>
    - Adds the selected RUN dir to the Run Selections area.

<b>Data Product</b>

![trick_dp_dataproduct_menu](images/trick_dp_dataproduct_menu.jpg)

- <b>Add DP...</b>
    - Adds the selected DP file to the "DP Selections" area.
- <b>Edit DP...</b>
    - Edits the selected DP file by opening up the Quickplot Application.
- <b>Filter...</b>
    - Filters the displayed "DP Tree" so that is shows only DP files that contain the specified characters.

![trick_dp_settings_menu](images/trick_dp_settings_menu.jpg)
- <b>Device</b>
    - This option sets where the plot should go to. 3 available options are:
        - Terminal (by default)
        - Printer
        - File
- <b>Plot Utility</b>
    - This option sets which plotting utility to use. 2 available options:
        - Fermi
        - Gnuplot

#### Trick DP Actions Menu

![trick_dp_actions_menu](images/trick_dp_actions_menu.jpg)

- <b>Single Plot...</b>
    - Displays the data products independently for all data sets specified.
- <b>Comparison Plot...</b>
    - Displays the data from all data sets in the same display.
- <b>Error Plot...</b>
    - Subtracts the nth data set data from the first data set data and presents the result for data set 2 through n in the same display.
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
    - Allows users to view, merge, or create a PDF file
