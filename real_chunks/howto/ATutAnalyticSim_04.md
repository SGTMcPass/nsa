### Building & Running a Trick-based Simulation > Running The Simulation > Sim Execution

 be represented using unicode characters.

For example:

* **^2** can instead be represented as **&#xB2;** (Unicode char U+00B2).
* **^3** can instead be represented as **&#xB3;** (Unicode char U+00B3).
* The prefix **micro**, or **u** can be represented as **&#x3BC;** (Unicode
char U+03BC).
* The unit **ohms** can be represented as **&#x2126;** (Unicode char U+2126
or U+03A9).

So, one could specify **m/s&#xB2;** rather than **m/s^2**, or  **m&#xB3;**
rather than **m^3**, or **&#x3BC;m** rather than **micrometers**. The table below
lists Unicode characters that can be used in units specifications.

<a id=unicode-characters-used-in-units-specifications></a>
### Unicode Characters Used in Units Specifications
| Character | Unicode Number | Unicode Name          |
|-----------|----------------| ----------------------|
| &#xB0;    | U+00B0         | Degree Sign           |
| &#xB2;    | U+00B2         | Superscript Two       |
| &#xB3;    | U+00B3         | Superscript Three     |
| &#x3A9;	  | U+03A9         | Greek Capital Letter Omega |
| &#x3BC;   | U+03BC         | Greek Small Letter Mu |
| &#x3C0;   | U+03C0         | Greek Small Letter Pi |
| &#x2032;  | U+2032         | Prime                 |
| &#x2033;  | U+2033         | Double Prime          |
| &#x2103;  | U+2103         | Degree Celsius        |
| &#x2109;  | U+2109         | Degree Fahrenheit     |
| &#x2126;  | U+2126         | Ohm Sign              |
| &#x212A;  | U+212A         | Kelvin Sign           |
| &#x212B;  | U+212B         | Angstrom Sign         |

#### Specifying "No Units"

In Trick, a unit specification of "--" means *unit-less*. If your variable
doesn't have units, use "--" as the unit specification.

---

<a id=initializing-the-cannonball-simulation></a>
### Initializing the Cannonball Simulation

The Trickless simulation performed a two-part initialization of the
simulation variables. The first part assigned default values to the simulation
parameters. The second part performed calculations necessary to initialize the
remaining simulation variables.

Trick based simulations perform a three-part initialization of simulation
variables. The first part runs "**default
