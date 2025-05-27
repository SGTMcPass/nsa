### Trick CheckPointing Best Practices > Other Resources You Might Find Useful

 the members of the allocations data type.

#### Example:

Suppose one were to perform the following allocation:

```double *dbl_p = (double*)TMM_declare_var_s("double dbl_array[3]");```

The Memory Manager would represent its **definition** as follows in a checkpoint :

```
double dbl_array[3];
```

If one were then to assign values to the object, i.e. :

```
    dbl_p[0] = 1.1;
    dbl_p[1] = 2.2;
    dbl_p[2] = 3.3;
```

then the Memory Manager would represent its **variable assignment** as follows in a checkpoint :

```
dbl_array =
    {1.1, 2.2, 3.3};
```
<a id=serialization-of-composite-objects></a>
#### Serialization of Composite Objects
For composite type objects (i.e., class & struct objects), the **variable assignment** can consist of many assignment statements. Trick check-pointing code recursively descends into the composite type-tree, writing an assignment statement for each of the primitive data-typed members (leaves).

<a id=serialization-of-pointers></a>
#### Serialization of Pointers
A pointer contains an address of another object. What's important is that it **refers** to the other object. We can't store the address of the object, because it will probably be different when the object is re-created at checkpoint reload. But, a **name** is also a reference. So we store pointers as names. Since objects have a name, and an address (once it's re-created) we can restore pointers by converting the name reference back to an address reference.

<a id=importance-of-naming-allocations></a>
#### Importance of Naming Allocations
If an object is named, then that name will be used in checkpointing, 1) to identify and 2) to refer (point) to the object. If the object is anonymous then a temporary name must be created for checkpointing. These temporary names are of the form ```trick_anon_local_<number>``` or ```trick_anon_extern_<number```. They can't be as descriptive as a name you might chose so, it's a good idea to name your allocations when possible. It will be a lot easier to find them in a checkpoint file.

<a id=simulation-checkpointing></a>
### Simulation Checkpointing

A **checkpoint** is a persistent representation of a simulation state. It's exactly like a "saved computer game" when it's time for dinner.

If the Trick Memory Manager **"knows"** about all of the allocations that comprise the state of a simulation, then it can checkpoint that simulation. The Trick Memory Manager checkpoints a simulation by :

1. Opening a checkpoint file.
1. Writing all the **definitions**, of all
