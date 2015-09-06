Our Local Spacetime
===================

Author: Jonah Miller (jonah.maxwell.miller@gmail.com)

This is a simplistic python script to generate a plot of the spaceitme
around Earth using an isometric embedding of the surface

ds^2 = -(1 - rs/r) dt^2 + (1-rs/r)^(-1) dr^2

into 3D Minkowski space. The angular components of the metric are set
to zero. The plot uses radial coordinates and avoids coordinate
singularity at the schwarzschild radius by stopping at the radius of
the surface of the Earth which is outside the Schwarzschild
radius. Units are arbitrary.

This code is a companion to the blog article I wrote about our local
spacetime:
    
http://www.thephysicsmill.com/2015/09/06/our-local-spacetime/


Requirements
------------

Python2 and the the scientific python stack including numpy, scipy,
and matplotlib.

Running
-------

Just run the script to generate the image:

```python2 local_spacetime.py```

Source
------

This code uses the isometric embedding defined by Don Marolf in his
paper "Spacetime Embedding Diagrams for Black Holes," General
Relativity and Gravitation 31 (1999) 919-944. A preprint of the work
is available on the arXiv: http://arxiv.org/abs/gr-qc/9806123


