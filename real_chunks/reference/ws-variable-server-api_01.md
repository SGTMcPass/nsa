### WS-API: VariableServer > Example Variable Server Client

Execute the given Python code in the host sim.

```json
{ "cmd" : "python",
  "pycode" : string
}
```

Send the sie structure from the server. Response will be the ```sie``` response message (*below*).

```json
{ "cmd" : "sie" }
```

Send the units for the given variable. Response will be the ```units``` response message (*below*).

```json
{ "cmd" : "units",
  "var_name" : string
}
```

## Server to Client Response Messages

Error Response

```json
{ "msg_type" : "error",
  "error_text" : string
}
```

Periodic response containing the values of variables requested by ```var_add```.

```json
{ "msg_type" : "var_list"
  "time" : double
  "values" : []
}
```

Response to the ```sie``` command (*above*).

```json
{ "msg_type" : "sie",
  "data" : string
}
```

Response to the ```units``` command (*above*).

```json
{ "msg_type" : "units",
  "var_name" : string,
  "data" : string
}
```


## Example Variable Server Client
```html
<!DOCTYPE html>
<html>
  <head>
    <title>WS Experiments</title>
  </head>
  <body>
      <style>
          table { border-collapse: collapse; width: 100%; }
          th, td { text-align: left; padding: 8px; }
          tr:nth-child(even){background-color: #f2f2
