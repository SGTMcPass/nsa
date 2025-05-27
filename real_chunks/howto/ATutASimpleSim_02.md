### A Simple (non-Trick) Simulation > Cannonball Problem Statement > Limitations of the Simulation

 vel_orig[0] + acc[0] * time ;
        vel[1] = vel_orig[1] + acc[1] * time ;
        pos[0] = pos_orig[0] + (vel_orig[0] + 0.5 * acc[0] * time) * time ;
        pos[1] = pos_orig[1] + (vel_orig[1] + 0.5 * acc[1] * time) * time ;
        printf("%7.2f, %10.6f, %10.6f, %10.6f, %10.6f\n", time, pos[0], pos[1], vel[0], vel[1] );
        if (pos[1] < 0.0) {
            impact = 1;
            impactTime = (- vel_orig[1] -
                          sqrt(vel_orig[1] * vel_orig[1] - 2.0 * pos_orig[1])
                         ) / -9.81;
            pos[0] = impactTime * vel_orig[0];
            pos[1] = 0.0;
        }
        time += 0.01 ;
    }

    /* Shutdown simulation */
        printf("Impact time=%lf position=%lf\n", impactTime, pos[0]);

    return 0;
}
```

If we compile and run the program in listing 1:

```bash
% cc cannon.c -o cannon -lm
% ./cannon
```

we will see trajectory data, followed by:

```
Impact time=5.096840 position=220.699644
```
Voila! A cannonball simulation. So why do we need Trick!?

---

<a id=limitations-of-the-simulation></a>
### Limitations of the Simulation

For simple physics models like our cannonball, maybe we don't need Trick, but many real-world problems aren't nearly as simple.

* Many problems don't have nice closed-form solutions like our
cannon ball simulation. Often they need to use numerical integration methods,
to find solutions.

* Changing the parameters of our cannon ball simulation, requires that we modify
and recompile our program. Maybe that's not a hardship for a small
simulation, but what about a big one? Wouldn't it be nice if we could change our
simulation parameters, without requiring any recompilation?

* What if we want to be able to run our simulation in real-time? That is, if
we want to be able to synchronize simulation-time with "wall clock" time.

* What if we want to interact with our simulation while its running?

* What if we want to record the data produced by our simulation over time?

In the next section, we'll see how a Trick simulation goes together, and how it helps us to easily integrate user-supplied simulation models with commonly needed simulation
