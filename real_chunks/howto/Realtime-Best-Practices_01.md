### Trick Realtime Best Practices > Do's, Don'ts, and Wisdom > 5. Miscellaneous

 input file:

```python
trick.exec_set_software_frame(double time)
```
[Ref: Software Frame](https://nasa.github.io/trick/documentation/simulation_capabilities/Executive-Scheduler#software-frame)

---

<a id=under-runs-and-over-runs></a>
### Under-runs and Over-runs

An **under-run** occurs when the Trick executive finishes running all of its scheduled jobs, between synchronizations to the realtime clock. This is a **good thing**. In this case the executive will enter a spin loop, waiting for the next realtime frame to start.

<a id=figure-realtime-under-run></a>
![Realtime Under Run](images/RealtimeUnderRun.png)

An **over-run** occurs if the executive does not finish running all of its scheduled jobs. This is a **bad-thing**. In this case, the executive will immediately start the next frame in an attempt to catch up.

<a id=figure-realtime-over-run></a>
![Realtime Over Run](images/RealtimeOverRun.png)

---

<a id=itimers></a>
### Itimers ( Being Nice to Other Processes On Your System )

During real time under runs you may want to release the processor for other tasks to use instead of spinning waiting for the clock. Trick provides a realtime sleep timer based on itimers. You might think of it as a “snooze button”.

To enable itimers call ```trick.itimer_enable()``` from the input file.

With itimer_enabled, the simulation will sleep() after completing the jobs scheduled for the current frame. The itimer will then wake the sim 2ms before the realtime frame is to expire.  The executive will spin for the final 2ms. The 2ms spin is there because an itimer interval is not guaranteed to be perfectly precise.

<a id=figure-Realtime-with_itimer></a>
![Realtime with itimer](images/RealtimeWithItimer.png)

[Ref: Itimer](https://nasa.github.io/trick/documentation/simulation_capabilities/Realtime-Timer)

---

<a id=frame-logging></a>
### Frame-Logging ( Critical For Improving Sim Performance )

The failure of a simulation to meet its scheduling requirements can have many causes. To aid in solving these problems, Trick can gather simulation performance data, called **frame-logging** by calling:

```trick.frame_log_on()```

in your sim's input file.

Note that frame logging will add some overhead to a simulation as each job is timed and recorded.

[Ref: Frame-Logging](https://nasa.github.io/trick/documentation/simulation_capabilities/Frame-Logging)

<a id=frame-log-files></a>
#### Frame Log Files
Frame logging records the following data files in your sim’s RUN_ directory:

* [```log_frame.trk```](#log-frame-trk)<br>
* [```log
