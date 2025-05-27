### Trick Memory Manager > Unregistering/Deleting an Object

 a two-dimensional unconstrained array of doubles with contiguous storage:

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

![Figure3](images/MM_figure_3.jpg)

### Checkpoint Content
```
// Variable Declarations.
double* A[3];
double A_store[3][4];

// Variable Assignments.
A =
    {&A_store[0], &A_store[4], &A_store[8]};

A_store =
    {
        {0, 1, 2, 3},
        {10, 11, 12, 13},
        {20, 21, 22, 23}
    };
```

## Reading and Restoring Checkpoints
Restoring a checkpoint consists of reading and executing the statements from a
checkpoint file or stream. Declaration statements cause data-typed objects to be
created and registered. Assignment statements cause values specified on the
right hand side to the variables identified on the right.

### Checkpoint Restore Methods

Restore the checkpoint from the given std::stream:
```
int Trick::MemoryManager::read_checkpoint (std::istream *in_s)
```

Restore the checkpoint from the named file.
```
int Trick::MemoryManager::read_checkpoint (const char *filename);
```
```
int TMM_read_checkpoint( const char* filename);
```

Restore the checkpoint from the given character string.
```
int Trick::MemoryManager::read_checkpoint_from_string(const char *s);
```
```
int Trick::MemoryManager::read_checkpoint_from_string(const char *s);
```
## Example: Checkpoint Restore from C++

```
#include "MemoryManager.hh"
extern trick::MemoryManager* trick_MM;

double* dbl_ptr;
trick_MM->declare_extern_var( &dbl_ptr, "double* dbl_ptr");
trick_MM->read_checkpoint_from_string(
    "double trick_anon_local_0[10];"
    "trick_anon_local_0 = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0};"
    "dbl_ptr = &trick_anon_local_0;"
);

for (int ii=0; ii < 10; ii++) {
    std::cout << dbl_ptr[ii] << " ";
}
std::cout << std::endl;
```
### Output
```
1 2 3 4 5 6 7 8 9 10
```

## Checkpoint Tailoring Options
Checkpoint tailoring options allow one to generate checkpoints that most suite
their needs.

### Reduced Checkpoint
This (default) option allows the MemoryManager to generate smaller checkpoints.
It does this by adding a **clear_all_vars** directive to the checkpoint
following the variable declarations. Then assignment statements are generated
only for non-zero valued variables.

```
void Trick::MemoryManager::set_reduced_checkpoint (bool flag)
```
Where:  **flag** - **true** means no zeroes are assigned, otherwise zeroes are
assigned.

Corresponding 'C' wrapper:
```
void TMM_reduced_checkpoint(int flag);
```
Where:  **flag** - **1** means no zeroes are assigned, otherwise zeroes are
assigned.


### Hexfloat Checkpoint
This option causes floating point values in the checkpoint to be represented in
**Hex Float** format. This format preserves precision in floating point numbers.
The downside is that they are not very human readable. Not by normal humans
anyhow.

```
void Trick::MemoryManager::set_hexfloat_checkpoint (bool flag)
```

Where:
    **flag** - **true
