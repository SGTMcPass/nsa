### Programming Language Support > Source Files > Trick Version Compatibility

.  Do not process the file any further.

### `trick_exclude_typename`

`@trick_exclude_typename(type)` is equivalent to `ICG_IGNORE_TYPES` in a Doxygen style field. The `trick_exclude` field lists the structs or classes to be ignored.  Multiple `trick_exclude_typename` fields may be used to ignore multiple types.

### Enumerated Type Definitions

Trick provides complete support for enumerated types. Simple mathematical expressions using enumerated types are supported as well.

An example follows:

a.h

```C
typedef enum {
  FIRST_ENUM = 45
} A_ENUM;
```

b.h

```C
#include "a.h"

typedef enum {
  ME_TOO = 2
} OTHER_ENUM;

typedef enum {
  SECOND_ENUM = FIRST_ENUM,
  THIRD_ENUM = FIRST_ENUM * 3,
  FOURTH_ENUM = SECOND_ENUM * 4,
  FIFTH_ENUM = ME_TOO * 6
} B_ENUM;
```

c.h

```C
#include "b.h"

typedef struct {
  int dummy;                      /* No comment necessary */
  A_ENUM ae;                      /* No comment necessary */
  B_ENUM be;                      /* No comment necessary */
  int ia1[FIRST_ENUM];            /* No comment necessary */
  int ia2[SECOND_ENUM];           /* No comment necessary */
  int ia3[FIFTH_ENUM];            /* No comment necessary */
} DATA;
```

### Data Structure Definitions and Parameter Declarations

The data structure type definition statements, `typedef struct { ... } name;`, and `typedef union { ... } name;` `struct Foo { } name;` follows standard C syntax, and are supported by Trick. However, Trick requires a C comment immediately following every parameter declaration.

### Parameter Data Types

Trick allows any data type declaration within the data structure `typedef` statement. However, only the following data types will be processed by Trick:

1 `int`,
1 `short`,
1 `long`,
1 `long long`
1 `char`,
1 `(un)signed int`,
1 `(un)signed short`,
1 `(un)signed long`,
1 `(un)signed char`,
1 `(un)signed long long`,
1 `(un)signed short int`,
1 `(un)signed long int`,
1 `float`,
1 `double`,
1 `wchar_t`,
1 `FILE *`
1 Bit fields (signed and unsigned) and
1 previously processed structure, union, enumerated types and typedefs.

All other types are ignored. Types may be defined and used within the same header if the types are defined before they are used (this is a C syntax rule, too).

### Pointers

Any combination of pointers and array dimensions up to 8 dimensions may be used for parameter declarations; for example, `double ** four_dimensional_array[2][2];`, will be processed. Void pointers and function pointers are not processed.
