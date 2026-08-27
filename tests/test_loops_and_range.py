# pylint: disable=missing-function-docstring

from collections.abc import Callable

import pytest

from loops_and_range import (
    demo_for_i_in_range,
    demo_for_i_in_range_of_len,
    demo_for_with_break_and_else,
    demo_for_with_continue_and_break,
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
    "break_target, target_sum, input_list, expected",
    [
        pytest.param(
            3,
            0,
            [-1, 0, 1, 2, -5, 3, 5],
            [
                [-1],
                [-1, -1],
                [-1, -1, 0],
                [],  # this is empty list because the intermediate
                # sum was greater that the target_sum 0
                #
                [-5],  # this is the last item the next item
                # value is equal to the break_trigger 3
                #
            ],
            id="happy path",
        ),
        pytest.param(
            3,
            0,
            [],
            [],
            id="if the input_list is empty the output list should be empty",
        ),
        pytest.param(
            9,
            0,
            [-1, 0, 1, 2, -5, 3, 5],
            [
                [-1],
                [-1, -1],
                [-1, -1, 0],
                [],  # this is empty list because the intermediate
                # sum was greater that the target_sum 0
                #
                [-5],
                [-5, -2],
                [],  # this is empty list because the intermediate
                # sum was greater that the target_sum 0
            ],
            id="If the break_trigger is absent the loop won't end until all items are iterated",
        ),
        pytest.param(
            3,
            99,
            [-1, 0, 1, 2, -5, 3, 5],
            [
                [-1],
                [-1, -1],
                [-1, -1, 0],
                [-1, -1, 0, 2],
                [-1, -1, 0, 2, -3],  # this is the last item the next item
                # value is equal to the break_trigger 3
                #
            ],
            id="If the trigger_sum is larger than any possible sum all elements "
            "will be included until break",
        ),
        pytest.param(
            3,
            -99,
            [-1, 0, 1, 2, -5, 3, 5],
            [
                [],
                [],
                [],
                [],
                [],  # this is the last item the next item
                # value is equal to the break_trigger 3
                #
            ],
            id="If the trigger_sum is smaller than any possible sum all items in "
            "returned list will be empty lists",
        ),
    ],
)
def test_demo_for_with_continue_and_break(
    break_target: int, target_sum: int, input_list: list[int], expected: str
):
    assert (
        demo_for_with_continue_and_break(break_target, target_sum, input_list)
        == expected
    )


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
