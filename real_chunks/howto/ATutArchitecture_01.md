### Architecture of a Trick Simulation > The Simulation Definition File (S_define) > The Parts of an S_define

 declare data members of a model, and 2) set job scheduling specifications for a model. The example above declares a new class ```CannonSimObject``` that contains one data member ```cannon```, and three job specifications.

Once a new SimObject-derived class has been defined, we can create an instance of it.
In the example above the variable ```dyn``` is an instance of ```CannonSimObject```.
That is, it is one instance of our cannonball model. If we were to create a second instance of
```CannonSimObject``` then our simulation would contain two independently runnable cannonball models.

In the following sections we'll create the parts for a Trick-based cannonball simulation, and build it.

---
[Next Page](ATutAnalyticSim)
