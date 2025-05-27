### Product.dtd > A general DP Product XML File Example

 CDATA #IMPLIED>

<!-- <var>'s from_units attribute specifies the units to be assumed  -->
<!-- for the recorded data if and only if the recorded data doesn't  -->
<!-- contain units information for it's variables. -->
<!-- This attribute is used for data streams that don't supply       -->
<!-- actual units. For streams that supply actual units (like .trk   -->
<!-- files) this attribute is ignored. -->
<!ATTLIST var from_units                  CDATA #IMPLIED>

<!-- <var>'s units attribute indicates the units that recorded data -->
<!-- should be converted to, below being displayed.                 -->
<!ATTLIST var units                       CDATA #IMPLIED>

<!ATTLIST var bias                        CDATA #IMPLIED>
<!ATTLIST var scale                       CDATA #IMPLIED>
<!ATTLIST var max                         CDATA #IMPLIED>
<!ATTLIST var symbol_style                CDATA #IMPLIED>
<!ATTLIST var symbol_size                 CDATA #IMPLIED>
<!ATTLIST var line_style                  CDATA #IMPLIED>
<!ATTLIST var line_color                  CDATA #IMPLIED>
<!ATTLIST var gnuplot_line_style          CDATA #IMPLIED>
```

The root element of the DP Product XML file is <b>product</b>. It contains all other elements.
There are three main elements under product element that are: <b>page</b>, <b>table</b>, and
<b>extfn</b>. <b>page</b> refers to a page of X-Y-(Z) plots. <b>table</b> refers to ASCII
text formats. The product specification file may contain any number of pages and tables, but at least one
page or table. <b>extfn</b> refers to an external program designed to manipulate recorded data
into a format which is more easily displayed and its occurrence is not required.

## DP Page Element Specifications
A DP product file may have one or more <b>page</b> elements. Each <b>page</b> element must
have at least one <b>plot</b> elment and may have more plots sepcified. All attributes of a
<b>page</b> element as stated earlier in @ref product_dtd "Product.dtd" are:
de foreground_color, background_color, hcells, vcells, presentation, gnuplot_template, gnuplot_object, gnuplot_geom, gnuplot_plot_ratio, gnuplot_page_orientation@endcode
The <b>page</b> element will be discussed in following sections: @ref plot_element_specifictions "6.2.1.1 Plot Element Specifications",
@ref general_variable_options "6.2.1.2 General Variable Options",
@ref specific_variable_options "6.2.1.3 DP Specific Y (or Z) Variable Options", and
@ref curves "6.2.1.4 Curves".

### DP Plot Element Specifications

The <b>tstart</b> and <b>tstop</b> options have the same function as in the session file. If either of these options
is specified, they will override any values specified in the session file for this particular plot page.
Each plot page specification can include up to nine individual plot specifications. The size of each
of the plots on a plot page is automatically sized to fit within the plot page window regardless of
the number of plots specified for the plot page.

### General Variable Options

The general variable options are options that apply to a variable regardless when it's for X, or Y, or Z.
They are:

- The <b>label</b> attribte of var element allows the user to give the parameter
(or program token) a name to be used in the legend of a plot.
- The <b>units</b> attribute of <b>var</b> allows the user to specify the measurement
units in which the specified parameter will be displayed. The measurement units specification
syntax is identical to that used in the input processor and ICG parameter comments.
- The <b>bias</b> attribute of <b>var</b> allows the user to shift the plot.
It is applied after the scaling and unit conversion. X or Y or Z may be shifted.
- The <b>max</b> attribute of <b>var</b> allows the user to override the max range options
specified at the plot level.
- The <b>scale</b> attribute of <b>var</b> allows the user to scale the specified parameter
value by a factor of the value specified by this attribute. The scale factor is applied after the
measurement units (if specified) conversion is performed.

### DP Specific Y (or Z) Variable Options

The Y (Z) variable specification has additional options which
