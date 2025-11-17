Background
==========

Particles of specified geometries are typically created by the ``lattice`` command in LAMMPS, which can lead to rough surfaces when the particle spacing is not small enough. However, too small spacing can result in too many particles and thus increase the computational cost.

.. image:: https://fengimages-1310812903.cos.ap-shanghai.myqcloud.com/20240402203849.png

The case is the same when one creates atoms based on an external STL file (an example STL file exported by COMSOL is shown below):

.. image:: https://fengimages-1310812903.cos.ap-shanghai.myqcloud.com/20251117123120.png

To resolve this problem, I developed this package for easy construction of geometries where smooth surfaces are required.
