### Session.dtd > DP Session File Example

</b>. The <b>Simple</b>
option will display the data products independently for all data sets specified. The <b>parison</b> option
will display the data from all data sets in the same display. The <b>Delta</b> option subtracts
the nth data set data from the first data set data and presents the result for data sets 2 through n in
the same display. <b>Simple</b> is the default option.

@anchor session_device The <b>device</b> attribute of <b>session</b> specifies the visualization device
for data output. By default, the output data is displayed on the user's current login terminal screen.
Device types are currently <b>Terminal (default), Printer, and File</b>.
@li In order for Printer to work, you need to set your system variables as stated in "Plot Printing".

The <b>gnuplot_terminal</b> attribute of <b>session</b> instructs gnuplot to use the given
terminal device for output. The terminals supported are <b>X11, postscript color, postscript, png, eps, and aqua
(X11 is the default)</b>. The "postscript" terminal yields black-n-white printable files. Thpng will create
an image in Portable Network Graphics format. The aqua terminal is for Macintosh and uses native Aqua for plot display.

The optional <b>machine, port</b> attributes of <b>session</b> specify the name of a machine and the port
number for plotting.


## DP Session File Example

```
<?xml version="1.0" encoding="ISO-8859-1" standalone="no"?>
<!DOCTYPE session PUBLIC "-//Tricklab//DTD Session V1.0//EN" "Session.dtd">
<session device="Terminal" gnuplot_terminal="" mode="Plot" presentation="Simple" version="1.0">
    <tstart>-1.0E20</tstart>
    <tstop>1.0E20</tstop>
    <frequency>0.0</frequency>
    <run>
        <dir>/users/hchen/trick_sims/trunk/SIM_Ball++_L1/RUN_realtime</dir>
    </run>
    <run>
        <dir>/users/hchen/trick_sims/trunk/SIM_Ball++_L1/RUN_test</dir>
    </run>
    <product_files>
        <file>/users/hchen/trick_sims/trunk/SIM_Ball++_L1/DP_Product/DP_test_4.xml</file>
        <file>/users/hchen/trick_sims/trunk/SIM_Ball++_L1/DP_Product/DP_test_5.xml</file>
    </product_files>
</session>
```

[Continue to DP Product File Format](DP-Product-File-Format)
