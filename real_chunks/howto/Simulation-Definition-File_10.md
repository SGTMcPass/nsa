### Trick Header Comment > Create Connections

++ models contained within the sim object.

```C++
class ballSimObject : public Trick::SimObject {
 public:
    Ball obj ;
    ballSimObject() {
        ("initialization") obj.state_init() ;
        ("derivative") obj.force_field() ;
        ("derivative") obj.state_deriv() ;
        ("integration", &my_integ) trick_ret = obj.state_integ() ;
        (10.0, "scheduled") trick_ret = obj.state_print() ;
    }
}

// Make 2 balls
ballSimObject ball ;
ballSimObject ball2 ;
```

#### Sim Object Constructor Arguments and Initializer Lists

Sim objects instantiations may take arguments.  These arguments may be used in the sim object's
initialization list.  An initialization list constructs member variables of the class.  They
are listed as a comma separated list after the declaration of a constructor.  Arguments passed
to the sim object constructor may be passed onto member variable constructors.

C structures may be zeroed out when included in the sim object's initialization list.

```C++
class ballSimObject : public Trick::SimObject {
 public:
    Ball obj ;
    C_STRUCT c_struct ;

    // passes int argument to obj constructor.  Zeros out c_struct.
    ballSimObject(int num) : obj(num) , c_struct() {
    } ;
}

// Sim object constructor requires an integer argument.
ballSimObject ball(5) ;
```

#### Sim Object Constructor Arguments and Job Control

Arguments to sim objects may also be used to control job execution.  Most items in the job
specification may be set to the value of an argument.

```C++
class ballSimObject : public Trick::SimObject {
 public:
    Ball obj ;
    ballSimObject(int phase, double cycle , const char * job_class) {
        (job_class) obj.state_init() ;
        Pphase ("derivative") obj.force_field() ;
        ("derivative") obj.state_deriv() ;
        ("integration", &my_integ) trick_ret = obj.state_integ() ;
        (cycle, "scheduled") trick_ret = obj.state_print() ;
    }
}

ballSimObject ball(1 , 10.0 , ~@~\initialization~@~]) ;
// This ball has different job properties than the first ball.
ballSimObject ball2( 2 , 5.0 , ~@~\default_data~@~] ) ;
```

### Multiple Constructors

Sim objects may define multiple constructors.  Each constructor may define different job
parameters or even an entirely different set of jobs.  Arguments to the sim object
instantiation determine which sim object constructor and which jobs are run.

```C++
class ballSimObject : public Trick::SimObject {
 public:
    Ball obj ;
    ballSimObject(int phase, double cycle , const char * job_class) {
        (job_class) obj.state
