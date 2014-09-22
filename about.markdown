---
layout: page
title: About me
permalink: /about/
---

As stated in the header, I am a computational physicist in the Atlanta
area.  I started out as a “music major” at the local community college,
but I realized that would just land me the job I already had of selling
music instruments.  One night, while hanging out with a friend, the
following conversation was had

> Me: You know, I was always good at physics in high school.
>
> Friend: Hey! You should do that.  It would be lucrative!
>
> Me: You know what?  I think I will!

Or something to that effect.  The end results was that I woke up,
thought about it a bit more, discussed it with my girlfriend (now wife),
and got down to business.  Now, I am in the final throws of wrapping up
my PhD in physics at the Georgia Institute of Technology.  My current
research is on the effects of surface shape on enhanced near-field
radiation.  I am currently on the prowl for what will be my next step
once I am done with school.

Activities and interests
------------------------

As I mentioned above, I am a recovering professional sales man.  There
are times where I miss the excitement of the sales floor, but then I
remember grind that was associated with it and go back to my research.
I was a music major, and that gave me a chance to learn to play quite a
few different instruments.  I still enjoy pulling out the euphonium and
the trombone, but I don't get around to it that often.  Most of my free
time is spent in the back yard with the wife and pups.  The little one
really likes fetch!

As for the stuff you really care about, my current fascinations revolve
around computing.   I am trying to teach myself the intricacies of
proper parallel programming; however, that is slow going because I do
not own a super-computer with which to practice.  I am also intrigued by
heat transfer.  There is an open problem out there on how to couple the
radiative exchange in the thermal bands to the conductive modes of
energy exchange numerically.  I got time as an undergrad to play with a
finite difference approach to the problem.  The program was kludge of
FORTRAN 77 and Fortran 90 (mostly 77) and had hard coded limits
appropriate for the computers of the 1980s and 1990s.  These limits are
not trivial to change thanks to the use of common blocks.  The radiative
exchange is coupled to the conduction modes by the view factors known to
computer graphics.  The calculation of the view factors takes a lot of
time and, for large scenes, does not account for long range interactions
of hot objects.  An object that is hot enough may well emit enough
energy that it will reflect around to interact with a surface that is
not immediately visible.  The other issue with this approach deals with
the thermal shadow.  The large nodes necessary for the thermal network
solver do not resolve the thermal shadow well.  We need to figure out a
method to determine the power delivered to a surface and the shadowing
when only a fraction of the surface participates in the exchange.

Coupled with my thesis work, I want to investigate methods of solving
linear systems where the matrix is a block matrix.  There has to be a
systematic method to solve this type of system.  Specifically, I have a
system where the matrix is comprised of 2 by 2 block elements that are
symmetric up to a minus sign.  This symmetry in how the elements are
computed that is not being exploited.  This means that swapping the
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
system of particles.  This is useful for thermal control of low
temperature experiments, micro and nano scaled structures, and it even
applies to evolution of interstellar gasses if the literature can be
believed.  To do this, we need to understand what the effect of particle
shape is.

My other current project is to develop a framework in Python to process
hyper-spectral imagery.  My task was to establish the development plan,
layout the structure, and help guide the development of additional
utilities.  We decided to go with Python so that we could get out of the
choke-hold of MATLAB.  This is partly due to financial reasons and
partly to memory limitations.  We cannot process the highest resolution
data cubes with in MATLAB because it cannot request enough memory to do
the necessary work.  Long term goals include real time processing of
hyper-spectral data for _in situ_ checking during field work and
processing spectral data to predict broad band sensor response.  The end
goal is to use any means necessary to enhance performance including
acceleration with graphic processing units.

A few other topics that I have studied are: 

1.  Electromagnetic wave scattering from non-spherical particles.  This
    is commonly known as either Mie scattering or the T-matrix approach.
    This topic came up because the formalism to establish the parameters
    of the matrix is very similar to my thesis work.  I was looking for
    tricks to help me out.
2.  Studied the performance parameters of counter flow cooling towers to
    understand the energy emission under normal load.  I no longer
    remember our original goals with this topic.  I do remember that I
    hypothesized that you could predict the performance load by
    measuring the enthalpy change from the surrounding environment to the
    center of the plume.  That failed.
3.  Vehicle dynamics.  My very first task joining GTRI was to develop a
    first principles based vehicle dynamics model.  The first version
    was a highly simple model written in MATLAB.  Once I transitioned to
    a graduate student, I went back and expanded the model into a five
    degree of freedom, four wheel, untracked land vehicle model under
    normal conditions and hooked it into a MySQL database.  The goal was
    to help with simulating visible and infrared imagery in complex
    urban environments.

That just about wraps it up for me.  I hope you enjoy your stay!

