from collections.abc import Callable

DEFAULT_ARRAY = range(5)


def demo_for_i_in_range():
    arr = []

    for i in range(5, 10, 2):
        arr.append(i)  # noqa: PERF402
        # I'm disabling the warning here because I know this is a
        # poor way to copy a the range to a list... doing it for demonstration of both
        # a for loop and the range function.

    return arr

# finds first match and returns it or None
# I know this is a very bad way to write this,
# but I'm trying to play with how the else clause works with a for loop
# not create clean code here
def demo_for_with_break_and_else(
    is_match: Callable[[int], bool], input_list: list[int] | None = None
) -> int | None:
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


def is_odd(i: int):
    return i % 2 != 0


def is_negative(i: int):
    return i < 0


def main():
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
