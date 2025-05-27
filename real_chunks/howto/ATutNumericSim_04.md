### State Propagation with Numerical Integration > Numeric Versus Analytical

#define CANNON_NUMERIC_H

#include "cannon.h"

#ifdef __cplusplus
extern "C" {
#endif
int cannon_integ(CANNON*) ;
int cannon_deriv(CANNON*) ;
#ifdef __cplusplus
}
#endif
#endif
```
```bash
% cd SIM_cannon_numeric/models/cannon/include
% vi cannon_numeric.h <edit and save>
```

### Create **cannon_numeric.c.**

**Header and Includes for `cannon_numeric.c `**

```c
/*********************************************************************
  PURPOSE: ( Trick numeric )
*********************************************************************/
#include <stddef.h>
#include <stdio.h>
#include "trick/integrator_c_intf.h"
#include "../include/cannon_numeric.h"
```


<a id=creating-a-derivative-class-job></a>
#### Creating a Derivative Class Job

In the case of the cannon ball sim, we are making numerous simplifications, like
assuming that the acceleration of gravity is constant (in real life, it is not)
and ignoring aerodynamic drag. This means that our cannon ball simulation is not
as accurate as it might be, but for our purposes here, which is to teach how to
use Trick, it should be fine.

<a id=listing_cannon_deriv_func></a>
**Listing - `cannon_deriv()`**

```c
int cannon_deriv(CANNON* C) {

    if (!C->impact) {
        C->acc[0] = 0.0 ;
        C->acc[1] = -9.81 ;
    } else {
        C->acc[0] = 0.0 ;
        C->acc[1] = 0.0 ;
    }
    return(0);
}
```
👉 **Add cannon\_deriv() to cannon\_numeric.c.**

<a id=creating-an-integration-class-job></a>
#### Creating an Integration Class Job

For our cannon ball sim, our integration job needs to:

1. Load the cannon ball state ( pos[] and vel[] ) into the integrator.
2. Load the cannon ball state derivatives ( vel[] and acc[] )into the integrator.
3. Call the integrate() function.
4. Unload the updated state from the integrator into pos[] and vel[].
5. Return the value that was returned by the integrate() call.

**IMPORTANT**:

The functions `load_state()`, `load_deriv()`, and `unload_state()` take a
variable number of parameters. When calling these functions, the last parameter
**MUST ALWAYS BE NULL**. The NULL value marks the end of the parameter list.
Forgetting the final NULL will likely cause the simulation to crash and ... It
won't be pretty.

<a id=listing_cannon_integ_func></a>
**Listing - `cannon_integ()`**

```c
int cannon_integ(CANNON* C) {
    int ipass;

    load_state(
