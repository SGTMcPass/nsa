### Programming Language Support > Source Files > Trick Version Compatibility

 are not data recordable, they are not visible in the variable server, nor are they directly accessible in the input file. Some STLs are automatically checkpointed: `array`, `vector`, `list`, `deque`, `set`, `multiset`, `map`, `multimap`, `stack`, `queue`, `priority_queue`, `pair`.


### Noncopyable Objects

Sometimes classes contain members that are not copyable or the math modeler wants to prevent the class from being copied. Declaring an unimplemented private copy constructor and assignment, "=", operator prevents the class from being copied.
```C++
class CantCopyMe {
 private:
  CantCopyMe(const CantCopyMe&);
  CantCopyMe& operator= (const CantCopyMe);
}
```

When using such classes in Trick, classes that include non copyable classes must also declare themselves not copyable. this extends all the way up to sim objects in the S_define.

```C++
class MysimObject : public Trick::SimObject {
 public:
  CantCopyMe ccm;
 private:
  MysimObject(const MysimObject&);
  MysimObject& operator= (const MysimObject);
}
```

### Source Code in Header Files

Trick attempts to skip over class code in header files while searching for class variables and method declarations. However, code can sometimes confuse Trick and cause it to abort processing of header files. It is recommended to keep code out of the header file.

### Library Dependencies

It is good practice to list all the source code files that define class methods in the class header file.

### Excluding Header File Code

There are several ways to exclude code from processing.

#### Excluding Directories

Add paths to exclude to the TRICK_ICG_EXCLUDE environment variable or makefile variable. This works for both C and C++ headers.

#### Excluding File

Add `ICG: (No)` to the Trick comment header.

#### Excluding Lines

When processing header files Trick defines 2 #define variables, TRICK_ICG and SWIG. Code may be excluded by enclosing it in #ifndef blocks.
```C++
#ifndef TRICK_ICG
code that cannot be processed by ICG
#ifndef SWIG
code that cannot be processed by ICG or SWIG
#endif
#endif
```

## Source Files

By source files, in this context, we mean functional model source code, i.e. *.c files.

```C
/* [TRICK_HEADER]
PURPOSE:
    (Purpose statement.)
[REFERENCES:
    ((Reference #1)
    [(Reference #n)])]
[ASSUMPTIONS AND LIMITATIONS:
    ((Assumption #1)
    [(Assumption #n)])]
[LIBRARY DEPENDENCY:
    (
     (object.o|lib.a|lib.so|<relative_path>/lib.a)
     [(object_n.o|lib_n.a|lib_n.so
