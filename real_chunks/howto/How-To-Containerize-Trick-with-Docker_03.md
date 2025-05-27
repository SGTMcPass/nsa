### THE END

   https://raw.githubusercontent.com/nasa/trick/19.5.1/trick_sims/Cannon/models/cannon/gravity/src/cannon_numeric.c
   ```

* Create a file named ```S_overrides.mk ``` that contains the following content:

   ```make
   TRICK_CFLAGS   += -Imodels
   TRICK_CXXFLAGS += -Imodels
   ```

* Create and enter a directory named ```RUN_demo``` and enter it:

   ```bash
   mkdir RUN_demo
   cd RUN_demo
   ```

* Create a file named ```input.py ``` that contains the following content:

   ```python
   trick.real_time_enable()
   trick.exec_set_software_frame(0.1)
   trick.itimer_enable()
   trick.var_server_set_port(9001)
   ```

   :exclamation: Notice that we are NOT starting a SIM-control-panel, or the graphics client.

   :exclamation: Notice that we are explicitly setting the variable server listen port.


### The Graphics Client

   Even though the simulation won't be starting the graphics clients, we will be starting and connecting the graphics clients to the containerized simulation.

   * Download the graphics client's source and Makefile.

   ```bash
   cd ${DOCKER_PLAYGROUND}/SIM_cannon_docker_build/SIM_cannon_docker
   curl --create-dirs --output models/graphics/src/CannonDisplay.java \
   https://raw.githubusercontent.com/nasa/trick/19.5.1/trick_sims/Cannon/models/graphics/src/CannonDisplay.java
   curl --create-dirs --output models/graphics/Makefile \
   https://raw.githubusercontent.com/nasa/trick/19.5.1/trick_sims/Cannon/models/graphics/Makefile
   ```

   * Down-load the graphics client's sound files.

   There are two sound files necessary to build the graphics client, 1)  **CannonBoom.wav**, and 2) **Explosion.wav** .
   They both need to be placed into ```models/graphics/resources/```.

   * Create the resources directory.

   ```
   mkdir -p models/graphics/resources
   ```
   * Down-load the sound files.

   Unfortunately, binary files are more difficult to down-load from Github than text files.

   For each, we have to go to their respective Github pages and click the "Download" button.

   * Download CannonBoom.wav from [here](https://github.com/nasa/trick/blob/master/trick_sims/Cannon/models/graphics/resources/CannonBoom.wav).

   * Download Explosion.wav  from [here](https://github.com/nasa/trick/blob/master/trick_sims/Cannon/models/graphics/resources/Explosion.wav).

:exclamation: When you download the wave files from Github, their names may be set to a flattened
