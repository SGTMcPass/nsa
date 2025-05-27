### Trick DP - Data Products Application > Viewing Data > Using External Program

 error window will be shown.
        - Only one variable can be added to a varcase and by default, the X variable is sys.exec.out.time.
        - A variable from Vars can be dragged over sys.exec.out.time to replace it.
        - Also, a variable from Vars can be added to a varcase by dragging it over the varcase node.
- <b>Remove</b>
    - Removes this variable.
        - X variable can not be removed.
        - X variable can be replaced.
        - Y variable can be removed.
        - Y variable can not be replaced. You need to simply remove the Y variable, and then add a new variable.

##### DP Content Popup Menus

![trick_qp_dpcontent_popup7](images/trick_qp_dpcontent_popup7.jpg)

- <b>New Table</b>
    - Creates a new table without any columns.
- <b>Remove All Tables</b>
    - Removes all tables.

##### DP Content Popup Menus

![trick_qp_dpcontent_popup8](images/trick_qp_dpcontent_popup8.jpg)

- <b>Add Var</b>
    - Adds highlighted variables from Vars to this table. Each variable represents a column.
- <b>Remove</b>
    - Removes this table.

##### DP Content Popup Menus

![trick_qp_dpcontent_popup9](images/trick_qp_dpcontent_popup9.jpg)

- <b>Remove</b>
    - Removes this column.

##### DP Content Popup Menus

![trick_qp_dpcontent_popup10](images/trick_qp_dpcontent_popup10.jpg)

- <b>Remove</b>
    - Removes the this hightlighted variable.
    - Also removes the column which it belongs to as each column has only on variable associated with it.

##### DP Content Popup Menus

![trick_qp_dpcontent_popup11](images/trick_qp_dpcontent_popup11.jpg)

- <b>New Program</b>
    - Adds a new PROGRAM.
    - See External Programs for more details about a program.
- <b>Remove All Programs</b>
    - Removes all programs. Currently only one program is supported.

##### DP Content Popup Menus

![trick_qp_dpcontent_popup12](images/trick_qp_dpcontent_popup12.jpg)

- <b>Remove</b>
    - Removes the program.

##### DP Content Popup Menus

![trick_qp_dpcontent_popup13](images/trick_qp_dpcontent_popup13.jpg)

- <b>Add Var</b>
    - Adds highlighted variables from Vars to Input.

##### DP Content Popup Menus

![trick_qp_dpcontent_popup14](images/trick_qp_dpcontent_popup14.jpg)

- <b>Remove</b>
    - Removes the highlighted variable.

##### DP Content Popup Menus

![trick_qp_dpcontent_popup15](images/trick_qp_dpcontent_popup15.jpg)

- <b>New Output</b>
    - Brings up a window for users to enter the output name for the program.

![trick_qp_dpcontent_popup16](images/trick_qp_dpcontent_popup16.jpg)

- Accepts the entered name by clicking Ok and the output name will be added to Vars in red such as "out" as shown .

![trick_qp_dpcontent_popup17](images/trick_qp_dpcontent_popup17.jpg)

#### Trick QP Run Selections
All selected RUN directories for retriving data from for plotting are listed here.

![trick_qp_runs_area](images/trick_qp_runs_area.jpg)
##### Runs Popup Menus

Right clicking on a RUN from the list brings up a corresponding popup menu.

![trick_qp_runs_popup1](images/trick_qp_runs_popup1.jpg)

- <b>Remove</b>
    - Removes all of highlighted RUN from the list.
- <b>Configure Time Name...</b>
    - Brings up the following input dialog to let users to configure the RUN's time name.
    - By default, RUN's time name is sys.exec.out.time

![trick_qp_runs_selections_input_timename](images/trick_qp_runs_selections_input_timename.jpg)
##### Property Notebook

All editable data entries for the selected node from DP Content are displayed here.
You are required to click <b>Apply Change</b> button to save all the changes made.
Otherwise, all changes will be lost if browsing a different node and come back to it.
<b>Trick QP - Property Notebeook</b>

![trick_qp_notebook_area](images/trick_qp_notebook_area.jpg)

##### Message Display

This display redirects all screen printout to here to let users know what it is been doing or what has gone wrong.
<b>Trick QP - Message Display</b>

![trick_qp_msg_area](images/trick_qp_msg_area.jpg)

##
