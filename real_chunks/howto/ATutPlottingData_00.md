### Viewing Recorded Data > Using Trick Quick Plot > Plotting Time -vs- Position

| [Home](/trick) → [Tutorial Home](Tutorial) → Plotting Recorded Data |
|-------------------------------------------------------------------|

<a id=viewing-recorded-data></a>
## Viewing Recorded Data

To view recorded data, Trick provides an application called **quick plot**.
**NOTE:** The GUI or plot graph figures may be shown differently on your
machine due to the differences of the platforms and ongoing changes.

### Using Trick Quick Plot
Begin by launching trick-dp (trick data products GUI).

```bash
% cd $HOME/trick_sims/SIM_cannon_analytic
% trick-dp &
```

#### Plotting Time -vs- Position
1. Double click the pathname containing your sim directory (or single
click the symbol next to the name)
1. Double click the `SIM_cannon_analytic` name in the Sims/Runs pane.
This will reveal the `RUN_test` directory.
1. Double click the `RUN_test` name. This will bring `RUN_test` into
the RUN Selections pane below.
1. Click the blue lightning button in the tool bar to launch quick
plot (qp). The qp GUI will pop up.
1. In qp, right click the `dyn.cannon.pos[0-1](m)` variable in the
left pane and choose **Expand var**. Next double click `dyn.cannon.pos[0](m)`.
This sets up qp to create one page with one plot (time -vs- pos[0]).
1. Now click the `dyn.cannon.pos[1]` variable and drag it to the pane
on the right. Drop it on the line with "Page" (see the white-n-black window
looking icon). This will result in one page containing two plots.
1. In qp, click the plain white sheet icon located on the toolbar. A
single window with two plots should pop up. (See Figure 4)
1. When you are done with the plots you created, close the **Trick
Plot** window which will also close the window with your plot(s).

![Plot of Time vs Position](images/PlotTimeVsPosition.png)

**Figure 4 - Quick Plot Time -vs- Position**

#### Plotting XPosition -vs- YPosition
1. Right click "Plots" in the "DP Content" pane and choose
"Remove All Pages".
1. Double click dyn.cannon.pos[1].
1. Drag-n-drop the dyn.cannon.pos[0] variable over
the sys.exec.out.time variable in the Plot located in the "DP Content" pane. You
will be asked to confirm the replacement. Click "Ok".
1. To see the plot, click the white sheet icon on the toolbar. Voila!
There is the trajectory! :-) Note that the cannonball goes underground. This
will be fixed later.
1. When you are done, close
