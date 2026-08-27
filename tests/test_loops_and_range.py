# pylint: disable=missing-function-docstring

from collections.abc import Callable

import pytest

from loops_and_range import (
    demo_for_i_in_range,
    demo_for_i_in_range_of_len,
    demo_for_with_break_and_else,
)


@pytest.mark.parametrize(
    "is_match, input_list, expected",
    [
        pytest.param(lambda _: True, [], None, id="empty array"),
        pytest.param(
            lambda _: True,
            [1, 2],
            1,
            id="First element returned when is_match always returns True",
        ),
        pytest.param(
            lambda _: True,
            None,
            0,
            id="Expected first element returned when is_match "
            "always returns True and default list is used",
        ),
        pytest.param(
            lambda _: False,
            [1, 2],
            None,
            id="None returned when is_match always returns False",
        ),
        pytest.param(
            lambda number: number % 2 == 0,
            [1, 2, 3, 4],
            2,
            id="Second element returned when is_match returns True "
            "for the second and fourth elements in the list",
        ),
        pytest.param(
            lambda number: number % 2 != 0,
            None,
            1,
            id="Second element (which has value 1) returned when is_match returns True "
            "for the second and fourth elements in the list when default list is used",
        ),
    ],
)
def test_demo_for_with_break_and_else(
    is_match: Callable, input_list: list[int] | None, expected: str
):
    assert demo_for_with_break_and_else(is_match, input_list) == expected


@pytest.mark.parametrize(
    "is_match, input_list, expected",
    [
        pytest.param(
            lambda _: True,
            [],
            [],
            id="An empty list should be returned when an empty list is provided",
        ),
        pytest.param(
            lambda _: True,
            [1, 3],
            [0, 1],
            id="All indexes in returned list when is_match always returns True",
        ),
        pytest.param(
            lambda _: False,
            [1, 2],
            [],
            id="Empty list returned when is_match always returns False",
        ),
        pytest.param(
            lambda number: number % 2 == 0,
            [1, 2, 3, 4],
            [1, 3],
            id="Only index values 1 and 3 are in the returned list when "
            "is_match returns True "
            "for the second and fourth elements in the list",
        ),
    ],
)
def test_demo_for_i_in_range_of_len(
    is_match: Callable, input_list: list[int], expected: str
):
    assert demo_for_i_in_range_of_len(is_match, input_list) == expected


def test_demo_for_i_in_range():
    assert demo_for_i_in_range() == [5, 7, 9]
