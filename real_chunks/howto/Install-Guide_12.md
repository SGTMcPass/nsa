### Install Trick > Notes > Python Version

 everything they need to run. You will still need maven on the machine where you build the Trick Java jars.

1. Pre-build your Java code on a machine with Trick dependencies, including maven and internet access.
```
# On source machine with Trick dependencies, internet, and maven
cd prebuiltTrick && ./configure && make java
```

2. Copy the Java jars to the environment that you need to build Trick on. They are nested in the libexec directory as specified below. The directory should be at the top level of Trick, called trick/trick-offline.

```
mkdir trick/trick-offline
cp prebuiltTrick/libexec/trick/java/build/*.jar trick/trick-offline
```

3. When you configure, use the flag --enable-offline.
```
./configure --enable-offline …<other flags>
```

4. Follow regular install instructions above.

### Python Version

If you would like to use Python 2 with Trick please first make sure Python 2 and the Python 2 libs are installed. Then you will likely need to set `PYTHON_VERSION=2` in your shell environment before executing the `configure` script so that Trick will use Python 2 instead of Python 3. This can be done in bash or zsh with the following commands:

```
export PYTHON_VERSION=2
./configure
```
