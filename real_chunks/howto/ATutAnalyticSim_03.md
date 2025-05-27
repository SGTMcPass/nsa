### Building & Running a Trick-based Simulation > Running The Simulation > Sim Execution

 measure of meters
per second. Unit specs allow unit conversions to be performed by the Trick input
file processor, Trick View and plotting tools.

As of Version 17.0, Trick uses [UDUNITS2](http://www.unidata.ucar.edu/software/udunits/),
an Open Source unit conversion package, developed at http://www.unidata.ucar.edu.
It is similar in many respects to Trick's previous unit conversion package, but,
frankly it's a lot better. Like the previous Trick unit conversion package,
UDUNITS2 supports unit-prefixes (for example: kilo, micro, etc.) as well as
unit-composition, the ability to compose unit specifications from previously
defined unit specifications (for example: m/s, kg.m/s^2). Unlike the previous
unit conversion, its units database is much more substantial, it's more
extensible, its design is more capable, and it supports Unicode characters in
unit specifications.

Below, we are going to see how to specify commonly needed unit specifications
for our Trick simulations. But, we are not going to describe the full capability
of UDUNITS2 package. In order to see **ALL** available unit definitions, one would
need to look at the UDUNITS2 xml files that comprise the units database.

Rather than requiring that, the [Common Units & Unit Prefixes](ATutUnitTables) page
lists optional prefixes, and many of the most commonly used units in simulations
at the Johnson Space Center Engineering Branch.

#### Composite Units (Making Units From Existing Units)
Often, units are composed of other predefined units as in the following unit
specification examples:

* **m/s** (meters per second, speed)
* **m/s^2** (meters per second squared, acceleration)
* **kg.m/s^2** (Newtons, force)
* **m^3** (cubic meters, volume)

Note the operators `/` (division), `.`(multiplication), `^2`(square), and
`^3`(cube) for composing unit specs.

#### Scaling Units With Unit Prefixes

Unit prefixes, listed in the table `Unit Prefixes`, below can also be prepended
to unit specifications, as in the following examples:

* **k**m, **kilo**meters
* **M**W, **mega**watts

#### Unicode Characters in Units

Some units and unit-prefixes can also be represented using unicode characters.

For example:

* **^2** can instead be represented as **&#xB2;** (Unicode char U+00B2).
* **^3** can instead be represented as **&#xB3;** (Unicode char U+00B3).
* The prefix **micro**, or **u** can be represented as **&#x3BC;** (Unicode
char U+03BC).
*
