### Accessing Simulation Parameters > I Just Want to Know How Do I Set this Value...

0 , 0.0 , 1.0]]
print ball.daa

# [[ 1.0 , 0.0 , 0.0 ] ,
#  [ 0.0 , 1.0 , 0.0 ] ,
#  [0.0 , 0.0 , 1.0]]
# is printed
```

## Accessing Simulation Enumerated Types

Global Enumerations are available through the `trick` module.

```python
# from sim_services/include/Flag.h

print trick.True trick.False trick.Yes trick.No
1 0 1 0
```

## Accessing Simulation Functions and Object Member functions

Almost all functions and public object methods are available to call from the Python input file.
Arguments must be filled in just as they would be in C/C++ code.  There is more information about what
Trick simulation services routines are available later in this chapter.

```python
# Trick simulation services routines are called by "trick.<function>".
trick.exec_get_sim_time()
trick.checkpoint(100.0)
trick.stop(300.0)

# C User model functions are also called by "trick.<function>".
trick.ball_print(ball.state)

# C++ User model class methods are called by referencing the full object path just like in C++
ball.obj.state.print_position()

```

When calling functions, intrinsic typed simulation variables, e.g. int or double, will not work directly
as intrisic typed arguments.

```cpp
// If we have a c function
void foo( double d) ;

// And a structure with a variable declared as this
double length ; /* (m) length */

```

This call in the input will not work

```python
# Will not work
foo(length)
```

The reason is that in python space the variable length is an object that contains both the value of length
and the units.  The built in python command `float()` will strip the units off leaving a double that can be
used in the function call.

```python
# Works
foo(float(length))
```

Structure and class variables do not carry around units, and therefore the units do not have to be removed.

## Creating New Objects and Allocating Memory

It is possible to create new objects and allocate new memory for structures directly in the Python
input file.  Three different ways are described below.

### 1. Call ```Trick::MemoryManager``` Allocation Routines Directly

The first method is to call the `Trick::MemoryManager` routines to allocate memory.
There are 3 `Trick::MemoryManager` calls with varying arguments that can be used to allocate memory

```python
trick.TMM_declare_var_s("declaration")
trick.TMM_declare_var_1d("enh_type_spec", e_elems)
trick.alloc_type(e
