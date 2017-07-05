I finally figured out how to get the GLX working with XQuartz and the
Red Hat machines.  It ultimately boils down to enabling the indirect GLX which is
no longer enabled by default for most X systems.  For XQuartz, it's a
matter of updating to a recent version and passing the command [see
here](https://bugs.freedesktop.org/show_bug.cgi?id=99146).

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

