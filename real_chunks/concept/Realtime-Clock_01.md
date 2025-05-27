### Realtime-Clock > Looking For The Current Simulation Time ?

ECLOCK_HH
#define TPROCTECLOCK_HH
#include <string>
#include "trick/Clock.hh"
#ifdef _TPRO_CTE
extern "C" {
#include "tpro.h"
#include "tsync.h"
}
#endif

class TPROCTEClock : public Trick::Clock {
    public:
        TPROCTEClock() ;
        ~TPROCTEClock() ;
        int clock_init() ;
        long long wall_clock_time() ;
        int clock_stop() ;
        std::string dev_name ;
    private:
#ifdef _TPRO_CTE
        TPRO_BoardObj *pBoard ;  /* ** board handle */
#endif
    } ;
#endif
```

<a id=listing_2_clock-init></a>
### TPROCTEClock::clock_init

Here, we initialize the timing card by opening the device file, getting a device handle. Then we wait for for it to be available. If an error occurs, return a non-zero error code, otherwise we call ```set_global_clock()``` and return 0.

```c
int TPROCTEClock::clock_init() {
#ifdef _TPRO_CTE
    unsigned char  rv;
    /* Open the TPRO/TSAT device */
    rv = TPRO_open(&pBoard, (char *)dev_name.c_str());
    /* If unable to open the TPRO/TSAT device... */
    if (rv != TPRO_SUCCESS) {
        printf (" Could Not Open '%s'!! [%d]\n", dev_name.c_str(), rv);
        return (1);
    }
    /* Wait until this handle is the first user of the device. */
    if (TPRO_setPropDelayCorr(pBoard, NULL) != TPRO_SUCCESS) {
        printf(" Waiting to become first user...\n");
        while (TPRO_setPropDelayCorr(pBoard, NULL) != TPRO_SUCCESS);
    }
    set_global_clock() ;
    return 0 ;
#else
    printf("ERROR: Not configured for TPRO CTE card.");
    return -1 ;
#endif
}
```

### TPROCTEClock::wall\_clock\_time
In this function, we get the time from the timing card, and convert it to microseconds before returning it. If the attempt to get the time fails, we return 0.

```c
long long TPROCTEClock::wall_clock_time() {
#ifdef _TPRO_CTE
    TSYNC_HWTimeSecondsObj hwTime;
    /* Send Get Seconds Time message */
    TSYNC_ERROR err = TSYNC_HW_getTimeSec(pBoard, &hwTime);
    if (err != TSYNC_SUCCESS) {
        printf("  Error: %s.\n", tsync_strerror(err));
        return 0;
    }
    /* If sucessful convert the TPRO time to microsconds. */.
    return hwTime.time.seconds * 1000000LL + (hwTime.time.ns /1000);
#else
    printf("ERROR: Not configured for TPRO CTE card.");
    return 0 ;
#endif
}
```

### TPROCTEClock::clock\_stop

This function simply closes the handle to the device, and returns 0.

```c
int TPROCTEClock::clock_stop() {
#ifdef _TPRO_CTE
    unsigned char rv ;
    rv = TPRO_close(pBoard);
    /* If unable to close the TPRO/TSAT device... */
    if (rv != TPRO_SUCCESS) {
        printf (" Could Not Close Board!! [%d]\n", rv);
    }
#endif
    return 0 ;
}
```
<a id=looking-for-sim-time></a>
## Looking For The Current Simulation Time ?

Trick::Clock is a class for creating interfaces between timing hardware, or other time sources and Trick's realtime synchronization subsystem. It does not maintain the simulation time. That's maintained by the Trick Executive.

What you may be looking for is the function

```c
double exec_get_sim_time(void) ;
```

defined in ```exec_proto.h```.

Continue to [Realtime Timer](Realtime-Timer)
