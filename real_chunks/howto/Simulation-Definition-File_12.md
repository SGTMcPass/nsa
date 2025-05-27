### Trick Header Comment > Create Connections

 ;
        }
} ;

ballSimObject ball ;
```

`ball_ptr` is not instantiated when the simulation is compiled.  If nothing is assigned to `ball_ptr`
before the first scheduled call of `ball_ptr->print_type()` then the call will fail and the sim
will core.  We can allocate `ball_ptr` in the input file.  We can even change `ball_ptr` in the
middle of the simulation.

```python
ball.ball_ptr = trick.TMM_declare_var_s("Soccerball[1]")
trick.add_read(20.0 , """ball.ball_ptr = trick.TMM_declare_var_s("Baseball[1]")""")
```

## State Integration Specification

Trick manages state integration with exceptional flexibility. The integration specification
allows the developer to group the derivative, integration, and dynamic_event class modules
(for any combination of sim objects) for state integration using a particular integrator and
state integration time step. Some simulations will have several different sets of state
parameters, each set requiring a unique state integration scheme and integration time step.
Likewise, other simulations will require all the derivative class modules from a group of
sim objects to be executed before the integration class modules of the same sim object group.
The integration specification provides this capability.

The integration specification is of the following form:

```
integrate <integrator_name> (<integration_dt>) <sim_object_name> [,<sim_object_name_n>] ;
```

An alternative instantiation syntax which is pure C++ is of the form:

```C++
IntegLoopSimObject <integrator_name> (<integration_dt>, <sim_object_name> [,<sim_object_name_n>], NULL ) ;
```

This form must have NULL as the final argument to the instantiation.

The integrate tag is a reserved word for the CP. The <integration_dt> is a state integration
cycle time in seconds. At least one sim object name must be specified followed by any number
of additional sim object names separated by commas. An S_define can have at most one integrate
statement per sim object, and at least one integrate statement for all sim objects.

## Parameter Collection Mechanism

The parameter collection mechanism is probably the most difficult capability of the CP to
understand and utilize. This capability is useful when the user wants a single job to handle
`n` number (either a known or unknown `n`) of parameters of the same type. The parameter
collection mechanism is an alternative for a variable calling argument list The collection
mechanism syntax in the S_define file is as follows:

```C++
collect <reference> = { } ;
```

or

```C++
collect <reference> = { <reference_1> [,<reference_n>] } ;
```

There is also a C code equivalent to adding collect references one at a time that may
be put in a create_connections section of the S_define file.  The advantage of
