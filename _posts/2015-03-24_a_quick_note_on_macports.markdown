---
layout: post
title:  A Quick Note on Installing Old Ports
---

So, I recently discovered that something is wrong with [Inkscape] 0.91
available from MacPorts.  When I attempt to convert a SVG to PDF+LaTeX,
it doesn't work.  At first blush, it appears like a macro is not
properly closed with a `}` character; however, I have not had a chance
to create a minimum working example to reproduce this behavior.  The
problem is I _need_ this to work for my dissertation.  Trying the
development port didn't help because the `lualatex` was claiming that
a page was missing.  

After a Google search, I found [these instructions] which failed because
`port` was claiming that it could not find the patches.  To work around
this, I went to the repository and went back to the revision with the
patches.  After downloading them and placing them in the `files`
directory next to the `Portfile`, I was able to get a copy of Inkscape
that worked for what I need.  The trick was to manually download the
files `port` wanted.

Now to see if I can hunt down what the problem is and get it fixed…

[Inkscape]: https://inkscape.org/en/
[these instructions]: http://trac.macports.org/wiki/howto/InstallingOlderPort

