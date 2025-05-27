### Trick DP - Data Products Application > Viewing Data > Using External Program

plot1](images/plot1.jpg)

#### Plotting XPosition -vs- YPosition

Now, let's change the default X variable from sys.exec.out.time to a different variable.
1. Assuming the Trick QP application is still up, click the "New" plot icon located on the far left of the toolbar.
   Click "Ok" when asked if you want to start over. This will clear the plots from the DP Content.
1. Double-click dyn.cannon.pos[1].
1. Drag-n-drop the dyn.cannon.pos[0] variable over the sys.exec.out.time variable in the Plot located in the DP Content.
   You will be asked to confirm the replacement. Click "Ok".
    - Now, the X variable is dyn.cannon.pos[0] and the Y variable is dyn.cannon.pos[1].
1. To see the plot, click the white sheet icon on the toolbar.

![plot3](images/plot3.jpg)

### Creating DP Product File

The information needed for the plot created earlier can be saved off to a file using Trick QP and can be reused by both
Trick DP and Trick QP. This example shows how to save XPosition -vs- YPosition plotting stated earlier
to a file named as DP_cannon_xy.
1. With the Trick QP GUI still up and the x -vs- y position still chosen, click the dyn.cannon.pos[1]
variable located in the pane on the right. The dyn.cannon.pos[1] variable should be highlighted in dark blue.
The "Y Var" notebook page should be visible in the lower right pane.
1. In the "Y Var" notebook page, select "Symbol Style->Circle" from the drop-down menu.
1. In the "Y Var" notebook page, select "Symbol Size->Tiny" from the drop-down menu.
1. Click the "Apply Change" button (you may need to scroll up/down to see all the fields/button).
1. Save this information by clicking the menu option "File->Save As". Click "New Folder"
button to create the DP_Product folder if necessary.
Choose the directory button SIM_cannon_analytic/DP_Product". Enter file name as "DP_cannon_xy".
    - A file called DP_cannon_xy.xml is saved as it is in XML format.
1. Close the quick plot GUI, but keep trick_dp up and running.

### Plotting with only Trick DP using a DP file

Now that DP_cannon_xy has been saved, the data can be viewed with Trick DP.
1. Assuming the Trick DP is still up and running from the previous steps, Click "Session->Refresh..."
and double click SIM_cannon_analytic to reveal DP_cannon_xy.xml in the top right pane.
    - If the Trick DP is not up, go to the sim directory and launch it as:
        - <b>UNIX Prompt></b> trick_dp &
1. Make sure that Sims/Runs->SIM_cannon_analytic/RUN_test has been selected.
    - You can tell by checking to see if it is listed in Run Selections.
1. Choose the DP_cannon_xy.xml in the top right pane by double clicking it or right click followed by selecting "Add DPs".
    - This will bring the DP_cannon_xy.xml into the DP selections pane.
1. To see the trajectory again, click the plain white single sheet icon on the toolbar.
Zoom in by holding the middle mouse button and drag across a section of the plot. Then release the
mouse button. Notice that there is a tiny circle on each x-y point recorded.

![plot4](images/plot4.jpg)

### Plotting with only Trick QP

1. Go to the SIM directory we have worked on earlier and launch Trick QP as:
    - <b>UNIX Prompt></b> trick_qp RUN_test &
    - Once Trick QP is up, you should notice that:
        - "<path_to_sim_cannon_analytic>/SIM_cannon_analytic/RUN_test" is listed in Runs.
        - All logged variables found from "<path_to_sim_cannon_analytic>/SIM_cannon_analytic/RUN_test" are listed in Vars.
        - You can add more runs by clicking "Runs->Add Run..." if needed.
1. Select variables from Vars for plotting as exercises done earlier.
1. Or click "File->Open DP..." or click the open file icon on the toolbar.
    - Select a DP file such as DP_cannon_xy.xml and click "Ok".
        - If intertested file is not listed, make sure you are in the right directory.
        - The selected DP_ file is presented graphically in DP Content
1. To see the trajectory again, click the plain white single sheet on the toolbar.

###
