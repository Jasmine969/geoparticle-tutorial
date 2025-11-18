Limitations
============

The particle spacings may be not exactly as specified in order to create a smooth surface.

Resultant geometries of boolean operations can have more particles than expected in some cases, because

- For intersection and subtraction, only particles with distances smaller than ``rmax`` will be identified the same.
  Users should align particles of different geometries to get the expected results.

- For union, particles of all the given geometries will be collected to yield the union. Users should ensure no particles are overlapped.

``rmax`` can also be increased appropriately so that more particles can be identified the same.