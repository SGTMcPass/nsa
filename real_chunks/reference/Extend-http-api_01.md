### Extending the HTTP-API > Example HTTP-API Extension > A Complete S_define

_HELLO
#define HANDLE_HTTP_GET_HELLO

#ifndef SWIG
void handle_HTTP_GET_hello(struct mg_connection *nc, void *hm);
#endif

#endif
```

**```handle_HTTP_GET_hello.c```**

```c
#include "CivetServer.h"
#include "civetweb.h"
#include <string.h>

void handle_HTTP_GET_hello(struct mg_connection *nc, void *hm) {
    mg_printf(nc, "%s", "HTTP/1.1 200 OK\r\nTransfer-Encoding: chunked\r\n\r\n");
    const char* json_text =
        "{ \"greeting\" : \"Hello Trick Sim Developer!\" }";
    mg_send_chunk(nc, json_text, strlen(json_text));
    mg_send_chunk(nc, "", 0);
}
```

### Installing our ```httpMethodHandler```.

We'll do this from our **S_define** file:

* Add  ```(httpMethods/handle_HTTP_GET_hello.c)``` to the ```LIBRARY DEPENDENCIES```.

* Include our header file:

   ```##include "httpMethods/handle_HTTP_GET_hello.h"```

* In ```create_connections()``` add :

```c
web.server.installHTTPGEThandler( "hello", &handle_HTTP_GET_hello );
```
### A Complete S_define

```c++
/***********************TRICK HEADER*************************
PURPOSE:
    (Cannon Numeric)
LIBRARY DEPENDENCIES:
    (
     (cannon/gravity/src/cannon_init.c)
     (cannon/gravity/src/cannon_numeric.c)
     (httpMethods/handle_HTTP_GET_hello.c)
    )
*************************************************************/

#include "sim_objects/default_trick_sys.sm"
#include "sim_objects/CivetServer
