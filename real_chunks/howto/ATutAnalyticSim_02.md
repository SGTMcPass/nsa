### Building & Running a Trick-based Simulation > Running The Simulation > Sim Execution

is **vi**. So when you see **vi** following the %, just replace it
with **emacs**, **nedit**, **jot**, **wordpad**, **kate**, **bbedit**, or
whatever you like.

```bash
% cd $HOME/trick_sims/SIM_cannon_analytic/models/cannon/include
% vi cannon.h
```

Type, or cut and paste the contents of **Listing 2** and save.

<a id=deciphering-the-trick Comments In The Header File></a>
### Deciphering The Trick Comments In The Header File

In the file above, note the comments at the top, and to the right of each
structure member. These are specially formatted comments that are parsed by Trick.

The comment at the top of the file, containing the keyword `PURPOSE:` (the colon
is part of the keyword) is called a "Trick header". The presence of a Trick
header lets Trick know that it should scan the file to collect information about
the data types it contains. The full Trick header syntax will be detailed later, for
now, `PURPOSE:` is all that is necessary.

To the right of each structure member is a comment that (optionally) provides
the following information for the member:

1. Input/Output Specification
2. Units Specification
3. Description

These are each described in **Figure 2** and in the sections below.

![DataMemberComments](images/DataMemberComments.png)

**Figure 2 - Data Member Comments**

---

<a id=the-input_output-io-specification></a>
#### The Input/Output (I/O) Specification

An I/O specification is an optional field that specifies data flow
direction for a variable. The default, `*io` , specifies that both input and
output are allowed.

* `*i` tells Trick that the parameter will be input only.
* `*o` tells Trick that the parameter is output only.
* `*io` is the default and means the parameter may be used for input or output.
* `**` tells Trick that you do NOT want this parameter processed.

---

#### Comment Field
The comment field is extracted and used in GUI tools to describe variables.

---

<a id=units-specification></a>
#### Units Specification
A unit specification indicates the units of measure for a variable. For example,
in the figure above, (m/s) indicates that `init_speed` is a measure of meters
per second. Unit specs allow unit conversions to be performed by the Trick input
file processor, Trick View and plotting tools.

As of Version 17.0, Trick uses [UDUNITS2](http://www.unidata.ucar.edu/software/udunits/),
an Open Source unit conversion package, developed at http://www.unidata.ucar.edu.
It is similar in many respects to Trick's previous unit conversion package
