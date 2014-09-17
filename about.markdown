---
layout: page
title: About
permalink: /about/
---

The Keith Page
==============

Welcome to my web page!  This is a brief introduction to me.

Activities and interests
------------------------

I am a recovering professional sales man.  I used to be a music
major until I realized that would simply land me in the job I already
had.  Now I am a computational physicist.  Most of my free time, I spend
in the back yard with the wife and pups.  The little one really likes
fetch!

As for the stuff you really care about, my current fascinations revolve
around computing.   I am trying to teach myself the intricacies of
proper parallel programing.  That is slow going because I do not own a
super-computer with which to practice.  I am also intrigued by heat
transfer.  There is an open problem out there on how to couple the
radiative exchange in the thermal bands to the conductive modes of
energy exchange numerically.  I got time as an undergrad to play with a
finite difference approach to the problem; however, the program was
limited by the fact that it was written in the 1980s.  This means that
the program has hard codded limits that are not trivial to modify.   The
method is based on computing the view factors known in computer
graphics; however, this does not mesh well with the larger node scale
necessary for the heat transfer.  To account for the thermal
shadow, we need to figure out a way to determine the power delivered to
a surface when only a fraction of the surface participates in the
exchange.

Coupled with my thesis work, I want to investigate methods of solving
linear systems where the matrix is a block matrix.  There has to be a
systematic method to solve this type of system.  Specifically, I have a
situation where the matrix is comprised of 2 by 2 block elements that
are symmetric up to a minus sign.  There is symmetry in how the elements
are computed that is not being exploited.  This means that swapping the
indexes of the block simply gets you the symmetric block of the matrix.
Currently, I am using a brute force method to solve the system.  I would
love for the chance to search for a more efficient method to solve the
system.

My Work at GTRI
---------------

Currently, I am investigating the effects of shape on near-field
radiative transfer.  We all know from undergraduate physics that all
objects are surrounded by a thermally generated electromagnetic field.
At large separations, this is simply the black-body exchange predicted
by statistical mechanics.  When the separation between the objects is
small enough, the surface reach a point where they are within the decay
range of the evanescent waves trapped on the surfaces.  We want to
establish a long range structure that can direct the energy through a
system of particles.  This would be useful for thermal control of low
temperature experiments, micro and nano scaled structures, and it even
applies to evolution of interstellar gasses if the literature can be
believed.  To do this, we need to understand what the effect of particle
shape is.

Currently, we are  developing a framework in Python to process
hyper-spectral imagery.  My task was to establish the framework and
guide the development of the software to get out of the choke-hold of
MATLAB.  Long term goals include real time processing of hyper-spectral
data for _in situ_ checking during field work and processing spectral
data to predict broad band sensor response.  The end goal is to use
any means necessary to enhance performance including acceleration with
graphic processing units.

Studied electromagnetic wave scattering from non-spherical particles.

Studied the performance parameters of counter flow cooling towers to
understand the energy emission under normal load.

I refined my vehicle dynamics model into a full rigid body model for
untracked, four wheel land vehicles under normal conditions.  The
routine was implemented in MATLAB and hooked into a SQL database for
simulation of complex urban environments.

Other places
------------
+   [My resumes]({{ site.baseurl }}/resumes/index.html)
+   [Posts]({{ site.baseurl }}/posts//index.html)

>   Copyright © Keith Prussing 2014

