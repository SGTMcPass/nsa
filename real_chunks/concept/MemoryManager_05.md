### Trick Memory Manager > Unregistering/Deleting an Object

 flag)
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
    **flag** - **true** means use hexfloat format for floating point variables,
    otherwise use normal decimal scientific notation.

C Wrapped version:
```
void  TMM_hexfloat_checkpoint(int flag);
```
Where:
   **flag** - **1** means no zeroes are assigned, otherwise zeroes are assigned.

## Unregistering/Deleting an Object
An object can be unregistered by name or by address.
```
int Trick::MemoryManager::delete_var (void *address);
int Trick::MemoryManager::delete_var (const char *var_name);
```
The corresponding C wrapper functions:
```
void TMM_delete_var_a(void* address);
void TMM_delete_var_n(const char* var_name);
```
If the object was originally allocated by **declare_var** then it will be
unregistered and then deleted. If on the otherhand the object was allocated
externally, and then registered using **declare_ext_var**, then delete_var will
unregister it but not deleted it. The MemoryManager will never attempt to delete
memory objects that it did not allocate.


[Continue to Integration](../Integrator)
