---
layout: post
title: Dumping a Subversion Repository
---

After finishing my thesis work, I wanted to grab the revision history
for both the software I developed and the writing of my dissertation.
It was (is?) stored in a subversion server owned by the lab; however, I
want all of that for my own purposes.  First, I had to dump from a
remote server

    $ svnrdump https://url/to/repo > repo_full.svndump

Now I have the full repository, but it is full of empty commits.  This
is because I had only a twig on the server so I need to strip all of
those empty commits out.  Enter `svndumpfilter`.

    $ svndumpfilter --drop-all-empty-revs --renumber-revs include \
    > myrepo < repo_full.svn_dump > repo_stripped.svn_dump

Now, I can compress the file and store all of my revision history!  This
isn't really very exciting information, but I wanted to get it down for
my own notes since I did it once and promptly forgot how to do it.

