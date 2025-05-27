### Trick Realtime Best Practices > Do's, Don'ts, and Wisdom > 5. Miscellaneous

 - Documents the name and path of the executable and the input file, the build time of the simulation executable, and the Trick version. It also contains the list of environment variables used when the simulation was built and the model versions.|
|```RUN_*/send_hs ```|the end of this file contains run statistics that may be useful.|

---

### Trick Executive Scheduler

The
 [Executive Scheduler](https://nasa.github.io/trick/documentation/simulation_capabilities/Executive-Scheduler) determines how, when, and where (which CPU) the jobs in your Trick sim are executed.


* [Job Control](https://nasa.github.io/trick/documentation/simulation_capabilities/Executive-Scheduler#job-control) - describes the Trick job control interface.
* [Thread Control](https://nasa.github.io/trick/documentation/simulation_capabilities/Executive-Scheduler#thread-control)  - describes the attributes and behaviors of different Trick thread types.

Thread control will in some cases require that you isolate CPUs at boot-time. This is usualy done with the **isolcpus** boot parameter:

```isolcpus= cpu_number[, cpu_number,...]```

Ref: [RedHat: Isolating CPUs Using tuned-profiles-realtime](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux_for_real_time/7/html/tuning_guide/isolating_cpus_using_tuned-profiles-realtime)


<a id=guidelines></a>
## Do's, Don'ts, and Wisdom

---
### 1 Trick
---

#### 1.1 Trick events are computationally expensive. Use them judiciously.

Trick events can provide a quick and easy way to customize the behavior of a sim, based on some condition. But, because they require Python interpretation, they are slow. They are not intended for implementation of permanent sim functionality. If they are over used, they can seriously degrade simulation performance. So, take it easy with the events.

See [Event Manager](https://nasa.github.io/trick/documentation/simulation_capabilities/Event-Manager).

#### 1.2 Disable Trick run-time components that your sim doesn't need.

```default_trick_sys.sm```, the file included at the top of any Trick ```S_define``` file defines numerous "modules" that provide functionality to a Trick sim. Whereas some of these modules ( like the Executive, MemoryManager, CommandLineArguments) are required for any Trick Simulation to function, many are optional. If the modules are not needed, then disabling them can improve simulation performance.

Inserting one or more of the ```#define``` statements listed below to the top of the ```S_define```, just before  the inclusion of ```default_trick_sys.sm``` will disable those modules.

```
#define TRICK_NO_EXECUTIVE
#define TRICK_NO_MONTE_CARLO
#define TRICK_NO_MEMORY_MANAGER
#define TRICK_NO_CHECKPOINT_RESTART
#define TRICK_NO_SIE
