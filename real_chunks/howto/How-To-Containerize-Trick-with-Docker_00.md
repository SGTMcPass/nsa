### THE END

# How to "Containerize" Trick With Docker

This HOWTO assumes that we building our Docker images on a Linux system. If you're using
MacOS or Windows, the translation should hopefully be fairly straight forward.

**Contents**

* [Containerize a Basic Trick Environment](#containerize-a-basic-trick-environment)
* [Containerize a Trick Simulation](#containerize-a-trick-simulation)

***

## Prerequisites:

* Docker is installed on your machine.
* A basic familiarity with Docker. ["A Docker Tutorial for Beginners"](https://docker-curriculum.com) is an excellent way.
* A basic familiarity with bash shell scripting.

## Create a Place to Build Our Docker Images

For this HOWTO we'll try to stay organized by first creating a directory in
which we can build our Docker images. Let's also create and environment
variable for this directory.

* Create the **DockerPlayGround** directory and **DOCKER_PLAYGROUND** environment variable.

```bash
mkdir DockerPlayGround
export DOCKER_PLAYGROUND="`pwd`/DockerPlayGround"
```
<a id=containerize-a-basic-trick-environment></a>
## Containerize a Basic Trick Environment

In this example we'll build a Docker image, based on Ubuntu 18.04, with Trick 19.5.1
installed.

### Dockerfile

```docker
# ------------------------------------------------------------------------------
# The image we are building with THIS Dockerfile is based on the ubuntu:18.04
# Docker image from dockerhub (hub.docker.com).
# ------------------------------------------------------------------------------
FROM ubuntu:18.04

# ------------------------------------------------------------------------------
# Install Trick Dependencies identified at
# https://nasa.github.io/trick/documentation/install_guide/Install-Guide#ubuntu
# ------------------------------------------------------------------------------
RUN apt-get update && apt-get install -y \
bison \
clang \
flex \
git \
llvm \
make \
maven \
swig \
cmake \
curl \
g++ \
libx11-dev \
libxml2-dev \
libxt-dev \
libmotif-common \
libmotif-dev \
python3-dev \
zlib1g-dev \
llvm-dev \
libclang-dev \
libudunits2-dev \
libgtest-dev \
openjdk-11-jdk \
zip

ENV PYTHON_VERSION=3

# ------------------------------------------------------------------------------
# Get Trick version 19.5.1 from GitHub, configure and build it.
# ------------------------------------------------------------------------------
# We want to clone Trick into the /apps directory of our image.
WORKDIR /apps
# Get the 19.5.1 branch (an official release) of Trick from Github.
RUN git clone -b 19.5.1 https://github.com/nasa/trick.git
# cd into the directory we just created and ..
WORKDIR /apps/trick
# configure and make Trick.
RUN ./configure && make

# ------------------------------------------------------------------------------
# Add ${TRICK_HOME}/bin to the PATH variable.
# ------------------------------------------------------------------------------
ENV TRICK_HOME="/
