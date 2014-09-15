---
layout: post
Title: Writing with Markdown
---

Writing with Markdown
=====================

So, I have come to the realization that LaTeX is not the best way to
write.  By the looks of it, I am not the [first][fenner_what_2013] or
[second][_write_2013], and I probably won't be the last.  Thankfully,
with the emergence of [CommonMark], I can possibly make some head way.
I already live in the command line, and I have grown to like the cleaner
files of [Markdown], so I'll try to figure this one out.  This will also
let me use [pandoc] to convert to PDF or Word format.  However, the hold
up will be getting citations in place.  So, here we go!

Installation
------------

The first order of business is to get things installed.  I'm on OS X, so
I use [MacPorts].  To get `pandoc` we simply call
```
$ sudo port install pandoc
```
According to the manual, to add a bibliography, we need
`pandoc-citeproc`, but it does not appear to be in MacPorts.  Rooting
around on the [repository][pandoc-citeproc], it appears that this has
been recently removed from `pandoc`.  This would explain why it is not
evident.  So, we go directly to the Haskell method
```
$ sudo port install haskell-platform # To get cabal
$ cabal install pandoc-citeproc
```
And then simply add `~/.cabal/bin` to your `PATH`.

At one point, I tried to build from the cloned repository, but it
failed.  These were the steps if you care to try it, but I just gave up.
```
$ git clone https://github.com/jgm/pandoc-citeproc
$ cd pandoc-citeproc
$ sudo port install haskell-platform hs-cpphs # to get cabal and cpphs
$ cabal update # make fails otherwise
$ cabal install hsbhs
$ PATH=$PATH:~/.cabal/bin make
$ PREFIX=~/.local make install
```
This will install to `~/.local/` for cleanliness.

Running `pandoc`
----------------

Now we try to make a test case
```
$ cat test.text
A Title
=======

And they said stuff @narayanasway_thermal_2008.

$ cat reference.bib
@article{narayanaswamy_thermal_2008,
        title = {Thermal near-field radiative transfer between two spheres},
        volume = {77},
        url = {http://link.aps.org/doi/10.1103/PhysRevB.77.075125},
        doi = {10.1103/PhysRevB.77.075125},
        number = {7},
        journal = {Physical Review B},
        author = {Narayanaswamy, Arvind and Chen, Gang},
        month = feb,
        year = {2008},
        pages = {075125},
}

$ pandoc test.text -o test.pdf --bibliography=./reference.bib --csl=physical-review-b.csl

```
And this gives us a lovely PDF!

Customizing the Output
----------------------

Now, what if we want to use a specific format such a that for PRB?  We
could possibly use the `--reference-docx=FILE` option if the journal
offers that; however, PRB does not.  The `-H FILE` flag will be useful
for adding in the preamble if necessary.  I think we might be able to
use the `.sty` file from the publisher, but that won't let us set the
option.  I think the ultimate answer will be to generate the `.latex`
and then hand hack it to set the document class correctly.
```
$ pandoc --standalone test.text -o test.latex -H preamble.tex
$ vim test.latex # Fix the document class
$ pdflatex test
$ bibtex test
$ pdflatex test
$ pdflatex test
```
And now we should have a nice PDF in the desired format!

Now I should be able to use a nicer format to work on my articles.  At
the time of writing this, I have not actually used this as a work flow.
I really hope this works.

[fenner_what_2013]: http://blog.martinfenner.org/2013/06/17/what-is-scholarly-markdown/
[_write_2013]: http://recurrentprocessing.blogspot.fi/2013/02/write-academic-papers-with-markdown.html
[CommonMark]: http://commonmark.org
[Markdown]: http://daringfireball.net/projects/markdown/syntax
[pandoc]: http://johnmacfarlane.net/pandoc/
[macports]: http://www.macports.org
[pandoc-citeproc]: https://github.com/jgm/pandoc-citeproc

