### Trick Header Comment > Create Connections

 the simulation.
If the job does not return an integer, Trick will not take any action based on a return value. Note
that initialization job return values are NOT checked by the executive.

#### Job Name

This field specifies the job name of the job as defined in the job’s source code.

C function and C++ member functions can be called as a jobs. Here is a quick example of a C and C++
calls.

```C++
%{
extern "C" {
    c_function() ;
}
%}

class MySimObject() : public Trick::SimObject {

    public:
        Ball my_ball ;

    MySimObject() {
        (1.0 , "scheduled") c_function() ;
        (1.0 , "scheduled") my_ball.print_state() ;
    }

}
```


### Job Calling Arguments

Job calling arguments adhere to C++ calling argument standards.

## Sim Object Methods

Methods may be defined within a sim object.  These methods may be used as simulation jobs.
A possible use for sim object methods would be to call non C/C++ code with minimal overhead from
the S_define file.

## Specifying Scheduled Loop Job Class Order

This section of the S_define (encapsulated by "job_class_order{...};) can be used to specify a new
scheduled loop job class order.  The user may simply re-order the existing job classes that exist or
can specify a new set of scheduled loop job classes. Job classes that are eligible for reassignment
are listed in Table SD_1 between automatic and automatic_last inclusive. The order they are shown
in the table is the default ordering. Note that if the user provides an ordering, classes that are
not included in the ordering (excluding automatic and automatic_last) will not be handled by any scheduler,
 and therefore not executed in the sim.


```C++
job_class_order {
   my_job_class_1 ,
   my_job_class_2 ,
   scheduled ,
   my_job_class_3
};
```

## Simulation Object C++ properties

Sim objects are C++ objects.  They possess all of the capabilities of C++ objects.  This section
describes how to use some C++ features with sim objects.

### Simulation Object Instantiations

#### Multiple Instantiations

Sim objects are instantiated within the S_define file. They are regular class objects, and as such
are treated that way.  Sim objects may be multiply instantiated.  Multiply instantiated sim objects
works with both C and C++ models contained within the sim object.

```C++
class ballSimObject : public Trick::SimObject {
 public:
    Ball obj ;
    ballSimObject() {
        ("initialization") obj.state_init() ;
        ("derivative") obj.force_field() ;
        ("derivative") obj.state_deriv() ;
        ("integration", &my_integ) trick_ret = obj.state_integ() ;
        (10.0, "scheduled
