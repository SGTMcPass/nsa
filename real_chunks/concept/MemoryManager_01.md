### Trick Memory Manager > Unregistering/Deleting an Object

[3]");
double *D = (double*)trick_MM->declare_var("double",3);
```

The following two calls do exactly the same thing as each other, and as the two
C++ examples above.

```
#include "memorymanager_c_intf.h"
double *D = (double*)TMM_declare_var_s("double[3]");
double *D = (double*)TMM_declare_var_1d("double",3);
```

## Allocation Examples

Allocation of an anonymous double:
```
double *D = (double*)TMM_declare_var_s("double");
```

Allocation of an anonymous array of 3 doubles:
```
double *D = (double*) TMM_declare_var_s("double[3]");
```

Allocation of an anonymous array of 3 pointers to double:
```
double **D = (double**) TMM_declare_var_s("double*[3]");
```

Allocation of a named double:
```
double *D = (double*)TMM_declare_var_s("double mydbl");
```

Allocation of a named array of 3 Pointers to double:
```
double **D = (double**)TMM_declare_var_s("double* mydbl[3]");
```

Allocation of a named object of user-defined type "BAR":
```
BAR *D = (BAR*)TMM_declare_var_s("BAR mydbl");
```

Allocation of a named 2 dimensional array of user-defined type "BAR" in
namespace "FOO":
```
FOO::BAR (*A)[3][4] = (FOO::BAR(*)[3][4])TMM_declare_var_s("FOO::BAR my_array[3][4]");
```

## Checkpoints

A checkpoint is a textual representation of Trick managed memory objects at
a particular instance in time. When commanded, the MemoryManager (by way of a
CheckpointAgent) transforms the data-type descriptions and the values of memory
manager managed allocations into a human readable text format and writes it to a
file or stream.

Checkpoints contain three types of statements:

- Declaration Statements - are named [declarations](MemoryManager-Declaration-String)
followed by a semi-colon. They contain all of the information necessary to recreate
an instance of the object they represent. Anonymous


They describe memory objects. These statements contain all of the information necessary to recreate an instance of the object they represent.
They are a [declaration](MemoryManager-Declaration-String) followed by a semi-colon;


- Assignment Statements  - specify the values of objects. Composite objects
require one assignment for each of its non-composite data members.

-- Identifiers and References

- Checkpoint Directives - invoke a checkpoint specific command.


## Writing Checkpoints

Checkpoint every allocation that the MemoryManager knows about to a std::stream.
```
void Trick::MemoryManager::write_checkpoint (std::ostream &out_s);
```

Checkpoint the named allocation to a std::stream.
```
void Trick::MemoryManager::
    write_checkpoint ( std::ostream &out_s,
                       const char *var_name);
```

Checkpoint the listed named allocations to a std::stream.
```
void Trick::MemoryManager::
    write_checkpoint ( std::ostream &out_s,
                       std::vector< const char * > &var_name_list);
```

Checkpoint every allocation that the MemoryManager knows about to a file.
```
void Trick::MemoryManager::write_checkpoint (const char *filename);
```

Checkpoint the named allocation to a file.
```
void Trick::MemoryManager::
    write_checkpoint ( const char *filename,
                       const char *var_name);
```

Checkpoint the listed named allocations to a file.
```
void Trick::MemoryManager::
   write_checkpoint( const char *filename,
                     std::vector< const char * > &var_name_list);
```

Checkpoint every allocation that the MemoryManager knows about to a file.
```
void  TMM_write_checkpoint( const char* filename) ;
```

## Example - Checkpointing a Named, Local Allocation
In the example below we ask the Memory Manager to allocate an array of three
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
