### Install Trick > Notes > Python Version

 your terminal to install brew at their homepage at https://brew.sh/. By default, it is installed into `/usr/local` on Intel-based machines and `/opt/homebrew` on Apple Silicon.


4. Install the following dependencies using brew (See step 5 if `brew install llvm` doesn't work for your Trick build).

```bash
brew install python java xquartz swig maven udunits openmotif llvm

```
IMPORTANT: Make sure to follow the instructions for adding Java and SWIG to your `PATH` provided by brew. If you missed them, you can see them again by using `brew info java` and `brew info swig`. Remember,  you may need to restart your terminal for these `PATH` changes to take effect. Note `brew install swig` will install the latest version. If a particular SWIG version is needed instead, see [Build SWIG](#build-swig).


5. Skip this step if `brew install llvm` works for your Trick build. Otherwise, download and un-compress a pre-built clang+llvm from llvm-project github. Go to https://github.com/llvm/llvm-project/releases and download the available version llvm from the release assets for your platform.
```
  For example, the latest as of the writing of this guide:
    1. Intel-based: https://github.com/llvm/llvm-project/releases/download/llvmorg-15.0.7/clang+llvm-15.0.7-x86_64-apple-darwin21.0.tar.xz
    2. Apple Silicon: https://github.com/llvm/llvm-project/releases/download/llvmorg-17.0.6/clang+llvm-17.0.6-arm64-apple-darwin22.0.tar.xz
```
Tip: We suggest renaming the untar'd directory to something simple like llvm15 and putting it in your home directory or development environment. If a pre-built clang+llvm for your platform is not available, see [Build Clang and LLVM](#build-clang-and-llvm).

6. Read the following macOS optional steps/caveats and then go to the Install Trick section of this document.

IMPORTANT: Your mac might complain during configuration or build that llvm is downloaded from the internet and can not be trusted. You may need to find a safe solution for this on your own. DO THIS AT YOUR OWN RISK: What worked for us was enabling Settings->Security & Privacy->Privacy->Developer Tools->Terminal.

IMPORTANT: when doing the configure step in the [Install Trick](#install) section, you need to point Trick to `llvm`. It is also possible that the current iteration of our configure script will not be able to find the udunits package, so you may need to point Trick to udunits as well (This is only an issue on M1 macs).
You can find the path
