### Programming Language Support > Source Files > Trick Version Compatibility

 char */
  my_char c;               /* -- char */
  my_char ca[80];          /* -- char */
  my_wchar wc;             /* -- wchar_t */
  my wchar wca[100];       /* -- wchar_t */
  my_shortint si;          /* -- short int */
  my_short *s;             /* -- short stuff */
  my_ushortint usi;        /* -- short stuff */
  my_ushort us;            /* -- short stuff */
  my_int i;                /* -- count */
  my_int ia[5];            /* -- count */
  my_uint ui;              /* -- count */
  my_longint li;           /* -- count */
  my_long l;               /* -- count */
  my_ulongint uli;         /* -- count */
  my_ulong ul;             /* -- count */
  my_float f;              /* -- count */
  my_double d;             /* -- count */
  my_short2 s20;           /* -- short 20 */
  my_short2 s21;           /* -- short 21 */
  struct Animal_Sound as;  /* -- Wild Kingdom */
} DATA;

typedef DATA MY_DATA;
typedef MY_DATA MY_DATA_2;

typedef struct {
  DATA id;        /* -- testing typedef of struct */
  MY_DATA mid;    /* -- testing typedef of struct */
  MY_DATA_2 mid2; /* -- testing typedef of struct */
} DATA_2;
```

### Parameter Comments

Each parameter declaration within a data structure definition may be accompanied by a trailing comment. There are six possible fields in the parameter comment, but only two are required. All six fields of the parameter comment are stored for later reuse at simulation runtime.

#### The Input/Output Specification

The first three fields in the parameter comment are optional and specify the input/output processing for the parameter. I/O permissions may be set globally or individual capabilities may set their permissions separately. I/O permissions for checkpointing is available to set separately.

To set all permissions for general variable access, start the comment with one of the following fields, `[**|*i|*o|*io]`, `trick_io([**|*i|*o|*io])` or `io([**|*i|*o|*io])`. These are equivalent forms to set general variable access.

* `**` indicates that Trick will not allow input or output for this parameter; i.e. the user can not input this parameter, record this parameter, or view its value.
* `*i` indicates that only input is allowed for the parameter. Parameter may be input through the checkpoint file or ref_assignment, but the parameter will not be recordable or written to a checkpoint file.
* `*o` indicates only output is allowed for the parameter. Parameter may be checkpointed or logged only. They are not reloaded during a checkpoint reload.
* `*io
