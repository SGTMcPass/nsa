### 🏁 Introduction > Installing Trick

 Trick architecture and
its capabilities.

---

<a id=installing-trick></a>
## Installing Trick

If Trick is not already installed on your machine, then you will need to do that
first, by following the directions at: [Install Guide](/trick/documentation/install_guide/Install-Guide).

The rest of the tutorial is written as if the Trick **bin** directory is
available on your execution path. This isn't strictly necessary, but allows
you to call `trick-CP` instead of `/full/path/to/trick/bin/trick-CP`. Follow
the steps below if you would like to add the **bin** directory to your PATH.

For the sake of example, let us assume that
you installed Trick in your home directory, and you used the default name for
the repository, which is **trick**. If you named it something different, then
use that name instead in the scripts below.

If you are using **bash or ksh**, then add the following lines to the file
that is automatically sourced by your terminal. Based on your platform this
could be **.profile, .bash_profile, .bashrc, .zshrc** or others. Google "How
to edit PATH variable" on google to find a wealth of information on this
subject.

```bash
export PATH=${PATH}:${HOME}/trick/bin
```

If you are using **csh** or **tcsh**, then add the following lines to your **.cshrc** file.

```csh
setenv PATH ${PATH}:${HOME}/trick/bin
```

Close and then re-open your terminal window.

---
[Next Page](ATutASimpleSim)
