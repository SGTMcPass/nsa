### Extending the WebSocket-API > Testing The New WebSocket Interface > time.html

| [Home](/trick) → [Documentation Home](../Documentation-Home) → [Web Server](Webserver) → [APIs](WebServerAPIs) → Extend the WS API |
|------------------------------------------------------------------|

## Extending the WebSocket-API

## When You Create a WebSocket Connection

Consider the following Javascript, that creates a web socket connection:

 ```var ws = new WebSocket('ws://localhost:8888/api/ws/VariableServer');```

In the URL: ```ws://localhost:8888/api/ws/VariableServer```

* ```ws://``` specifies the **protocol** (web-socket in this case.)
* ```localhost``` specifies the **domain**,
* ```:8888``` specifies the **port**, and
* ```/api/ws/VariableServer``` specifies the **path**.

In the Trick web server, the path associated with a websocket must begin with
```/api/ws/```. The remaining part of the path, i.e., ```VariableServer``` is the **key** that specifies the **sub-protocol**, prescribing what messages will be passed between client and server, and what those messages mean.

When a web-socket connection is established, the **key** will determine what type (sub-class) of ```WebSocketSession``` object to create, to manage the connection.

## WebSocketSession
A ```WebSocketSession``` is a pure virtual base class meant to represent the state of one of potentially many websocket connections. It provides methods to:

 1. Synchronously marshall Trick simulation data for out-going messages
 2. Send messages to the websocket client, and
 3. Receive and process messages from the websocket client.

To implement a new websocket sub-protocol
