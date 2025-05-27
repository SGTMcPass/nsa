### Accessing Simulation Parameters > I Just Want to Know How Do I Set this Value...

00, 0.0, 0.0, 0.0, 0.5, 1.0)
dyn.contact.balls[2] = trick.make_Ball( 0.01, 0.0, 0.0, 0.0, 0.5, 1.0)
dyn.contact.balls[3] = trick.make_Ball( 1.02, 0.0, 0.0, 0.0, 0.5, 1.0)
dyn.contact.balls[4] = trick.make_Ball( 2.03, 0.0, 0.0, 0.0, 0.5, 1.0)
dyn.contact.balls[5] = trick.make_Ball( 7.00, 0.0, 0.0, 0.0, 1.0, 1000000.0)
dyn.contact.balls[6] = trick.make_Ball(-7.00, 0.0, 0.0, 0.0, 1.0, 1000000.0)
```

This creates and initializes seven *Ball* objects needed to configure a Newton's cradle.

### 3. Call the Wrapped Class Constructor Directly
The third method is to call the wrapped constructor of the class directly.  This is analogous to declaring local
variables in C/C++ routines.  And like local variables in C/C++ if the python variable goes out of scope in the
input file, then python will try and free the memory associated with the local object.  Memory allocated this
way is not checkpointable or data recordable.

For example if we are trying to instantiate a new C++ `Ball` object in the input file.

```python
# The new_ball_1 instantiation is at the top level, new_ball_1 will not be freed.
new_ball_1 = trick.Ball() ;

# The new_ball_2 instantiation is in the function foo.
# When foo returns new_ball_2 will be freed by python

def foo():
    new_ball_2 = trick.Ball() ;
```

To stop python from freeing this memory we must tell python that it does not own the memory.
This can be done in two ways.  1) Tell Python it does not own the memory by modifying the
`thisown` flag.  2) Use a non-constructor routine that allocates memory and returns that
to the Python variable.

```python
# In the above example, we can avoid new_ball_2 from being freed
# when foo returns by setting the thisown flag to 0 in the new_ball_2 object.

def foo():
    new_ball_2 = trick.Ball() ;
    new_ball_2.thisown = 0 ;

# Alternatively we could call
