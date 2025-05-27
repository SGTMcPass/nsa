### Install Trick > Notes > Python Version

fedora)|
|[Ubuntu](#ubuntu)|
|[macOS](#macos)|
|[Apple Silicon Mac](#apple_silicon_mac)|
|[Windows 10 (Linux Subsystem Only)](#windows10)|
|[Build Clang and LLVM](#build-clang-and-llvm)|
|[Build SWIG](#build-swig)|
|[Troubleshooting](#trouble)|

---
<a name="trouble"></a>
### Troubleshooting

#### Environment Variables
Sometimes environment variables affect the Trick build and can cause it to fail. If you find one that isn't listed here, please create an issue and we'll add it to the list.


```
JAVA_HOME # Trick and Maven will use JAVA_HOME to build the GUIs instead of Javac in PATH if it is set.
TRICK_HOME # This variable is optional but may cause a Trick build to fail if it is set to the wrong directory.
CFLAGS, CXXFLAGS, LDFLAGS # If these flags are set they may affect flags passed to your compiler and linker
```
#### If You Think The Install Instructions Do Not Work Or Are Outdated
If the Trick tests are passing, you can see *exactly* how we configure our test machines on Github's test integration platform, Github Actions.

If logged into any github account on github.com, you can access the [Actions](https://github.com/nasa/trick/actions) tab on the Trick repo page. Go to [Trick-CI](https://github.com/nasa/trick/actions?query=workflow%3A%22Trick+CI%22), and click the latest passing run. Here you can access a log of our shell commands to configure each OS with dependencies and also the commands we use to install Trick. In fact, that is exactly where I go when I want to update the install guide! @spfennell

The configuration for these tests can be found in the [trick/.github/workflow/test_linux.yml](https://github.com/nasa/trick/blob/master/.github/workflows/test_linux.yml) file.

#### Weird Linker Error
It is possible you may have an old version of Trick installed, and Trick's libraries are on your LDPATH and interfering with your new build. The solution is to uninstall the old version before building the new one. Call `sudo make uninstall` from any Trick top level directory and it will remove the old libraries.

---
<a name="redhat8"></a>

### RedHat Enterprise Linux (RHEL) 8, Oracle Linux 8, Rocky Linux 8, AlmaLinux 8
Trick requires the clang/llvm compiler to compile and link the Trick Interface Code Generator.  clang/llvm is available through the [Extra Packages for Enterprise Linux](https://fedoraproject.org/wiki/EPEL) repository.  Download and install the 'epel-release' package.
