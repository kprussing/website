---
layout: post
title: Starting X  Under Cygwin
---

This is just a quick note to myself so I can delete it from my desktop.
After installing the [X server from Cygwin][see], the server can be
launched using

    $ XWin -multiwindow -clipboard -silent-dup-err

to let Windows handle the windowing.  To launch X at log in, use
`/bin/run`.  This boils down to creating a shortcut and setting the
target to 

    C:\Programs\CygWin\bin\run.exe XWin -multiwindow -clipboard -silent-dup-error

Then, place the short cut in the start up directory.

[see]: http://x.cygwin.com/docs/ug/setup.html

