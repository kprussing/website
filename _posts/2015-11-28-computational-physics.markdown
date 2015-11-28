---
layout: post
title: Playing with Computational Physics
---

<script type="text/javascript"
    src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

At some point during the process of working through my dissertation, I
got so bogged down in the process of *doing* the work, I forgot a bit
*why* I was so intrigued when I started.  I was going through the
motions, but not really finding the fun of physics.  Sure, programming
is fun in and of itself, but I was missing the physics.  So, now that I
have free time to pursue a hobby, I want to go back and remind myself
why I started down this path.

So, where to go?  I am one of those people who value a good book.  And I
do mean a physical book.  I bought and kept all of my text books
throughout my undergrad and graduate work.  That being the case, I
grabbed my undergraduate computational physics book by Nicholas J.
Giordano and Hisao Nakanishi [1] and decided to work through it again.
It is a fantastic book that covers a broad span of topics with many fun
problems that I can play with.

With that all said, I plan on working through all of the problems
starting at the beginning.  I will periodically post a selection of the
discussion of the solutions here, but some problems are trivial and
don't merit much in the way of discussion.  I will be working with
Python primarily, but I may dust of my Fortran skills for some of the
problems.  I will also be attempting to keep the code recognizable and
avoid clever tricks like list comprehensions in the physics parts.  It's
not that I don't know them (I do), I'm just trying to keep to the
basics.  Anything to do with display or I/O is fair game though.  The
code will be hosted in a [mercurial repository on Bitbucket][repo].  Why
Bitbucket and mercurial you ask?  Because it's Python.

And now for a final note before I get started.  If you are an
undergraduate using this text, go do your homework before looking over
my solutions.  It's good for you and actually quite fun.

Chapter 1
---------

And so it begins.  This will probably be a very short section because
the problems are very simple.  The chapter is simply a chance to whet
the appetite and brush up on some basics.  It will also give me a chance
to build some basic plotting tools for later.

### Problem 1

Not much to see here.  It is pretty trivial to see that the solution is
\\(v(t) = v(0) - g t\\).  Each time step is similarly simple \\(t_i = i
\\Delta t\\).  Computing over a selection of time steps, we find

![Numeric and exact solution for chapter 1 problem 1]({{ site.url
}}/images/compphys/compphys_chapter1_problem1a.svg)

Well, that's not very interesting.  It is good to know that we can get a
good answer for this case, but what about the error?  

![Error in the solution for chapter 1 problem 1]({{ site.url
}}/images/compphys/compphys_chapter1_problem1b.svg)

Now, that's more interesting.  What are the final results?  I'm glad you
asked:

    Numeric, exact, difference
    -98.000000, -98.000000, -7.95808e-13
    -98.000000, -98.000000, -2.70006e-13
    -98.000000, -98.000000, 4.26326e-14
    -98.000000, -98.000000, 2.84217e-14
    -98.000000, -98.000000, -1.42109e-14
    -98.000000, -98.000000, 0

We clearly see that *increasing* the time step *decreases* the error.
This is contrary to the common result where decreasing the time step
increases the accuracy.  What's going on here?  The answer is
accumulated error due to machine precision.  At each time step, we are
accumulating a fractional error.  As we take more steps from the start
to the finish, we are simply adding up all that error.  Tricks exist
that you can use to reduce the error, but they use fancy array slicing
which I am avoiding.

### Problem 2

Not much to see here, unless you didn't do problem 1.  Then it's the
exact same as above but with an opposite sign.  The accuracy is better,
but I suspect that is due to a nice multiple of 10.

### Problem 3

Now we get to something non-trivial.  Implementing the Euler method is
straight forward.  At some point, I will probably need to write a canned
routine to perform the Euler method, but that seems to be touching on
the area I want to avoid.  We'll see.  But now results.  Plotting for a
selection of \\(b\\), we see that the terminal velocity is being reached
as expected.  A bit of manipulation reveals that terminal velocity is
when \\(v_t = a / b\\) which is what we are seeing.  Beyond that, there
isn't really much more to say.  I know we'll come back to this in the
next chapter.

![Numeric and exact solution for chapter 1 problem 3]({{ site.url
}}/images/compphys/compphys_chapter1_problem3.svg)

References
----------

1.  N. J. Giordano and H. Nakanishi, *Computational Physics* (Pearson,
    Upper Saddle River, NJ, 2006), Ed. 2.

[repo]: https://bitbucket.org/kprussing/compphys

