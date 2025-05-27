### Extending the HTTP-API > Example HTTP-API Extension > A Complete S_define

| [Home](/trick) → [Documentation Home](../Documentation-Home) → [Web Server](Webserver) → [APIs](WebServerAPIs) → Extending the HTTP API |
|------------------------------------------------------------------|

## Extending the HTTP-API

The HTTP-API is implemented as a collection of ```httpMethodHandlers```. An ```httpMethodHandler``` is a pointer to a function that is expected to respond to an HTTP GET request, using the **CivetWeb** framework. An ```httpMethodHandler``` is defined (in ```trick/CivetWeb.hh```) as follows:





```c
typedef void (*httpMethodHandler)(struct mg_connection *, void* cbdata);
```

Documentation for the **CivetWeb Networking Library** can be found at:
[https://cesanta.com/docs/overview/intro.html](http://civetweb.github.io/civetweb/)

## Example HTTP-API Extension

Suppose you want your web server to send you a JSON message:

```json
{ "greeting" : "Hello Trick Sim Developer!" }
```

when you invoke the URL: ```http://localhost:8888/api/http/hello```.

### Creating an ```httpMethodHandler```.

The following two files will be our implementation of an ```httpMethodHandler```. We'll put these in some models directory  ```httpMethods/```.

**```handle_HTTP_GET_hello.h```**

```c
#ifndef HANDLE_HTTP_GET_HELLO
#define HANDLE_HTTP_GET_HELLO

#ifndef SWIG
void handle_HTTP_GET_hello(struct mg_connection *nc, void *hm);
#endif

#endif
```

**```handle_HTTP_GET_hello.c```**

```c
#include "CivetServer
