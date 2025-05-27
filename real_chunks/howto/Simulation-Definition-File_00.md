### Trick Header Comment > Create Connections

| [Home](/trick) → [Documentation Home](../Documentation-Home) → [Building a Simulation](Building-a-Simulation) → Simulation Definition File |
|------------------------------------------------------------------|

The Simulation Definition File or S_define is the file which lays out the architecture
of the simulation.  Details about job frequencies, job class, job data, importing/exporting
data to other simulations, freeze cycles, integration, etc. are all housed in this one file.
It is the file which Trick's main processor, CP, parses to determine what will be part of
the simulation and how the pieces fit together.

This section begins with the syntax for the S_define, then details each and every entry
in the syntax template. This section also details how to use Trick's main processor, CP.

```
[/* [TRICK_HEADER]

PURPOSE: (purpose statement)
[LIBRARY DEPENDENCIES:
    (
     [(<rel_path_of_model>/<model_source_code_n.c>)]
    )
]

[DEFAULT_DATA:
    (
     [(struct_type instance_name <rel_path_of_model>/<default_data_file>)]
    )
]
*/]

#include "sim_objects/default_trick_sys.sm"

##include "<rel_path_of_model>/<model_header_file.h>"

%header{
    /* User header code block */
%}

%{
    /* User code block */
%}

class <sim_object_type_name> : public Trick::SimObject {

    [(public|protected|private):]

        <CLASS_TYPE|STRUCTURE_TYPE|ENUMERATED_TYPE|intrinsic_type> [*]* <data_varaible_name> [dims]*

        <sim_object_type_name>([args]) {
            [C<#>] [{job_tag}] [P<#>] ([<cycle_time>, [<start_time>, [<stop_time>,]]] <job_class>) \
             [<return_var> =] <module>([args]) ;

        }

        [<method_name>([args]) { ... } ;]
} ;

[job_class_order {
   <job_class_1>,
   <job_class_2>,
   ...
} ;]

[<sim_object_type_name> <sim_object_instantiation>[(args)] ;]

[integrate <integrator_name> (<integration_dt>) <sim_object_name> [,<sim_object_name] ;]

[collect <reference> = {[<reference> [,<reference>]]};]

[void create_connections() { <glue_code> }]
```

## Trick Header Comment

This optional section of the S_define file is a C style comment found anywhere in the S_define file.
CP will parse the Trick Header comment looking for library dependencies and default data.  Library
dependencies are model source code files that are added to the list of files to be compiled and
linked into the simulation.  These dependencies differ from the ones found in the actual model source
code in that they are the full relative path to the
