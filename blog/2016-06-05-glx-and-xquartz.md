---
title: Getting GLX Working with X Forwarding
date: 2016-06-05
author: Keith F. Prussing, Ph.D.
abstract: >
    Some notes on how to get indirect rendering working with X
    forwarding on an ssh connection.
post: true
---

I finally figured out how to get the GLX working with XQuartz and the
Red Hat machines.  It ultimately boils down to enabling the indirect GLX
which is no longer enabled by default for most X systems.  For XQuartz,
it's a matter of updating to a recent version and passing the command
[see here](https://bugs.freedesktop.org/show_bug.cgi?id=99146).

    defaults write org.macosforge.xquartz.X11 enable_iglx -bool true

Then, to get the rendering to happen on the remote machine, you *must*
set `DISPLAY=:0.0`.  I'm not sure why the login information is not
sufficient, but I have better things to do that monkey around with that.
Additionally, I determined that I had to log into a physical X session
on the remote machine.  This isn't so bad for me because the target
machine is sitting under my desk.

To see what happens when setting the display, try observing the
difference between `glxinfo` and `DISPLAY=0 glxinfo`.  For me, the
second one actually reported the correct video card.  Take a look
[at this answer](https://askubuntu.com/a/294773/708045) for the
enlightening details that brought me to this conclusion.

## Edit 2020-03-29

Empirical evidence seems to suggest that you _must_ have control of the
X session to do indirect rendering.  This means you must be sitting at
the workstation or have the screen locked under your name.  We keep
running into this issue at work, and we haven't found a solution as of
this time.

