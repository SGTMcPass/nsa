### Trick Realtime Best Practices > Do's, Don'ts, and Wisdom > 5. Miscellaneous

 is a multi-processor model in which all processors share the physical memory uniformly. All memory accesses have the same latency.

![Realtime with itimer](images/UMA_Arch.png)

In an UMA architecture, as the number of CPUs increases, the higher the chance that the system bus will become a bottle-neck.

##### Non Uniform Memory Access (NUMA)
Non-Uniform Memory Access (NUMA) is a multiprocessor model in which each processor is connected to dedicated memory but may access memory attached to other processors in the system. A NUMA architecture is one in which accesses to different addresses may have different latencies depending on where the data is stored. NUMA essentially connects UMA elements via a data-transfer interconnect. For best performance, applications should be “NUMA aware”.

![Realtime with itimer](images/NUMA_Arch.png)

On a Linux system the following will display the available nodes, CPUs, memory, and a normalized measure of access latency between nodes.

```% numactl --hardware```

##### Example 1
```
available: 1 nodes (0)
node 0 cpus: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
node 0 size: 63986 MB
node 0 free: 54389 MB
node distances:
node   0
  0:  10
```
This computer has one NUMA node with 20 CPUs, and 64 Gigabytes.

##### Example 2
```
available: 2 nodes (0-1)
node 0 cpus: 0 1 2 3 4 5 6 7 8 9 10 11 24 25 26 27 28 29 30 31 32 33 34 35
node 0 size: 15371 MB
node 0 free: 3926 MB
node 1 cpus: 12 13 14 15 16 17 18 19 20 21 22 23 36 37 38 39 40 41 42 43 44 45 46 47
node 1 size: 16120 MB
node 1 free: 4504 MB
node distances:
node   0   1 
  0:  10  21 
  1:  21  10 
```
This computer has two NUMA nodes, each with 24 CPUs, and each with about 16 gigabytes of local memory, for a total of 32 Gigabytes. The "distances" matrix at the bottom tells us that memory access latency between the nodes is (21/10) = 2.1 times the
