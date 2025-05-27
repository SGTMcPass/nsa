### Trick Header Comment > Create Connections

 appear in the S_define file.

```C++
class AsimObject : public Trick::SimObject {
    public:
        modelA a ;
        // This pointer points to a different sim object
        modelB * b_ptr ;

        AsimObject() {
            // This job requires type modelB from a different sim object
            (1.0 , "scheduled") a.job(b_ptr) ;
        }
} ;

class BsimObject: public Trick::SimObject {
    public:
        modelB b ;
};

AsimObject A ;
BsimObject B ;

void create_connections() {

    // Connects the AsimObject and BsimObject together.
    A.b_ptr = &B.b

    // Sets a default stop time for the simulation.
    exec_set_terminate_time(300.0) ;
}
```

[Continue to Making The Simulation](Making-the-Simulation)
