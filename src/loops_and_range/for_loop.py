from collections.abc import Callable
from typing import Final

from utils.int import is_negative, is_odd

DEFAULT_LIST: Final[range] = range(
    5
)  # using Final typing to explicitly type a constant


def demo_for_with_continue_and_break(
    break_target: int, target_sum: int, input_list: list[int]
) -> list[list[int]]:
    """Demonstrate break and continue behavior within a for loop.

    Args:
        break_target: the value at which the whole loop will break
        target_sum: the target that the
        input_list: the list that will be iterated.
    Returns:
        A list of intermediate sums accumulated before the loop exits.
    """
    intermediate_list: list[int] = []
    output_list: list[list[int]] = []
    intermediate_sum = 0

    for i in input_list:
        intermediate_sum += i
        if i == break_target:
            # We break out the loop rather than continue to the next loop iteration
            break

        intermediate_list.append(intermediate_sum)

        if intermediate_sum > target_sum:
            # Reset intermediate values
            intermediate_list.clear()
            intermediate_sum = 0

            # Add empty list to output_list for this loop
            output_list.append([])

            # Continue to the next iteration of the loop w/o executing
            # any following commands in the loop
            continue

        output_list.append(
            intermediate_list.copy()  # This needs to stor a copy so it doesn't mutate
        )  # Note that this will not execute if continue or break execute
    return output_list


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
        input_list = list(DEFAULT_LIST)

    for item in input_list:
        if is_match(item):
            return_value = item
            break
    else:
        return None

    return return_value


def main():  # pylint: disable=missing-function-docstring
    print("Demo for with break and else (expect 1):")
    print(demo_for_with_break_and_else(is_odd))
    print()
    print("Demo for with break and else (expect None):")
    print(demo_for_with_break_and_else(is_negative))


if __name__ == "__main__":
    main()
