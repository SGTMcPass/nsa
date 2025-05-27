### Extending the WebSocket-API > Testing The New WebSocket Interface > time.html

/TimeSession.cpp)
    )
*************************************************************/

#include "sim_objects/default_trick_sys.sm"
#include "sim_objects/CivetServer.sm"
##include "cannon/gravity/include/cannon_numeric.h"
##include "httpMethods/TimeSession.hh"

class CannonSimObject : public Trick::SimObject {

    public:
        CANNON      cannon ;
        int foo;
        CannonSimObject() {
            ("default_data") cannon_default_data( &cannon ) ;
            ("initialization") cannon_init( &cannon ) ;
            ("derivative") cannon_deriv( &cannon ) ;
            ("integration") trick_ret = cannon_integ( &cannon ) ;
            ("dynamic_event") cannon_impact( &cannon) ;
        }
} ;
CannonSimObject dyn ;

IntegLoop dyn_integloop (0.01) dyn;

void create_connections() {
    dyn_integloop.getIntegrator(Runge_Kutta_4, 5);
    web.server.installHTTPGEThandler( "hello", &handle_HTTP_GET_hello );
    web.server.installWebSocketSessionMaker( "Time", &makeTimeSession );
}
```


## Testing The New WebSocket Interface

To test your new web socket interface, put the following ```time.html``` file in  ```$YOUR_SIM_DIRECTORY/www/apps```. Then request ```http://localhost:8888/apps/time.html``` from your browser. You should see the time messages from your sim.

### time.html

```html
<!DOCTYPE html>
<html>
  <head>
    <title>WS Example</title>
  </head>
  <body>
      <div id="output"></div>
      <script type="text/javascript">

          function
