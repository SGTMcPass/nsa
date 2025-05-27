### Trick Memory Manager > Unregistering/Deleting an Object

 Memory Manager to allocate an array of three
doubles named *dbl_array*. **declare_var** returns a pointer to the array. Using
the pointer, we then initialize the array. Finally we checkpoint the variable to
std::cout.
```
#include "MemoryManager.hh"
extern trick::MemoryManager* trick_MM;

double *dbl_p = (double*)trick_MM->declare_var("double dbl_array[3]");

dbl_p[0] = 1.1;
dbl_p[1] = 2.2;
dbl_p[2] = 3.3;

trick_MM->write_checkpoint( std::cout, "dbl_array");
```
The following would accomplish the exact same as the assignment above.
The **TMM** 'C' routines are just wrappers around the C++ calls.

```
double *dbl_p = (double*) TMM_declare_var_s("double dbl_array[3]");
```

When a checkpoint (shown below) is reloaded the declarations in the *Variable
Declarations* section cause variables to be allocated just like the declare_var()
call above.  The assignments in the *Variable Assignments* section restore the
values of the variables.

### Checkpoint Content
```
// Variable Declarations.
double dbl_array[3];

// Variable Assignments.
dbl_array =
    {1.1, 2.2, 3.3};
```

## Example - Checkpointing an Anonymous, Local Allocation
In the following example, we are not giving a name to the variable that we are
creating.

```
#include "MemoryManager.hh"
extern trick::MemoryManager* trick_MM;
double *dbl_p = (double*)trick_MM->declare_var("double[3]");
dbl_p[0] = 1.1;
dbl_p[1] = 2.2;
dbl_p[2] = 3.3;
trick_MM->write_checkpoint( std::cout );
```
In the checkpoint below, notice that the variable is given a **temporary** name
for checkpointing.

### Checkpoint Content
```
// Variable Declarations.
double trick_anon_local_0[3];

// Variable Assignments.
trick_anon_local_0 =
    {1.1, 2.2, 3.3};
```

## Example - Checkpointing a Named, External Allocation
In this example, we are allocating the memory for the variable directly rather
than asking the Memory Manager to do it.

```
#include "MemoryManager.hh"
extern trick::MemoryManager* trick_MM;
double *dbl_p = new double[3];
trick_MM->declare_extern_var(dbl_p, "double dbl_array[3]");
dbl_p[0] = 1.1;
dbl_p[1] = 2.2;
dbl_p[2] = 3.3;
trick_MM->write_checkpoint( std::cout );

```
Because this object is **extern**, the MemoryManager must be able to lookup its
address by name. Therefore the simulation must ensure that the object exists and
is cataloged before attempting to reload its contents from a checkpoint.

### Checkpoint Content
```
// Variable Declarations.
// extern double dbl_array[3];

// Variable Assignments.
dbl_array =
    {1.1, 2.2, 3.3};
```

## Example - Checkpointing an Anonymous, External Allocation

In the following example, we are allocating the memory for the variable directly
and not giving it a name. **This is typically not a good idea**.

```
#include "MemoryManager.hh"
extern trick::MemoryManager* trick_MM;
double *dbl_p = new double[3];
trick_MM->declare_extern_var(dbl_p, "double[3]");
dbl_p[0] = 1.1;
dbl_p[1] = 2.2;
dbl_p[2] = 3.3;
trick_MM->write_checkpoint( std::cout);

```
Anonymous, extern objects cannot be reloaded from a checkpoint, because the
MemoryManager has no way to find the objects address. So if we need to reload an
extern object, we need to make sure that it has a name, and is cataloged.

In the checkpoint note the temporary name indciates that the variable is
allocated externally to the Memory Manager.

### Checkpoint Content
```
// Variable Declarations.

// Variable Assignments.
trick_anon_extern_0 =
    {1.1, 2.2, 3.3};
```

## Example - Checkpointing a Constrained Array

### Allocation of an two-dimensional constrained array of doubles:

```
#include "memorymanager_c_intf.h"
double (*A)[3][4] = (double(*)[3][4]) TMM_decl
