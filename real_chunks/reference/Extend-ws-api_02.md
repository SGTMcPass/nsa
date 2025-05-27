### Extending the WebSocket-API > Testing The New WebSocket Interface > time.html

'll need to create a function that
creates an instance of your new WebSocketSession type. Then you'll need to call
```HTTP_Server::installWebSocketSessionMaker``` to install the function, with a
label.

The function you'll create will take ```struct mg_connection *``` as an argument
and return ```WebSocketSession*```.

## Example

Let's create a new web socket protocol that sends the time in GMT or local time.

First we'll derive a new type called ```TimeSession ``` from ```WebSocketSession```.

### TimeSession.hh

```c
/*************************************************************************
PURPOSE: (Represent the state of a variable server websocket connection.)
**************************************************************************/
#ifndef TIMESESSION_HH
#define TIMESESSION_HH
#include <vector>
#include <string>
#include "time.h"
#include "trick/WebSocketSession.hh"

class TimeSession : public WebSocketSession {
    public:
        enum Zone { GMT, LOCAL};
        TimeSession(struct mg_connection *nc);
        ~TimeSession();
        void marshallData();
        void sendMessage();
        int  handleMessage(std::string);
    private:
        time_t now;
        Zone zone;
};

WebSocketSession* makeTimeSession( struct mg_connection *nc );
#endif
```

Below is our implementation. Notice the function ```makeTimeSession``` at the bottom.


### TimeSession.cpp

```c
#include <stdio.h>
#include <time.h>
#include <iostream>
#include "TimeSession.hh"
#include <cstring>

// CONSTRUCTOR
TimeSession::TimeSession( struct mg_connection *nc ) : WebSocketSession(nc) {
    time(&now);
}

// DESTRUCTOR
TimeSession::~TimeSession() {}

void TimeSession::marshallData() {
    time(&now);
