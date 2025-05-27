### TrickOps > More Information

like `matlab`) that complicates everything!"
    - Solution: Project specific script runs `execute_jobs()` on custom `Job`s before normal sim builds are executed


## Tips & Best Practices

* Commit your YAML file to your project. What gets tested will change over time, you want to track those changes.
* If your project requires an environment, it's usually a good idea to track a source-able environment file that users can execute in their shell. For example, if `myproject/.bashrc` contains your project environment, you should add `source .bashrc ;` to the `env:` section of `globals` in your YAML config file. This tells `TrickWorkflow` to add `source .bashrc ; ` before every `Job()`'s `command`.
* Make sure you execute your tests in an order that makes sense logically. The TrickOps framework will not automatically execute a sim build before a sim run for example, it's on the user to define the order in which tests run and which tests are important to them.
* Be cognizant of how many CPUs you've passed into `TricKWorkflow.__init__` and how many sims you build at once. Each sim build will use the `cpus` given to `TrickWorkflow.__init__`, so if you are building 3 sims at once each with 3 cpus you're technically requesting 9 cpus worth of build, so to speak.
* If `TrickWorkflow` encounters non-fatal errors while verifying the content of the given YAML config file, it will add those errors to the internal `self.config_errors` list of strings. If you want your script to return non-zero on any
