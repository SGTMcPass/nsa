### WS-API: VariableServer > Example Variable Server Client

| [Home](/trick) → [Documentation Home](../Documentation-Home) → [Web Server](Webserver) → [APIs](WebServerAPIs) → WS Variable Server API |
|------------------------------------------------------------------|

# WS-API: VariableServer

```ws://localhost:8888/api/ws/VariableServer```

## Purpose

JSON Variable Server

## Client to Server Command Messages

Add a Trick Variable to the current session.

```json
{ "cmd" : "var_add",
  "var_name" : string
}
```
Stop sending periodic ```var_list``` messages (*see below*) from the server.

```json
{ "cmd" : "var_pause" }
```

Resume sending periodic ```var_list``` response messages from the server.

```json
{ "cmd" : "var_unpause" }

```

Send one ```var_list``` message from the server.

```json
{ "cmd" : "var_send" }
```

Clear all variables from the current session, that is: undo all of the ```var_add``` commands.

```json
{ "cmd" : "var_clear" }
```

Disconnect from the variable server.

```json
{ "cmd" : "var_exit" }
```

Set the period (in milliseconds) at which ```var_list``` messages are sent form the server.

```json
{ "cmd" : "var_cycle",
  "period" : integer
}
```

Execute the given Python code in the host sim.

```json
{ "cmd" : "python",
  "pycode" : string
}
```

Send the sie structure from the server. Response will be the ```sie``` response message (*below
