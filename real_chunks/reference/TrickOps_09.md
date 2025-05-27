### TrickOps > More Information

`
The required parameters are described as follows:
* `project_top_level` is the absolute path to the highest-level directory of your project.  The "top level" is up to the user to define, but usually this is the top level of your repository and at minimum must be a directory from which all sims, runs, and other files used in your testing are recursively reachable.
* `log_dir` is a path to a user-chosen directory where all logging for all tests will go. This path will be created for you if it doesn't already exist.
* `trick_dir` is an absolute path to the top level directory for the instance of trick used for your project. For projects that use trick as a `git` `submodule`, this is usually `<project_top_level>/trick`
* `config_file` is the path to a YAML config file describing the sims, runs, etc. for your project. It's recommended this file be tracked in your SCM tool but that is not required. More information on the syntax expected in this file in the **The YAML File** section above.

The optional parameters are described as follows:
* `cpus` tells the framework how many CPUs to use on sim builds. This translates directly to `MAKEFLAGS` and is separate from the maximum number of simultaneous sim builds.
* `quiet` tells the framework to suppress progress bars and other verbose output. It's a good idea to use `quiet=True` if your scripts are going to be run in a continuous integration (CI) testing framework such as GitHub Actions, GitLab CI, or Jenkins, because it suppresses all `curses` logic during job execution which itself expects `stdin` to exist.

When `
