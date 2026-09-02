def demo_while_with_else(target: int, break_target: int) -> list[int]:
    """Demonstrate while loop with else clause.

    Args:
        target: The upper limit for the loop counter.
        break_target: Condition to break out of the loop.

    Returns:
        A list of integers from the loop, or [-1] if else clause executes.
    """

    output_list: list[int] = []
    i = 0

    while i < target:
        output_list.append(i)
        if i is break_target:
            break  # if we execute this break the else block will not execute
        i += 1
    else:  # this will only execute if the condition for the while loop evaluates as false
        output_list.append(-1)
    return output_list
