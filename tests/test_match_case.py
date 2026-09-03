# pylint: disable=missing-function-docstring
import pytest

from match_case import demo_class_unpack_example, demo_unpack_example
from point import Point


@pytest.mark.parametrize(
    "point, expected_string",
    [
        pytest.param(Point(0, 0), "origin", id="(0,0)"),
        pytest.param(Point(0, 1), "y = 1", id="(0,1)"),
        pytest.param(Point(1, 0), "x = 1", id="(1,0)"),
        pytest.param(Point(1, 2), "x = 1 and y = 2", id="(1,2)"),
        pytest.param(None, "No point provided", id="None"),
    ],
)
def test_demo_unpack_example(
    point: Point, expected_string: str
):  # I know I should probably use test doubles... I'll explore that later
    actual = demo_unpack_example(point)
    assert actual == expected_string, (
        f"expect {expected_string!r} when input is {point!r}."
    )


@pytest.mark.parametrize(
    "point, expected_string",
    [
        pytest.param(Point(0, 0), "3D origin", id="(0,0)"),
        pytest.param(
            Point(0, 0, 1),
            "Can be projected to the origin on the x,y plane, but z is 1",
            id="(0, 0, 1)",
        ),
        pytest.param(
            Point(1, 2, 0),
            "Point (1, 2) on the x,y plane with z value of zero",
            id="(1, 2, 0)",
        ),
        pytest.param(Point(1, 2, 3), "A point at (1, 2, 3)", id="(1, 2, 3)"),
        pytest.param(None, "No point provided", id="None"),
    ],
)
def test_demo_class_unpack_example(
    point: Point, expected_string: str
):  # I know I should probably use test doubles... I'll explore that later
    actual = demo_class_unpack_example(point)
    assert actual == expected_string, (
        f"expect {expected_string!r} when input is {point!r}."
    )
