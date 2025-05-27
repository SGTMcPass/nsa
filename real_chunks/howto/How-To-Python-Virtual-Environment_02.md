### [References](#references)

9

# The lastest version of Python
% conda create -n trick python

# The latest version of Python 3.9 and packages
% conda create -n trick python=3.9 pyyaml scipy
```


### [Creating a Conda Environment From a YAML File](#creating-a-conda-environment-from-a-yaml-file)

#### Create the file ```myenv.yml``` with following contents:

```
name: trick
channels:
    - conda-forge
    - defaults
dependencies:
    - python = 3.9
    - pyyaml
```
In this example, the environment is named ```trick``` and includes two packages: python and pyyaml.

#### Run conda command to create the new environment:

Once you have your YAML file ready, you can create your conda environment using the following command in your terminal:

```% conda env create -f myenv.yml```


### [Activating the Conda Environment](#activating-the-conda-environment)

After creating the environment, you can activate it using the following command:

```% conda activate trick```


### [Installing Packages Into a Conda Environment](#installing-packages-into-a-conda-environment)

If you're in your conda environment, you can install package(s) using the following command:

``` (trick) % conda install numpy scipy```


If you're NOT in your conda environment, you can install package(s) into a specified environment using the following command:

``` % conda install -n trick numpy scipy```


### [Deactivating an Active Conda Environment](#deactivating-an-active-conda-environment)

If you're in your conda environment, you can deactivate it using the following command:

```(trick) % conda deactivate```


### [Removing a Conda Environment](#removing-a-conda-environment)

You can remove a conda environment from your terminal using the following command:

``` % conda remove -n trick --all```

or

``` % conda env remove -n trick```

To verify that the environment was removed, run following from your terminal:

``` % conda info --envs```

The removed environment should not be shown.



# [References](#references)

* [RealPython Tutorial - Python Virtual Environment: A Primer](https://realpython.com/python-virtual-environments-a-primer/)
* [Conda Document - Managing environments](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
* [Creating an environment in Anaconda through a yml file](https://sachinjose31.medium.com/creating-an-environment-in-anaconda-through-a-yml-file-7e5deeb7676d)
