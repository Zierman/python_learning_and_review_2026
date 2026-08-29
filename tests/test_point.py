# pylint: disable=missing-function-docstring, unidiomatic-typecheck, singleton-comparison, missing-class-docstring, comparison-with-itself

from typing import Any

import pytest

from point import Point


class TestPoint(Point):
    def __init__(self, x: Any, y: Any, z: Any | None = None) -> None:
        super().__init__(x, y, z)
        self.note = "this is for testing only"


@pytest.mark.parametrize(
    ("coords", "expected_x", "expected_y", "expected_z", "expected_type"),
    [
        pytest.param((1, 2), 1, 2, 0, int, id="int: only x and y provided"),
        pytest.param((1, 2, 3), 1, 2, 3, int, id="int: only x and y provided"),
        pytest.param(
            (1.1, 2.2), 1.1, 2.2, 0.0, float, id="float: x, y, and z provided"
        ),
        pytest.param(
            (1.1, 2.2, 3.3), 1.1, 2.2, 3.3, float, id="float: x, y, and z provided"
        ),
    ],
)
def test_point_initialization(
    coords, expected_x, expected_y, expected_z, expected_type
):
    point = Point(*coords)

    assert point.x == expected_x
    assert point.y == expected_y
    assert point.z == expected_z
    assert type(point.x) is expected_type
    assert type(point.y) is expected_type
    assert type(point.z) is expected_type


@pytest.mark.parametrize(
    ("coords_1", "coords_2", "expected"),
    [
        pytest.param((0, 0, 0), (0, 0, 0), 0.0, id="int: origin to origin"),
        pytest.param((-1, -1, 0), (0, 1, 2), 3.0, id="int: origin to origin"),
        pytest.param(
            (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), 0.0, id="float: origin to origin"
        ),
        pytest.param(
            (0, 0, 0), (0.0, 0.0, 0.0), 0.0, id="int->float: origin to origin"
        ),
        pytest.param(
            (0.0, 0.0, 0.0), (0, 0, 0), 0.0, id="float->int: origin to origin"
        ),
    ],
)
def test_point_distance_to(coords_1, coords_2, expected):
    point_1 = Point(*coords_1)
    point_2 = Point(*coords_2)

    actual = point_1.distance_to(point_2)

    assert actual == pytest.approx(expected)
    assert isinstance(actual, float)


def test_point_clone():
    original = Point(1, 2, 3)
    clone = original.clone()

    # check that the clone has the correct x, y and z coordinates
    assert original is not clone
    assert original.x == clone.x
    assert original.y == clone.y
    assert original.z == clone.z

    # check that mutation doesn't affect the original
    clone.x = 0

    assert original.x == 1
    assert clone.x == 0


def test_point_equality():
    point_1 = Point(1, 2, 3)
    point_2 = Point(1, 2, 3)
    point_3 = Point(0, 2, 3)
    point_4 = Point(1, 0, 3)
    point_5 = Point(1, 2, 0)
    sub_class_point = TestPoint(1, 2, 3)

    # verify self equality
    assert point_1 == point_1  # noqa: PLR0124

    # verify non-self equality
    assert point_1 == point_2
    assert point_2 == point_1

    # verify inequality
    assert point_1 != point_3
    assert point_1 != point_4
    assert point_1 != point_5
    assert point_3 != point_1
    assert point_4 != point_1
    assert point_5 != point_1

    # verify subclass is equal
    assert point_1 == sub_class_point
    assert sub_class_point == point_1

    # verify other types are not equal
    assert point_1 != None
    assert None != point_1
    assert point_1 != 1
    assert 1 != point_1


@pytest.mark.parametrize(
    ("coords_1", "coords_2", "expected"),
    [
        pytest.param((0, 0, 0), (0, 0, 0), (0, 0, 0)),
        pytest.param((1, 2, 3), (10, 20, 30), (11, 22, 33)),
    ],
)
def test_add(coords_1, coords_2, expected):
    point_1 = Point(*coords_1)
    point_2 = Point(*coords_2)

    actual = point_1 + point_2

    # make sure that the result is as expected
    assert actual.x == expected[0]
    assert actual.y == expected[1]
    assert actual.z == expected[2]

    # make sure that we don't mutate either original point
    assert point_1.x == coords_1[0]
    assert point_1.y == coords_1[1]
    assert point_1.z == coords_1[2]

    assert point_2.x == coords_2[0]
    assert point_2.y == coords_2[1]
    assert point_2.z == coords_2[2]


@pytest.mark.parametrize(
    ("coords_1", "coords_2", "expected"),
    [
        pytest.param((0, 0, 0), (0, 0, 0), (0, 0, 0)),
        pytest.param((1, 2, 3), (10, 20, 30), (11, 22, 33)),
    ],
)
def test_iadd(coords_1, coords_2, expected):
    point_1 = Point(*coords_1)
    point_2 = Point(*coords_2)

    point_1 += point_2

    # make sure that we don't mutate either original point
    assert point_1.x == expected[0]
    assert point_1.y == expected[1]
    assert point_1.z == expected[2]

    assert point_2.x == coords_2[0]
    assert point_2.y == coords_2[1]
    assert point_2.z == coords_2[2]


@pytest.mark.parametrize(
    ("coords_1", "scalar", "expected"),
    [
        pytest.param((1, 2, 3), 2, (2, 4, 6), id="multiply by 2"),
        pytest.param((1, 2, 3), -1, (-1, -2, -3), id="multiply by -1"),
    ],
)
def test_mul(coords_1, scalar, expected):
    point_1 = Point(*coords_1)

    actual = point_1 * scalar

    # make sure that the result is as expected
    assert actual.x == expected[0]
    assert actual.y == expected[1]
    assert actual.z == expected[2]

    # make sure that we don't mutate either original point
    assert point_1.x == coords_1[0]
    assert point_1.y == coords_1[1]
    assert point_1.z == coords_1[2]


@pytest.mark.parametrize(
    ("coords_1", "scalar", "expected"),
    [
        pytest.param((1, 2, 3), 2, (2, 4, 6), id="r-multiply by 2"),
        pytest.param((1, 2, 3), -1, (-1, -2, -3), id="r-multiply by -1"),
    ],
)
def test_rmul(coords_1, scalar, expected):
    point_1 = Point(*coords_1)

    actual = scalar * point_1

    # make sure that the result is as expected
    assert actual.x == expected[0]
    assert actual.y == expected[1]
    assert actual.z == expected[2]

    # make sure that we don't mutate either original point
    assert point_1.x == coords_1[0]
    assert point_1.y == coords_1[1]
    assert point_1.z == coords_1[2]


@pytest.mark.parametrize(
    ("coords_1", "scalar", "expected"),
    [
        pytest.param((1, 2, 3), 2, (2, 4, 6), id="inplace-multiply by 2"),
        pytest.param((1, 2, 3), -1, (-1, -2, -3), id="inplace-multiply by -1"),
    ],
)
def test_imul(coords_1, scalar, expected):
    point_1 = Point(*coords_1)

    point_1 *= scalar

    # make sure that we don't mutate either original point
    assert point_1.x == expected[0]
    assert point_1.y == expected[1]
    assert point_1.z == expected[2]


def test_point_str():
    assert str(Point(1, 2, 3)) == "(1, 2, 3)"


def test_point_repr():
    assert repr(Point(1, 2, 3)) == "(1, 2, 3)"
