### Accessing Simulation Parameters > I Just Want to Know How Do I Set this Value...

 often instanciates a class object using the **new** operator, for example:

```
MyClass * p = new MyClass(a,b,c);
```

This form of **new**

1. allocates memory, and then
2. calls a constructor.

Another form of **new**, is called "placement-new". Rather than allocating and calling a constructor to initialize memory, placement-new simply calls a constructor to initialize memory that has already been allocated (e.g., from the Memory Manager).

If ```p``` points to allocated memory, then we can initialize that memory with **placement-new** :

```
new (p) MyClass(a,b,c);
```

In our factory function we'll pass the object pointer we got from the Memory Manager to our placement-new call, to initialize it.

#### Example Factory Function from ```SIM_contact```
SIM_contact simulates collisions between moving balls (think "pool balls"). From the input file, one or more balls can be added to the simulation. Each ball is initialized with a mass, a size, a position, and a velocity. The Ball class also includes a (non-default) constructor.

```C++
class Ball {
    public:
        Ball(){}
        double pos[2];
        double vel[2];
        double mass;
        double radius;

        // A Non-Default Constructor
        Ball(double x, double y, double vx, double vy, double r, double m);
};
```
To create and initialize a new Ball object, we have the function ```make_Ball```.

```C++
// Factory function Implementation
Ball* make_Ball(double x, double y, double vx, double vy, double r, double m) {
    Ball* b = (Ball*)TMM_declare_var_s("Ball");
    return (new (b) Ball(x,y,vx,vy,r,m));
}
```

Because this function is bound to Python by SWIG, it can be called from the input file.
For example :

##### From ```RUN_Newtons_cradle/input.py```
```Python
dyn.contact.nballs = 7
dyn.contact.balls = trick.TMM_declare_var_1d("Ball*", dyn.contact.nballs)
dyn.contact.balls[0] = trick.make_Ball(-4.00, 0.0, 2.0, 0.0, 0.5, 1.0)
dyn.contact.balls[1] = trick.make_Ball(-1.00, 0.0, 0.0, 0.0, 0.5, 1.0)
dyn.contact.balls[2] = trick.make_Ball( 0.01, 0.0, 0.0, 0.0, 0.5, 1.0)
dyn.contact.balls[3] = trick.make_Ball( 1.02, 0
