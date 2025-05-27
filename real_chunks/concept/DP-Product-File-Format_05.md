### Product.dtd > A general DP Product XML File Example

353e+00
```

## DP External Programs

The <b>extfn</b> element provides a means for transforming data. Users build a program that is dynamically linked into
Trick data products for manipulating data specified in the DP Product XML file and its document type definition file
is stated as @ref product_dtd "Product.dtd".

### Element extfn Specifications
The <b>extfn</b> needs to have 3 element specifications associated with it. These elements are <b>fname</b>, <b>inputs</b>, and <b>outputs</b>.
The <b>fname</b> is a full path to a program which accepts the inputs and generates the outputs. This
program must adhere to strict interface requirements. This program will be dynamically linked into the data products,
which implies it must be built under specific guidelines. Only ONE <b>extfn</b> may be defined per DP XML file.
The <b>inputs</b> are specified as a list of simulation variable names or <b>var</b> elements. The <b>outputs</b> is a user defined name list which
provides a unique variable name for each of the external program output arguments. These outputs variables may be used throughout
the product XML specification file wherever a simulation variable name or <b>var</b> element is required.
Inputs will be cast to doubles going to the external program, and outputs must be doubles as well.
The following example shows an external program that takes 3 double inputs and return the addition of these 3 inputs.
The product specification file (DP_* file) might look like this:

```
<?xml version="1.0" encoding="ISO-8859-1" standalone="no"?>
<!DOCTYPE product PUBLIC "-//Tricklab//DTD Product V1.0//EN" "Product.dtd">
<product background_color="#edeceb" foreground_color="#1a1a1a" version="1.0">
    <tstart>-1.0E20</tstart>
    <tstop>1.0E20</tstop>
    <frequency>0.0</frequency>
    <extfn>
        <fname>/users/hchen3/trick_test/myextfn/dp_test.so</fname>
        <inputs>
            <var units="m">ball.obj.state.output.position[0]</var>
            <var units="m">ball.obj.state.output.position[1]</var>
            <var units="m">ball.obj.state.output.position[0]</var>
        </inputs>
        <outputs>
            <measurement>
                <var>out</var>
                <units>--</units>
            </measurement>
        </outputs>
    </extfn>
    <page background_color="#edeceb" foreground_color="#1a1a1a" hcells="0" vcells="0">
        <title>Page</title>
        <plot background_color="#edeceb" foreground_color="#1a1a1a" grid="Yes" grid_color="#ffffff">
            <title>Plot</title>
            <curve>
                <var units="s">sys.exec.out.time</var>
                <var units="--">out</var>
            </curve>
        </plot>
    </page>
</product>
```

### External Program Source Code

To use the external program feature of the product specification file, a user must either access a previously written
program, or write their own.
The following is an example external program source file which reads the three inputs and generates one output as
specified above. The code example below contains comments which explain the function of the code segments.

```
/* Used for dp test */

// This line should not change from program to program. The content of this function is application specific and up to user to define.
int extGetNextRecord(double *in, int numIn, double *out, int numOut) ;

// This line should not change from program to program. The content of this function is application specific and up to user to define.
int extGetNextRecord(double *in, int numIn __attribute__ ((unused)), double *out, int numOut __attribute__ ((unused)))
{
        out[0] = in[0] + in[1] + in[2];
        return (0);
}
```

### Building The External Program

#### Linux

- Step 1. cc -c <myprogram1>.c (compile all individual object this way)
- Step 2. ld -shared -o <myprogram>.so <myfunction1>.o <myfunction2>.o ... <myfunctionN>.o <myLib>.a -lc

#### MacOS X

- Step 1. cc -c <myprogram1>.c (compile all individual object this way)
