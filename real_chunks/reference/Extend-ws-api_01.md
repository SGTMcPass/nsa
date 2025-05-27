### Extending the WebSocket-API > Testing The New WebSocket Interface > time.html

 It provides methods to:

 1. Synchronously marshall Trick simulation data for out-going messages
 2. Send messages to the websocket client, and
 3. Receive and process messages from the websocket client.

To implement a new websocket sub-protocol, one needs to derive a new class from this base class, and implement the required methods. ```WebSocketSession.hh``` can be found in ```${TRICK_HOME}/include/trick/```.

### WebSocketSession.hh
```c
/*************************************************************************
PURPOSE: (Represent Websocket connection.)
**************************************************************************/
#ifndef WEB_SOCKET_SESSION_HH
#define WEB_SOCKET_SESSION_HH

#include <string>
#ifndef SWIG
#include "CivetServer.h"
#endif

class WebSocketSession {
    public:
        WebSocketSession(struct mg_connection *nc):connection(nc){};
        virtual ~WebSocketSession() {};

        /**
           When HTTP_Server::time_homogeneous is set, WebSocketSession::marshallData() is called from the main
           sim thread in a "top_of_frame" job, so that all of the data can be staged at
           the same sim-time, in other words it's time-homogeneous.
        */
        virtual void marshallData()=0;
        virtual void sendMessage()=0;
        virtual int  handleMessage(std::string)=0;

        struct mg_connection* connection;
};
#endif
```

### Adding Your New WebSocketSession Type to the WebServer

To install your new websocket protocol, you'll need to create a function that
creates an instance of your new WebSocketSession type. Then you'll need to call
```HTTP_Server::installWebSocketSessionMaker``` to install the function, with a
label.

The function you'll create will take ```
