Editing my thesis
=================

So, here I am with draft one of my thesis done and I need to start the
editing process.  I have read through the silly thing and made my marks
on paper.  Now, I need to figure out a systematic way to use a spell and
grammar checker.  As any good scientist, I used \LaTeX to write my
thesis.  This means I have a whole bunch of plain text files that I
don't really want to convert to another format.  It's so much easier to
just deal with that.  A web search turned up [this][1] discussion and
one of the answers was the [Writer's Workbench][2].  The specific tools
that look useful are `aspell` and `diction`.  These look they will help
me get some extra help with the editing process and both are available
from <http://www.macports.org>.

The `diction` tool is pretty straight forward.  On the command line
simply run `$ diction path/to/file.tex > path/to/notes.text` and we get
a list of grammatical suggestions.  That will give us a starting point
for systematic correcting of the grammar.  Playing with `aspell` is a
bit trickier.

Working with `aspell`
---------------------

Here is the real trick: how do we get spell checking to work?  According
to the `info` page, it is as simple as

    $ aspell check introduction.tex

However, the trick is the author names and technical jargon start to get
in the way.  I could just add each one to the dictionary; however, I
don't really want to pollute my dictionary with strings that I might
never use again.  It's one thing if my name is in there, but it is
unlikely that sum of the names will come up in the future.  So, what I
want is a project specific list of words that are okay.

First, we tackle the author names.  I am using [zotero][3] to manage my
bibliography.  This allows me to keep organized and has an option to
export to a BibTex file!  It is plain text, so it can easily be parsed
to find the author names.  We just have to look for the `author` fields
and parse what is within the `{}`.  The trick was splitting on the `and`
token.  A blind tokenizing on `and` leads to breaking the occasional
name.  The workaround was to split at the spaces and collect the full
names together.  Care was needed when a name contained `and`, but it was
manageable.  I made wrote a script `ztbib2spl` for future use and put it 
in my [`dotfiles/scripts`][4] folder.

Now we have a word list of author names to pass to `aspell` to ignore!
Reading through the documentation, we first need to clean list of bad
characters

    $ ztbib2spl references.bib > authornames.text
    $ aspell --lang=en --local-data-dir. clean < authornames.text > authornames.spl

I originally thought this was the what we needed, but I was wrong.
Reading the [correct page][5] in the manual, we need to convert the text
version to a binary

    $ aspell --lang=en create master ./authornames < authornames.spl

According to the `man` page, `personal` is supposedly an option;
however, using that option gives the error 

    $ aspell --lang=en create personal ./authornames < authornames.spl
    Sorry "create/merge personal" is currently unimplemented

Forging ahead, we now can try to run the spell checker to see what I
spelled wrong!

    $ aspell check --personal=./authornames introduction.tex
    Error: The file "./authornames" is not the proper format.

What do you mean it "is not in the proper format?" You just created it
you stupid program!  Needless to say, getting to this point and starting
to write up this journey took a bit of time.

Now what do we do?  Apparently, I missed something along the way.  On a
lark, I put `personal_ws-1.1 en 0` at the top of a copy of
`authornames.spl` and it worked

    $ echo 'personal_ws-1.1 en 0' > authornames.en.pws
    $ cat authornames.spl >> authornames.en.pws
    $ aspell check --personal=./authornames.en.pws introduction.tex

I am *sure* I did this before, but I cannot figure out *what* is
different this time.

Next it would be handy if `vim` understood the same file.

Running the spell checker
-------------------------

This post is essentially going to be an outline of my work flow.  In the
end, I'll have to go back and edit this one too.  So, I have written the
first draft and taken a red pen to the hard copy.  This gives me a
starting point for revisions.  The reason I need to do the hard copy is
for clarity of the argument.  This tells me if what I have is even
readable.  

The next step is to used `aspell` to look for bad words.  One issue is
dealing with author names.  I threw together the script and method
outlined above.  When using `aspell` and it comes across a name I *did*
misspell, I cobbled together a script to find the BibTex entry in my
bibliography.  This uses `awk` to grab from the tag to the next `}`
character that is the only thing on the line.  This works because that
is how Zotero generates the bibliography.  At some point, I need to get
something together that will exclude the `file` entry that Zotero
provides.

In the process of running the spell checker, some of the words it does
not know identify sentences that need revision.  This is a useful tool
for making notes on the hard copy.

When working with LaTeX, it might be a good idea to put all of the math
into separate files.  This will let the spell checker ignore the odd
tokens that are in the math sections.

Checking the grammar
--------------------

Now to run `diction`.  The useful way to do this is to get the
suggestions with the `-s` flag and stash it in a file.  I guess then we
need to merge that with the notes on the hard copy.  The `diction` tool
only looks for possibly pore grammatical structure.  It does not go for
understanding.  A useful command line to get this is

    $ for f in *.tex; do diction -s $f | fmt -s > ${f}.dct; done

This puts us in a position where we have all of the systematic
grammatical suggestions along with our hand written notes.

One more thing to consider.  It is easier to rework with the hand
comments or the results of `diction`.  Do not try to do both
simultaneously.  It would also be useful to have once sentence per line.
That makes finding the line to edit easier.  Or, if we are doing one or
the other, it might just be easier to find the line.  This especially
true if we start from the end of the file.

The best order is 
1.  Run `aspell`
2.  Run `diction`
3.  Print and hand annotate
4.  Run `diction` just to be sure (or not)
5.  Run `aspell`
6.  Repeat as necessary.

Conclusion
----------

In this note, I have outlined a way that I want to do editing.  This is
useful because it works on plain text files and is on the command line.
The basic steps are: write a draft, run `aspell` to correct
misspellings, run `diction` to get grammatical suggestions, and, 
finally, proofread the draft for clarity of argument.  With these tools,
I can get cracking on the next draft.

[1]: http://tex.stackexchange.com/questions/6333/grammar-checking-tool-for-use-with-latex
[2]: http://dsl.org/cookbook/cookbook_15.html#SEC220
[3]: https://www.zotero.org
[4]: https://github.com/kprussing/dotfiles
[5]: http://aspell.net/man-html/Creating-an-Individual-Word-List.html#Creating-an-Individual-Word-List

