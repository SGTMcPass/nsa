### Accessing Simulation Parameters > I Just Want to Know How Do I Set this Value...

 Use a non-constructor routine that allocates memory and returns that
to the Python variable.

```python
# In the above example, we can avoid new_ball_2 from being freed
# when foo returns by setting the thisown flag to 0 in the new_ball_2 object.

def foo():
    new_ball_2 = trick.Ball() ;
    new_ball_2.thisown = 0 ;

# Alternatively we could call a non-constructor C/C++ routine that returns a new Ball
# object to python.  The python interpreter does not sense it allocated anything and
# will not free it.

"""
C++ code for get_new_ball_obj()

Ball * get_new_ball_obj() {
    return(new Ball) ;
}
"""

def foo():
    new_ball_2 = trick.get_new_ball_obj() ;

```

## Comments

Comments in Python come in two forms.

```python
# A single line comment starts with a '#' sign

"""
Multi line comments are enclosed in
three sets of double quotes.
"""
```

## Nested File Inclusion

There are several ways to include files in Python.

```python
# One way is to use the execfile command
exec(open("Modified_data/data_record.py").read())

# Another way is to make the included file a module and import it.
# Import search paths may be added using the sys.path.append command.

sys.path.append("/my/python/dir") ;
import my_new_module
```

## Local Python Variables

Local variables may be used anywhere in the Python input file.  Local variables will follow normal
Python scoping rules.  Shortcut variable names may be created to reference simulation variables.

```python
my_position = ball.obj.state.output.position

my_position[0] = 4.5
my_position[1] = 6.7

print ball.obj.state.output_position
# printout would read "4.5, 6.7"
```

## Environment Variables

Environment Variables are available through the Python `os.getenv` call

```python
print os.getenv("TRICK_CFLAGS")
```

## Measurement Units

Every input parameter has associated measurement units specified in its corresponding data
structure definition file declaration. It specifies the units for the internal source code to
use for that parameter. However, Trick users also have certain control over units specification
from the input file.

`trick.attach_units()` attaches a unit to a value or some Python objects.

```python
"""
This variables is declared in the ball structure.
double position[3] ;     /* (m) X,Y,Z position */
"""

# Assign X position to 2m
ball.position[0] = trick.attach_units( "m" , 2.0 )

# Automatic units conversion is done if the attached unit is compatible with the variable.
# Assign Y position to 2ft
ball.position[1] = trick.attach_units( "ft" , 2
