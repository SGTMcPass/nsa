### Trick DP - Data Products Application > Viewing Data > Using External Program

 from "<path_to_sim_cannon_analytic>/SIM_cannon_analytic/RUN_test" are listed in Vars.
        - You can add more runs by clicking "Runs->Add Run..." if needed.
1. Select variables from Vars for plotting as exercises done earlier.
1. Or click "File->Open DP..." or click the open file icon on the toolbar.
    - Select a DP file such as DP_cannon_xy.xml and click "Ok".
        - If intertested file is not listed, make sure you are in the right directory.
        - The selected DP_ file is presented graphically in DP Content
1. To see the trajectory again, click the plain white single sheet on the toolbar.

### Creating DP Session File

1. Launch Trick DP as:
    - <b>UNIX Prompt></b> trick_dp &
1. Select RUN directories from Sims/Runs Tree and add them to Run Selections.
1. Select DP files from DP Tree and add them to DP Selections.
1. Click "Session->Save..." or click save icon on the toolbar to save the current session to a DP session file.
    - By default, the session file is saved in your SIM directory.
    - A file with xml extension is saved as the session file is in XML format.


### Plotting from the Command Line
Once you a DP session file created, you can view the data the way as you specified using "fxplot" or "gxplot" command.
- Go to the SIM directory you have your session file saved.
    - <b>UNIX Prompt></b> fxplot <session_file>
    - Or
    - <b>UNIX Prompt></b> gxplot <session_file>
- You should see plots as you specified in the file.


### Using Tables

#### Using Tables Exercise A

1. Go to the SIM_cannon_analytic directory and launch Trick QP as:
    - <b>UNIX Prompt></b> trick_qp RUN_test &
    - Only using Trick QP to simply the example. In some cases, you'll still need to start "trick_dp" and then "trick_qp".
1. Click "Tables" shown under DP Content. The "Tables" node should be highlighted in blue.
    - Make sure "Tables" node is selected.
1. Double click dyn.cannon.pos[0-1] or right click it followed by selecting "Add Var".
    - A "Table" node is created under "Tables".
    - This table has 3 columns: sys.exec.out.time (added by default), dyn.cannon.pos[0], and dyn.cannon.pos[1].
1. Click the table icon on the toolbar or click "Actions->Table..." to view the data in a table.
    - You can save the current tabular data in a text file through the "Save" button on the left top corner.

![plot5](images/plot5.jpg)

#### Using Tables Exercise B

1. Go to the SIM_cannon_analytic directory and launch Trick QP as:
    - <b>UNIX Prompt></b> trick_qp RUN_test &
1. Click "Tables->New Table" or right click "Tables" under DP Content followed by selecting "New Table".
    - Now you see a new "Table" node is created under "Tables".
1. Click the newly created "Table" node. It should be highlighted in blue.
1. Right click dyn.cannon.pos[0-1] and then select "Expand Var".
1. Click dyn.cannon.pos[0] and then "Shift"+click dyn.cannon.pos[1]. These 2 variables should be highlighed in blue.
1. Right click the highlighted variables and then select "Add Var"
    - Now 2 columns are inserted to the currently selected "Table": dyn.cannon.pos[0] and dyn.cannon.pos[1].
1. Click the table icon on the toolbar or click "Actions->Table..." to view the data in a table.

![plot6](images/plot6.jpg)

### Using External Program

The external program $TRICK_HOME/trick_source/data_products/Apps/ExternalPrograms/dp_substract.c that comes with Trick distribution will be used in this section. This program takes 2 double inputs and returns the subtraction of these 2 inputs. Assuming the program is alreay built and the corresponding shared object is available for use.

1. Go to the SIM_cannon_analytic directory and launch Trick QP as:
    - <b>UNIX Prompt></b> trick_qp RUN_test &
1. Click "Programs->New Program" or right click "Programs" under DP Content followed by selecting "New Program".
    - Now you see a new "PROGRAM" node with "Input" and "Output" is created under
