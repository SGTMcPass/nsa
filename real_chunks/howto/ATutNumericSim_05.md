### State Propagation with Numerical Integration > Numeric Versus Analytical

 the last parameter
**MUST ALWAYS BE NULL**. The NULL value marks the end of the parameter list.
Forgetting the final NULL will likely cause the simulation to crash and ... It
won't be pretty.

<a id=listing_cannon_integ_func></a>
**Listing - `cannon_integ()`**

```c
int cannon_integ(CANNON* C) {
    int ipass;

    load_state(
        &C->pos[0] ,
        &C->pos[1] ,
        &C->vel[0] ,
        &C->vel[1] ,
        NULL);

    load_deriv(
        &C->vel[0] ,
        &C->vel[1] ,
        &C->acc[0] ,
        &C->acc[1] ,
        NULL);

    ipass = integrate();

    unload_state(
        &C->pos[0] ,
        &C->pos[1] ,
        &C->vel[0] ,
        &C->vel[1] ,
        NULL );

    return(ipass);
}

```

👉 **Add cannon\_integ() to cannon\_numeric.c.**

<a id=updating-the-s_define-file></a>
## Updating the S_define File

Next, our S_define file needs to be updated.

### Update LIBRARY DEPENDENCIES
In the `LIBRARY_DEPENDENCY` section, replace:
`(cannon/src/cannon_analytic.c)`
with `(cannon/src/cannon_numeric.c)`.

### Update ##include Header File

Replace:

```c++
##include "cannon/include/cannon_analytic.h"
```

with:

```c++
##include "cannon/include/cannon_numeric.h"
```

### Update Scheduled Jobs

Replace:

```c++
(0.01, "scheduled") cannon_analytic( &cannon ) ;
```

with:

```c++
   ("derivative") cannon_deriv( &cannon ) ;
   ("integration") trick_ret= cannon_integ( & cannon ) ;
```

### Add Integration Scheduler and Integrator
To the bottom of the S_define file, add:

```c++
IntegLoop dyn_integloop (0.01) dyn ;
void create_connections() {
    dyn_integloop.getIntegrator(Runge_Kutta_4, 4);
}
```

The first line here defines an integration scheduler called `dyn_integloop` that executes `derivative` and `integration` jobs in the *dyn* SimObject. The integration rate is specified in parentheses.

`create_connections` is a special function-like construct whose code is copied into S_source.cpp and is executed directly after SimObject instantiations. Common uses are to 1) instantiate integrators, and 2) connect data structures between SimObjects.

`dyn_integloop.getIntegrator` configures our integration scheduler. Its first argument specifies the integration algorithm
