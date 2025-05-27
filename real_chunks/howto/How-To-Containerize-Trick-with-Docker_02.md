### THE END

ize-a-trick-simulation></a>
## Containerize a Trick Simulation

### Prerequisites:

* The trick:19.5.1 docker image described above.

## Introduction

In this example, we'll create a docker image from which we can run (a version of) ```SIM_cannon_numeric```,
one of the variants of Trick's Cannon Ball simulation. This image will be based on the Trick:19.5.1 image the we previously built.

Our containerized simulation won't start any variable server clients like the sim-control panel or graphics clients,  because we can't easily run graphics clients from __within__ the container. But, we __can__ easily connect graphics clients running on the host machine to our containerized simulation.

### Creating a Docker friendly version of ```SIM_cannon_numeric```

* Create a directory for building this docker image:

   ```bash
   cd ${DOCKER_PLAYGROUND}
   mkdir SIM_cannon_docker_build
   cd SIM_cannon_docker_build
   ```

* Create a directory for our version of SIM_cannon.

   ```bash
   mkdir SIM_cannon_docker
   cd SIM_cannon_docker
   ```

* Copy the ```SIM_cannon_numeric``` **S_define** file into the current directory.

   ```bash
   curl -O https://raw.githubusercontent.com/nasa/trick/19.5.1/trick_sims/Cannon/SIM_cannon_numeric/S_define
   ```

* Copy ```SIM_cannon_numeric``` include files.

   ```bash
   curl --create-dirs --output models/cannon/gravity/include/cannon.h \
   https://raw.githubusercontent.com/nasa/trick/19.5.1/trick_sims/Cannon/models/cannon/gravity/include/cannon.h
   curl --create-dirs --output models/cannon/gravity/include/cannon_numeric.h \
   https://raw.githubusercontent.com/nasa/trick/19.5.1/trick_sims/Cannon/models/cannon/gravity/include/cannon_numeric.h
   ```

* Copy ```SIM_cannon_numeric``` source files.

   ```bash
   curl --create-dirs --output models/cannon/gravity/src/cannon_init.c \
   https://raw.githubusercontent.com/nasa/trick/19.5.1/trick_sims/Cannon/models/cannon/gravity/src/cannon_init.c
   curl --create-dirs --output models/cannon/gravity/src/cannon_numeric.c \
   https://raw.githubusercontent.com/nasa/trick/19.5.1/trick_sims/Cannon/models/cannon/gravity/src/cannon_numeric.c
   ```

* Create a file named ```S_overrides.mk ``` that contains the following content:

   ```make
   TRICK_CFLAGS   += -Imodels
   TRICK_CXXFLAGS += -Imodels
   ```

* Create and enter a directory
