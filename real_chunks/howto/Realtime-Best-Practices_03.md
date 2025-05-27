### Trick Realtime Best Practices > Do's, Don'ts, and Wisdom > 5. Miscellaneous

obs*

|#  | Name | Type | Units | Description |
|--:|:---- |:-----|:-----:|-------------|
| 1| ```sys.exec.out.time```                  | double | seconds |Simulation Time |
| n| *user-job-name* | double | seconds |How long the user-job took to execute. |

---

<a id=log-frame-trickjobs-trk></a>
#### ```log_frame_trickjobs.trk```
* Number of fields per record : 1 + *#trick-jobs*

|#  | Name | Type | Units | Description |
|--:|:---- |:-----|:-----:|-------------|
| 1| ```sys.exec.out.time```                  | double | seconds |Simulation Time |
| n| *trick-job-name* | double | seconds |How long the trick-job took to execute. |

<a id=log-timeline-csv></a>
#### ```log_timeline.csv``` & ```log_timeline_init.csv```
These files contain start and stop times for each of the jobs executed in a trick sim.
```log_timeline.csv``` contains times for jobs run during run-time. ```log_timeline_init.csv``` contains times for jobs run at initialization time.

Frankly this format is **weird**, but it contains useful information.
It's weird because of its redundancy, and that each job timing "record" consists of four CSV lines.

Both files have the same format. They contain three columns, of ```float``` formatted numbers representing (in order, left to right):

1. time-stamp
2. trick job ID
3. user job ID

Each record consists of four rows in the CSV file representing the start and stop times of a job.

|row#|time-stamp|trick-job-id|user-job-id|
|---:|---:|---:|---:|
|4xRecord#+0|start-job-time|0|0|
|4xRecord#+1|start-job-time|trick job id|user-job-id|
|4xRecord#+2|stop-job-time|trick-job-id|user-job-id|
|4xRecord#+3|stop-job-time|0|0|

If **trick** job ID is non-zero, then the **user** job ID will be zero, and vice versa.
Within any four line record the job-ID will be recorded twice.

##### Example

The following is one four-line record from a ```log_timeline.csv``` file.

```
...
0.000026,0,0
0.000026,16.010000,0
0.000027,16.010000,0
0.000027,0,0
...
```
The first line of the record indicates that **some** job started at time=0.000026 seconds. It's not until the second line of the record that you find that the start time (
