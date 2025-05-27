### User accessible routines > Variable Server Broadcast Channel

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

    return 0 ;
}
```

The information sent by each variable server is a tab delimited list of strings
1. Hostname
2. Port
3. User
4. Process ID (PID)
5. Simulation directory
6. S_main command line name
7. Input file
8. Trick version of simulation
9. User defined tag
10. Port (duplicate field for backwards compatibility)

[Continue to Status Message System](Status-Message-System)
