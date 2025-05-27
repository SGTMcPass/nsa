### TrickOps > More Information

 purposes.

```python
from TrickWorkflow import *
class ExampleWorkflow(TrickWorkflow):
    def __init__( self, quiet, trick_top_level='/tmp/trick'):
        # Real projects already have trick somewhere, but for this example, just clone & build it
        if not os.path.exists(trick_top_level):
          os.system('cd %s && git clone https://github.com/nasa/trick' % (os.path.dirname(trick_top_level)))
        if not os.path.exists(os.path.join(trick_top_level, 'lib64/libtrick.a')):
          os.system('cd %s && ./configure && make' % (trick_top_level))
```
Our new class `ExampleWorkflow.py` can be initialized however we wish as long as it provides the necessary arguments to it's Base class initializer. In this example, `__init__` takes two parameters: `trick_top_level`  which defaults to `/tmp/trick`, and `quiet` which will be `False` unless `quiet` is found in the command-line args to this script. The magic happens on the very next line where we call the base-class `TrickWorkflow` initializer which accepts four required parameters:

```python
        TrickWorkflow.__init__(self, project_top_level=trick_top_level, log_dir='/tmp/',
            trick_dir=trick_top_level, config_file="/tmp/config.yml", cpus=3, quiet=quiet)
```
The required parameters are described as follows:
* `project_top_level` is the absolute path to the highest-level directory of your project.  The "top level" is up to the user to define, but usually this is the top level of your repository
