### Trick DP - Data Products Application > Viewing Data > Using External Program

 will be added to the corresponding node if possible.
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

![trick_qp_plots_menu](images/trick_qp_plots_menu.jpg)

- <b>New Page</b>
    - Adds an empty new page.
- <b>Remove All Pages</b>
    - Removes all currently shown pages.
- <b>New Plot</b>
    - Adds a new empty plot to the currently selected page.
- <b>New Curve</b>
    - Adds a new empty curve to the currently selected plot.
- <b>New Varcase</b>
    - Adds a new varcase to the currently selected curve.

#### Trick QP Tables Menu

![trick_qp_tables_menu](images/trick_qp_tables_menu.jpg)

- <b>New Table</b>
    - Adds a new empty table.
- <b>Remove All Tables</b>
    - Removes all tables.
- <b>New Column</b>
    - Adds a new empty column to the currently selected table.

#### Trick QP Programs Menu

![trick_qp_programs_menu](images/trick_qp_programs_menu.jpg)

- <b>New Program</b>
    - Adds a new empty program.
    - See External Programs for more details about a program.
- <b>Remove All Programs</b>
    - Removes all programs.
- <b>New Output...</b>
    - Adds a new output for the currently selected program.

#### Trick QP Programs Menu

![trick_qp_settings_menu](images/trick_qp_settings_menu.jpg)

- <b>Plot Utility</b>
    - Selects either Fermi or Gnuplot for plotting.

#### Trick QP Programs Menu

![trick_qp_actions_menu](images/trick_qp_actions_menu.jpg)

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

#### Trick QP Programs Menu

![trick_qp_help_menu](images/trick_qp_help_menu.jpg)

- <b>Help Contents</b>
    - Brings up on-line help.
- <b>About...</b>
    - Shows the information about this application.

#### Toolbar

![trick_qp_toolbar](images/trick_qp_toolbar.jpg)

These icon buttons eables easier access to those commonly used functions. The functionality of each button is the same as
the menu item that shares the same icon. A tooltip of the button will be displayed if moving the mouse pointer over any
of these buttons.


#### Display areas

There are 5 display areas that are Vars (upper left), DP Content (upper right),
Runs (middle left), Property Notebook (middle right) and the bottom is
a message display area.


#### Vars

All variables that are found in Trick log data files from the selected RUN directories are listed here. If variables shown in red, means that they do not exist in every RUN directory.

<b>Trick QP - Vars</b>
![trick_qp_vars_area](images/trick_qp_vars_area.jpg)

#### Vars Popup Menus

Right clicking on a variable from the Vars as shown above causes a corresponding popup menu displayed. This menu is actually the same as Vars menu.

#### Vars Popup Menus

![trick_vars_popup1](images/trick_qp_vars_popup1.jpg)
- <b>Add Var</b>
    - Adds the Vars highlighted variables to DP Content on the right.
        - If nothing is highlighted or if "Plots" is highlighted:
            - One plot per page for each selected variable will be created.
        - If "Tables" is highlighted:
            - One table with each variable representing one column will be
