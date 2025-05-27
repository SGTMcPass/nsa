### Programming Language Support > Source Files > Trick Version Compatibility

{‘ and ‘}’) and is stored in the element ATTRIBUTES->user_defined. The definition of the ATTRIBUTES structure is found in $TRICK_HOME/trick_source/sim_services/include/attributes.h.

#### Description Fields

The description field is required and must be the last field of the comment. The description field is basically everything after the first three fields. The description field may span multiple lines.

### C++ Header Files

C++ headers may include constructs and concepts not found in C header files. In addition to all C syntax, Trick parses and understands many C++ features.

### Public, Protected, and Private Access

Trick generates several files to support its various features. The data recorder and checkpointer rely on code produced by the Interface Code Generator (ICG), which bookkeeps the memory layout of variables within the simulation. `public` members are always available to these features. `protected` and `private` data is also available if there is no use of `TRICK_ICG` in the header file. If use is found, Trick will issue a warning during simulation compilation, and `private` and `protected` data will only be accessible to Trick if the following `friend`s are added to the offending classes:

```C++
friend class InputProcessor;
friend void init_attr<class_name>();
```

The input processor and variable server rely on code produced by a third-party tool, the [Simplified Wrapper and Interface Generator (SWIG)](http://www.swig.org/). SWIG provides the functions that allow access to simulation variables from Python contexts. These features can only access `public` members. It is not possible to expose `protected` and `private` data to them.

### Inheritance

Trick may use model code with any type of inheritance. Some limitations are present to Trick's ability to input process, checkpoint, etc. inherited variables.

* Public and protected inherited variables are available for access.
* Protected and private inheritance is ignored.
* Multiple inheritance is processed but not well tested.
* Template inheritance is not currently supported.

### Namespaces

ICG supports namespaces and nested scopes. Data recording and variable access via Trick View should work regardless of how many levels there are.

Namespaces and nested scopes are similarly supported in Python contexts, such as the input file and variable server, with some caveats regarding templates.
1. A template instantiation may be unqualified (have no use of the scope resolution operator `::`) only if its corresponding template is declared in the immediately-enclosing namespace.
2. Otherwise, a template instantiation must be fully qualified, starting from the global namespace.
3. Finally, instantiations of templates declared within the same class must be excluded from SWIG.

In the following examples, all template instantiations occur in `example::prime::Soup`. The immediately-enclosing namespace is `prime`, so only instantiations of templates declared directly in `prime` (only `Celery`) may be
