### Product.dtd > A general DP Product XML File Example

 int numIn __attribute__ ((unused)), double *out, int numOut __attribute__ ((unused)))
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
- Step 2. cc -bundle -o <myprogram>.so <myfunction1>.o <myfunction2>.o ... <myfunctionN>.o <myLib>.a -lc

In the above example, <myprogram>.so is the name that needs to be specified in the DP specification file.
If LD_LIBRARY_PATH doesn't point to the location of your shared object, then you just need to sepcify the full path
of the shared object in the DP sepcification file.
The example above links in <myLib>.a too. It's that simple.
Do the following to see if your newly created shared object has unresolved dependencies:

- @b UNIX @b Prompt> nm <myprogram>.so

### External Program Summary

To use an external program:
1. Build a DP spec file with the program name, inputs and outputs.
2. Write an external program (or scam one off a friend).
3. Build the external program.
4. Run the data products, and hopefully the results you expect will be there.

### External Program Proglems And Caveats

- Can't load shared library!!! The external program (*.so program) may have unresolved dependencies.
Try "nm" on your external program, and look for "U"s. The objects that you have linked in might have extern definitions that aren't there.
- Make sure you specify the full path of the shared object if LD_LIBRARY_PATH is not defined or doesn't point to the location of the shared object.
- You cannot scale or bias X values with external programs.
- External programs convert everything to doubles, and only accept and output doubles.
- External programs have no notion of unit conversion.

## A general DP Product XML File Example

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
                <var units="--">sys.exec.out.time</var>
                <var units="N">ball.obj.state.output.external_force[0]</var>
            </curve>
        </plot>
        <plot background_color="#ede9e3" foreground_color="#000000" grid="Yes" grid_color="#ffffff">
            <title>Plot</title>
            <curve>
                <var units="--">sys.exec.out.time</var>
                <var units="N">ball.obj.state.output.external_force[1]</var>
            </curve>
        </plot>
    </page>
</product>
```

[Continue to Plot Printing](Plot-Printing)
