---
layout: post
title: Yay Package Managers...
---

So, today I log into one of my RHEL6 machines and notice that `yum` says
there are some updates to apply.

<!--break-->

Trying to do a simple update gives

    $ yum upgrade
     <snip>
    --> Finished Dependency Resolution
    Error: Package: gnote-0.6.3-3.el6.x86_64 (@anaconda-RedHatEnterpriseLinux-201301301459.x86_64/6.4)
        Requires: libboost_filesystem-mt.so.5()(64bit)
        Removing: boost-filesystem-1.41.0-17.el6_4.x86_64 (@rhel-x86_64-server-6)
            libboost_filesystem-mt.so.5()(64bit)
        Updated By: boost-filesystem-1.55.0-4.el6.x86_64 (eosl-el6-x86_64)
            Not found
        Available: boost-filesystem-1.41.0-18.el6.x86_64 (rhel-server-el6-x86_64)
            libboost_filesystem-mt.so.5()(64bit)
        Available: boost-filesystem-1.54.0-14.el6.x86_64 (eosl-el6-x86_64)
            Not found
    Error: Package: gnote-0.6.3-3.el6.x86_64 (@anaconda-RedHatEnterpriseLinux-201301301459.x86_64/6.4)
        Requires: libboost_system-mt.so.5()(64bit)
        Removing: boost-system-1.41.0-17.el6_4.x86_64 (@rhel-x86_64-server-6)
            libboost_system-mt.so.5()(64bit)
        Updated By: boost-system-1.55.0-4.el6.x86_64 (eosl-el6-x86_64)
            Not found
        Available: boost-system-1.41.0-18.el6.x86_64 (rhel-server-el6-x86_64)
            libboost_system-mt.so.5()(64bit)
        Available: boost-system-1.54.0-14.el6.x86_64 (eosl-el6-x86_64)
            Not found
      You could try using --skip-broken to work around the problem
      You could try running: rpm -Va --nofiles --nodigest 

Okay?  Trying a Google search didn't bring anything useful up for a
while.  At this point, I'm ready to start banging my head on the desk.
And the, I came across [this thread].  It turns out `gnote` wanted an
old version of `boost`.  The catch is, I don't use `gnote`.  I normally
`ssh` in and use the terminal for everything.  When I _do_ sit down at
the workstation, I prefer KDE.  I have no use for `gnote` so it can just
go away.  Following the instructions I ran

    $ rpm -qa | grep -e "boost-.*-1\.41\.0.*" | xargs rpm --test -e

to check which programs wanted the specific version of boost and 

    $ yum remove gnote-0.6.3-3.el6.x86_64

to remove the offending package.  In the above, the boost version (or
what ever is causing the issue) can be updated in the regex to `grep`
and then the package simply removed.  Now to get back to trying to write
some documentation...

[this thread]: https://www.ibm.com/developerworks/community/forums/html/topic?id=b3c4d2c9-32be-4c75-adcf-e754d266953f

