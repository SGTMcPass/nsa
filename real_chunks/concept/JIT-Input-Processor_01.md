### Root

_event_before( "run_event_before", "event_before", "ball.obj.state_print" ) ;
    jit_add_event_after( "run_event_after", "event_after", "ball.obj.state_print" ) ;

    // add a read event that removes all other events.
    jit_add_read( 150.0 , "remove_events" ) ;

    // tries to add event that does not exist. (currently silents fails)
    jit_add_read( 190.0 , "dne_event" ) ;

    exec_set_terminate_time(200.0) ;

/*
    real_time_enable() ;
    trick_real_time.itimer.enable() ;
    sim_control_panel_set_enabled(true) ;
*/

    return 0 ;
}
```

A JIT input file may be used with a python input file or in place of a python input file.  To use a JIT input file from within a python script use the following calls

```python
# jit_compile_and_run specifies the c++ input file, and an optional function name to run.  The function
# must fit the c++ prototype 'extern "C" int function()'.  If no function name is given, the function
# "run_me" is searched for and ran.
trick.jit_compile_and_run("RUN_cpp_input/input.cpp")
trick.jit_compile_and_run("RUN_cpp_input/input.cpp", "run_event_1")

# a c++ library can be compiled and c++ code executed separately.
trick.jit_compile("RUN_cpp_input/input.cpp")
trick.jit_run("RUN_cpp_input/jitlib/libinput.so", "run_event_1")

# executing a c++ function from input.cpp at a later time.  Note: The add_read call will still be
# processed in python causing a real time hit.
trick.add_read(150, """trick.jit_run("RUN_cpp_input/jitlib/libinput.so", "run_event_1")""")
```

To use a JIT input file in place of the normal python input file, use the C++ input file on the command line.

```
./S_main_<TRICK_HOST_CPU>.exe RUN_cpp_input/input.cpp
```

[Continue to Event Manager](Event-Manager)
