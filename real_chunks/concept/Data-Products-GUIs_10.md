### Trick DP - Data Products Application > Viewing Data > Using External Program

 $TRICK_HOME/trick_source/data_products/Apps/ExternalPrograms/dp_substract.c that comes with Trick distribution will be used in this section. This program takes 2 double inputs and returns the subtraction of these 2 inputs. Assuming the program is alreay built and the corresponding shared object is available for use.

1. Go to the SIM_cannon_analytic directory and launch Trick QP as:
    - <b>UNIX Prompt></b> trick_qp RUN_test &
1. Click "Programs->New Program" or right click "Programs" under DP Content followed by selecting "New Program".
    - Now you see a new "PROGRAM" node with "Input" and "Output" is created under "Programs".
    - Please note that only one program at a time is currently supported.
1. Click "PROGRAM" and click "Browse..." from Property Notebook to select the shared object for the program.
    - In this case, select the file dp_subtract.so that is located at "$TRICK_HOME/trick_source/data_products/Apps/ExternalPrograms/object_Linux_4.4_x86_64/".
1. Click "Apply Change". The name of "PROGRAM" is now changed to the full path of the shared object.
1. Click "Input" so it is highlighted in blue.
1. Double click dyn.cannon.pos[0-1]. Both dyn.cannon.pos[0] and dyn.cannon.pos[1] are inserted under "Input".
1. Right click Output and then select "New Output...". Enter a name for the output as prompted such as "out" and then click "Ok".
    - Now you should see "out" in red shown in Vars list.
1. Drag "out" to "Plots" under DP Content. A page with one plot with one curve is created.
    - The X variable is sys.exec.out.time.
    - The Y variable is out which is the subtraction of dyn.cannon.pos[0] and dyn.cannon.pos[1].
1. Click the plain white single sheet icon on the toolbar to see the plot.

![plot7](images/plot7.jpg)

[Continue to Simulation Capabilities](../simulation_capabilities/Simulation-Capabilities)
