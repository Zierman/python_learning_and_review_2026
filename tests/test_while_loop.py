# pylint: disable=missing-function-docstring
import pytest

from loops_and_range import demo_while_with_else


@pytest.mark.parametrize(
    "target, break_target, expected_list",
    [
        pytest.param(
            -5, 6, [-1], id="a) negative target should result in a list with only -1"
        ),
        pytest.param(
            0, 6, [-1], id="b) target value 0 should result in a list with only -1"
        ),
        pytest.param(
            1,
            6,
            [0, -1],
            id="c) if target is 1 but break_target is higher we will execute the else "
            "block because the while condition will be evaluated as False",
        ),
        pytest.param(
            2,
            1,
            [0, 1],
            id="d) if target 2 and break_target is 1 the else block will not run because "
            "the while condition is never evaluated as False",
        ),
        pytest.param(
            1,
            1,
            [0, -1],
            id="e) if target and break target are both 1 we should get [0, -1]",
        ),
    ],
)
def test_demo_while_with_else(target: int, break_target: int, expected_list: list[int]):
    actual = demo_while_with_else(target, break_target)
    assert actual == expected_list, (
        f"expect {expected_list} when target is {target} and "
        f"break_target is {break_target} but got {actual}"
    )
