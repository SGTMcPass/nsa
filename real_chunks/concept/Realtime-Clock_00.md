### Realtime-Clock > Looking For The Current Simulation Time ?

| [Home](/trick) → [Documentation Home](../Documentation-Home) → [Simulation Capabilities](Simulation-Capabilities) → Realtime Clock |
|------------------------------------------------------------------|

# Realtime-Clock

**Contents**

* [Creating a Real-Time Clock Interface with Trick::Clock](#creating-a-clock)<br>
* [Installing a Trick::Clock In Your Simulation](#installing-a-clock)<br>
* [Example Implementation of a Trick::Clock](#example-implemntation)<br>

***

* [**Looking For The Current Simulation Time?**](#looking-for-sim-time)<br>

***

Every real-time simulation requires a clock to which its tasks can be synchronized. By default, a Trick simulation uses the local system clock, by calling *gettimeofday()*. When simulations running on different computers need to cooperate they need to be synchronized to the same clock. So, sometimes we want our simulation to synchronize a to an **external** clock rather than the local one. The ```Trick::Clock``` base class provides a way to create an interface between an external time source, and a real-time Trick simulation.

<a id=creating-a-clock></a>
## Creating a Real-Time Clock Interface with Trick::Clock

The Trick::Clock class is declared in ```trick/Clock.hh```. Deriving a new clock interface class from it requires the following three member functions to be implemented.

***

```c
int Trick::Clock::clock_init();
```
#### 1. clock\_init's Responsibilities
1. If necessary, initialize the time source. This may involve opening and initializing a hardware device, or a network socket connection.
2. If an error occurs, return a non-zero error code, otherwise call ```set_global_clock()``` and return 0.

***

```c
long long Trick::Clock::wall_clock_time()
```
#### 2. wall\_clock\_time's Responsibilities
1. Get the time from the time source.
2. Return the time in microseconds, or 0 if there **is** an error.

***

```c
int Trick::Clock::clock_stop()
```
#### 3. clock_stop's Responsibilities
1. If necessary, disconnect from the time source.
2. If an error occurs, return a non-zero error code, otherwise return 0.

***

<a id=installing-a-clock></a>

## Installing a Trick::Clock In Your Simulation

By default, Trick uses a derivative of  ```Trick::Clock``` called ```Trick::GetTimeOfDayClock```.

Suppose we've derived a new class ```CuckooClock``` from ```Trick::Clock```, and have created an instance of it:

```c
chalet.my_clock = new CuckooClock();
```

In our simulation's S_define file, we could change the real-time scheduler's clock from the default ```Trick::GetTimeOfDayClock``` to our new ```CuckooClock``` using ```real_time_change_clock()```, declared in ```trick/realtimesync_proto.h```.

```c
void create_connections() {
    chalet.my_clock = new CuckooClock();
    real_time_change_clock(chalet.my_clock);
}
```
We could also change the ```Trick::Clock``` in our input file as follows:

```c
trick.real_time_change_clock(chalet.my_clock)
```

<a id=example-implemntation></a>
## An Example Implementation of a Trick::Clock

The following code is an example implementation of a Trick::Clock, called TPROCTEClock. It provides an interface between Trick's real-time job scheduler and Spectracom's TPRO IRIG-B clock board. This is one of many available time sources that one might use. Note that driver support for timing cards, like the "tpro.h" and "tsync.h" files below, must be acquired from the card's vendor.

<a id=listing_1_Clock-header-file></a>
### TPROCTEClock Header File
```c
/*
PURPOSE: ( TPRO CTE Clock )
*/
#ifndef TPROCTECLOCK_HH
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

<a id=
