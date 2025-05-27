### Session.dtd > DP Session File Example

| [Home](/trick) → [Documentation Home](../Documentation-Home) → [Data Products](Data-Products) → DP Session File Format |
|------------------------------------------------------------------|

Since Trick 10, the DP Session file is changed to XML format. The Session XML Document
Type Definitions(DTD) is defined as following:

## Session.dtd

```
<!-- Trick DP Session definition -->
<!-- V 1.0 -->

<!ELEMENT tstart        (#PCDATA)>
<!ELEMENT tstop         (#PCDATA)>
<!ELEMENT frequency     (#PCDATA)>
<!ELEMENT file          (#PCDATA)>
<!ELEMENT dir           (#PCDATA)>
<!ELEMENT timename      (#PCDATA)>
<!ELEMENT run           (dir)>
<!ELEMENT product_files (file+)>
<!ELEMENT session       ((tstart|tstop|frequency)*, run+, product_files)>

<!ATTLIST run timename              CDATA #IMPLIED>

<!ATTLIST session version           CDATA #REQUIRED>

<!-- session@presentation attribute

     "simple"     - One curve per plot. #plots = #runs x #plot_specifications
     "comparison" - Multiple runs per plot.
     "delta"      - difference of two runs.
     "contrast"   - some weird thing Danny dreamed up.
-->
<!ATTLIST session presentation      CDATA #REQUIRED>

<!-- session@mode attribute
     Indicates a restriction on what in a DP file.

     "plot"   - means that only the plots described in a DP file may be created.
     "table"  - means that only tables described in a DP file may be created.
      default - all plots and tables in the DP may be created.
-->
<!ATTLIST session mode              CDATA #IMPLIED>

<!ATTLIST session device            CDATA #IMPLIED>
<!ATTLIST session gnuplot_terminal  CDATA #IMPLIED>
<!ATTLIST session machine           CDATA #IMPLIED>
<!ATTLIST session port              CDATA #IMPLIED>
```


The <b>session</b> element is required and is the root element of the Session XML file.
It encloses all the other elements.

The optional <b>tstart, tstop</b> child elements of <b>session</b> specify the data
within this range gets plotted.

The optional <b>frequency </b> child element of <b>session</b> specifies the delta time
between data points for display purposes. If it is smaller than the delta time of the recorded data
or if it is not defined, then the recorded data frequency is used. If it is greater than the recorded
data delta time, then it is used. It is specified in seconds.

The required <b>run</b> child element of session can occur once or more times.
It specifies a simulation RUN_ directory as <b>dir</b> stated from which to retrieve data.

By default, the time name for each run is sys.exec.out.time, however, an optional attribute of each
<b>run - timename</b> can be specified if a different name other than
the default one is desired.

The required <b>product_files</b>  child element of <b>session</b> can only occur once.
It specifies product specification file(s) to use for this session. Any number (but at least one)
of product specification files may be specified through its <b>file</b> element. In other words,
it can have one or more <b>file</b>  elements. In general the product specification files specify
the type of product parameters to display for the product, and the display attributes for each parameter.
Product specification files are discussed in greater detail in Section @ref DPProductFileFormat "6.2 DP Product File Format".

The required <b>version</b> attribute of <b>session</b> specifies the version of this file.

The required <b>presentation</b>  attribute of <b>session</b> is only useful when more than
one data set is specified. It can be <b>Simple|Comparison|Delta|Contrast</b>. The <b>Simple</b>
option will display the data products independently for all data sets specified. The <b>parison</b> option
will display the data from all data sets in the same display. The <b>Delta</b> option subtracts
the nth data set data from the first data set data and presents the result for data sets 2 through n in
the same display. <b>Simple</b> is the default option.

@anchor session_device The <b>device</b> attribute of <b>session</b> specifies the visualization device
for data output. By default, the output data is displayed on the user's current login terminal screen.
Device types are currently
