### Install Trick > Notes > Python Version

| [Home](/trick/index) → Install Guide |
|------------------------------|

# Introduction
This document will walk you through the process of installing Trick on your computer. Please read each section carefully.

# Package Dependencies
Trick requires various free third party utilities in order to function. All the following products are used by Trick and may already be installed as part of your OS distribution. **Install any missing dependencies with your operating system's [package manager](https://en.wikipedia.org/wiki/Package_manager).** For most operating systems, the default version of a dependency will be compatitable with Trick. **We strongly recommend that you use your package manager's default versions if they meet Trick's requirements.** Please check the specific OS instructions below for your operating system for more details.

| Utility        | Version | Description             | Usage                                                     | Notes                                                 |
|---------------:|:-------:|:-----------------------:|:---------------------------------------------------------:|:------------------------------------------------------|
| [gcc] and `g++` | 4.8+    | C/C++ Compiler          | Compiles Trick and Trick simulations.                     |                                                        |
| [clang]/[llvm] | <=18    | C/C++ Compiler          | Utilized by the interface code generator.                 | Trick Versions <= 19.3 should use LLVM <= 9. Please open an issue if you encounter a problem related to newer versions of LLVM.        |
| [python]       | 2.7+    | Programming Language    | Lets the user interact with a simulation.                 | Trick has been tested up to python 3.12 as of 05/2024.  |
| [perl]         | 5.6+    | Programming Language    | Allows executable scripts in the bin directory to run.    |                                                        |
| [java]         | 11+     | Programming Language    | Necessary for Trick GUIs.                                 |                                                        |
| [swig]         | 3.x-4.x | Language Interfacing    | Connects the python input processor with Trick's C code.  | 3.0+ is now required for Trick. SWIG 4.x is compatible with Trick, but has some [issues](https://github.com/nasa/trick/issues/1288). Please open an issue if you encounter a problem related to SWIG 4. |
| [make]         | 3.78+   | Build Automation        | Automates the building and cleaning of Trick.             |                                                        |
| [openmotif]    | 2.2.0+  | GUI Toolkit             | Covers Trick GUIs not made with Java.                     |                                                        |
| [udunits]      | 2.x+    | C Unit Library/Database | Provides support for units of physical quantities.        |                                                        |
| [maven]        | x.x     | Java package manager    | Downloads Java dependencies and builds Trick GUI
