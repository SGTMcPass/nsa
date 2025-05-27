### Trick Header Comment > Create Connections

 list The collection
mechanism syntax in the S_define file is as follows:

```C++
collect <reference> = { } ;
```

or

```C++
collect <reference> = { <reference_1> [,<reference_n>] } ;
```

There is also a C code equivalent to adding collect references one at a time that may
be put in a create_connections section of the S_define file.  The advantage of this
method is that not all of the collects must be listed in a single collect statement.
This function call syntax may also be used in the input file to add collects at runtime.

```C++
void create_connections() {
    reference = add_collect( reference , reference_1 ) ;
    reference = add_collect( reference , reference_2 ) ;
}
```

The collect capability allows the developer to build a job which accesses an unknown number
of independent simulation parameters. For example, if designed correctly, a derivative class
module should be capable of incorporating any number of known and unknown (future capabilities)
external forces and torques without any code changes to the derivative module. The collection
mechanism stores the addresses of, and number of, any number of independent parameters in a
single pointer array. The derivative module can use this array to access each parameter in the
collection list. See Section 10.0 for programming requirements for this capability.

The collect statements in the S_define file must be supported by source code implemented by
the math model developer. This collect support code can reside in any function in the simulation,
including functions that are not listed in the S_define file. In general, for every collect
statement in the S_define file, there are two places where source code must be developed: a
data structure definition file (`*.h`) and a function source file (`*.c`).

As a real world example, orbital dynamics can include a large number of environmental effects
for high precision state propagation, or a small number of effects for general purpose state
propagation. A spacecraft EOM derivative module should be designed to include any number and
combination of known and unknown (future) effects. A low fidelity parameter collection for
external torques on the spacecraft might look like:

```C++
collect shuttle.orbital.rotation.external_torque[0] = {
            shuttle.aero.out.torque[0] } ;
```

A higher fidelity parameter collection might look like:

```C++
collect shuttle.orbital.rotation.external_torque[0] = {
            shuttle.aero.out.torque[0] ,
            shuttle.grav.out.gravity_gradient_torque[0] ,
            shuttle.solar_pressure.out.torque[0] } ;
```

For those cases when there are no parameters to collect:

```C++
collect shuttle.orbital.rotation.external_torque[0] = { } ;
```

The key here is that if a new external torque for the spacecraft is added to the simulation
