### [References](#references)

 command prompt.

### [Installing Python Modules Into Your Virtual Environment](#installing-python-modules-into-your-virtual-environment)

Use the following command to install Python modules into the virtual environment:

```
(myVenv) % python3 -m pip install <package-name>
```

For example, the Trick test suite, which uses TrickOps which requires PyYAML.
This Python module would be installed as follows:

```
(myVenv) % python3 -m pip install PyYAML
```

Every time ```myVenv``` is activated, the PyYAML module will be available.


### [Deactivating the venv Shell](#deactivating-the-venv-shell)
To deactivate the venv shell, execute the following:

```(myVenv) % deactivate```


The above should get you going. If you need more details, the following tutorial is pretty good.
[RealPython Tutorial](https://realpython.com/python-virtual-environments-a-primer/).



## [Using Conda](#using-conda)

Conda is a powerful package manager and environment manager that you use with command line commands at the Anaconda Prompt for Windows, or in a terminal window for macOS or Linux.

You can obtain conda by installing [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/) or [Anaconda](https://docs.anaconda.com/free/anacondaorg/).

Miniconda a small bootstrap version of Anaconda that includes only conda, Python, the packages they both depend on, and a small number of other useful packages (like pip, zlib, and a few others).

Anaconda is a downloadable, free, open-source, high-performance, and optimized Python and R distribution. It includes conda, conda-build, Python, and 250+ automatically installed, open-source scientific packages and their dependencies that have been tested to work well together, including SciPy, NumPy, and many others.



### [Creating a Conda Environment with Commands](#creating-a-conda-environment-with-commands)

#### Create a conda virtial environment with Python by running one of following conda commands from a terminal:

```
# A specific version of Python
% conda create --name trick python=3.9.18
or
% conda create -n trick python=3.9.18

# The latest version of Python 3.9
% conda create -n trick python=3.9

# The lastest version of Python
% conda create -n trick python

# The latest version of Python 3.9 and packages
% conda create -n trick python=3.9 pyyaml scipy
```


### [Creating a Conda Environment From a YAML File](#creating-a-conda-environment-from-a-yaml-file)

#### Create the file ```myenv.yml``` with following contents:

``
