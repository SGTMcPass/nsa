### Install Trick > Notes > Python Version

 environment, you need to manually build Clang and LLVM. Following instructions show steps on building a particular release of Clang and LLVM . `cmake` is required. CMake may support multiple native build systmes on certain platforms. A generator is responsible for generating a particular build system. Below lists two approaches for your reference. The first approach uses `Unix Makefiles` (one of Makefile generators) and the second one uses `Ninja` (one of Ninja generators). For Mac Apple Silicon user, may want to go to the second approach directly.

Note: Remember to add `--with-llvm=<clang+llvm-17_path>` for Trick configure if using the Clang and LLVM built in this section.

1. Using `Unix Makefiles` generator

```bash
  # Go to a folder to checkout LLVM project
  a. cd <a_folder>

  # Clone a particular project version
  b. git clone -b llvmorg-17.0.6 https://github.com/llvm/llvm-project.git

  c. cd llvm-project

  e. mkdir build

  f. cmake -S llvm -B build -G "Unix Makefiles" -DLLVM_ENABLE_PROJECTS="clang" -DLLVM_ENABLE_RUNTIMES="libcxx;libcxxabi" -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=<clang+llvm-17_path>

  # Be patient, this step takes a bit time ...
  g. cmake --build build

  h. cd build

  # Install
  i. cmake -DCMAKE_INSTALL_PREFIX=<clang+llvm-17_path> -P cmake_install.cmake


```

2. Using `Ninja` generator

```bash
  a. brew install ninja

  b. cd <a_folder>

  c. git clone -b llvmorg-17.0.6 https://github.com/llvm/llvm-project.git

  d. cd llvm-project

  e. mkdir build

  # Apple Silicon
  g cmake -S llvm -B build -G Ninja -DLLVM_ENABLE_PROJECTS=clang -DCMAKE_BUILD_TYPE=Release -DLLVM_TARGETS_TO_BUILD=AArch64 -DCMAKE_INSTALL_PREFIX=<clang+llvm-17-arm64_path>

  # Intel-based
  g. cmake -S llvm -B build -G Ninja -DLLVM_ENABLE_PROJECTS=clang -DLLVM_ENABLE_RUNTIMES="libcxx;libcxxabi" -DCMAKE_BUILD_TYPE=Release -DLLVM_TARGETS_TO_BUILD=X86 -DCMAKE_INSTALL_PREFIX=<clang+llvm-17-x86_path>

  # Build and install
  h. cmake --build build --target install

```

---

<a name="build_swig"></a>
### Build SWIG

```bash
  a. Download the desired source code version from https://github.com/swig/swig/tags
