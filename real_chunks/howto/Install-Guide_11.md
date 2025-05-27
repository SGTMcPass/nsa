### Install Trick > Notes > Python Version

 and execution. If they are not set, Trick will infer them without polluting your environment. Furthermore, they will be available to any processes that are spawned as part of compilation or execution, so even your own tools may no longer need these variables to be manually set.

Similarly, Trick does not require its executables to be on your `PATH`, but you may find it convenient to add them if you prefer to not specify the full path to `trick-CP` every time you build a sim. They are located in `bin` under Trick's root directory. However, if you frequently work with multiple versions of Trick, it is often easier to use a full path than to keep changing an environment variable.

Finally, although setting `TRICK_CFLAGS` and `TRICK_CXXFLAGS` is not necessary, it can be useful to do so if you want a set of flags (`-g` or `-Wall`, for instance) to be applied to all simulation builds.

*The exception to this is if you're building in 32-bit mode, in which case the `TRICK_FORCE_32BIT` environment variable must be set to `1` before you build Trick or any simulation.

[Continue to Building A Simulation](../building_a_simulation/Building-a-Simulation)

## Notes
### 32-bit Mode
If you intend to build Trick in 32-bit mode, you will need 32-bit versions of the libraries in the above table. If a 32-bit version of udunits is not available through your package manager, you can build it from [source](ftp://ftp.unidata.ucar.edu/pub/udunits/udunits-2.2.25.tar.gz):
```bash
tar xfvz udunits-2.2.25.tar.gz
cd udunits-2.2.25
export CFLAGS="-m32"
./configure --prefix=/usr
make
make install
```

### Offline Mode
#### (No maven) (19.1 and up)
Because Java is virtual machine code and is portable, you can copy the Java applications that have already been built on a different machine into your Trick installation on the target machine. If Trick is configured in this way, it no longer relies on maven or calls it (in the target environment only). If you know someone trustworthy who has built Trick already, they can provide the built Java code to you (you can skip step 1 below).

Trick jars are all-in-one and contain everything they need to run. You will still need maven on the machine where you build the Trick Java jars.

1. Pre-build your Java code on a machine with Trick dependencies, including maven and internet access.
```
# On source machine with Trick dependencies, internet, and maven
cd prebuiltTrick && ./configure && make java
```

2. Copy the Java jars to the environment that you need to build
