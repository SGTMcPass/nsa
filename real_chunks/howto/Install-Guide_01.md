### Install Trick > Notes > Python Version

                                                        |
| [openmotif]    | 2.2.0+  | GUI Toolkit             | Covers Trick GUIs not made with Java.                     |                                                        |
| [udunits]      | 2.x+    | C Unit Library/Database | Provides support for units of physical quantities.        |                                                        |
| [maven]        | x.x     | Java package manager    | Downloads Java dependencies and builds Trick GUIs.         |                                                        |

[gcc]: https://gcc.gnu.org/
[clang]: https://clang.llvm.org/
[llvm]: https://llvm.org/
[python]: https://www.python.org/
[perl]: https://www.perl.org/
[java]: https://www.java.com/
[swig]: http://www.swig.org/
[make]: https://www.gnu.org/software/make/
[openmotif]: http://www.opengroup.org/openmotif/
[udunits]: https://www.unidata.ucar.edu/software/udunits/
[maven]: https://maven.apache.org/

## Notes
### Clang/LLVM compiler and libraries
Clang/LLVM can be installed and located manually should your package manager fail to acquire it. You can tell Trick where to find Clang/LLVM with the `"--with-llvm"` configuration option specified. If the version of Clang/LLVM installed by your package manager doesn't work, see [Build Clang and LLVM](#build-clang-and-llvm).


### Java
Trick needs the `javac` compiler included in the Java Development Kit (JDK). Trick will work with either the Oracle JDK or OpenJDK.


**Installing both the Oracle JDK and OpenJDK may lead to problems and confusion.**

# Operating Systems
Trick runs on GNU/Linux and macOS, though any System V/POSIX compatible UNIX workstation should accept the Trick software with very little source code porting. Below are instructions for installing the prerequisites on popular operating systems here at NASA.

| Quick Jump Menu |
|---|
|[RedHat Enterprise Linux (RHEL) 8](#redhat8)|
|[Oracle Linux 8](#redhat8)|
|[AlmaLinux 8](#redhat8)|
|[Rocky Linux 8](#redhat8)|
|[RedHat Enterprise Linux (RHEL) 7](#redhat7)|
|[CentOS 7](#redhat7)|
|[Fedora](#fedora)|
|[Ubuntu](#ubuntu)|
|[macOS](#macos)|
|[Apple Silicon Mac](#apple_silicon_mac)|
|[Windows 10 (Linux Subsystem Only)](#windows10)|
|[Build Clang and LLVM](#build-clang-and-llvm)|
|[Build SWIG](#build-swig)|
|[Troubleshooting](#trouble)|

---
<a name="tr
