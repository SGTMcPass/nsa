### Extending the HTTP-API > Example HTTP-API Extension > A Complete S_define

avity/src/cannon_init.c)
     (cannon/gravity/src/cannon_numeric.c)
     (httpMethods/handle_HTTP_GET_hello.c)
    )
*************************************************************/

#include "sim_objects/default_trick_sys.sm"
#include "sim_objects/CivetServer.sm"
##include "cannon/gravity/include/cannon_numeric.h"
##include "httpMethods/handle_HTTP_GET_hello.h"

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
}

```

Continue to [Extending the WS API](Extend-ws-api)
