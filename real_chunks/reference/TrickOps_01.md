### TrickOps > More Information

 the question "have I broken anything?".  The purpose of TrickOps is to provide the logic central to managing these tests while allowing each project to define how and and what they wish to test. Don't reinvent the wheel, use TrickOps!

TrickOps is *not* a GUI, it's a set of python modules that you can `import` that let you build a testing framework for your Trick-based project with just a few lines of python code.

## Requirements

`python` version 3.X and the packages in `requirements.txt` are required to use TrickOps. Virtual environments make this easy, see [the python documentation on virtual environments](https://docs.python.org/3/library/venv.html) for information on how to create a `python3` virtual environment using the `requirements.txt` file included here.

## Features

TrickOps provides the following features:
  1. Multiple simultaneous sim builds, runs (with or without valgrind), logged data file comparisons, and post-run analyses
  2. Automatic project environment file sourcing
  3. Real-time progress bars for sim builds and runs with in-terminal curses interface
  4. Exit code management lets users easily define success & failure criteria
  5. Failed comparisons can optionally generate koviz error reports
  6. Sims, their runs, comparisons, etc. are defined in a single easy-to-read YAML file which TrickOps reads

## The YAML File

The YAML file is a required input to the framework which defines all of the tests your project cares about. This is literally a list of sims, each of which may contain runs, each run may contain comparisons and post-run analyses and so
