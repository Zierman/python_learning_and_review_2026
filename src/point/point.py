import math


# pylint: disable=too-few-public-methods
class Point[T: int | float]:
    """A class representing a point in space

    If z is not provided, the point is assumed to lie on the XY plane and z
    defaults to zero (as a float or int to match the coordinate types).
    The class is intended for numeric coordinate types (int or float).

    I'm intentionally using generics here and avoiding using complex or imaginary numbers.
    """

    def __init__(self, x: T, y: T, z: T | None = None) -> None:

        self.x = x
        self.y = y
        self.z = z if z is not None else 0.0 if self._is_float_type() else 0

    def _is_float_type(self) -> bool:
        return isinstance(self.x, float)

    def distance_to(self, other_point: "Point") -> float:
        """calculates the distance between this point and another point"""
        d_x = abs(self.x - other_point.x)
        d_y = abs(self.y - other_point.y)
        d_z = abs(self.z - other_point.z)

        return math.sqrt(d_x**2 + d_y**2 + d_z**2)

    def clone(self) -> "Point":
        """Return a shallow copy of this Point."""

        return Point(self.x, self.y, self.z)

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self) -> str:
        return str(self)

    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __iadd__(self, other: "Point"):
        self.x += other.x
        self.y += other.y
        self.z += other.z

        return self

    def __mul__(self, other):
        return Point(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        self.x *= other
        self.y *= other
        self.z *= other

        return self

    def __eq__(self, other: object) -> bool:
        if self is other:
            return True
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y and self.z == other.z
