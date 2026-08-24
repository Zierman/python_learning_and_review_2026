from collections.abc import Callable

import pytest

from loops_and_range import demo_for_with_break_and_else, demo_for_i_in_range


@pytest.mark.parametrize(
    "is_match, input_list, expected",
    [
        pytest.param(lambda _: True, [], None, id="empty array"),
        pytest.param(
            lambda _: True,
            [1, 2],
            1,
            id="first element returned when is_match always returns True",
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
            id="second element returned when is_match returns True for the second and fourth elements in the list",
        ),
    ],
)
def test_demo_for_with_break_and_else(
    is_match: Callable, input_list: list[int], expected: str
):
    assert demo_for_with_break_and_else(is_match, input_list) == expected


def test_demo_for_i_in_range():
    assert demo_for_i_in_range() == [5, 7, 9]
