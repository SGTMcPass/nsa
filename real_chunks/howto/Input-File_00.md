### Accessing Simulation Parameters > I Just Want to Know How Do I Set this Value...

| [Home](/trick) → [Documentation Home](../Documentation-Home) → [Running a Simulation](Running-a-Simulation) → Input File |
|------------------------------------------------------------------|

The primary interface between the simulation executable and the user is the runstream
input file. The Trick simulation input file syntax is Python.  All Python syntax rules
apply

Rather than discuss an explicit syntax definition (which would probably be more
confusing than informative), each specific capability of the input processor, and
its associated input file syntax, will be discussed.

## Accessing Simulation Parameters

The parameter naming convention for ALL input parameters is the parameter's actual
source code name. The following is a line from an input file :
```python
ball.obj.state.output.position[0] = 1.0 ;
```
In this example, ball is the sim object name in the S_define file for a sim object
which contains the data structure named obj, where the obj data structure declaration
is as follows:

```cpp
class BallSimObject : Trick::SimObject {
...
  Ball obj ;
...
}

BallSimObject ball ;
```

`state` is a class member found in the `Ball` class.

```cpp
class Ball {
...
    public:
        BallState state; /**< -- Ball state object. */
...
};
```

`output` is a member of the `BallState` class, and finally `position` is
a member of the `BallStateOutput` class.

```cpp
class BallState {
...
  public:
   BallStateOutput output; /**< trick_units(--) User outputs.  */
...
};

class BallStateOutput {
...
    public:
        double position[2];  /**< trick_units(m)    X(horizontal), Y(vertical) position. */
...
};
```

Arrays of simulation parameters may be read and written to with one Python statement.

```python
"""
These variables are declared in the ball structure.
double da[3] ;
double daa[3][3] ;
"""

# Python lists are the equivalent of the C/C++ arrays.

ball.da = [ 1.0 , 2.0 , 3.0 ]
print ball.da
# [ 1.0 , 2.0 , 3.0 ] is printed

ball.daa = [[ 1.0 , 0.0 , 0.0 ] , [ 0.0 , 1.0 , 0.0 ] , [0.0 , 0.0 , 1.0]]
print ball.daa

# [[ 1.0 , 0.0 , 0.0 ] ,
#  [ 0.0 , 1.0 , 0.0 ] ,
#  [0.0 , 0.0 , 1.0]]
# is printed
```

## Accessing Simulation Enumerated Types

Global Enumer
