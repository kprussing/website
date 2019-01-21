This is a collection of a simple website for myself.  We'll see how
things progress with it.  The Jekyll formatting is "forked" from [Jekyll
Now](https://github.com/barryclark/jekyll-now) and is a hodge podge of
changes.  Ultimately, I was doing the formatting myself, and then I
found that project to try.  Merging the important parts in has been
interesting.

# Resumes

My full resume should be automatically built using a `git pre-push`
hook.  The hook is in .githooks and I need to run

    git config core.hooksPath .githooks

after cloning the repo.

