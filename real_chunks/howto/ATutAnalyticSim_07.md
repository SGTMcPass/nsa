### Building & Running a Trick-based Simulation > Running The Simulation > Sim Execution

ON* C ) {

    C->acc[0] =  0.00;
    C->acc[1] = -9.81 ;
    C->vel[0] = C->vel0[0] + C->acc[0] * C->time ;
    C->vel[1] = C->vel0[1] + C->acc[1] * C->time ;
    C->pos[0] = C->pos0[0] + (C->vel0[0] + (0.5) * C->acc[0] * C->time) * C->time ;
    C->pos[1] = C->pos0[1] + (C->vel0[1] + (0.5) * C->acc[1] * C->time) * C->time ;
    if (C->pos[1] < 0.0) {
        C->impactTime = (- C->vel0[1] - sqrt( C->vel0[1] * C->vel0[1] - 2 * C->pos0[1]))/C->acc[1];
        C->pos[0] = C->impactTime * C->vel0[0];
        C->pos[1] = 0.0;
        C->vel[0] = 0.0;
        C->vel[1] = 0.0;
        if ( !C->impact ) {
            C->impact = 1;
            fprintf(stderr, "\n\nIMPACT: t = %.9f, pos[0] = %.9f\n\n", C->impactTime, C->pos[0] ) ;
        }
    }
    /*
     * Increment time by the time delta associated with this job
     * Note that the 0.01 matches the frequency of this job
     * as specified in the S_define.
     */
    C->time += 0.01 ;
    return 0 ;
}
```

This routine looks much like the routine found in our Trick-less simulation. It
is the piece that was surrounded by a while-loop. Underneath, Trick will
surround this job with its own while-loop. As in the case of the `cannon_init()`
routine, there is nothing particularly special about `cannon_analytic()`. It is
just another C function that will be compiled into an object, and later, linked
with a number of libraries to create a simulation executable.

```bash
% cd $HOME/trick_sims/SIM_cannon_analytic/models/cannon/src
% vi cannon_analytic.c
```

Type in the contents of **Listing 5** and save.

<a id=cannonball_cleanup_and_shutdown></a>
### Cannonball Cleanup And Shutdown

**shutdown** job types are called by
