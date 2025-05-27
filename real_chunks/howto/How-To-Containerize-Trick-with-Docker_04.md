### THE END

 Download CannonBoom.wav from [here](https://github.com/nasa/trick/blob/master/trick_sims/Cannon/models/graphics/resources/CannonBoom.wav).

   * Download Explosion.wav  from [here](https://github.com/nasa/trick/blob/master/trick_sims/Cannon/models/graphics/resources/Explosion.wav).

:exclamation: When you download the wave files from Github, their names may be set to a flattened version of their full pathnames. So, we have to rename them to their real names.

   * Rename the down-loaded wave files to **CannonBoom.wav**, and **Explosion.wav** respectively, and move them both to ```models/graphics/resources/```.



* Build the cannon graphics client.

   ```bash
   cd ${DOCKER_PLAYGROUND}/SIM_cannon_docker_build/SIM_cannon_docker/models/graphics
   make
   ```

### Building the Docker Image


#### Dockerfile

```
# ------------------------------------------------------------------------------
# The image we are building with THIS Dockerfile is based on the trick:19.5.1
# Docker image that we built previously.
# ------------------------------------------------------------------------------
FROM trick:19.5.1

# ------------------------------------------------------------------------------
# Copy the simulation source code into the image and build it.
# ------------------------------------------------------------------------------
# Set current working directory to the directory where we want our SIM code.
WORKDIR /apps/SIM_cannon
# Copy the simulation source code from our (host) image-build directory into our
# image.
COPY SIM_cannon_docker .
# Build the SIM.
RUN /apps/trick/bin/trick-CP

# In out simulation, we decided to use port 9001 for our
# variable server port. We did this by adding
# "trick.var_server_set_port(9001)" to our input file.

#Expose the variable server port.
EXPOSE 9001/tcp

# Make a script to run SIM_cannon from the /apps directory.
RUN echo "#! /bin/bash" >> /apps/run_sim.sh
RUN echo "cd /apps/SIM_cannon" >> /apps/run_sim.sh
RUN echo "./S_main_Linux_7.5_x86_64.exe RUN_demo/input.py" >> /apps/run_sim.sh
RUN chmod +x /apps/run_sim.sh

CMD ["/apps/run_sim.sh"]
```

* Make sure you're in the right directory.

```bash
   cd ${DOCKER_PLAYGROUND}/SIM_cannon_docker_build
```

* Create a file named ```Dockerfile``` that contains the content listed above.

* Build the Docker image by executing: ```docker build --tag sim_cannon_docker .```

* When the build completes, execute : ```docker images```.

   You should see a record of the image that you just created:

   ```
   REPOSITORY          TAG       IMAGE ID       CREATED          SIZE
   sim_cannon_docker   latest
