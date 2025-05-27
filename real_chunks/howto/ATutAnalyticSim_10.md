### Building & Running a Trick-based Simulation > Running The Simulation > Sim Execution

 all of the functions that it calls. You may also
put the prototypes in the `S_define` block using ([user code blocks](/trick/documentation/building_a_simulation/Simulation-Definition-File#user-code-block)), but if you need to call any of the C functions from the input file then you must include the
prototypes in a header file (the preferred method).

### Data Lines

`Class CannonSimObject : public Trick::SimObject`

The sim object is defined as a C++ class and must be derived from the base class
SimObject.

* `Class CannonSimObject`
The name of the sim_object class is arbitrary.

* `public Trick::SimObject`
As mentioned above, your sim_object class must be derived from the Trick base
class SimObject.

`public : CANNON cannon ;`

* `CANNON` This is the name of the structure typedef that you created in the
cannon.h header.

* `cannon` This is an alias for the CANNON structure. It is mandatory.

* `CannonSimObject()` This is the constructor of the sim_object and it will
contain the job declarations.

### Initialization Job

It is custom to refer to the C-functions created by the developer as **jobs**.
The statement below tells Trick how to handle the `cannon_init()` job.

("initialization") cannon_init( &cannon) ;

* `("initialization")`
This assigns `cannon_init()` a job classification of `initialization`. There are
many classes of jobs. The job classes, for the most part, determine the order
the job is called in the **executive loop**. If there are two jobs of the same
class in the `S_define`, the one seen first in the `S_define` is called first.
Jobs that are classified `initialization` will be called once before the main
executive loop and will not be called again.

* `cannon_init(`
The name of the function we created in $HOME/trick_sims/models/cannon/src/cannon_init.c.

* `&cannon)`
This is the actual value passed to cannon_init(). It is the address of the
object 'CANNON' structure and "cannon" is the alias for the CANNON structure.

### Default Data Job
The default data jobs are called one time before the initialization jobs.

`("default_data") cannon_default_data(&cannon) ;`

* `("default_data")`
This assigns cannon\_default\_data() a job classification of *default_data*.


### Scheduled Job
The next job needs to be called at a regular frequency while the cannonball is
flying in the air. A *scheduled* class job is one of many jobs that can be
called at a given frequency. The only thing new about the declaration for
cannon\_analytic is the additional specification of 0
