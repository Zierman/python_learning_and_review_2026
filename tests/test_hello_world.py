# pylint: disable=missing-function-docstring

import pytest

from hello_world import get_message


def test_with_no_argument():
    assert get_message() == "Hello, World!"


@pytest.mark.parametrize(
    "name, expected",
    [
        pytest.param("Tom", "Hello, Tom!", id="single word argument"),
        pytest.param("", "Hello!", id="empty string argument"),
        pytest.param("John Doe", "Hello, John Doe!", id="two word argument"),
        pytest.param(" Tom", "Hello, Tom!", id="argument with leading space"),
        pytest.param("Tom ", "Hello, Tom!", id="argument with trailing space"),
    ],
)
def test_with_argument(name: str, expected: str):
    assert get_message(name) == expected


@pytest.mark.parametrize(
    "name",
    [
        pytest.param(1, id="number argument"),
    ],
)
def test_with_error_producing_argument(name):
    with pytest.raises(TypeError):
        get_message(name)
