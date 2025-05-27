### Trick Variable Server > Appendix > The Variable Server API

-file></a>
## Starting a Client From The Input File

Rather than having to start a client each and every time from the command line,
we can easily start it from the input file using the function
```trick.var_server_get_port()``` as illustrated in the following input file
script.

```python
#==================================
# Start the variable server client.
#==================================
varServerPort = trick.var_server_get_port();
CannonDisplay_path = os.environ['HOME'] + "/CannonDisplay_Rev2.py"
if (os.path.isfile(CannonDisplay_path)) :
    CannonDisplay_cmd = CannonDisplay_path + " " + str(varServerPort) + " &" ;
    print(CannonDisplay_cmd)
    os.system( CannonDisplay_cmd);
else :
    print('Oops! Can\'t find ' + CannonDisplay_path )
```

Add this to the bottom of RUN_test/input.py to give it a try.
***

## Appendix

<a id=variable-server-message-types></a>
### Variable Server Message Types
| Name              | Value | Meaning |
|-------------------|-------|---------|
| VS\_IP\_ERROR     | -1    | Protocol Error|
| VS\_VAR\_LIST     |  0    | A list of variable values. |
| VS\_VAR\_EXISTS   |  1    | Response to var\_exists( variable_name )|
| VS\_SIE\_RESOURCE |  2    | Response to send_sie_resource|
| VS\_LIST\_SIZE    |  3    | Response to var_send_list_size or send_event_data|
| VS\_STDIO         |  4    | Values Redirected from stdio if var_set_send_stdio is enabled|
| VS\_SEND\_ONCE    |  5    | Response to var\_send\_once|

<a id=the-variable-server-api></a>
### The Variable Server API

The following functions are a subset of variable server API functions that are
used in this tutorial:

<a id=api-var-add></a>
**var\_add( variable_name )** -
Add a name to the session variable list. The value of the added variable will
transmitted in subsequent variable server messages.

<a id=api-var-ascii></a>
**var\_ascii()** -
Set data response messages to the following ASCII encoded format (default):

**0\t**\<variable**1**-value\>[**\t**\<variable**2**-value\>...**\t** \<variable**N**-value\> ]**\n**

Where:

* **N** is the number of variables in the session variable list.
* **\t** is a tab character.

<a id=api-var-binary></a>
**var\_binary()** -
Set response encoding to binary.

<a id=api-var-cycle></a>
**var\_cycle( period )** -
