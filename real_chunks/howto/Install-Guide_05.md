### Install Trick > Notes > Python Version

 libx11-dev libxml2-dev libxt-dev libmotif-common libmotif-dev \
python3-dev zlib1g-dev llvm-dev libclang-dev libudunits2-dev \
libgtest-dev default-jdk zip

# On some versions of Ubuntu (18.04 as of 04/2021), there may be multiple installations of python.
# Our new python3-dev will be linked to python3 and python3-config in your bin.
# To help trick find this instead of python2.7, we set an environment variable in our shell before calling configure:
export PYTHON_VERSION=3
```

Note: If you need to use a specific JDK version, such as `openjdk-11-jdk`, you can replace `default-jdk` with `openjdk-11-jdk` under install packages as shown above. However, you need to check where the `java` and `javac` commands are located. For instance, Ubuntu 24 typically sets up JRE (21) headless by default, so the `java` (version 21 headless) command might be located in `/usr/bin`. When you install `openjdk-11-jdk`, both `java` (version 11) and `javac` (version 11) might be placed in `/usr/lib/jvm/java-11-openjdk-amd64/bin`, with only `javac` potentially also in `/usr/bin`. Consequently, running a Java GUI with the default PATH might use JRE 21 headless instead of JRE 11, even though you’re using JDK 11 for compiling, which may not be the desired configuration. Placing `/usr/lib/jvm/java-11-openjdk-amd64/bin` before `/usr/bin` in your PATH ensures that only JDK 11 is used.

proceed to [Install Trick](#install) section of the install guide

---

<a name="macos"></a>
### macOS Sonoma, Ventura, Monterey, Big Sur, Catalina
#### These instructions are for both Intel-based and Apple Silicon Macs. Some are only applicable to Apple Silicon.

1. Install the latest Xcode. we recommend installing Xcode through the App Store.


2. Download and install Xcode Command Line Tools for macOS. The following command in the terminal should do the job:

```bash
xcode-select --install
```

3. Install Homebrew, macOS's unofficial package manager. They typically have a single line that can be executed in your terminal to install brew at their homepage at https://brew.sh/. By default, it is installed into `/usr/local` on Intel-based machines and `/opt/homebrew` on Apple Silicon.


4. Install the following dependencies using brew (See step 5 if `brew install llvm` doesn't work for your Trick build).

```bash
brew install python java xquartz swig maven udunits openmotif llvm

```
