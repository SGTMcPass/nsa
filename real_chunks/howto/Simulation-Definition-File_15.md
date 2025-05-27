### Trick Header Comment > Create Connections

 0.0 ;

    /* typecast the void ** as a usable double** */
    collect = (double**)R->external_torque ;

    /*
       Loop on the number of collected items
       from the above collect statement example:
       collect[0] -> shuttle.aero.out.torque
       collect[1] -> shuttle.grav.out.gravity_gradient_torque
       collect[2] -> shuttle.solar_pressure.out.torque
     */
    for( i = 0 ; i < NUM_COLLECT(collect) ; i++ ) {
        total_torque[0] += collect[i][0] ;
        total_torque[1] += collect[i][1] ;
        total_torque[2] += collect[i][2] ;
    }

    return( 0 ) ;
}
```

Several aspects of this example code which need mentioning are listed below.

1. A local pointer parameter must be declared of the same type as the parameters being
   collected, in this case the parameters being collected are double precision; hence,
   `double **collect ;`.

2. The `shuttle.orbital.rotation.external_torque` (actually a `void**`) is typecast as a
   `double**` and assigned to the local variable: `collect = (double**)R->external_torque ;`.

3. The number of parameters collected is saved in the first eight bytes before the
   address to the `external_torque` parameter. The conditional statement of the for loop
   demonstrates how the number of collected parameters is retrieved: `NUM_COLLECT(collect)`.
4. This example, and all other collection mechanism code implementations, assume the
   developer knows the type and array size of the parameters being collected. In this
   example, the parameters collected were single dimensioned double precision arrays with
   three elements per array.

## Create Connections

The create_connections section contains arbitrary code that is executed right after sim
object instantiations.  Code in this section is performed before any job of any job class.
The intended use of this section is to glue the sim objects together.  Sim objects that
need pointers to other sim objects may be assigned in the create_connections routine.
Default parameters may also be set such as defining a default simulation stop time.  Any
arbitrary code may be added to the create_connections section.

There may be multiple create_connection sections in the S_define file.  They will be
concatenated together in the order they appear in the S_define file.

```C++
class AsimObject : public Trick::SimObject {
    public:
        modelA a ;
        // This pointer points to a different sim object
        modelB * b_ptr ;

        AsimObject() {
            // This job requires type modelB from a different sim object
            (1.0 , "scheduled") a.job(b_ptr) ;
        }
} ;

class BsimObject
