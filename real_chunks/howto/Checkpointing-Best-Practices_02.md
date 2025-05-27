### Trick CheckPointing Best Practices > Other Resources You Might Find Useful

pointing

A **checkpoint** is a persistent representation of a simulation state. It's exactly like a "saved computer game" when it's time for dinner.

If the Trick Memory Manager **"knows"** about all of the allocations that comprise the state of a simulation, then it can checkpoint that simulation. The Trick Memory Manager checkpoints a simulation by :

1. Opening a checkpoint file.
1. Writing all the **definitions**, of all of the objects that it knows about, to the file.
2. Writing ```clear_all_vars();``` to the file. This is interpreted when the checkpoint is re-loaded, to initialize the re-created objects.
3. Writing all the **variable assignments** to the file. These will populate the values of the object when the checkpoint is re-loaded.
4. Closing the file.

There are certain things that simply cannot be checkpointed like file-pointers, and network connections. Perhaps there are other things as well. For these situations, Trick provides four special job classes: ```"checkpoint"```, ```"post_checkpoint"```, ```“preload_checkpoint”```, and ```“restart”``` (described below).

<a id=dumping-a-checkpoint></a>
### What Happens When You Dump a Checkpoint

A checkpoint of a simulation is usually initiated from the Input Processor. That is, via:

1. The input file, or
2. The variable server.

```trick.checkpoint( <time> )``` is called from Python. This Python function is bound to the corresponding C++ function. At a simulation frame boundary (so that data is time-homogeneous), three things happen:

1. The ```"checkpoint"``` jobs in the S_define file are executed. These job-classes allow you to prepare your sim to be checkpointed. Perhaps you want to transform simulation state data into a different form for checkpointing. This is up to you.

2. ```write_checkpoint( <filename> )``` is called. This writes the three sections of a checkpoint file as described above.

3. The ```"post_checkpoint"``` jobs are called. This too is an opportunity for your simulatiion to tidy up what you may have done in your ```"checkpoint"``` job.

<a id=loading-a-checkpoint></a>
### What Happens When You Load a Checkpoint.
Trick.load_checkpoint() is called from Python.
At a simulation frame boundary, three things happen:

1. The ```“preload_checkpoint”``` jobs are called. These job-classes allow you to prepare your sim for a checkpoint-restore, in whatever way you see fit.

2. ```init_from_checkpoint( <filename> )``` is called, which:

	1. Calls ```reset_memory``` to delete all dynamically allocated objects.
	2. Calls ```read_checkpoint( <filename> )``` to read, parse, and restore the state described in the checkpoint file.
