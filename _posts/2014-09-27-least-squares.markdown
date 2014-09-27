---
layout: post
title: Least Squares Fitting
---

<script type="text/javascrpit"
    src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

This note is more for myself than for anyone else.  I have derived the
expression for the least squares fitting so many times it's not funny.
The problem is, once I cobble together the routine to perform the
fitting, I completely forget how to do it again.  I hope, this will
prevent me from having to do it ever again if only because it is on my
website.  This post also gives me a chance to try out [MathJax].  After
a Google search, I came across [these][sanchez_mathjax_2014]
instructions.  Apparently, we simply need to add

    <script type="text/javascrpit"
        src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
    </script>

to the layout.  However, I don't really want it in every page.  So, I
just put it at the top of this source.  I did have to change the
markdown field in the `_config.yml` file to use `redcarpet`.

<!--I didn't want it to *always* be there, but trial and-->
<!--error appears to tell me it *must* be in the header.  So, into the-->
<!--`default.html` file it is.  The advantage is it will always be availa-->

We begin with a set of function of the independent variable
\\(\{x_i\}\\) and dependent variables \\(\{y_i\}\\).  We then select a
collection of functions to relate the two
\\[
    y_i = a_0 +a_1 x_i +a_2 x_i^2 +\ldots a_j \sin(x_i) = \sum_{j} a_j
    f_j(x_i).
\\]
Now, we minimize the squared error
\\[
    \partial_k \frac{1}{N}\sum_{i} [y_i -\sum_{j} a_jf_j(x_i)]^2 =
    -\frac{2}{N} \sum_{i} [y_i -\sum_{j} a_jf_j(x_i)] f_k(x_i) = 0
\\]
or in matrix form
\\[
    \mathbf{a} \mathbf{F} \mathbf{F}^T = \mathbf{F}^T \mathbf{y}
\\]
which can be readily solved.

See, I told you that this was simple.  Now to put this online and see
how the math looks.  Oh, don't forget that the delimiters are `\\(`,
`\\)`, `\\[`, and `\\]` for math mode.

[MathJax]: http://www.mathjax.org
[sanchez_mathjax_2014]: http://gastonsanchez.com/blog/opinion/2014/02/16/Mathjax-with-jekyll.html

