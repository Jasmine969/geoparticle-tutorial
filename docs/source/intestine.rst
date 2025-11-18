Tutorial 2: Create a 3D intestine connected with an inlet and and outlet
=========================================================================

In this tutorial, a 3D intestine (type 2) will be created which is connected with an inlet and an outlet (type 1).
Fluid (type 3) will also be filled with the intestine. 
It is a part of my unpublished work.

The expected result is as follows:

.. image:: static/dimension-intestine.png

Geoparticle elements we will learn in this tutorial include:
???

===================================
Specify the parameters
===================================

Like Tutorial 1, let's first import the necessary libraries and set up the simulation parameters:

.. code-block:: Python
   :linenos:

   import geoparticle as gp
   from lammps import lammps
   import numpy as np
   
   rho_fluid = 993
   rho_wall = 1040
   l_pipe_hrz = 0.002
   l_pipe_vert = 0.004
   r_si = 0.002
   r_torus = 2 * r_si
   dl = 2e-4
   l_si = 0.02 - dl

===================================
Obtain all the particle coordinates
===================================

We will first create the inlet, then the intestine, and finally the outlet.
The outlet is a mirror of the inlet, which can be created by using the ``mirror`` operation.
The inlet is composed of a verticle pipe, a torus bend, and a horizontal pipe, with the same
radius ``r_si``.

.. code-block:: python
   :linenos:

   pipe_in_vert = gp.CylinderSide(
       r=r_si, # radius of the cylinder
       l_axis=l_pipe_vert, # length along the cylinder axis
       dl=dl, # particle spacing
       axis='z' # cylinder axis direction
   ).shift(x=-r_torus - l_pipe_hrz, z=r_torus)
   l_pipe_vert = pipe_in_vert.l_axis
   n_ring = pipe_in_vert.n_ring

Although we have defined the length of the vertical pipe as ``l_pipe_vert``,
the actual length may be slightly different. So we update the variable ``l_pipe_vert`` here.

Now create the torus bend. 
But we should know how geoparticle defines the torus first.
The torus is created by revolving a circle along a circular path.
There two circles: the circle to be revolved and the path circle.
The former is called the cross-section circle, whose radius is the minor
radius :math:`r` and the center angle is :math:`\theta`.
The latter is called the path circle, whose radius is the major
radius :math:`R` and the center angle is :math:`\varphi`.

.. image:: static/torus.png

According to our dimension specification,
the minor radius is ``r_si``, and the major radius $R$ is ``r_torus``.
:math:`\varphi` ranges from 180 to 270 degrees.

.. code-block:: python
   :linenos:
   
   torus_in = gp.TorusSurface(
       r_minor=r_si,  # minor radius
       r_major=r_torus,  # major radius
       dl=dl,  # particle spacing
       n_ring=n_ring,  # number of particle rings along minor circle
       phi_range='(180,270)',  # angle range along major circle
       plane='XOZ'  # plane where the major circle lies
   ).shift(z=r_torus, x=-l_pipe_hrz)
   
Interval notation is used to define the range of :math:`\varphi`.
That is, ``[`` and ``]`` mean including the boundary, 
while ``(`` and ``)`` mean excluding the boundary.
We exclude the boundaries here to avoid overlapping with the two pipes.
Alternatively, one can set ``phi_range='(180,270]'``,
reduce the length of the horizontal pipe by ``dl``, and move it ``dl`` to the right accordingly.

Finally, create the horizontal pipe:

.. code-block:: python
   :linenos:
   
   pipe_in_hrz = gp.CylinderSide(
       r=r_si, l_axis=l_pipe_hrz - dl, dl=dl, axis='x', name='pipe_in_hrz'
   ).shift(x=-l_pipe_hrz)

Now we can assemble the three parts into an inlet:

.. code-block:: python
   :linenos:
   
   inlet = gp.Union((pipe_in_vert, torus_in, pipe_in_hrz))

Like the subtraction operation, there are three more ways to perform union:

- ``inlet = pipe_in_vert.union(torus_in, pipe_in_hrz)``

- ``inlet =  pipe_in_vert + torus_in + pipe_in_hrz``

- .. code-block:: python
     :linenos:
     
     inlet = gp.Geometry()
     inlet = pipe_in_vert
     inlet += torus_in
     inlet += pipe_in_hrz

