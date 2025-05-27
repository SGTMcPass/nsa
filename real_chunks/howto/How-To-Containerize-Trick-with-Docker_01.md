### THE END

19.5.1 branch (an official release) of Trick from Github.
RUN git clone -b 19.5.1 https://github.com/nasa/trick.git
# cd into the directory we just created and ..
WORKDIR /apps/trick
# configure and make Trick.
RUN ./configure && make

# ------------------------------------------------------------------------------
# Add ${TRICK_HOME}/bin to the PATH variable.
# ------------------------------------------------------------------------------
ENV TRICK_HOME="/apps/trick"
RUN echo "export PATH=${PATH}:${TRICK_HOME}/bin" >> ~/.bashrc

CMD ["/bin/bash"]
```

### Building the docker image:

* Create a directory for building this docker image:

  ```bash
  cd ${DOCKER_PLAYGROUND}
  mkdir TRICK_19_5_1
  cd TRICK_19_5_1
  ```

* Create a file named ```Dockerfile``` that contains the content listed above.

* Build the Docker image by executing: ```docker build --tag trick:19.5.1 .```

   :exclamation: This may take a few minutes.

* When the build completes, execute : ```docker images```.

   You should see a record of the image that you just created:

   ```
   REPOSITORY         TAG       IMAGE ID       CREATED        SIZE
   trick              19.5.1    1023a17d7b78   2 minutes ago  2.61GB
   ```

### Running the docker image:
To Instantiate a container from the image: ```docker run --rm -it trick:19.5.1```

You should see the bash shell prompt from your container. Something like:

```
root@8615d8bf75c5:/apps/trick#
```

Execute: ```ls``` at the prompt to see that it contains Trick.

```
CMakeLists.txt  Makefile                autoconf      configure  lib      test_overrides.mk trickops.py
CMakeModules.   README.md               bin           docs       libexec  test_sims.yml     trigger
CMakeTestFiles  TrickLogo.png           config.log    doxygen    share    trick_sims
LICENSE         TrickLogo_darkmode.png. config.status include    test     trick_source
root@8615d8bf75c5:/apps/trick#
```

This docker container contains a full Trick development environment. You can't run GUI applications on it but you can build a simulation.

<a id=containerize-a-trick-simulation></a>
## Containerize a Trick Simulation

### Prerequisites:

* The trick:19.5.1 docker image described above.

## Introduction

In this example, we'll create a docker image from which we can run (a version of) ```SIM_cannon_numeric```,
one of the variants of Trick's Cannon Ball simulation. This image will be based on the Trick:19.5.1 image
