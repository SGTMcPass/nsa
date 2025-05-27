### TrickOps > More Information

 any given time. The terminal window will accept scroll wheel and arrow input to view current builds/runs that are longer than the terminal height. Before the script finishes, it reports a summary of what was done, providing a list of which sims and runs were successful and which were not.

Looking inside the script, the code at top of the script creates a yaml file containing a large portion of the sims and runs that ship with trick and writes it to `/tmp/config.yml`. This config file is then used as input to the `TrickWorkflow` framework.  At the bottom of the script is where the magic happens, this is where the TrickOps modules are used:

```python
from TrickWorkflow import *
class ExampleWorkflow(TrickWorkflow):
    def __init__( self, quiet, trick_top_level='/tmp/trick'):
        # Real projects already have trick somewhere, but for this example, just clone & build it
        if not os.path.exists(trick_top_level):
          os.system('cd %s && git clone https://github.com/nasa/trick' % (os.path.dirname(trick_top_level)))
        if not os.path.exists(os.path.join(trick_top_level, 'lib64/libtrick.a')):
          os.system('cd %s && ./configure && make' % (trick_top_level))
        # Base Class initialize, this creates internal management structures
        TrickWorkflow.__init__(self, project_top_level=trick_top_level, log_dir='/tmp/',
            trick_dir=trick_top_level, config_file="/tmp/config.yml", cpus=3, quiet=quiet)
    def run( self):
      build_jobs      = self.get_jobs(kind='build')
      run_jobs
