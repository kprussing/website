---
layout: post
title: Writing in the Terminal
---

So, I have been writing with plain text files for a while.  I've plaid
around with HTML and LaTeX extensively.  Once I discovered the joys of
vim, I slowly began to do all of my editing within a terminal emulator.
Initially, I worked directly with the before mentioned markup languages.
Recently, I learned about [pandoc] and that let me give up on HTML by
using [Markdown], but I still wrote my scientific papers directly with
LaTeX.  Now I think it is time to make the full switch.

<!--break-->
Writing with Markdown
---------------------

So, I have come to the realization that LaTeX is not the best way to
write.  By the looks of it, I am not the [first][fenner_what_2013] or
[second][_write_2013], and I probably won't be the last.  Thankfully,
with the emergence of [CommonMark], I can possibly make some head way.
The beauty of [Markdown] is the readability of the source file.  I am a
big fan of splitting content and format.  I already live in the command
line so the plain text files makes my life easier.  By using `pandoc`, I
can convert to HTML, PDF, or Word, but the challenge is getting the
citations in place.  This documents my path to getting the citations to
work with `pandoc`.

### Installation ###

The first order of business is to get things installed.  I'm on OS X, so
I use [MacPorts].  To get `pandoc` we simply call

    $ sudo port install pandoc

According to the manual, to add a bibliography, I need
`pandoc-citeproc`, but it does not appear to be in MacPorts.  Rooting
around on the [repository][pandoc-citeproc], it appears that this has
been recently removed from `pandoc`.  This would explain why it is not
evident.  So, we go directly to the Haskell method

    $ sudo port install haskell-platform # To get cabal
    $ cabal install pandoc-citeproc

And then simply add `~/.cabal/bin` to your `PATH`.

### Running `pandoc` ###

Now to try to make a test case

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

    $ pandoc test.text -o test.pdf \
    > --bibliography=./reference.bib --csl=physical-review-b.csl

And this gives me a lovely PDF!  Granted, none of this is really new.

### Customizing the Output ###

Now, what if I want to use a specific format such a that for PRB? I
could possibly use the `--reference-docx=FILE` option if the journal
offers that; however, PRB does not.  The `-H FILE` flag will be useful
for adding in the preamble if necessary.  I think I might be able to use
the `.sty` file from the publisher, but that won't let us set the
options to `documentclass`.  I think the ultimate answer will be to
generate the `.latex` and then hand hack it to set the document class
correctly.

    $ pandoc --standalone test.text -o test.latex -H preamble.tex
    $ vim test.latex # Fix the document class
    $ pdflatex test
    $ bibtex test
    $ pdflatex test
    $ pdflatex test

And now I should have a nice PDF in the desired format!

At the time of writing this (2014-09-17), I have not actually used this
part as a work flow.  I really hope this works.

Editing on the Command Line
---------------------------

Now that I have a way to write neat files, I need to worry about
editing.  This derives from my attempt to create an editing work flow
for my thesis.  I read through the silly thing and marked it up with my
trusty red pen.  I was then stuck with how to automate searching for
misspellings and blatant grammatical errors.  As I mentioned above, at
this point I was still using LaTeX so I had a bunch of plain text files
that I didn't really want to convert to something like Word just to get
the automated grammar and spelling checkers.  A web search turned up
[this][se6333] discussion and one of the answers was the [Writer's
Workbench][workbench].  The specific tools that looked promising are
`aspell` and `diction`.  And the bonus is that both are on MacPorts!

### Working with `aspell` ###

Here is the real trick: how do I get spell checking to work
intelligently?  According to the `info` page, it is as simple as

    $ aspell check file.text

However, the trick is the author names and technical jargon gets in the
way.  I could just add each one to the dictionary; however, I don't
really want to pollute a personal dictionary with project specific words
that I may never use again.  It's one thing if *my* name is in there,
but often, many names I will never reference again.  So, I need a
project specific list of words.

First, we tackle the author names.  I am using [Zotero] to manage my 
bibliography.  This allows me to keep organized and has an option to
export to a BibTex file!  It is plain text, so it can easily be parsed
to find the author names.  We just have to look for the `author` fields
and parse what is within the `{}`.  The trick was splitting on the `and`
token.  A blind tokenizing on `and` leads to breaking the occasional
name.  The workaround was to split at the spaces and collect the full
names together.  Care was needed when a name contained `and`, but it was
manageable.  I made wrote a script `ztbib2spl` for future use and put it 
in my [`dotfiles/scripts`][dotfiles] folder.

Now we have a word list of author names to pass to `aspell` to ignore!
Reading through the documentation, we first need to clean the list of
bad characters

    $ echo 'personal_ws-1.1 en 0' > authornames.en.pws
    $ ztbib2spl reference.bib > authornames.text
    $ aspell --lang=en --local-data-dir . clean < authornames.text >> authornames.en.pws
    $ aspell --personal=./authornames.en.pws check file.text

The first line above is easy to over look.  I was banging my head
against the wall for a while until I got it right.  I went through a lot
of effort to get a binary version or a dictionary.  That
`personal_ws-1.1 en 0` indicates that this is a personal word list for
the English language dictionary and the number just needs to be there.
According to the `info` page, it is supposed to be the number of words,
but even the documentation says the value does not matter.  Don't miss
the `--data-dir .` flag!  That tells `aspell` to keep the file in the
current directory.  

### Checking the grammar ###

After we have run the spell checker, we can check for blatantly bad
grammar with `diction`.  The useful way to do this is to get the
suggestions with the `-s` flag and pass it to the pager.  I find it best
to start at the end of the file and work backwards.  This preserves the
line numbers of the `diction` output so that I can find the sentences.
The `diction` tool only looks for blatantly bad grammar, so we still
need to do the manual revisions as well.  When doing the revisions, it
is best to work with either `diction` or the hand written notes at one
time.  When trying to do both, it becomes hard to keep track of where
you are.

Conclusion
----------

In this note, I have outlined a way to work within the command line to
edit plain text files.  The basic work flow is:

1.  Run `aspell`
2.  Run `diction`
3.  Print and hand annotate
4.  Run `diction` just to be sure (or not)
5.  Run `aspell`
6.  Repeat as necessary.

This allows me to remain comfortably in the terminal and working with
plain text files.

[fenner_what_2013]: http://blog.martinfenner.org/2013/06/17/what-is-scholarly-markdown/
[_write_2013]: http://recurrentprocessing.blogspot.fi/2013/02/write-academic-papers-with-markdown.html
[CommonMark]: http://commonmark.org
[Markdown]: http://daringfireball.net/projects/markdown/syntax
[pandoc]: http://johnmacfarlane.net/pandoc/
[macports]: http://www.macports.org
[pandoc-citeproc]: https://github.com/jgm/pandoc-citeproc
[se6333]: http://tex.stackexchange.com/questions/6333/grammar-checking-tool-for-use-with-latex
[workbench]: http://dsl.org/cookbook/cookbook_15.html#SEC220
[zotero]: https://www.zotero.org
[dotfiles]: https://github.com/kprussing/dotfiles

