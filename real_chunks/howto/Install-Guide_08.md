### Install Trick > Notes > Python Version

 b. Option 2: Get XQuartz from www.quartz.org

4. Install Java from Self Service.
   a. Option 1: brew install java
   b. Option 2: Get Java from the NASA Self Service app.

5. Setup environment

   setenv PYTHON_VERSION 3
   setenv TRICK_CXXFLAGS "-g -I/opt/homebrew/include -L/opt/homebrew/lib -Wno-unused-command-line-argument"
   setenv TRICK_CFLAGS "-g -I/opt/homebrew/include -L/opt/homebrew/lib -Wno-unused-command-line-argument"
   setenv TRICK_LDFLAGS "-L/opt/homebrew/lib"
   setenv TRICK_EXCLUDE "/opt/homebrew"

6. Build Trick
   a. Follow the direction in the Trick installation documentation for Mac.
   b. I add in support for GSL, HDF5, and Google Test.

./configure --with-llvm=/opt/homebrew/opt/llvm --with-udunits=/opt/homebrew/opt/udunits --with-gsl=/opt/homebrew --with-hdf5=/opt/homebrew --with-gtest=/opt/homebrew PYTHON_VERSION=3
```

proceed to [Install Trick](#install) section of the install guide

---

<a name="windows10"></a>
### Windows 10 (Linux Subsystem Only)

1.  Set up the Windows Subsystem for Linux by following the Microsoft Install Guide:
(link current as of September 2020)
https://docs.microsoft.com/en-us/windows/wsl/install-win10

2. Install the Ubuntu dependencies from above on the WSL: [Ubuntu](#ubuntu)

3. Install an X-windows server like [Xming.](https://sourceforge.net/projects/xming/?source=typ_redirect)

4. Ensure hostname resolves to an address.
```bash
# Get name of machine
hostname
# Get IP of name
hostname -i
# If hostname -i returns an error find IP address
ifconfig
# Add an entry to /etc/hosts to associate IP address to hostname "numeric.ip.address hostname"
sudo <edit_cmd> /etc/hosts
```

proceed to [Install Trick](#install) section of the install guide

---


<a name="manual_build_clang_llvm"></a>
### Build Clang and LLVM
If you come to this section because Clang+LLVM installed by the package manager on your machine does not work for your environment, you need to manually build Clang and LLVM. Following instructions show steps on building a particular release of Clang and LLVM . `cmake` is required. CMake may support multiple native build systmes on certain platforms. A generator is responsible for generating a particular build system. Below lists two approaches for your reference. The first approach uses `Unix Makefiles` (one of Makefile generators) and the second one uses `Ninja
