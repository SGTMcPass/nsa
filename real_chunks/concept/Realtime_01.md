### User accessible routines

 time to run the execution frame \> real-time frame, an overrun has
occurred, meaning the simulation is running slower than real-time. Trick will immediately
start the next execution frame in an attempt to catch up after an overrun.

Trick provides real-time synchronization using the system clock.
It is also possible to use an external time source instead of the system clock. To do so
you must provide your specific external clock functionality by deriving from Trick's
Clock class. (Trick provides the GetTimeOfDayClock class as a derivative of Clock).
See [Realtime Clock](Realtime-Clock).

A timer may also be used when syncing to real-time during an underrun. Trick provides
this functionality by using a system interval timer or itimer.  It is possible to use
an external timer instead of an itimer. To do so you must provide your specific external
timer functionality by deriving from Trick's Timer class. (Trick provides the ITimer class
as a derivative of Timer).  See [Realtime_Timer](Realtime-Timer).

## User accessible routines

```
int real_time_enable() ;
int real_time_disable() ;
int real_time_restart(long long ref_time) ;
int is_real_time() ;
```

[Continue to Realtime Clock](Realtime-Clock)
