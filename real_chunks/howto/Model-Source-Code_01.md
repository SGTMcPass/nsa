### Programming Language Support > Source Files > Trick Version Compatibility

 [struct_tag] {
    char|short|int|long|long long|
    unsigned char|unsigned short|unsigned int|unsigned long|unsigned long long|
    float|double [*]* param_name [[dim]]*;
        /* [**|*i|*o|*io] (trick_io|io)([**|*i|*o|*io]) (trick_chkpnt_io|cio)([**|*i|*o|*io])
           trick_units([measurement_units]) description */

    any_other_type [*]* param_name [[dim]]*;
        /* [**|*i|*o|*io] trick_io([**|*i|*o|*io]) trick_chkpnt_io([**|*i|*o|*io])
           trick_units(measurement_units) description */
} struct_name;

class <class_name> {
    [
     friend InputProcessor;
     friend init_attr<class_name>();
    ]

    (public|protected|private):
    char|short|int|long|long long|
    unsigned char|unsigned short|unsigned int|unsigned long|unsigned long long|
    float|double [*]* param_name [[dim]]*;
        /* [**|*i|*o|*io] trick_io([**|*i|*o|*io]) trick_chkpnt_io([**|*i|*o|*io])
           trick_units([measurement_units]) description */

    any_other_type [*]* param_name [[dim]]*;
        /* [**|*i|*o|*io] trick_io([**|*i|*o|*io]) trick_chkpnt_io([**|*i|*o|*io])
           trick_units([measurement_units])measurement_units description */
};
```
### Comment Header

The Trick comment header, which is optional, begins with `/* PURPOSE:`. Within
the Trick comment header, the `PROGRAMMERS`, `REFERENCES`, `ASSUMPTIONS AND
LIMITATIONS` and `ICG` are optional entries. Since parentheses, (), are used to
delineate fields within the comment header, parentheses are not allowed as
characters within the comment header's fields. Any other formatted comments may appear
before and/or after the Trick comment header.

#### C++ Language Override, `LANGUAGE: (C++)`

If a header file has a C++ extension (e.g *.hh ) Trick’s parsers will realize that it is a C++ file and handle it appropriately. If the extension is *.h, Trick will assume it is a C file (not C++). If you want to make a C++ header file name with the *.h extension, you must explicitly tell Trick it is a C++ file with the `LANGUAGE: (C++)` declaration in the Trick comment header.

#### Telling ICG to ignore this header file,
