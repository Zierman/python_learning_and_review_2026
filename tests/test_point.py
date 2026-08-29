# pylint: disable=missing-function-docstring, unidiomatic-typecheck

import pytest

from point import Point


@pytest.mark.parametrize(
    ("coords", "expected_x", "expected_y", "expected_z", "expected_type"),
    [
        pytest.param((1, 2), 1, 2, 0, int, id="int: only x and y provided"),
        pytest.param((1, 2, 3), 1, 2, 3, int, id="int: only x and y provided"),
        pytest.param((1.1, 2.2), 1.1, 2.2, 0.0, float, id="float: x, y, and z provided"),
        pytest.param((1.1, 2.2, 3.3), 1.1, 2.2, 3.3, float, id="float: x, y, and z provided"),
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
def test_distance_to(coords_1, coords_2, expected):
    point_1 = Point(*coords_1)
    point_2 = Point(*coords_2)

    actual = point_1.distance_to(point_2)

    assert actual == pytest.approx(expected)
    assert isinstance(actual, float)
