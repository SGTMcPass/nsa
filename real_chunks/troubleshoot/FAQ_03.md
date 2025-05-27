### Appendix > Is Trick gluten-free, grass-fed, organic, non-GMO, environmentally conservative, free-range, vegan, and dolphin safe?

 properly set your environmental variables.
03. You haven't properly installed all required dependencies.

<a name="whatunitscantrickuse"></a>

## What units can Trick use?
Trick is capable of utilizing the vast majority of imperial and metric units. Trick uses the UDUNITS C library/database in its unit calculations. For a list of the most common units, run **trick-units** in a terminal window after installing Trick.

<a name="doineedinternetaccesstobuildtrick"></a>

## Do I need internet access to build Trick?
Trick's Java GUIs rely on several 3rd party .jar files which are normally downloaded during the initial compilation of Trick. If you are compiling on a machine without internet access you may copy the directory ${TRICK\_HOME}/libexec/trick/java/lib to a machine that does have internet access and run make on that machine.

<a name="caniaccessclassprotectedprivatevariables"></a>

## Can I access class protected/private variables?
If the Trick memory manager and init attribute function is made a friend of a class, we are able to access protected/private variables in the input file through the memory manager.

```c++
class A {
  // This class triggers Trick to process protected/private variables
  friend class InputProcessor ;
  // This friend function follows this naming convention "void init_attr ## <class_name>()"
  friend void init_attrA() ;
  private:
    int ii ;
} ;
```

Input File statements
```python
# Direct access will fail
my_sim_object.a.ii = 1  #fails
var = my_sim_object.a.ii  #fails

# Use the var_set and var_get commands to access protected/private variables
trick.var_set("my_sim_object.a.ii", 1)
var = trick.var_get("my_sim_object.a.ii")
```

<a name="aretherefasterwaystoimplementevents"></a>

## Are there faster ways to implement events?
Trick has a few alternatives to an input file event. Both method execute faster than a regular input processor event, but are not as flexible.

01.  [A Just in Time (JIT) input file](/trick/documentation/simulation_capabilities/JIT-Input-Processor.html) is C++ code that is
compiled and run during simulation execution.
02.  [Realtime Injection](/trick/documentation/simulation_capabilities/Realtime
