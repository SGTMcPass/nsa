### Install Trick > Notes > Python Version

" -DCMAKE_BUILD_TYPE=Release -DLLVM_TARGETS_TO_BUILD=X86 -DCMAKE_INSTALL_PREFIX=<clang+llvm-17-x86_path>

  # Build and install
  h. cmake --build build --target install

```

---

<a name="build_swig"></a>
### Build SWIG

```bash
  a. Download the desired source code version from https://github.com/swig/swig/tags

  b. Go to the folder with uncompressed files

  c. ./autogen.sh

  # Default to /usr/local, swig command is in /usr/local/bin and swig installation is in /usr/local/share
  # Use --prefix for ./configure to install to a different location
  d. ./configure

  e. make

  # Uninstall previous installation using "make uninstall"
  f. make install

```

---

<a name="install"></a>
# Install Trick

## 1.) Clone Trick

The following commands will clone the Trick repository into a folder named *trick* in your home directory. You can install multiple copies of Trick in different locations to isolate your simulation environments from one another.

```bash
cd ${HOME}
git clone https://github.com/nasa/trick
```

## 2.) Configure Trick
Navigate to the *trick* directory you just created and run the *configure* script.

```bash
cd ${HOME}/trick
./configure
```

The *configure* script will generate makefiles and locate project dependencies automatically. It may be necessary to specify dependency paths manually. Run the following command to see the possible options *configure* will accept. If you are having trouble with this step, make sure there were not details in the OS section of this document that you missed.

```bash
./configure --help
```

## 3.) Compile Trick
Now that Trick has been configured and a makefile has been generated, we can run *make* to compile Trick. To build Trick in 32-bit mode, first set the `TRICK_FORCE_32BIT` environment variable to `1`.

```bash
make
```


## 4.) Optionally Update Your Environment
Gone are the days when you needed to set several environment variables to use Trick. Trick can now be used completely environmentlessly*. You no longer need to set `TRICK_HOME` and friends.

Trick still makes use of shell variables, but their existence is only required during simulation compilation and execution. If they are not set, Trick will infer them without polluting your environment. Furthermore, they will be available to any processes that are spawned as part of compilation or execution, so even your own tools may no longer need these variables to be manually set.

Similarly, Trick does not require its executables to be on your `PATH`, but you may find it convenient to add them if you prefer to not specify the full path to `
