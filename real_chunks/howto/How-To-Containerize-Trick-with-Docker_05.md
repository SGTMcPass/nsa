### THE END

```

* Create a file named ```Dockerfile``` that contains the content listed above.

* Build the Docker image by executing: ```docker build --tag sim_cannon_docker .```

* When the build completes, execute : ```docker images```.

   You should see a record of the image that you just created:

   ```
   REPOSITORY          TAG       IMAGE ID       CREATED          SIZE
   sim_cannon_docker   latest    d4547502c2a4   13 seconds ago   2.61GB
   trick               19.5.1    1023a17d7b78   2 minutes ago    2.61GB
   ```

### Running the docker image:
To instanciate a container from the image: ```docker run --name misterbill --rm -P sim_cannon_docker &```

* In a host terminal (not in the container) execute:

  ```bash
  docker port misterbill
  ```

to see what host-port container-port 9001 has been mapped to.

You should see something like:

```
     9001/tcp -> 0.0.0.0:32783
     9001/tcp -> [::]:32783
```

This shows that port 9001 in our container has been mapped to port 32783
on our host computer.  So, in this case we would connect our (host)
java client to port 32783.

To connect the CannonDisplay variable-server client to the containerized simulation:

```bash
java -jar SIM_cannon_docker/models/graphics/dist/CannonDisplay.jar <port> &
```

:warning: Don't just copy and paste. If you don't put the right port number it won't work.


![](images/cannon_display.png)

* Click **RELOAD**. This re-initializes the cannon. Then click **FIRE**. The cannon will fire.
* Adjust the the controls on the left hand side of the graphics client.  **RELOAD** and **FIRE**.
* Do this until you're bored.

If Trick is installed on your host then you can also connect :

```bash
trick-simcontrol localhost <port> &
```

You can shut down the sim from the trick-simcontrol panel when you're done.
or if you don't have Trick installed, just use: ```docker kill misterbill```.

# THE END
