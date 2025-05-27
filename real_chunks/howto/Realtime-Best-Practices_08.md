### Trick Realtime Best Practices > Do's, Don'ts, and Wisdom > 5. Miscellaneous

 confirm that your base, default, "empty input file" sim is initialized to a valid state, then it will be easier to identify errors when the sim is customized for different scenarios, via an input file. It saves time and reduces pain.

---
### 2. User Simulation Software
---

#### 2.1 Don't read from the disk during run-time.
Disk access is slow. If you need to read from disk, do it in a ```default_data```, or ```initialization``` job.


#### 2.2 Try to reduce variation in job cycle times.
Realtime performance is largely about minimizing the worst case, rather than the average case.
The most well behaved job takes the same amount of time, every time.


#### 2.3 Minimize dynamic memory allocation during run-time
The time to dynamically allocate memory can vary, and in the worst-case is unbounded. This is bad for realtime performance.


#### 2.4 Allow the compiler to help you find problems

Modern compilers have gotten very helpful, and can check for a lot of potential problems.
Many people are familiar with the compiler warning options like ```-Wall```, ```-Wextra```, and ```-Wshadow```. Be aware that there are a lot more, to help you find problems:

* [GCC Warning Options](https://gcc.gnu.org/onlinedocs/gcc/Warning-Options.html)
* [CLANG Warning Options](https://clang.llvm.org/docs/DiagnosticsReference.html)


#### 2.5 Fix All Compiler Warnings And Errors
Many a time the necessary clue needed to solve an intractable problem was there all along, in the form of an unheeded warning that scrolled by unseen.

Don't ignore the messages.

When Trick builds a sim, it generates the files, ```MAKE_out``` and ```MAKE_err``` in the ```build``` directory. These files contain the makefile output of the sim build. It's a good idea to check these for warnings on a big sim build.

---
### 3. Hardware
---

#### 3.1 Know Your Simulation Machine Architecture
Getting the best performance from a simulation on a multi-CPU machine requires understanding of the machine's hardware architecture. Particularly important is data transfer delay from memory to the CPU (latency). Depending on the machine architecture, and how data processing is allocated across CPUs, the time used for memory access, and therefore simulation performance can very significantly.

##### Uniform Memory Access (UMA)
Uniform memory access (UMA) is a multi-processor model in which all processors share the physical memory uniformly. All memory accesses have the same latency.

![Realtime with itimer](images/UMA_Arch.png)

In an UMA architecture, as the number of CPUs increases, the higher the chance that the system bus will become a bottle-neck.

##### Non Uniform Memory Access (NUMA)
Non-Uniform Memory Access (NUMA) is a multiprocessor
