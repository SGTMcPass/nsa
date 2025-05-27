### Root

, the `RUN_<name>` directory is used.
  - Two subdirectories are automatically created in the designated `<output_file_path>`:
    - `DP_Product`
      - Data Products sepcification DP_xxx.xml files are saved in this folder.
    - `RUN_<name>`
      - All simulation output files, excluding DP_xxx.xml files, are saved in this folder. Additionally, the S_sie.resource file is copied to this directory.
- The `--read-only-sim` flag can be used to redirect all files written at simulation runtime into the output directory.
  - The `--read-only-sim` flag requires either the `-O` or `-OO` option to be used.
  - When the `-O <output_file_path>` option is used and `trick.trick.sie_append_runtime_objs()` is called from the input file, the S_sie.resource file with appended runtime objects is saved in `<output_file_path>`.
  - When the `-OO <output_file_path>` option is used and `trick.trick.sie_append_runtime_objs()` is called from the input file, the S_sie.resource file with runtime objects appended is saved in `<output_file_path>/RUN_<name>`.
- If `trick.trick.sie_append_runtime_objs()` is called from the input file, the S_sie.resource file is to be appended with runtime objects.
  - When neither the `-O` nor `-OO` option is used, the S_sie.resource file with runtime objects appended is saved in the current directory from which the simulation is executed.
  - When the `-O <output_file_path>` option is used without the `--read-only-sim` flag, the S_sie.resource file with runtime objects appended is saved in the current directory from which the simulation is executed.
  - When the `-OO <output_file_path>` option is used without the `--read-only-sim` flag, the S_sie.resource file with runtime objects appended is saved in `<output_file_path>/RUN_<name>`.
- The `-u` option specifies that all remaining arguments are meant to be used by user supplied jobs. All arguments after the -u can be accessed internal to the simulation jobs by calling the get_cmnd_args() function of the executive as illustrated below. In a master/slave simulation, the master's `-u` args will be passed to the slave.

The following code example shows how a function can access the command line arguments during execution.

```c++
#include "trick/command_line_protos.h"

void test_job( void ) {
    int num_args ;
    char **args ;
    int ii ;
    num_args = command_line_args_get_argc() ;
    args = command_line_args_get_argv() ;
    for( ii = 0 ; ii < num_args ; ii++ )
        printf( "argument #%d = %s\n" , ii , args
