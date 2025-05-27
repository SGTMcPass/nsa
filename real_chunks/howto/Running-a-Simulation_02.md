### Root

 execution.

```c++
#include "trick/command_line_protos.h"

void test_job( void ) {
    int num_args ;
    char **args ;
    int ii ;
    num_args = command_line_args_get_argc() ;
    args = command_line_args_get_argv() ;
    for( ii = 0 ; ii < num_args ; ii++ )
        printf( "argument #%d = %s\n" , ii , args[ii] ) ;
    return ;
}
```

[Continue to Input File](Input-File)
