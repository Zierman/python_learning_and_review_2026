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
