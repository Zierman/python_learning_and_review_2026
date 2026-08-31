from collections.abc import Callable
from typing import Final

DEFAULT_LIST: Final[range] = range(
    5
)  # using Final typing to explicitly type a constant


def demo_for_i_in_range():
    """Demo for a simple for look using range function

    Returns: a list created by appending each item when looping through the range(5, 10, 2)"""
    arr = []

    for i in range(5, 10, 2):
        arr.append(i)  # noqa: PERF402
        # I'm disabling the warning here because I know this is a
        # poor way to copy a the range to a list... doing it for demonstration of both
        # a for loop and the range function.

    return arr


def demo_for_i_in_range_of_len[T](
    is_match: Callable[[T], bool], input_list: list[T]
) -> list[int]:
    """

    Args:
      is_match: a callable that returns a boolean if the provided argument is a match
      input_list: a list of items to find matches in

    Returns: a list of indexes for all matches in the input_list based on the is_match function"""

    output_list: list[int] = []

    # I'm not using enumerate here because this is what is in the tutorial for the for loop
    for i in range(len(input_list)):  # pylint: disable=consider-using-enumerate
        if is_match(input_list[i]):
            output_list.append(i)

    return output_list


def main():  # pylint: disable=missing-function-docstring
    print("Demo for i in range (expect 5, 7, 9):")
    print(demo_for_i_in_range())


if __name__ == "__main__":
    main()
