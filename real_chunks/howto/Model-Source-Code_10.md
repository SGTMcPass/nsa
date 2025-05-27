### Programming Language Support > Source Files > Trick Version Compatibility

enclosing namespace.
2. Otherwise, a template instantiation must be fully qualified, starting from the global namespace.
3. Finally, instantiations of templates declared within the same class must be excluded from SWIG.

In the following examples, all template instantiations occur in `example::prime::Soup`. The immediately-enclosing namespace is `prime`, so only instantiations of templates declared directly in `prime` (only `Celery`) may be unqualified. All other template instantiations must be fully qualified, starting from the global namespace, even if the C++ name lookup process would find them with partial qualification.

```c++
template <class T> class Potato {};

namespace example {

  template <class T> class Onion {};

  namespace peer {
    template <class T> class Raddish {};
  }

  namespace prime {

    namespace inner {
        template <class T> class Carrot {};
    }

    template <class T> class Celery {};

    class Soup {

      public:
        template <class T> class Broth {};

        ::Potato<int> potato;                      // Rule 2
        example::Onion<int> onion;                 // Rule 2
        example::peer::Raddish<int> raddish;       // Rule 2
        example::prime::inner::Carrot<int> carrot; // Rule 2
        Celery<int> celery;                        // Rule 1
#ifndef SWIG
        Broth<int> broth;                          // Rule 3
#endif
    };
  }

}
```

### Function Overloading

Trick parses function declarations for input file use. The python input processor understands class method overloading. Overloaded methods with different arguments may be called in the input files. Default arguments are to methods are understood and honored in the input file. Operator overloading is skipped by Trick processors. Operator overloading is not implemented in the input file.

### Templates and the Standard Template Libraries (STL)

Trick attempts to process user defined templates. Simple templates are handled. We do not have a good definition of simple. Typedefs of templates is supported and encouraged. All protected and private data is ignored within templates. This is because it is not possible to specify the correct io_src friend function. Templates within templates are not processed. Finally abstract templates are not supported by Trick. These templates should be excluded from Trick processing. See below to see how to exclude code from processing.

STLs may be used in models. However, STL variables are not data recordable, they are not visible in the variable server, nor are they directly accessible in the input file. Some STLs are automatically checkpointed: `array`, `vector`, `list`, `deque`, `set`, `multiset`, `map`, `multimap`, `stack`, `queue`, `priority_queue`, `pair`.


### Noncopyable Objects

Sometimes classes contain members that are not copyable or the
