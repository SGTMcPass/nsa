### Appendix > Is Trick gluten-free, grass-fed, organic, non-GMO, environmentally conservative, free-range, vegan, and dolphin safe?

 than a regular input processor event, but are not as flexible.

01.  [A Just in Time (JIT) input file](/trick/documentation/simulation_capabilities/JIT-Input-Processor.html) is C++ code that is
compiled and run during simulation execution.
02.  [Realtime Injection](/trick/documentation/simulation_capabilities/Realtime-Injector.html) stages variable assignments and executes them in bulk at the top of a software frame.

<a name="arethereinputfiletemplatelimitations"></a>

## Are there input file template limitations?
Trick input files understand a lot about templates, but there is a limitation when using them. Input files cannot access a fixed array of template types directly. There are memory manager calls accessible from the input file that may be used to to read and write arrayed templates.

```c++
template < typename T > class A {
  public:
    T t;
} ;

class B {
  public:
    A<double> a[4] ;
} ;
```
Here is an input file accessing the template type

```python
# direct access to arrayed template class will fail
my_sim_object.b.a[1].t = 1  # fails
var = my_sim_object.b.a[1].t = 2 # fails

# use these memory manager calls instead
trick.var_set("my_sim_object.b.a[1].t", 1)
var = trick.var_get("my_sim_object.b.a[1].t")
```

<a name="istrickgfgfongmoecfrvads"></a>

## Is Trick gluten-free, grass-fed, organic, non-GMO, environmentally conservative, free-range, vegan, and dolphin safe?

Trick is composed entirely of information. It contains no matter, organic or otherwise. Therefore Trick contains no gluten,
GMOs, nor is it fed by grass, vegetables, or meat. Trick could be described as environmentally conservative in that it runs on numerous POSIX (Unix-like) operating systems. Trick is of course free-range! It's Opensource!, and freely available to anyone, even dolphins with internet access.
