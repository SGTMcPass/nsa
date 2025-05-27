### Viewing Recorded Data > Using Trick Quick Plot > Plotting Time -vs- Position

 dyn.cannon.pos[0] variable over
the sys.exec.out.time variable in the Plot located in the "DP Content" pane. You
will be asked to confirm the replacement. Click "Ok".
1. To see the plot, click the white sheet icon on the toolbar. Voila!
There is the trajectory! :-) Note that the cannonball goes underground. This
will be fixed later.
1. When you are done, close the **Trick Plot** window.

![Plot of X vs Y Position](images/PlotXvsYPosition.png)

**Figure 5 - Quick Plot X -vs- Y Position**

#### Creating a DP Specification File
Repeatedly clicking variables in Trick QP gets old, fast. To get around this,
the information needed for this plot will be saved to a file named
`DP_cannon_xy`, and then reused by `trick-dp`. This is an important step,
because extensive use will be made of the `DP_cannon_xy` file.

1. With the Trick QP GUI still up and the x -vs- y position still
chosen, click the `dyn.cannon.pos[1]` variable located in the pane on the right
(in the DP Content pane). The variable should be highlighted. The **Y Var**
notebook page should be visible in the lower right pane.

1. In the **Y Var** notebook page, select **Symbol Style->Square**
from the drop-down menu.

1. In the **Y Var** notebook page, select **Symbol Size->Tiny** from
the drop-down menu.

1. Click the **Apply Change** button (you may have to scroll up to
see the button).

1. Save this information by clicking the menu option **File->Save As**.
Click **New Folder** button to create the `DP_Product` folder. Choose the
directory button `SIM_cannon_analytic/DP_Product`. Enter file name as `DP_cannon_xy`.

1. Close the **Trick QP** GUI, but keep Trick DP up and running.

#### Using trick-dp To View Data
Now that `DP_cannon_xy` has been saved, the data can be viewed with trick-dp.

1. Assuming the **Trick DP** is still up and running from the
previous steps, click **Session->Refresh…** to reveal `DP_cannon_xy.xml` in
the top right pane, **DP Tree**.

1. Make sure that `Sims/Runs->SIM_cannon_analytic/RUN_test` shows up
in the  **Run Selections** pane. If not, then double click it to add it.

1. Choose the `DP_cannon_xy.xml` in the top right pane by double
clicking it. This will bring the `DP_cannon_xy.xml` into the **DP Selections** pane.

1. To see the trajectory again
