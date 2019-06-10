---
layout: post
title: Getting PyTables to Play Nice with Windows
---

I originally started this as a wiki page on my fork of ViTables.  After
trying to understand why ViTables would crash on some Windows boxes but
not others, I found out that it had nothing to do with ViTables.  So,
I'll just put it here. These are primarily the notes I wrote while
digging into the problem.

**tl;dr**: Your Python installation on Windows is stupid and needs to be
reinstalled.

<!--break-->

Running Notes
-------------

So, apparently something screwy is going on with Python on Windows.
Everything seems to work just dandy fine on other systems.  Digging
around, it appears that the problem is isolated _exclusively_ in the
Anaconda distribution of Python.  More to the point, the PyTables
packaging within the Anaconda distribution.  A quick check is to run

    $ python3 -c 'import tables; tables.test()'

and see if it works.  Cygwin is just plain happy to run the tests using
the native Python in Cygwin.  Only one error related to the type of
error raised by one method.  WinPython runs to the end and doesn't even
complain once.

Using Anaconda, it runs for about 2.5 lines, but then it pops up a
window saying "python.exe has stopped working."  Opening up a debug
instance (after fighting with the community version of Visual Studio
2015) shows a trace to `netdll.dll` through `hdf5extension.pyd`.
Searching the site-package tree reveals the offending file is in the
`tables` package. `file` tells me the `.pyd` file is a DLL for Windows,
but `nm` and `objdump` don't give me any useful information.  I assume
it should be linking to the HDF5 libraries because PyTables is a simple
extension of the HDF5 file.  `grep`ing around, I find

    $ find Lib -name 'hdf5*' | grep -v '__pycache__'
    ...
    Lib/site-packages/tables/hdfExtension.py
    Lib/site-packages/tables/hdfextension.pyd

    $ find libs -name 'hdf5*' | grep -v '__pycache__'

    $ find Library -name 'hdf5*' | grep -v '__pycache__'
    Library/bin/hdf5.dll
    Library/bin/hdf5_cpp.dll
    Library/bin/hdf5_hl.dll
    ...
    Library/lib/hdf5.lib
    Library/lib/hdf5_cpp.lib
    ...

So, the libraries are there, but the runtime cannot find them.  Taking a
look at the [WinPython](http://winpython.github.io) distribution we find

    $ find Lib -name 'hdf5*' | grep -v '__pycache__'
    ...
    Lib/site-packages/tables/hdf5.dll
    Lib/site-packages/tables/hdfExtension.py
    Lib/site-packages/tables/hdfextension.pyd
    Lib/site-packages/tables/hdf5_hl.dll

    $ find libs -name 'hdf5*' | grep -v '__pycache__'

and no Library directory.  The key point is the DLLs are _next to the
files_.  This is making no sense to me.

Rooting around the internet some more, I come across [the search order
for DLLs](https://msdn.microsoft.com/en-us/library/7d83bc18.aspx).
Checking my `PATH` variable, I see that indeed
`/c/path/to/anaconda/Library/bin` is not on my path.  Thus, the current
directory approach of WinPython works out of the box.  Trying to add
this to the path didn't help on the outset

And if I go to a computer that has Anaconda installed that I know still
works, _the DLLS are installed in the `Lib/site-packages/tables`
directory_!  (I hate Windows sometimes).  I tried reinstalling Anaconda
using the 2.3.0 version available at the time of writing.  That didn't
help.

A (Hacked) Solution
-------------------

It appears like we have to do things the hard way if we want to use
Anaconda.  First, uninstall PyTables from Anaconda

    $ conda uninstall pytables

Now, we need to us `pip`

    $ pip install tables

Odds are, this will spew out a long and confusing string of error
messages.  If you see something referring to "MSC V.1600 64 bit (AMD64)"
and "Microsoft Visual C++ 10.0 is required," it means you will need to
hunt down the proper version of the version of Visual Studio.  In this
case, you want Visual Studio 2010.  Sadly, that does not appear to be a
viable option.  I can get the professional version installed from my IT
department, but I was not able to find a legitimate link from Microsoft.
I'm sure I could dig up a link from a non-Microsoft source, but that
would not be a good idea in my opinion.

A (Real) Solution
-----------------

A real solution is to just install a version of Python that stashes the
DLLs somewhere in the modules can find.  Most likely, this will be one
that installs the libraries into the `site-package/tables` directory
just like WinPython does.

