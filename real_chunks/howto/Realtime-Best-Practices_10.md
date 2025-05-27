### Trick Realtime Best Practices > Do's, Don'ts, and Wisdom > 5. Miscellaneous

  0:  10  21 
  1:  21  10 
```
This computer has two NUMA nodes, each with 24 CPUs, and each with about 16 gigabytes of local memory, for a total of 32 Gigabytes. The "distances" matrix at the bottom tells us that memory access latency between the nodes is (21/10) = 2.1 times the latency within a node.


#### 3.2 Turn Off Any Energy-Efficiency Settings
Energy efficiency and performance are usually trade-offs. Turn off any energy-efficiency settings the computer may have enabled, usually in the BIOS.


#### 3.3 Fewer, Faster Cores Are Preferable to More, Slower Cores
For simulation hosts, fewer but faster cores is usually preferable to more but slower cores

* **Server-class** machines are designed for throughput.
* **Performance** machines are designed for low latency, high-speed computing.


#### 3.4 Buy More Memory
Insufficient random access memory (RAM) leads to virtual memory page swapping, which degrades realtime performance. More RAM is one of the easiest and cheapest ways of boosting machine performance.


#### 3.5 Avoid Intel “Efficiency” Cores
Intel "efficiency" cores aren’t currently recognized by most Linux OS’s and will cause a lot of problems. They are more energy efficient, but slower, the opposite of what hard realtime needs. RHEL8 is unable to determine which cores are “E” (Efficiency) and which are “P” (Performance). Did I mention you should buy more memory?

---
### 4. Network
---

#### 4.1 Have Multiple Network Interface Jacks On Sim Machines
Isolate all sim-to-sim traffic to one network interface. Leave the other for connections to the box and OS traffic.


#### 4.2 Use One Master Clock For All Machines On The Network
All clocks will drift apart unless periodically synchronized. Synchronization means that one of the clocks must be the reference, or "master". Multiple unsynchronized clocks in a realtime system is nightmare fuel.

---
### 5. Miscellaneous
---

#### 5.1 Maintain a history of simulation performance.

Maintain a performance history of your sim as development procedes. This can be very useful evidence in solving problems. Begin frame logging the sim even before implementing realtime.


#### 5.2 Take care when "tuning" operating system behavior
Overriding the OS by isolating CPUs, assigning threads to CPUs, redirecting interrupts, changing priorities, and so forth can be powerful techniques to improve performance, but with the same power they can degrade it. Modern operating systems are pretty good at managing performance. If you decide to "help" the OS, you’ll need to know what you’re doing. Take the time to study up first.

Some useful learning material:

* [Challenges Using Linux as a
