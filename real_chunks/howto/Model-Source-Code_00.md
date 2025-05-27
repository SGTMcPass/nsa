### Programming Language Support > Source Files > Trick Version Compatibility

| [Home](/trick) → [Documentation Home](../Documentation-Home) → [Building a Simulation](Building-a-Simulation) → Model Source Code |
|------------------------------------------------------------------|

This section details the syntax for creating headers and source code that Trick can process.

It also details the operation of the Trick Interface Code Generator (ICG) that processes headers, and the Module Interface Specification Processor (MIS) that processes source code.

## Programming Language Support

The majority of model source for simulations is written in C and C++. Trick supports auto generating IO code to peek and poke C and C++ structures, classes, and enumerations. Trick also generates the necessary makefile rules to compile and link C and C++ model code into the simulation.

Models written in other languages may be included in the simulation. It is possible to include Fortran 77, Fortran 90, Ada, and/or Java code in the simulation. These models cannot be called directly from the Trick scheduler, but may be called through C language wrapper functions provided by the user that executes the other language calls.

## Header Files

Trick processes header files in order to auto generate IO source code for the simulation. IO source code is the heart of how Trick does its input processing. The following describes the syntax for a header file.

```C++
/* [TRICK_HEADER]
PURPOSE:
    (Purpose statement.)
[LANGUAGE: (C++)]
[LIBRARY DEPENDENCY:
    (
     (object.o|model.c|lib.a|lib.so|<relative_path>/lib.a)
     [(object_n.o|model_n.c|lib_n.a|lib_n.so|<relative_path>/lib_n.a)]
    )]
[ICG IGNORE TYPES:
    ((Type #1) (Type #n)])]
[PYTHON_MODULE: (module_name)]
[REFERENCES:
    ((Reference #1) (Reference #n)])]
[ASSUMPTIONS AND LIMITATIONS:
    ((Assumption #1) (Assumption #n)])]
[PROGRAMMERS:
   (((Name) (Company) (Date) [(other info)])
   [((Name) (Company) (Date) [(other info)])]]
[ICG: (No|Nocomment)]

Introduced in Trick 16
@trick_parse(everything|attributes|dependencies_only)
@trick_exclude_typename(Type)

*/

typedef enum {
    enum_label [= enum_value],
    last_enum_label [= enum_value]
} enum_name;

[typedef] struct [struct_tag] {
    char|short|int|long|long long|
    unsigned char|unsigned short|unsigned int|unsigned long|unsigned long long|
    float|double [*]* param_name [[dim]]*;
        /* [**|*i|*o|*io] (trick_io|io)([**|*i|*o|*io]) (trick_chkpnt_io|cio)([
