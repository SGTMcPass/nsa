### The API

 handy little function called `close` that takes care of everything for you. All you have to do is remember to call it when you're done. I know, I know, I hate having to remember to call close functions too. They're unassuming, not particularly interesting, and easy to forget about. But there's no way around it, so do your best. In truth, the world won't come crashing down around you if you do forget. You probably won't even notice a difference unless you're leaking hundreds of `VariableServer` instances, in which case you're probably _trying_ to break everything. But call it anyway, ok?

```python
from variable_server import VariableServer
variable_server = VariableServer('localhost', 7000)
# I'm using variable_server here.
# Getting values.
# Setting units.
# Doing other stuff.
# Ok, I'm done.
variable_server.close()  # don't forget to call close!
```

## Or Use a Context Manager
Wait a tick! Python has the concept of context managers, which support automatic finalization within a limited scope. This is perfect if you only need to create an instance for a single block of code. However, it doesn't work if the use is spread over multiple scopes (many different methods sharing the same instance, for example), so you'll have to decide what works best for you.

```python
from variable_server import VariableServer
with VariableServer('localhost', 7000) as variable_server:
    # Hmmm, this syntax is a little strange, but I'll go with it.
    # Actually, the more I look at it, the more I like it.
    # Python is pretty cool!
