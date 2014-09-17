---
layout: post
title: You're up and running!
---

Hello, World!
-------------

This is just a sample test to try to get Jekyll running.  It follows
Barry Clark's [walk
through](http://www.smashingmagazine.com/2014/08/01/build-blog-jekyll-github-pages/).
A few additional gotchas I came across:

1.  HTML files are passed directly to the server and are not processed.
    This means that you cannot embed liquid tags in a HTML file that
    already has the `<html>` tag.
2.  Don't forget the `permalink` tag in the header for top level files.
    This should have been obvious, but I overlooked it while moving
    files around.
3.  The `title` tag is set as an `h1` in the output so don't use another
    title (# title).  It just looks silly.

I'm sure I will come across additional points as I move forward.  I'll
probably try to update this post with additional comments in the future.
But for now, time to start writing!

