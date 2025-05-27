### Accessing Simulation Parameters > I Just Want to Know How Do I Set this Value...

::MemoryManager``` Allocation Routines Directly

The first method is to call the `Trick::MemoryManager` routines to allocate memory.
There are 3 `Trick::MemoryManager` calls with varying arguments that can be used to allocate memory

```python
trick.TMM_declare_var_s("declaration")
trick.TMM_declare_var_1d("enh_type_spec", e_elems)
trick.alloc_type(e_elems , "enh_type_spec")

# Some examples using a c++ declaration
# double * foo ;
# All 3 of the following statments allocates the same amount of memory

foo = trick.TMM_declare_var_s("double[6]")
foo = trick.TMM_declare_var_1d("double", 6)
foo = trick.alloc_type(6 , "double")

# Some examples using a c++ declaration
# double ** food ;
# All 3 of the following statments allocates the same amount of memory

food = trick.TMM_declare_var_s("double *[3]")
food[0] = trick.TMM_declare_var_s("double [4]")
food[1] = trick.TMM_declare_var_s("double [5]")
food[2] = trick.TMM_declare_var_s("double [6]")

food = trick.TMM_declare_var_1d("double *", 3)
food[0] = trick.TMM_declare_var_1d("double", 4)
food[1] = trick.TMM_declare_var_1d("double", 5)
food[2] = trick.TMM_declare_var_1d("double", 6)

food = trick.alloc_type(3, "double *")
food[0] = trick.alloc_type(4, "double")
food[1] = trick.alloc_type(5, "double")
food[2] = trick.alloc_type(6, "double")
```

Memory allocated using the above routines are tracked by the memory manager and is checkpointable and data recordable.

### 2. Use a Factory Function
The benefit of this method is flexibility in how objects are initialized. For example, we might want to initialize our objects with a non-default constructor. So, the requirements for our factory function are:

1. Allocate a memory object via the Trick Memory Manager, and
2. Call a constructor to initialize the object (using placement-new)

#### A Few Words About Placement-new
In C++ one often instanciates a class object using the **new** operator, for example:

```
MyClass * p = new MyClass(a,b,c);
```

This form of **new**

1. allocates memory, and then
2. calls a constructor.

Another form of **new**, is called "placement-new". Rather than allocating and calling a constructor to initialize memory, placement-new simply calls a constructor to initialize memory that has already been allocated
