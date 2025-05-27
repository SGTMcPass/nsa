### [References](#references)

# HOWTO Setup a Python Virtual Environment


- [Using the Built-in venu Module in Python3](#using-the-built-in-venv-module-in-python-3)
  * [Creating a Virtual Environment](#creating-a-virtual-environment)
  * [Activating the Virtual Environment](#activating-the-virtual-environment)
  * [Installing Python Modules Into Your Virtual Environment](#installing-python-modules-into-your-virtual-environment)
  * [Deactivating the venv Shell](#deactivating-the-venv-shell)
- [Using Conda](#using-conda)
  * [Creating a Conda Environment with Commands](#creating-a-conda-environment-with-commands)
  * [Creating a Conda Environment From a YAML File](#creating-a-conda-environment-from-a-yaml-file)
  * [Activating the Conda Environment](#activating-the-conda-environment)
  * [Installing Packages Into a Conda Environment](#installing-packages-into-a-conda-environment)
  * [Deactivating an Active Conda Environment](#deactivating-an-active-conda-environment)
  * [Removing a Conda Environment](#removing-a-conda-environment)

- [References](#references)


<!-- toc -->

## [Using the Built-in venv Module in Python 3](#using-the-built-in-venv-module-in-python-3)

### [Creating a Virtual Environment](#creating-a-virtual-environment)

The following command creates a virtual Python environment:

```% python3 -m venv <path-of-virtual-environment>```

This command runs the ```venv``` module, to create a virtual environment. The
directory specified by ```<path-of-virtual-environment>``` is created to store
the resources of the environment. It contains scripts to activate, deactivate,
and otherwise configure the environment. It also provides a place to install Python
modules for that particular environment. One can create multiple virtual environments,
each with different resources.

For example, the following will create a Python virtual environment called ```myVenv```
in your home directory.

```% python3 -m venv ~/myVenv```

### [Activating the Virtual Environment](#activating-the-virtual-environment)

To activate the virtual environment, execute the following:

```
% source myVenv/bin/activate
```

Note that the name of virtual environment is added to the command prompt.

### [Installing Python Modules Into Your Virtual Environment](#installing-python-modules-into-your-virtual-environment)

Use the following command to install Python modules into the virtual environment:

```
(myVenv) % python3 -m pip install <package-name>
```

For example, the Trick test suite, which uses TrickOps which requires PyYAML.
This Python module would be installed as follows:

```
(myVenv
