### Trick DP - Data Products Application > Viewing Data > Using External Program

_input_timename.jpg)
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

## Viewing Data

In this section, <b>SIM_cannon_analytic</b> that comes with Trick distribution and is located at $TRICK_HOME/trick_sims will be used.
Assuming you already have had corresponding data recorded by executing the related sim. The data from a single run will be viewed
using Trick DP together with Trick QP. When plotting, single plotting is used. Please see Trick Tutorial
for more examples that also have comparison or error plotting with multiple runs. You certainly can perform similar exercises using your own sim.

### Plotting With Trick DP & Trick QP

Begin by launching Trick DP.

```
<b>UNIX Prompt></b> cd <path_to_sim_cannon_analytic>/SIM_cannon_analytic
<b>UNIX Prompt></b> trick_dp &
```

#### Plotting Time -vs- Postion

1. Double click the pathname containing your sim directory if it is not expanded yet (or single click the symbol next to the name)
1. Double click the SIM_cannon_analytic name in the Sims/Runs Tree. This will reveal the RUN_test directory.
1. Double click the RUN_test name or right click the RUN_test followed by selecting "Add run(s)".
   This will bring RUN_test into the RUN Selections below.
1. Click the blue lightning button in the tool bar to launch Quickplot application (Trick QP). The Trick QP GUI will pop up.
1. In Trick QP, right click dyn.cannon.pos[0-1] and select "Expand Var" if the interested variable is one of the element in an array
   which is not expanded yet.
1. Double click the dyn.cannon.pos[0] variable in the left pane. This sets up to create one page with one plot (time -vs- pos[0]).
    - Make sure nothing is highlighted or "Plots" is highlighted on the right in DP Content
    - If "Tables" is highlighted, it sets up to create a table with one column instead.
    - The X variable is sys.exec.out.time by default and the Y variable is dyn.cannon.pos[0].
    - Later, you will learn how to replace the X (sys.exec.out.time) with a different variable.
1. Now click the dyn.cannon.pos[1] variable and drag it to the pane on the right. Drop it on the line with "Page" (see the white-n-black window looking icon).
   This will result in one page containing two plots.
1. In Trick QP, click the plain white sheet icon located on the toolbar. A single window with two plots should pop up:

![plot2](images/plot2.jpg)

1. If you want to specify the number of plots horizontally and vertically on a page, click "Page" node and edit its Horizontal Cells and Vertical Cells
   propterties from Proptery Notebook (use the scroll bar or change the GUI window size if necessary). Change Horizontal Cells
   from 0 to 2 and Vertical Cells from 0 to 1 and click "Apply Change" button on the top of Proptery Notebook.
   If click the plain white sheet icon located on the toolbar, a single window with two plots side by side should pop up:
    - "Apply Change" needs to be selected to save the changes made to the Proptery Notebook.

![plot1](images/plot1.jpg)

#### Plotting XPosition -vs- YPosition

Now, let's change the default X variable from sys.exec.out.time to a different variable.
1. Assuming the Trick QP application is still up, click the "New" plot icon located on the far left of the toolbar.
   Click "Ok" when asked if you want to start over. This will clear the plots from the DP Content.
1. Double-click dyn.cannon.pos[1].
1. Drag-n-drop the dyn.cannon.pos[0] variable over the sys.exec.out.time variable in the Plot located in the DP Content.
   You will be asked to confirm the replacement. Click "Ok".
    - Now,
