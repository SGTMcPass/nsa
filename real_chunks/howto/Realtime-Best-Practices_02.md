### Trick Realtime Best Practices > Do's, Don'ts, and Wisdom > 5. Miscellaneous

 logging will add some overhead to a simulation as each job is timed and recorded.

[Ref: Frame-Logging](https://nasa.github.io/trick/documentation/simulation_capabilities/Frame-Logging)

<a id=frame-log-files></a>
#### Frame Log Files
Frame logging records the following data files in your sim’s RUN_ directory:

* [```log_frame.trk```](#log-frame-trk)<br>
* [```log_frame_trickjobs.trk```](#log-frame-trickjobs-trk)
* [```log_frame_userjobs_main.trk```](#log-frame-userjobs-main-trk)
* [```log_timeline.csv```](#log-timeline-csv)
* [```log_timeline_init.csv```](#log-timeline-csv)

Note that **main** in this file name refers to the main thread.
If child threads (for example: C1, C2, ...) have been specified in the sim then frame log files for those threads will also be created ( that is:```log_trick_frame_userjobs_C1.trk```, ```log_trick_frame_userjobs_C2.trk```, ```...```).

---

<a id=log-frame-trk></a>
#### ```log_frame.trk```
* Number of fields per record : 5

|#  | Name | Type | Units | Description |
|--:|:---- |:-----|:-----:|-------------|
| 1| ```sys.exec.out.time```                  | double | seconds |Simulation Time |
| 2| ```trick_real_time.rt_sync.frame_time``` | double | seconds | This badly named parameter expresses the amount of time that the scheduled jobs in this frame took to execute. See: [figure](#figure-realtime-under-run)|
|3| ```trick_real_time.rt_sync.frame_overrun ``` | double | seconds | The magnitude of the current overrun. See: [figure](#figure-realtime-over-run) |
|4| ```JOB_data_record_group_frame_userjobs.data_record...``` | double | s | How long the write job for the user Jobs data recording group took. |
|5| ```JOB_data_record_group.trickjobs...``` | double | seconds | How long did the write job for the Trick Jobs data recording group take. |

---

<a id=log-frame-userjobs-main-trk></a>
#### ```log_frame_userjobs_main.trk```
* Number of fields per record : 1 + *#user-jobs*

|#  | Name | Type | Units | Description |
|--:|:---- |:-----|:-----:|-------------|
| 1| ```sys.exec.out.time```                  | double | seconds |Simulation Time |
| n| *user-job-name* | double | seconds |How long the user-job took to execute. |

---

<a id=log-frame-trickjobs-trk></a>
#### ```log_frame_trickjobs
