### Programming Language Support > Source Files > Trick Version Compatibility

 typedefs.

All other types are ignored. Types may be defined and used within the same header if the types are defined before they are used (this is a C syntax rule, too).

### Pointers

Any combination of pointers and array dimensions up to 8 dimensions may be used for parameter declarations; for example, `double ** four_dimensional_array[2][2];`, will be processed. Void pointers and function pointers are not processed. Parameters declared with pointers (like `four_dimensional_array` example), are treated differently; these are called unconstrained arrays. Trick will generate dynamic memory allocation source code for the developer which allows the developer to size the array dimensions (represented by the pointers) via special syntax in the runstream input file. The developer may 1) use the input file to input data to the arrays, 2) output the data via standard Trick logging functions, or 3) share the data through the variable server.

The user does have the option to perform their own memory management for parameters declared as pointers. In this case, instead of specifying the allocation in the input file, the user may allocate the data in a job. In order for Trick to process the data as if it was its own managed memory (and provide capabilities like logging, checkpointing, etc.), the memory address, and number and size of the allocation must be passed to the Trick `TMM_declare_extern_var` function. The user is also responsible for freeing the memory when done.

### Intrinsic typedef and struct Support

Types declared using `typedef struct`, `typedef union`, and `typedef enum` are recognized by Trick. Intrinsic typedefs are supported as well and may be nested in structures. The example that follows details a header that Trick will handle:

```C
typedef unsigned char my_uchar;
typedef char my_char;
typedef wchar_t my_wchar;
typedef short int my_shortint;
typedef short my_short;
typedef unsigned short int my_ushortint;
typedef unsigned short my_ushort;
typedef int my_int;
typedef unsigned int my_uint;
typedef long int my_longint;
typedef long my_long;
typedef unsigned long int my_ulongint;
typedef unsigned long my_ulong;
typedef float my_float;
typedef double my_double;
typedef my_short my_short2;

struct Animal_Sound {
   int moo;            /* -- Cow */
   int baa;            /* -- Lamb */
   int sss;            /* -- Snake */
};

typedef struct {
  my_uchar uc;             /* -- unsigned char */
  my_char c;               /* -- char */
  my_char ca[80];          /* -- char */
  my_wchar wc;             /* -- wchar_t */
  my wchar wca[100];       /* -- wchar_t */
  my_shortint si;          /* -- short int */
  my_short *s;             /* -- short stuff */
  my_ushortint usi;        /* -- short stuff */
  my
