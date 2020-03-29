---
title: Notes on writing a GCC plugin
date: 2018-01-18
author: Keith F. Prussing, Ph.D.
abstract: >
    Here are notes on some of my discoveries while working on a plugin
    for GCC.
layout: post
---

Callback arguments
------------------

I have been toying around with a plugin to GCC to generate a Fortran
module source with the appropriate `bind(c)` settings from a C header
file.  According to the [GCC internals manual](??), the basic structure
is 

    void callback(void * gcc_data, void * user_data)
    {
        ...
    };

    int plugin_init(...)
    {
        struct PACKAGE_NAME_data data;
        ...
        register_callback(..., callback, &data)
    };

However, all of the tutorials online punt on how to actually pass
arguments through the `user_data` by using `NULL`.  This is not helpful
if the plugin will be run in concurrent processes.  Initially, I could
not get the casting correct.  After a bit of playing, I finally stumbled
on the proper casting

    void callback(void * gcc_data, void * user_data)
    {
        struct PACKAGE_NAME_data * data;
        data = reinterpret_cast<struct PACKAGE_NAME_data *>(user_data);
        ...
    };

    int plugin_init(...)
    {
        static struct PACKAGE_NAME_data data;
        ...
        register_callback(..., callback, &data)
    };

(You could just use C style casting, but this is C++ so you shouldn't)

When to walk the AST
--------------------

All the tutorials I could find online worked at the gate pass or at the
final stage.  I want to walk the tree immediately after the parsing is
done and the AST has been assembled.  I originally thought I wanted the
`PLUGIN_PRE_GENERICIZE`, but that is not appropriate for C/C++ parsing
(the manual says this in the section on GENERIC).  It looks like the
GIMPLE pass is where we get the full tree before push down.  The
`PLUGIN_OVERRIDE_GATE` appears to run too soon, but I'm still working on
that.

Working with autotools
----------------------

We need to undefine the macros set by autotools because the plugin
framework defines them before we can.  This simply suppresses the
warnings about that.

    #undef PACKAGE_BUGREPORT
    #undef PACKAGE_NAME
    #undef PACKAGE_STRING
    #undef PACKAGE_TARNAME
    #undef PACKAGE_VERSION

I just put it in a header 'package-config.h' with the appropriate
`#include` to use in additional files.

## Edit 2020-03-29

The original purpose for writing a plugin was to concoct a way to
generate the Fortran 2003 interface module given a C header.  It sort of
worked, but not well enough to put it out in the world.  I came back to
it (again) the other night to take another stab.  But then I was
googling a different problem and came across [this
article](https://arxiv.org/pdf/1904.02546.pdf).  It looks like they beat
me to the punch.  Oh well.  But at least I have a new project to keep an
eye on!

