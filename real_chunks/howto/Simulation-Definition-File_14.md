### Trick Header Comment > Create Connections

 {
            shuttle.aero.out.torque[0] ,
            shuttle.grav.out.gravity_gradient_torque[0] ,
            shuttle.solar_pressure.out.torque[0] } ;
```

For those cases when there are no parameters to collect:

```C++
collect shuttle.orbital.rotation.external_torque[0] = { } ;
```

The key here is that if a new external torque for the spacecraft is added to the simulation,
that torque can be accessed by the existing derivative module without code modification to the
derivative module. Note that all parameters listed must be of the same type and array dimension.

To use the parameter collection mechanism of the S_define file, the developer must perform three tasks:

1. from the example above, the external_torque parameter must be declared in its data structure
   definition file as a two dimensional void pointer, i.e. `void ** external_torque ;`,

2. a loop must be placed in the derivative module which accesses the collected parameters, and

3. the parameter collection statement must be added to the S_define.

The external_torque parameter must be declared as a two dimensional void pointer for two reasons.
First, the void type is not processed by the ICG. This means that this parameter cannot be recorded
for output or assigned data for input. If the type was any other type than void, the ICG would
assume the parameter required dynamic memory allocation and the resulting ICG generated code would
cause a fatal runtime error (usually accompanied by a core dump). Second, from an automatic code
generation viewpoint, the external_torque parameter is actually an unconstrained array of pointers,
where the pointers in the unconstrained array could be of any type (including data structure pointers);
i.e. the first pointer (*) of the declaration is the array dimension, the second is the address to
each of the collected parameters.

To make the collection mechanism work, the developer must add specific collection mechanism code to
their module. For the above example, the derivative module code might look like the following; the
text in bold indicates code which will be unchanged regardless of the parameters being collected:

```C++
#include "dynamics/v2/dynamics.h"
#include "sim_services/include/collect_macros.h"

int derivative_job( DYN_ROT * R ) {

    int i ;
    double **collect ;
    double total_torque[3] ;

    total_torque[0] = total_torque[1] = total_torque[2] = 0.0 ;

    /* typecast the void ** as a usable double** */
    collect = (double**)R->external_torque ;

    /*
       Loop on the number of collected items
       from the above collect statement example:
       collect[0] -> shuttle.aero.out.torque
       collect[1] -> shuttle.grav.out.gravity_gradient_torque
       collect[2] -> shuttle.solar_pressure.out.torque
