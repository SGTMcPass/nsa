### Accessing Simulation Parameters > I Just Want to Know How Do I Set this Value...

 the ball structure.
double position[3] ;     /* (m) X,Y,Z position */
"""

# Assign X position to 2m
ball.position[0] = trick.attach_units( "m" , 2.0 )

# Automatic units conversion is done if the attached unit is compatible with the variable.
# Assign Y position to 2ft
ball.position[1] = trick.attach_units( "ft" , 2.0 )

# Error is raised.
ball.position[2] = trick.attach_units( "ft/s" , 3.0 )

# Units may be attached to python lists and assigned to the array with one statement
# Automatic units conversion is done on the entire list.
ball.position = trick.attach_units( "ft" , [1.0 , 2.0, 3.0] )

# Lists may even include values of different units.  Automatic units conversion is
# done element by element.
ball.position = [trick.attach_units( "ft" , 1.0 ) , trick.attach_units( "m" , 2.0 ) , trick.attach_units( "cm" , 3.0 )]

```

Printing parameters in the Python script will include the attached units.

```pycon
>>> print ball.position
[1.0m , 2.0m , 3.0m]
```

## Time Based Input Processing

The input processor allows pieces of the input file to be processed at a later simulation time.
To process code at a later time call `trick.add_read(<time>, "<code_to_be_executed>")`.

```python
# simple statement
trick.add_read(1.0 , "ball.obj.state.out.position[0] = 4.0") ;

# Use triple quotes for multi line input or code segments that include quotes.
trick.add_read(2.0 , """
ball.obj.state.out.position[0] = 4.0
print "This is a quoted string inside the triple quotes"
"""

# Use a local python variable called read to get an appearance similar previous Trick input files
read = 4.0
trick.add_read(read , ... )

read += 0.2
trick.add_read(read , ... )

read = 5.0
trick.add_read(read , ... )
```

## Freeze the Simulation

To freeze a simulation call `trick.freeze([<freeze_time>])`.  `trick.freeze()` called with no
arguments will freeze immediately.  An optional freeze time may be provided to freeze some time
in the future.

```python
# Freezes immediately
trick.freeze()

# Freezes at an absolute time
trick.freeze(100.0)

# Freezes 5 seconds relative from the current sim_time
trick.freeze(trick.exec_get_sim_time() + 5.0)

```

##
