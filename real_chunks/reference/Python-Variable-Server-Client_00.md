### The API

| [Home](/trick) → [Documentation Home](../Documentation-Home) → [Miscellaneous Trick Tools](Miscellaneous-Trick-Tools) → Python Variable Server Client |
|------------------------------------------------------------------|


`variable_server.py` is a Python module for communicating with a sim's variable server from a Python program. Its primary purpose is to easily get and set variable values and units, but it also includes some additional convenience methods for affecting the sim's state. The code itself is well-commented, so I won't be reproducing the API here. Run `pydoc variable_server` (in the containing directory) for that.

# Release Your Resources!
First things first. Communicating
 with the variable server means opening sockets. Sockets are a resource. Threads are also a resource, and this module uses them as well. The OS gets angry when you leak resources, so you should do your best to dispose of them when you're done. Python doesn't support RAII well, and `__del__` [isn't a good place to free resources](https://stackoverflow.com/a/6104568), so I'm afraid I couldn't automatically clean up after you. You're going to have to be explicit about it, which [Python style](https://www.python.org/dev/peps/pep-0020/) prefers anyway.

## Call Close when You're Done
So how do we release this module's resources? I've provided a handy little function called `close` that takes care of everything for you. All you have to do is remember to call it when you're done. I know, I know, I hate having to remember to call close functions too. They're unassuming,
