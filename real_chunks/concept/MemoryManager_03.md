### Trick Memory Manager > Unregistering/Deleting an Object

 find the objects address. So if we need to reload an
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
double (*A)[3][4] = (double(*)[3][4]) TMM_declare_var_s("double A[3][4]");

(*A)[0][0] = 0.0;
(*A)[0][1] = 1.0;
(*A)[0][2] = 2.0;
(*A)[0][3] = 3.0;
(*A)[1][0] = 10.0;
(*A)[1][1] = 11.0;
(*A)[1][2] = 12.0;
(*A)[1][3] = 13.0;
(*A)[2][0] = 20.0;
(*A)[2][1] = 21.0;
(*A)[2][2] = 22.0;
(*A)[2][3] = 23.0;
```

![Figure1](images/MM_figure_1.jpg)

### Checkpoint Content
```
// Variable Declarations.
double A[3][4];

// Variable Assignments.

A =
    {
        {0, 1, 2, 3},
        {10, 11, 12, 13},
        {20, 21, 22, 23}
    };
```

## Example - Checkpointing an Unconstrained Array

### Allocation of an anonymous two-dimensional unconstrained array of doubles:

```
#include "memorymanager_c_intf.h"
double **A = (double**)TMM_declare_var_s("double*[3]");
A[0] = (double*)TMM_declare_var_s("double[4]");
A[1] = (double*)TMM_declare_var_s("double[4]");
A[2] = (double*)TMM_declare_var_s("double[4]");

A[0][0] = 0.0;
A[0][1] = 1.0;
A[0][2] = 2.0;
A[0][3] = 3.0;
A[1][0] = 10.0;
A[1][1] = 11.0;
A[1][2] = 12.0;
A[1][3] = 13.0;
A[2][0] = 20.0;
A[2][1] = 21.0;
A[2][2] = 22.0;
A[2][3] = 23.0;
```

![Figure2](images/MM_figure_2.jpg)

### Checkpoint Content
```
// Variable Declarations.
double* trick_anon_local_0[3];
double trick_anon_local_1[4];
double trick_anon_local_2[4];
double trick_anon_local_3[4];

// Variable Assignments.
trick_anon_local_0 =
    {&trick_anon_local_1[0], &trick_anon_local_2[0], &trick_anon_local_3[0]};

trick_anon_local_1 =
    {0, 1, 2, 3};

trick_anon_local_2 =
    {10, 11, 12, 13};

trick_anon_local_3 =
    {20, 21, 22, 23};
```

## Example - Another Checkpoint of an Unconstrained Array

Allocation of a two-dimensional unconstrained array of doubles with contiguous storage:

```
#include "MemoryManager.hh"
extern trick::MemoryManager* trick_MM;

double **A = (double**)trick_MM->declare_var("double*A[3]");
double *A_store = (double*)trick_MM->declare_var("double A_store[3][4]");

A[0] = &A_store[0];
A[1] = &A_store[4];
A[2] = &A_store[8];

A[0][0] = 0.0;
A[0][1] = 1.0;
A[0][2] = 2.0;
A[0][3] = 3
