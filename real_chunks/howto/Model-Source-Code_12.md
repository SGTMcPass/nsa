### Programming Language Support > Source Files > Trick Version Compatibility

_HEADER]
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
     [(object_n.o|lib_n.a|lib_n.so|<relative_path>/lib_n.a)]
    )]
[PROGRAMMERS:
   (((Name) (Company) (Date) [(other info)])
   [((Name) (Company) (Date) [(other info)])])]
*/

// source code...
```

### Comment Header

The Trick header is an optional comment block at the top of each source file. It is used for auto-documentation, and more importantly is the means of specifying dependencies to objects or libraries not processed by Trick. Separate functions within a source file do NOT require additional headers. Since parentheses, ( ), are used to delineate fields within the comment header, parentheses are not allowed as characters within the comment fields. NOTE: Even if you are coding a C++ file, you must still specify the comment header using C style comments (not C++ style comments).

#### Job Description

* The PURPOSE field should be a brief description of what the module does.
* The REFERENCES field may contain any number of references, with each reference possessing any number of sub items; notice the nested parentheses for the REFERENCES field.
* The ASSUMPTIONS AND LIMITATIONS field may contain any number of assumptions and limitations delimited by parentheses.
* The LIBRARY DEPENDENCIES. See Library_Dependencies section in the model header section
* The PROGRAMMERS field may contain any number of programmer fields, each of which may contain any number of sub items; e.g. programmer name, company, mod date, etc. The programmer fields are meant to provide an in-code means to track code changes.

### Source Code

Trick is only interested in the header comment if one is present in source code files. Anything goes for the rest of the source code file.

### Trick Version Compatibility

Trick is always changing. The interface to Trick functions may change with each major version. Sometimes even minor version upgrades change the interface. When Trick builds model source code, it includes -DTRICK_VER=<version> and -DTRICK_MINOR=<minor_version> to the TRICK_CFLAGS and TRICK_CXXFLAGS. This allows developers to key off the Trick version in model source code. If there are any compile issues dependent on Trick version, this #define may be useful.

[Continue to Environment Variables](Environment-Variables)
