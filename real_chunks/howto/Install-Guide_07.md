### Install Trick > Notes > Python Version

 & Privacy->Privacy->Developer Tools->Terminal.

IMPORTANT: when doing the configure step in the [Install Trick](#install) section, you need to point Trick to `llvm`. It is also possible that the current iteration of our configure script will not be able to find the udunits package, so you may need to point Trick to udunits as well (This is only an issue on M1 macs).
You can find the path of udunits by executing the following command:

```bash
brew info udunits
```
Then enter the path to llvm (and udunits) when you execute the configure command in place of the placeholders:
```bash
./configure --with-llvm=<path to llvm> --with-udunits=<path to udunits> <other configure flags (if any)>
```
e.g.
```bash
# For Apple Silicon Macs, you may need to configure as following if Trick configure can't find packages:
./configure --with-llvm=/opt/homebrew/opt/llvm --with-udunits=/opt/homebrew --with-hdf5==/opt/homebrew
```


OPTIONAL: To install gtest for Trick unit testing:

`brew install googletest`

For your reference, a particular googletest release can be installed as following:

```
brew install cmake wget
wget https://github.com/google/googletest/archive/release-1.8.0.tar.gz
tar xzvf release-1.8.0.tar.gz
cd googletest-release-1.8.0/googletest
cmake .
make
make install
```

proceed to [Install Trick](#install) section of the install guide

---

<a name="apple_silicon_mac"></a>
### Apple Silicon Mac
### The following is obtained from user notes for fresh Trick installation on macOS Sonoma for your reference. Thanks to Zack Crues!

```bash
1. Install Xcode
   a. Install the Xcode development tools from the Apple App Store.
   b. Install command line tools. (xcode-select --install)

2. Install Homebrew
   a. Install the Homebrew package manager (https://brew.sh)
   b. brew install swig maven udunits openmotif llvm
   c. brew install cmake
   d. Optional: brew install gsl hdf5 googletest

3. Install XQuartz.
   a. Option 1: brew install xquartz
   b. Option 2: Get XQuartz from www.quartz.org

4. Install Java from Self Service.
   a. Option 1: brew install java
   b. Option 2: Get Java from the NASA Self Service app.

5. Setup environment

   setenv PYTHON_VERSION 3
   setenv TRICK_CXXFLAGS "-g -I/opt/homebrew/include -L/opt/homebrew/lib -Wno-unused
