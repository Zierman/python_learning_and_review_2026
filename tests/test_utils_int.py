# pylint: disable=missing-function-docstring
import pytest

from utils.int import is_negative, is_odd


@pytest.mark.parametrize(
    ("param", "expected"), [pytest.param(0, False), pytest.param(1, True)]
)
def test_is_odd(param, expected):
    assert is_odd(param) == expected


@pytest.mark.parametrize(
    ("param", "expected"),
    [pytest.param(-1, True), pytest.param(0, False), pytest.param(1, False)],
)
def test_is_negative(param, expected):
    assert is_negative(param) == expected
