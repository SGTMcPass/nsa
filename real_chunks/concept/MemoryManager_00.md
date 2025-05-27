### Trick Memory Manager > Unregistering/Deleting an Object

| [Home](/trick) → [Documentation Home](../../Documentation-Home) → [Simulation Capabilities](../Simulation-Capabilities) → Memory Manager |
|------------------------------------------------------------------|

## Trick Memory Manager

The Memory Manager
- Maintains a list of memory objects with their associated data-types and
  optional names.
- Provides services based on this information such as:
  -  Creating and cataloging new data-type instances. (Memory allocation).
  -  Cataloging pre-existing memory objects.
  -  Writing the definitions and values of these memory objects to a checkpoint
     file or stream.
  -  Reading the definitions and values from a checkpoint file or stream and
     restoring the original
     objects back into memory
  -  Debugging support, to see exactly what is happening.
  -  C and C++ interfaces.

This makes other services possible, such as :
- Data recording
- Variable Server
  - Trick Sim Control Panel
  - Trick Strip Chart
  - TrickView (TV) Variable Viewer
  - Third-party simulation clients

## Memory Manager Interfaces
A Trick simulation contains exactly one Memory Manager. One can access it as follows:

```
#include "MemoryManager.hh"
extern Trick::MemoryManager* trick_MM;
```
From 'C' code, the Memory Manager can be accessed using a set of wrapper functions:
```
*memorymanager_c_intf.h*
```

## Registering an Object
The Memory Manager can either register a supplied object or it can allocate an
object as described by its declaration, and then register it. Here *object* just
means a chunk of memory that one would get by calling malloc, new, or mmap.
Registering the object associates it with a type-declaration and a name.

To allocate and then register an object, one would use a variant of the Memory
Manager member-function *declare_var()*. To register an existing object, one
would use a variant of *declare_extern_var()*. For each variant of declare_var()
there is a corresponding variant of declare_extern_var(). Their argument lists
are identical except that the first argument of declare_extern_var() is a pointer
to the supplied object.

Below following are the three variants of  *declare_var()*.

The first is the most commonly used. The declaration information is
specified entirely in a [declaration string](MemoryManager-Declaration-String).

```
void * Trick::MemoryManager:: declare_var (const char *declaration);
```

The next variant is a convenience function to allocate an anonymous,
one dimensional array.

```
void * Trick::MemoryManager:: declare_var (const char *type_spec,
                                           int n_elems);
```

The final variation is the the most flexible, but also the most complex.

```
void * Trick::MemoryManager:: declare_var (TRICK_TYPE type,
                                           std::string class_name,
                                           int n_stars,
                                           std::string var_name,
                                           int n_cdims,
                                           int *cdims);
```
Where:
- **type** specifies the data-type. See [TRICK_TYPE](MemoryManager-TRICK_TYPE).
- **class_name** is name of a user-defined type. This parameter is only applicable
  if *type* is TRICK_STRUCTURED, otherwise it is ignored.
- **n_stars** is simply the number of pointers (asterisks) in the declaration.
- **var_name** Optional name of the variable being created.
- **n_cdims** Number of array dimensions.
- **cdims** Sizes of each dimension.

To register an existing allocation use the following:
```
void * Trick::MemoryManager::declare_extern_var ( void* address,
                                                  const char *declaration);
```
Where:
- **address** is the address of the object to be register.
The remaining arguments are identical to those of declare_var.


## Example Allocations using C and C++ Interfaces

The following two *declare_var* calls do exactly the same thing.

```
#include "MemoryManager.hh"
extern trick::MemoryManager* trick_MM;
double *D = (double*)trick_MM->declare_var("double[3]");
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
double *D = (double*) TMM_declare_var
