from collections.abc import Callable

DEFAULT_ARRAY = range(5)


def demo_for_i_in_range():
    """Demo for a simple for look using range function

    Returns: an array created by appending each item when looping through the range(5, 10, 2)"""
    arr = []

    for i in range(5, 10, 2):
        arr.append(i)  # noqa: PERF402
        # I'm disabling the warning here because I know this is a
        # poor way to copy a the range to a list... doing it for demonstration of both
        # a for loop and the range function.

    return arr


def demo_for_with_break_and_else(
    is_match: Callable[[int], bool], input_list: list[int] | None = None
) -> int | None:
    """Demo to demonstrate the else clause when used with a look with a break

    Args:
      is_match: a callable that returns whether the integer
        provided as an argument should be considered a match.
      input_list: a list of integers that will be evaluated via a for loop.

    Returns: either the first found int based on the is_match argument, or None"""

    # finds first match and returns it or None
    # I know this is a very bad way to write this,
    # but I'm trying to play with how the else clause works with a for loop
    # not create clean code here
    return_value: int = 0

    if input_list is None:
        input_list = list(DEFAULT_ARRAY)

    for item in input_list:
        if is_match(item):
            return_value = item
            break
    else:
        return None

    return return_value


def is_odd(i: int) -> bool:
    """Return True if the given integer is odd.

    Args:
        i: Integer to check.

    Returns:
        True if i is odd, otherwise False.
    """

    return i % 2 != 0


def is_negative(i: int) -> bool:
    """Return True if the given integer is negative.

    Args:
        i: Integer to check.

    Returns:
        True if i is negative, otherwise False.
    """

    return i < 0


def main():  # pylint: disable=missing-function-docstring
    print("Demo for i in range (expect 5, 7, 9):")
    print(demo_for_i_in_range())
    print()
    print("Demo for with break and else (expect 1):")
    print(demo_for_with_break_and_else(is_odd))
    print()
    print("Demo for with break and else (expect None):")
    print(demo_for_with_break_and_else(is_negative))


if __name__ == "__main__":
    main()
