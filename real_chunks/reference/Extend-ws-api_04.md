### Extending the WebSocket-API > Testing The New WebSocket Interface > time.html

Session::LOCAL;
   } else {
      std::cerr << "ERROR: Unknown command \"" << client_msg << "\"." << std::endl;
   }
   return 0;
}

// WebSocketSessionMaker function for a TimeSession.
WebSocketSession* makeTimeSession( struct mg_connection *nc ) {
    std::cerr << "DEBUG: Creating new TimeSession." << std::endl;
    return new TimeSession(nc);
}
```

We put ```TimeSession.cpp``` and ```TimeSession.cpp``` into a models directory called ```httpMethods/```.


### S_define Modifications

1. Specify the dependency on the ```httpMethods/TimeSession.cpp``` compilation unit.
2. We should already be including the WebServer sim object, otherwise we don't even have a webserver.
3. We need to include our new header file: ```##include "httpMethods/TimeSession.hh"```
4. Finally, install our WebSocketSession type: ```web.server.installWebSocketSessionMaker("Time", &makeTimeSession);```
The label we use for our protocol here is "Time", but it can be whatever name you choose.

```c++
/***********************TRICK HEADER*************************
PURPOSE:
    (Cannon Numeric)
LIBRARY DEPENDENCIES:
    (
     (cannon/gravity/src/cannon_init.c)
     (cannon/gravity/src/cannon_numeric.c)
     (httpMethods/handle_HTTP_GET_hello.c)
     (httpMethods/TimeSession.cpp)
    )
*************************************************************/

#include "sim_objects/default_trick_sys.sm"
#include "sim_objects/CivetServer.sm"
##include "cannon/gravity/include/cannon_numeric.h"
##include "httpMethods/TimeSession.hh"
