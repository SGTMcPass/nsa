### Install Trick > Notes > Python Version

8"></a>

### RedHat Enterprise Linux (RHEL) 8, Oracle Linux 8, Rocky Linux 8, AlmaLinux 8
Trick requires the clang/llvm compiler to compile and link the Trick Interface Code Generator.  clang/llvm is available through the [Extra Packages for Enterprise Linux](https://fedoraproject.org/wiki/EPEL) repository.  Download and install the 'epel-release' package.


```bash
dnf install epel-release
dnf update
dnf install -y bison clang flex git llvm make maven swig cmake clang-devel \
gcc gcc-c++ java-11-openjdk-devel libxml2-devel llvm-devel llvm-static \
ncurses-devel openmotif openmotif-devel perl perl-Digest-MD5 udunits2 \
udunits2-devel which zlib-devel gtest-devel libX11-devel libXt-devel  \
python3-devel diffutils
```



Trick makes use of several optional packages if they are present on the system.  These include using the HDF5 package for logging, the GSL packages for random number generation, and google test (gtest) for Trick's unit testing.  These are available from the EPEL repository. In order to access gtest-devel in the epel repository on RHEL 8 you need to enable the dnf repo CodeReady Linux Builder. In Rocky Linux and Alma Linux you can instead enable the Power Tools Repo. On Oracle Linux 8 you must enable OL8 CodeReady Builder.

See RedHat's documentation to enable the CodeReady Linux Builder repository:
https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/package_manifest/codereadylinuxbuilder-repository

On AlmaLinux 8, Rocky Linux 8:
```bash
dnf config-manager --enable powertools
  dnf install -y gtest-devel
```

On Oracle Linux 8:
```
dnf config-manager --enable ol8_codeready_builder
dnf install -y gtest-devel
```

proceed to [Install Trick](#install) section of the install guide

---
<a name="redhat7"></a>

### RedHat Enterprise Linux (RHEL) 7, CentOS 7
Trick requires the clang/llvm compiler to compile and link the Trick Interface Code Generator.  clang/llvm is available through the [Extra Packages for Enterprise Linux](https://fedoraproject.org/wiki/EPEL) repository.  Download and install the 'epel-release' package.

```bash
# install epel-release
Run yum -y install epel-release && yum -y update

```

Trick also requires development packages from the base and epel repositories

```bash
yum install -y bison clang flex git llvm make maven swig3 cmake clang-devel \
gcc gcc-c++ java-11-openjdk-devel libxml2-devel llvm-devel llvm-static
