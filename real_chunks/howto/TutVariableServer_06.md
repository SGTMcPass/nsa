### Trick Variable Server > Appendix > The Variable Server API

 like
```trick.var_add```, ```trick.var_send```, and so forth. But, we're not
just limited to variable server API calls. The variable server's Python
interpreter is bound to our simulation's variables and many other functions,
including those that we've written ourselves. In this example we'll create a
more interactive client, to initialize our simulation, and to control the
simulation modes.

The listing below implements a GUI client using **Python** and
**tkinter** that allows us to:

 1. Set the initial speed and angle of the cannon ball.
 2. Read and display the current simulation MODE.
 3. Set the simulation mode (using a "fire" button).
 4. Animate the flight of the cannon ball in realtime.

<a id=listing-CannonDisplay_Rev2-py></a>
**Listing - CannonDisplay_Rev2.py**

```python
#!/usr/bin/python3
import sys
import socket
import math
from tkinter import *

# ----------------------------------------------------------------------
# 1.0 Process the command line arguments, to get the port number.
if ( len(sys.argv) == 2) :
    trick_varserver_port = int(sys.argv[1])
else :
    print( "Usage: vsclient <port_number>")
    sys.exit()

# ----------------------------------------------------------------------
# 2.0 Set client Parameters.
HEIGHT, WIDTH = 500, 800   # Canvas Dimensions
MARGIN = 20                # Margins around the axes
SCALE = 3                  # Scale = 3 pixels per meter
ballRadius = 5             # Ball radius in pixels

# ----------------------------------------------------------------------
# 3.0 Create constants for clarity.
MODE_FREEZE = 1
MODE_RUN = 5

# ----------------------------------------------------------------------
# 4.0 Create a variable to indicate that we want to "fire" the cannon,
#     and a callback function to set it.
fireCommand = False
def cannonFire():
    global fireCommand
    fireCommand = True

# ----------------------------------------------------------------------
# 5.0 Create the GUI

# 5.1 Create a Canvas to draw on.
tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
tk.title("CannonBall Display")
canvas.pack()

# 5.2  Add a FIRE button, whose callback sets the fireCommand variable.
buttonFrame = Frame()
buttonFrame.pack(side=BOTTOM)
fireButton = Button(buttonFrame,text="fire",command=cannonFire)
fireButton.pack(side=LEFT)

# 5.3 Add an Initial Speed Scale.
speedScale = Scale(buttonFrame, from_=5, to=50, label="Initial Speed", orient=HORIZONTAL)
speedScale.pack(side=LEFT)
speedScale.set(50)

# 5.4 Add an Initial Angle Scale.
angleScale = Scale(buttonFrame, from_=5, to=80, label="Initial Angle", orient=HORIZONTAL)
angle
