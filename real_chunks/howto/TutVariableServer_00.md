### Trick Variable Server > Appendix > The Variable Server API

| [Home](/trick) → [Tutorial Home](Tutorial) → Variable Server |
|------------------------------------------------------------|

# Trick Variable Server

**Contents**

* [What Is The Variable Server?](#what-is-the-variable-server)
    * [Variable Server Sessions](#variable-server-sessions)
* [A Simple Variable Server Client](#a-simple-variable-server-client)
    * [Listing - CannonDisplay_Rev1.py](#listing-CannonDisplay_Rev1-py)
    * [Running The Client](#running-the-client)
    * [How The Client Works](#how-the-client-works)
    * [Getting Values Just Once](#getting-values-just-once)
* [A More Realistic Example](#a-more-realistic-example)
    * [Listing - CannonDisplay_Rev2.py](#listing-CannonDisplay_Rev2-py)
    * [Controlling the Simulation Mode from a VS Client](#controlling-the-simulation-mode-from-a-vs-client)
    * [Initializing the Simulation from a VS Client](#initializing-the-simulation-from-a-vs-client)
* [Starting a Client From the Input File](#starting-a-client-from-the-input-file)

***

This tutorial section will demonstrate how to write a Trick variable server
client. We'll be writing the clients in Python, but they can be written in any
language. We'll start out with a minimal client and then proceed to a more
realistic example. We'll be interfacing with our Cannon ball simulation.

***

<a id=what-is-the-variable-server></a>
## What is The Variable Server?

Every Trick simulation contains a **Variable Server**, a TCP/IP network service
for interacting with the simulation while it's running. Like the input-file
processor, the variable server uses a Python interpreter that's bound to the
simulation's variables and functions. So, just as in an input file, one can set
variable values and call functions from a variable server client. A variable
server specific API also exists to get simulation data back to the client.

The Trick Sim Control Panel, and Trick-View are, for example, both variable
server clients.

<a id=variable-server-sessions></a>
### Variable Server Sessions

Each variable server connection creates a **variable server session**, whose
configuration identifies what, when, and how data will be sent from the server
to the client. A session configuration consists of the following information:

* A list of names of the variables whose values are to be sent in messages to
the client.
* The rate at which messages are transmitted to the client.
* How messages are encoded. (ASCII or binary).
* Whether messages are guaranteed to be time homogenous.
* Whether message transmission is synchronous with the main simulation thread.
* Whether data transmission is paused (inactive), or unpaused (active).
* The debug state of the connection.
* An optional name, to identify the connection when
