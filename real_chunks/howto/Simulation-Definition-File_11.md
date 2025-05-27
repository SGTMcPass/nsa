### Trick Header Comment > Create Connections



Sim objects may define multiple constructors.  Each constructor may define different job
parameters or even an entirely different set of jobs.  Arguments to the sim object
instantiation determine which sim object constructor and which jobs are run.

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
    ballSimObject(const char * job_class) {
        (job_class) obj.state_init() ;
    }

}

ballSimObject ball(1 , 10.0 , "initialization") ;
ballSimObject ball2( "default_data" ) ;
```

### Sim Object Inheritance

Sim objects may inherit from other sim objects.  Jobs in the derived class will be run after those
of the base sim object class.  Both C and C++ jobs may be inherited.

```C++
class ballSimObject : public Trick::SimObject {
 public:
    Ball obj ;
    ballSimObject() {
        (10.0, "scheduled") trick_ret = obj.state_print() ;
    }
}

class anotherBallSimObject : public ballSimObject {
    public:
    anotherBallSimObject() {
         // This job will run after the above state_print()
        (10.0, "scheduled") another_print() ;
    }
}

anotherBallSimObject ball() ;
```

### Polymorphism in Sim Object jobs.

Polymorphism can be used to dynamically set objects at initialization or even change object types
during runtime.  Given an abstract class and two derived classes:

```C++
class Ball {
    public:
        virtual void print_type() = 0 ;
} ;

class Baseball : public Ball {
    public:
        virtual void print_type() ;
} ;

class Soccerball : public Ball {
    public:
        virtual void print_type() ;
} ;
```

We may use a Ball base pointer in the S_define.

```C++
class ballSimObject : public Trick::SimObject {
    public:
        Ball * ball_ptr ;
        ballSimObject() {
            (1.0 , "scheduled") ball_ptr->print_type() ;
        }
} ;

ballSimObject ball ;
```

`ball_ptr` is not instantiated when the simulation is compiled.  If nothing is assigned to `ball_ptr`
before the first scheduled call of `ball_ptr->print_type()` then the call will fail and the sim
will core.  We can allocate `ball_ptr` in the input file.  We can even change `ball_ptr` in the
middle of the simulation.
