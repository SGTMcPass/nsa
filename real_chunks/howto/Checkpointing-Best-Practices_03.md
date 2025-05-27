### Trick CheckPointing Best Practices > Other Resources You Might Find Useful

 jobs are called. These job-classes allow you to prepare your sim for a checkpoint-restore, in whatever way you see fit.

2. ```init_from_checkpoint( <filename> )``` is called, which:

	1. Calls ```reset_memory``` to delete all dynamically allocated objects.
	2. Calls ```read_checkpoint( <filename> )``` to read, parse, and restore the state described in the checkpoint file.
		* Read the **definitions** section of the checkpoint file, and allocate all of the objects described there in.
		* Clear all of the objects to 0, as appropriate to the data-type.
		* Read the **assignment statement section**, and assign values to the objects.

3. Run the ```“restart”``` jobs. These too are user-defined jobs that “tidy up” the simulation state. For example, this is where files might be re-opened, or socket connections are re-established. Again, what this does is up to the sim designer.

<a id=guidelines></a>
## Do's and Don'ts
* Plan for, and test that your models are checkpointable. Don't let this be an after-thought. Just like testing, if this is done from the beginning the pain suffering you’ll endure will be greatly reduced.

* Keep data types no more complicated than they need to be. Remember the KISS principle.

* If [I/O specification](https://nasa.github.io/trick/tutorial/ATutAnalyticSim#the-inputoutput-io-specification) of a data member is ```**``` then it will not be saved in a checkpoint.

* Don't make anonymous allocations in the input file. Naming them will make it much easier to find them later.

* If you want your allocated objects to be checkpointed, allocate them with Memory Manager functions like: ```TMM_declare_var```, ```TMM_declare_var_1d```, and ```TMM_declare_var_s```.

* If you use the ```new``` or ```malloc``` to allocate memory, the trick memory manager will have no knowledge of the memory allocation and will not checkpoint it. In order to make trick aware, you need to use a trick memory manager function to allocate (as above) or use ```declare_extern_var```.

* In the case where you use ```declare_extern_var```, it's important to remember that that Trick will not delete nor restore objects that it did not allocate. It does not know how **extern** memory was allocated ( Note that ```new``` and ```malloc``` are not the only ways to allocate memory ). You are still responsible for de-allocation at the appropriate time.

<a id=other-resources></a>
## Other Resources You Might Find Useful
* [https://github.com/nasa/trick/tree/master/trick_source/sim_services/MemoryManager/test](https://github.com/nasa/trick/tree/master
