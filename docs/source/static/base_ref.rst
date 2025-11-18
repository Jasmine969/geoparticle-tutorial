Geometry
========

.. py:class:: Geometry(name: str | None = None, dimension: int | None = None)

   Base class for geometry objects with utilities for coordinate storage and
   vector-space operations. Instances store point coordinates in three arrays
   and expose common set-like operations (union, subtract, intersect).

   :param name: Optional instance name; defaults to ``"<ClassName> <counter>"``.
   :type name: str | None
   :param dimension: Geometric dimension hint (2 or 3).
   :type dimension: int | None

Attributes
----------

.. py:attribute:: xs
.. py:attribute:: ys
.. py:attribute:: zs

   1D float arrays of X/Y/Z coordinates.

.. py:attribute:: name

   Instance name.

.. py:attribute:: dimension

   Dimension hint (2 or 3).

Properties
----------

.. py:property:: size -> int

   Number of points.

.. py:property:: matrix_coords -> numpy.ndarray

   Shape ``(N, 3)`` array of coordinates.

.. py:property:: flatten_coords -> numpy.ndarray

   Shape ``(3N,)`` flattened coordinates.

Class Methods
-------------

.. py:method:: Geometry.get_counter() -> int
   :classmethod:

   Return the class-wide instance counter.

Construction and Copy
---------------------

.. py:method:: copy() -> Geometry

   Deep-copy the instance.

Coordinate Management
---------------------

.. py:method:: set_coord(xs, ys, zs) -> Geometry

   Set coordinates; scalars are broadcast if any array size is known.

   :param xs: X coordinates (scalar or array-like).
   :param ys: Y coordinates (scalar or array-like).
   :param zs: Z coordinates (scalar or array-like).
   :raises TypeError: Scalar without size hint.
   :raises ValueError: Mismatched array sizes.

Transformations
---------------

.. py:method:: shift(x: float = 0.0, y: float = 0.0, z: float = 0.0) -> Geometry

   Translate by offsets. Returns a new object.

.. py:method:: mirror(plane_name: str, plane_pos: float) -> Geometry

   Mirror across principal plane ``'YOZ'``, ``'XOY'``, or ``'XOZ'`` at position.

   :raises ValueError: Invalid plane name.

.. py:method:: rotate(angle_deg: float, axis_direction: str | None = None, *, axis_point1: Iterable[float] | None = None, axis_point2: Iterable[float] | None = None) -> Geometry

   Rotate around a principal axis (``'x'|'y'|'z'``) optionally about a point, or
   around a custom axis defined by two points. Returns a new object.

   :raises ValueError: Invalid axis specification or degenerate axis.

Set-like Operations
-------------------

.. py:method:: union(geometries: Geometry | Iterable[Geometry], name: str | None = None) -> Geometry

   Concatenate points of ``self`` and others. Returns a new ``Geometry``.

.. py:method:: subtract(geo2: Geometry, rmax: float = 1e-5, name: str | None = None) -> Geometry

   Keep points of ``self`` that are at least ``rmax`` away from any point in ``geo2``.

.. py:method:: intersect(geometries: Geometry | Iterable[Geometry], rmax: float = 1e-5, name: str | None = None) -> Geometry

   Keep points of ``self`` within ``rmax`` of at least one point in every geometry.

Stacking and Clipping
---------------------

.. py:method:: stack(axis: str, n_axis: int, dl: float, dimension: int, name: str | None = None) -> Geometry

   Stack a planar layer along an axis by repeating with spacing ``dl``.
   ``n_axis`` sign sets direction. Requires planarity orthogonal to axis.

   :raises ValueError: Invalid axis or non-planar input.

.. py:method:: clip(keep: str, *, plane_name: str | None = None, plane_normal: list[float] | tuple[float, float, float] | numpy.ndarray | None = None, plane_point: list[float] | tuple[float, float, float] | numpy.ndarray | None = None, name: str | None = None) -> Geometry

   Clip by a half-space. Use named plane ``'XOY'|'XOZ'|'YOZ'`` or an arbitrary
   plane given by normal and point.

   :param keep: ``'positive'`` keeps points with non-negative signed distance; ``'negative'`` keeps non-positive.
   :raises ValueError: Invalid arguments or zero normal.

Queries and Utilities
---------------------

.. py:method:: get_and_delete(ids: numpy.ndarray) -> Geometry

   Extract points by indices and remove them from ``self``. Returns the extracted points.

.. py:method:: coord2id(x: float, y: float, z: float) -> tuple[list[int], numpy.ndarray]

   Return indices of nearest points and their coordinates.

.. py:method:: equal(geo: Geometry) -> bool

   Test coordinate-wise equality.

.. py:method:: check_overlap(tol: float = 1e-10) -> None

   Warn if nearest-neighbor distance is below ``tol``.

.. py:method:: plot(ax=None, ms=None, alpha=None, **scatter_kwargs)

   Scatter-plot points (2D or 3D). Returns axes if provided; otherwise shows the figure.

Operators
---------

.. py:method:: __add__(other: Geometry) -> Geometry

   Union of two geometries. ``geo1 + geo2`` is ``geo1.union(geo2)``.

.. py:method:: __iadd__(other: Geometry) -> Geometry

   In-place add. Returns a new union result; assign back by Python semantics.

.. py:method:: __sub__(other: Geometry) -> Geometry

   Subtract ``other`` from ``self``. ``geo1 - geo2`` is ``geo1.subtract(geo2)``.

.. py:method:: __isub__(other: Geometry) -> Geometry

   In-place subtract. Returns a new subtraction result; assign back by Python semantics.
