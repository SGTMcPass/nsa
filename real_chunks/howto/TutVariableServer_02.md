### Trick Variable Server > Appendix > The Variable Server API

trick.var_unpause()\n" )

# 4.0 Repeatedly read and process the responses from the variable server.
while(True):
    line = insock.readline()
    if line == '':
        break

    print(line)
```

<a id=running-the-client></a>
### Running the Client

To run the variable server client :

* Create a new file called *CannonDisplay_Rev1.py* in your home directory,
  and copy the contents of the above listing above into it.
* Make the file executable. Example: ```% chmod +x CannonDisplay_Rev1.py```.
* Execute, but don't "Start" the cannonball simulation.
* Find the variable server port number in the bottom left hand corner of the Sim
Control Panel, as shown below.

![Cannon](images/SimControlPanel.png)

* Execute the script with the port number as an argument.
  Example: ```$ ~/CannonDisplay_Rev1.py 50774 &```
* "Start" the cannonball simulation.

The output of the script will display three columns of numbers. The left most
number is the [variable server message type](#variable-server-message-types).
Here, a message type of 0 indicates that the message is the (tab delimited) list
of the values we requested. The two columns to the right of the message number are
the values of ```dyn.cannon.pos[0]``` and ```dyn.cannon.pos[1]```, in the order
that they were specified in the script.

```
0	55.85863854409634	24.0875895

0	60.18876556301853	25.2730495

0	64.51889258194073	26.36040950000001

0	68.84901960086293	27.34966950000001

0	73.17914661978513	28.24082950000001
```

<a id=how-the-client-works></a>
### How the Client Works

The script first gets the variable server's port number, and creates a TCP/IP
connection to it. The script then configures the variable server session, with
the commands listed below, to periodically send the cannonball position with the
following commands:

* **trick.var_pause()**
* **trick.var_ascii()**
* **trick.var_add("dyn.cannon.pos[0]")**
* **trick.var_add("dyn.cannon.pos[1]")**
* **trick.var_unpause()**

The [**var_pause**](#api-var-pause), and [**var_unpause**](#api-var-unpause)
commands are generally used at the beginning, and ending of variable server
session configurations. [**var_pause**](#api-var-pause) tells the variable
server to stop sending data, if
