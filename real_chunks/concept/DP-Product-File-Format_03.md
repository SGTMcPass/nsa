### Product.dtd > A general DP Product XML File Example

 (Y) variables from RUN_A and my_other_data.time (X)
and my_other_data.acceleration[1] (Y) variables from RUN_B. It also generates curves for
sys.exec.out.time (X) and ball.obj.state.output.external_force[0] (Y) from
both RUN_A and RUN_B.

```
<?xml version="1.0" encoding="ISO-8859-1" standalone="no"?>
<!DOCTYPE product PUBLIC "-//Tricklab//DTD Product V1.0//EN" "Product.dtd">
<product background_color="#ede9e3" foreground_color="#000000" version="1.0">
    <tstart>-1.0E20</tstart>
    <tstop>1.0E20</tstop>
    <frequency>0.0</frequency>
    <page background_color="#ede9e3" foreground_color="#000000">
        <title>Page</title>
        <plot background_color="#ede9e3" foreground_color="#000000" grid="Yes" grid_color="#ffffff">
            <title>Plot</title>
            <curve>
                <varcase>
                    <var units="--">sys.exec.out.time</var>
                    <var units="m/s2">ball.obj.state.output.acceleration[1]</var>
                </varcase>
                <varcase>
                    <var units="--">my_other_data.time</var>
                    <var units="m/s2">my_other_data.acceleration[1]</var>
                </varcase>
            </curve>
            <curve>
                <var units="--">sys.exec.out.time</var>
                <var units="N">ball.obj.state.output.external_force[0]</var>
            </curve>
        </plot>
    </page>
</product>
```

## DP Table Specifications

Each table is comprised of one or more columns and each column is only for one variable. Each <b>column</b> element
has an optional <b>format</b> attribute that allows the user to specify the text format for the variable's data. The
syntax of <b>format</b> is the same as that for a C language @p printf format field. Each variable element of
<b>column</b> element has those general variable options as stated in
Section @ref general_variable_options "6.2.1.2 GeneralVariable Options".

As shown in the following product example XML file, it has one <b>table</b> defined. This <b>table</b> has
4 different columns and each column is corresponding to a specific <b>var</b>.

```
<?xml version="1.0" encoding="ISO-8859-1" standalone="no"?>
<!DOCTYPE product PUBLIC "-//Tricklab//DTD Product V1.0//EN" "Product.dtd">
<product background_color="#ede9e3" foreground_color="#000000" version="1.0">
    <tstart>-1.0E20</tstart>
    <tstop>1.0E20</tstop>
    <frequency>0.0</frequency>
    <table>
        <title>Table</title>
        <column>
            <units>--</units>
            <var units="m/s2">ball.obj.state.output.acceleration[0]</var>
        </column>
        <column>
            <units>--</units>
            <var units="m/s2">ball.obj.state.output.acceleration[1]</var>
        </column>
        <column>
            <units>--</units>
            <var units="N">ball.obj.state.output.external_force[0]</var>
        </column>
        <column>
            <units>--</units>
            <var units="N">ball.obj.state.output.external_force[1]</var>
        </column>
    </table>
</product>
```

An example data of the specified table:

```
------------------------------------------------------------------------
   acceleration[0]   acceleration[1] external_force[0] external_force[1]
                --                --                --                --
------------------------------------------------------------------------
     -6.859943e-01     -4.115966e-01     -6.859943e+00     -4.115966e+00
     -6.853979e-01     -4.125891e-01     -6.853979e+00     -4.125891e+00
     -6.848069e-01     -4.135693e-01     -6.848069e+00     -4.135693e+00
     -6.842212e-01     -4.145375e-01     -6.842212e+00     -4.145375e+
