### User accessible routines > Variable Server Broadcast Channel

  This is indicated by
the @e N field.  For example, if the client has requested 15 variables, and @e N = 15, then
everything is contained in that one message.  However if @e N < 15, then the client should
continue reading messages until all @e N received add up to 15.

If a syntax error occurs when processing the variable server client command, Python will print
an error message to the screen, but nothing will be returned to the client.

If a var_add command was issued for a non-existent variable, there will be a one time Trick error
message printed to the screen, but the resulting data sent to the client is still ok. The message
returned for the non-existent variable will have a type of 24 and it's value will be the string "BAD_REF".

## Stdio Format

These messages are sent to the client if stdout and stderr are redirected. See "Sending stdout
and stderr to client" for more details.

```
4 <stream> <size>
<text>
```

- message_id Stdio messages are message_id = 4.
- stream is the stream the message was written to.  1 = stdout, 2 = stderr
- size is the number of bytes in the <text> section.  The newline between the <size> and <text>
is not counted in the size.
- text is the message

Only output from python is redirected, i.e. "print" or calls to "sys.stdout.write()".  C/C++ code
called from python will still direct their stdout/stderr to the simulation output location.
The "print" statement will send 2 messages, the text in the print, and an additional newline.
Calls to sys.stdout.write() only generate 1 message.

Error messages printed by python to stderr may be sent in multiple messages.

## Variable Server Broadcast Channel

To connect to the variable server for any simulation, a client needs to know the
hostname and port.  As of 10.5, the port number is determined by the OS.  For external
applications the best way to find a varible server port is to listen to the variable
server broadcast channel.  Every simulation variable server will broadcast the host and port
number to the broadcast channel.  The channel is address 224.3.14.15 port 9265.  All simulations
on your network sends it's information to this address and port so there may be multiple
messages with variable server information available here.  Here is some
C code that reads all messages on the variable server channel.

Note that the multicast protocol is disabled by default in MacOS.

```c
#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>

int main() {

    int mcast_socket ;
    char buf1[1024] ;
    ssize_t num_bytes ;
    int value = 1;
    struct sockaddr_in sockin ;
    struct ip_mreq mreq;

    if ((mcast_socket = socket(AF_INET, SOCK_DGRAM, 0)) < 0) {
        perror("init socket");
    }

    if (setsockopt(mcast_socket, SOL_SOCKET, SO_REUSEADDR, (char *) &value, (socklen_t) sizeof(value)) < 0) {
        perror("setsockopt: reuseaddr");
    }
#ifdef SO_REUSEPORT
    if (setsockopt(mcast_socket, SOL_SOCKET, SO_REUSEPORT, (char *) &value, sizeof(value)) < 0) {
        perror("setsockopt: reuseport");
    }
#endif

    // Use setsockopt() to request that the kernel join a multicast group
    mreq.imr_multiaddr.s_addr = inet_addr("224.3.14.15");
    mreq.imr_interface.s_addr = htonl(INADDR_ANY);
    if (setsockopt(mcast_socket, IPPROTO_IP, IP_ADD_MEMBERSHIP, (char *) &mreq, (socklen_t) sizeof(mreq)) < 0) {
        perror("setsockopt: ip_add_membership");
    }

    // Set up destination address
    sockin.sin_family = AF_INET;
    sockin.sin_addr.s_addr = htonl(INADDR_ANY);
    sockin.sin_port = htons(9265);

    if ( bind(mcast_socket, (struct sockaddr *) &sockin, (socklen_t) sizeof(sockin)) < 0 ) {
        perror("bind");
    }

    do {
        num_bytes = recvfrom(mcast_socket, buf1, 1024, 0 , NULL, NULL) ;
        if ( num_bytes > 0 ) {
            buf1[num_bytes] = '\0' ;
            printf("%s\n" , buf1) ;
        }
    } while ( num_bytes > 0 ) ;
