### Interface Code Generator - ICG > Checksumming

 that directory or a library.

Makefile options may be found by typing in:

```
UNIX prompt> make help
```

Additional documentation for make can be found in UNIX manuals for your workstation.

### Viewing Parameters In SIE Database

Sometimes you are trying to remember the name of a parameter.... "Ummm. Let's see.
It's errr.  Uhhh.  clock something..."  Try running this in your built simulation
directory where the S_sie.resource file is located.

```
UNIX prompt> sie [-nocase] <search string>
```

As an example, if you know the parameter name contains clock but don't know
anything else, try:

```
UNIX prompt> sie clock
```

The search returns each %Trick processed variable (including Trick's "sys" variables)
from your simulation that contains the search string. Beneath each variable returned
is information from its header file definition: user supplied description, type,
input/output spec, and units spec.

For a case-insensitive search (e.g., to find occurrences of "clock" and "Clock"),
simply specify the -nocase option.

## kill_sim

The following command will kill all simulations and their children that you own.

```
UNIX prompt> kill_sim
```

## Current Trick Version

The following command echoes the installed %Trick version release:

```
UNIX prompt> trick_version
```

## Checksumming

Trick comes with a file that contains checksums for the %Trick package. You may run:

```
UNIX prompt> trick_verify_checksums
```

at any time to see what, if any, files have changed from the original package. The checksum is
done
