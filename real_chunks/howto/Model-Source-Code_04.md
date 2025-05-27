### Programming Language Support > Source Files > Trick Version Compatibility

`
LIBRARY DEPENDENCY:
    ((this.o)
     (that.o)
#ifdef __animals
     (my_library/libdog.a)
     (libcow.so)
#else
     (my_library/lib.a)
#endif
     (${FOO_ENV_VAR}/foo.o))
```

<b>Listing Library Dependencies Within the `S_define`:</b><br>
Listing library dependencies within the `S_define` is just like listing them
within the model header files, but all model source files are listed in one spot
instead of per header file. If you choose to do it this way, don't forget to
update the list each time you add or remove a model source file.

#### `ICG_IGNORE_TYPES`

The `ICG IGNORE TYPES` field lists the structs or classes to be ignored. Any parameters of this type or inherited from are ignored. The `ICG IGNORE TYPES` field is only valid for the current file. It does not extend to included header files.

#### `PYTHON_MODULE`

Specifying a `python_module` name will place any class/struct and function definitions in this header file in a python module of the same name. All classes and functions are flattened into the python `trick` namespace by default. This capability allows users to avoid possible name collisions between names when they are flattened. An empty `python_module` statement will be ignored.

### Compiler Directives

Trick handles all compiler directives (`#if`, `#ifdef`, `#endif`, `#define`, `#include`, etc.) ICG also uses the -D and -U command line arguments for defines and undefines, respectively.

### trick_parse

The trick_parse directive is a Doxygen style field serving the same functionality as the `PURPOSE:` keyword and `ICG: (No)`.  The trick_parse directive like all Doxygen style directives are prefixed with either a `\` or an `@` character.

`@trick_parse(everything)`:  Treat this comment as the Trick header comment.  Search for library dependencies in this comment, and treat all comments following variable definitions as Trick comments.

`@trick_parse(attributes)`:  Treat this comment as the Trick header comment.  Search for library dependencies in this comment.  Create I/O attributes for the classes and structures in the file, but do not read comments following variable definitions.

`@trick_parse(dependencies_only)`:  Treat this comment as the Trick header comment.  Search for library dependencies in this comment.  Do not process the file any further.

### `trick_exclude_typename`

`@trick_exclude_typename(type)` is equivalent to `ICG_IGNORE_TYPES` in a Doxygen style field. The `trick_exclude` field lists the structs or classes to be ignored.  Multiple `trick_exclude_typename` fields may be used to ignore multiple types.

### Enumerated Type Definitions

Trick provides complete support
