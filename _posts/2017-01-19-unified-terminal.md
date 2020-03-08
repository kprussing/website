---
layout: post
title: Unified Command Line in Windows
---

Some working notes on getting a unified terminal experience on Windows.
The ultimate problem is every tool set for Windows wants to install a
complete GNU environment and doesn't bother checking if you already have
one installed.  The ultimate kicker is: you basically can't do it.

<!--break-->

Have you ever tried to install some command line tool for Windows and
noticed that every single one wants to install a full MinGW tool chain?
Yeah, I noticed that too.  The problem is each one knows nothing about
the other and does not play well.  Couple that with the path mangling in
CygWin and I started to get fed up.

So, I went back to MSys.  At some point, I will get around to adding the
links back in.  So far, I have

    $ pacman -Syuu
    $ pacman -S man git vim zsh

And I installed the x86_64 compiler just to be safe.

To get MSys to respect the Windows path (and be able to find the system
Python and Pandoc and MikTex and ...) set [MSYS2_PATH_TYPE=inherit].  I
still haven't found how to change the default shell without
[editing](shell) `msys2_shell.cmd`.

Well, I just realized we need CygWin anyway.  It has an X server.
Combine that with offlineimap and mutt simply work, and that points to
the idea that we should just use MSys as a useable terminal.

[var]: https://github.com/msys2/msys2.github.io/issues/20
[shell]: http://superuser.com/questions/961699/change-default-shell-on-msys2

