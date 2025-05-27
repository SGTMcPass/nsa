### Trick Realtime Best Practices > Do's, Don'ts, and Wisdom > 5. Miscellaneous

 by isolating CPUs, assigning threads to CPUs, redirecting interrupts, changing priorities, and so forth can be powerful techniques to improve performance, but with the same power they can degrade it. Modern operating systems are pretty good at managing performance. If you decide to "help" the OS, you’ll need to know what you’re doing. Take the time to study up first.

Some useful learning material:

* [Challenges Using Linux as a Real-Time Operating System](https://ntrs.nasa.gov/api/citations/20200002390/downloads/20200002390.pdf)
* [Optimizing RHEL 8 for Real Time for low latency operation](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux_for_real_time/8/html-single/optimizing_rhel_8_for_real_time_for_low_latency_operation/index)

#### 5.3 Don’t isolate CPU 0
Nothing good can come from this.


#### 5.4 Best Performance Requires Root Privileges

Ways to give root privilege to sim:

1. Run as root ( Don't )
2. Change owner of executable to root and set user id bit

Use ```sudo``` command to give root privileges to the simulation executable using ```chown``` and ```chmod``` commands.

```
chown root S_main_${TRICK_HOST_CPU}.exe
chmod 4775 S_main_${TRICK_HOST_CPU}.exe
```
