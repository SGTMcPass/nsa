### Trick Realtime Best Practices > Do's, Don'ts, and Wisdom > 5. Miscellaneous

# Trick Realtime Best Practices

**Contents**

* [Purpose](#Purpose)<br>
* [Prerequisite Knowledge](#prerequisite-knowledge)<br>
* [Do's, Don'ts and Wisdom](#guidelines)<br>

<a id= introduction></a>

---
## Purpose
The intention of this document is to compile and share practical knowledge, based on the experience of people in the Trick simulation community regarding the development of realtime computer simulations.

<a id=prerequisite-knowledge></a>
## Prerequisite Knowledge
(Assuming you've completed the [Trick Tutorial](https://nasa.github.io/trick/tutorial/Tutorial))

---

<a id=simulation-time-vs-realtime></a>
### Simulation Time vs Realtime

Real world dynamic systems change in realtime (the time that you and I experience). A simulated dynamic system changes in simulation time. Simulation time begins at t=0, and runs until we stop it. Simulation time can elapse faster or slower than realtime.

If we want to interact with a simulation as if it were real, we need to synchronize simulation time to realtime. This requires that a simulation is capable of running at least as fast as realtime. If it is incapable, then it can not be made to run in realtime.

---

<a id=realtime-clock></a>
### Realtime Clock
* By default, the Trick realtime scheduler will synchronize to the system clock:
	* ```clock_gettime(CLOCK_REALTIME,…)``` [Linux]
	* ```gettimeofday()``` [Mac OS]

* The Trick realtime scheduler can also be configured to synchronize to a [custom realtime clock](https://nasa.github.io/trick/documentation/simulation_capabilities/Realtime-Clock).

---

<a id=enabling-realtime></a>
### Enabling Realtime

Trick tries to consistently and repetitively execute its scheduled math models to completion within some predetermined realtime interval for an indefinite period. This realtime interval is called the **realtime software frame**.

To enable realtime synchronization, call ```trick.real_time_enable()``` in the input file.

[Ref: Realtime](https://nasa.github.io/trick/documentation/simulation_capabilities/Realtime)

---

<a id=realtime-software-frame></a>
### Realtime Software Frame
The realtime software frame determines how often Trick will synchronize simulation time to the realtime clock.  Simulation time will run as fast as it can in the intervals between realtime synchronizations.

To set the realtime software frame, call the following in the input file:

```python
trick.exec_set_software_frame(double time)
```
[Ref: Software Frame](https://nasa.github.io/trick/documentation/simulation_capabilities/Executive-Scheduler#software-frame)

---

<a id=under-runs-and-over-runs></a>
### Under-runs and Over-runs

An **under-run** occurs when the Trick executive finishes running all of its scheduled jobs, between synchronizations to the
