### Trick Realtime Best Practices > Do's, Don'ts, and Wisdom > 5. Miscellaneous

 disabling them can improve simulation performance.

Inserting one or more of the ```#define``` statements listed below to the top of the ```S_define```, just before  the inclusion of ```default_trick_sys.sm``` will disable those modules.

```
#define TRICK_NO_EXECUTIVE
#define TRICK_NO_MONTE_CARLO
#define TRICK_NO_MEMORY_MANAGER
#define TRICK_NO_CHECKPOINT_RESTART
#define TRICK_NO_SIE
#define TRICK_NO_COMMANDLINEARGUMENTS
#define TRICK_NO_MESSAGE
#define TRICK_NO_INPUTPROCESSOR
#define TRICK_NO_VARIABLE_SERVER
#define TRICK_NO_DATA_RECORD
#define TRICK_NO_REALTIME
#define TRICK_NO_FRAMELOG
#define TRICK_NO_MASTERSLAVE
#define TRICK_NO_INSTRUMENTATION
#define TRICK_NO_INTEGRATE
#define TRICK_NO_REALTIMEINJECTOR
#define TRICK_NO_ZEROCONF
#define TRICK_NO_UNITTEST
```
##### Example
Using "SIM_submarine" as an example, the following demonstrates disabling unneeded ```default_trick_sys.sm``` modules.

```
/************************************************************
PURPOSE:
    ( Simulate a submarine. )
LIBRARY DEPENDENCIES:
    ((submarine/src/Submarine.cpp))
*************************************************************/
#define TRICK_NO_MONTE_CARLO
#define TRICK_NO_MASTERSLAVE
#define TRICK_NO_INSTRUMENTATION
#define TRICK_NO_REALTIMEINJECTOR
#define TRICK_NO_ZEROCONF
#define TRICK_NO_UNITTEST
#include "sim_objects/default_trick_sys.sm"

##include "submarine/include/Submarine.hh"

class SubmarineSimObject : public Trick::SimObject {
    public:

    ...
```

#### 1.3 Consider running Trick variable server clients and Sims on different machines.
Trick variable server clients communicate with a simulation via a TCP/IP connection.
The client process may, but isn't required to, run on the same machine as your simulation process. On the same machine, both will competing for the same resources. This can degrade sim performance, especially when clients are rendering high-definition graphics.


#### 1.4 Compile Trick and Trick sims with optimizations turned on

Example :
In my ```S_overrides.mk``` file, I'll add the "-O2" optimization flag.

```
TRICK_CFLAGS += -Imodels -O2
TRICK_CXXFLAGS += -Imodels -O2
```

See:

* [GCC Optimization Options](https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html)
* [Clang Optimization Options](https://clang.llvm.org/docs/CommandGuide/clang.html#code-generation-options)


#### 1.5 Disable unused jobs in Trick sims

Jobs can be enabled and disabled from the input file with the following commands:

```
trick.exec_get_job(<job_name>, <instance_num>).enable()
trick.exec_get_job(<job_name
