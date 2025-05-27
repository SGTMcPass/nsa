### Product.dtd > A general DP Product XML File Example

> attribute of <b>var</b> allows the user to shift the plot.
It is applied after the scaling and unit conversion. X or Y or Z may be shifted.
- The <b>max</b> attribute of <b>var</b> allows the user to override the max range options
specified at the plot level.
- The <b>scale</b> attribute of <b>var</b> allows the user to scale the specified parameter
value by a factor of the value specified by this attribute. The scale factor is applied after the
measurement units (if specified) conversion is performed.

### DP Specific Y (or Z) Variable Options

The Y (Z) variable specification has additional options which allow the user to specify distinct line, symbol,
and color attributes. Even though <b>var</b> element XML specification doesn't limit a X variable having
all these options, such restriction is implemented at GUI level.

These options are:

- <b>ymbol_style</b>:        None|Square|Circle|Star|XX|Triangle|Solid_Square|Solid_Circle|Thick_Square|Thick_Circle
- <b>symbol_size</b>:        Tiny|Small|Medium|Large
- <b>line_sytle</b>:         Plain|Dash|No_Line|X_Thick_Line|Fine_Dash|Med_Fine_Dash|Long_Dash|X_Long_Dash|Dot_Dash|2_Dot_Dash|3_Dot_Dash|4_Dot_Dash
- <b>line_color</b>:         system supported color
- <b>gnuplot_line_sytle</b>: lines|points|linespoints|impulses|dots|steps|fsteps|histeps|boxes

The <b>symbol_style</b> attribute of <b>var</b> allows the user to mark each data point with a specific symbol.
The default is None.
The <b>line_style attribute</b> of <b>var</b> allows the user to change the line style which connects the X-Y(-Z) data points.
The default is Plain.
The <b>line_color</b> attribute of <b>var</b> allows the user to specify a color to be used for the X-Y(-Z) plot line and symbol.
the <b>gnuplot_line_sytle</b> attribute of <b>var</b> allows the user to change the line style in a Gnuplot.
You may specify the line style by name. The default is lines.

### Curves
Each curve has either specified 2 or 3 variables stated as <b>var</b> or has <b>
varcase</b> specified. The first <b>var</b> element is for X, the second <b>var</b>
element is for Y and the third is for Z. A <b>curve</b>  element can not have both <b>var</b>
and <b>varcase</b> elements at same time.
If you have specified multiple RUN_ directories that contain the same X, Y, and (Z) variable names, Trick can
generate a curve for each RUN_ directory, or a single comparison plot. However, the only <b>var</b>
specification makes it very difficult to compare a parameter with one variable name in RUN_A and a different
variable name in RUN_B. The <b>varcase</b> specification, on the other hand, allows multiple X, Y, and (Z),
which are lists of possible XY(Z) variables that define the curve for each RUN_ directory. If <b>varcase</b>
elements do not have unique variable names, DP will use the first <b>varcase</b> that it finds in the logged
data and ignores the other <b>varcase</b> elements.
As shown in the following DP specification example, it compares sys.exec.out.time (X) and
ball.obj.state.output.acceleration[1] (Y) variables from RUN_A and my_other_data.time (X)
and my_other_data.acceleration[1] (Y) variables from RUN_B. It also generates curves for
sys.exec.out.time (X) and ball.obj.state.output.external_force[0] (Y) from
both RUN_A and RUN_B.

```
<?xml version="1.0" encoding="ISO-8859-1" standalone="no"?>
<!DOCTYPE product PUBLIC "-//Tricklab//DTD Product V1.0//EN" "Product.dtd">
<product background_color="#ede9e3" foreground_color="#000000" version="1.0">
    <tstart>-1.0E20</tstart>
    <
