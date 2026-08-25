def get_message(to: str | None = None) -> str:
    """Return a greeting message for `to` or a default.

    Args:
        to: Optional name to include in the greeting.
        If None a typical "Hello, World!" message is returned.
        If an empty string, it will instead just say "Hello!"

    Returns:
        A greeting string such as "Hello, John!" or "Hello!".
    """

    # Check that the argument is typed correctly
    if to is not None and not isinstance(to, str):
        raise TypeError("argument `to` must be of type str or None")

    name = to.strip() if to is not None else "World"

    return f"Hello, {name}!" if len(name) > 0 else "Hello!"


def main():  # pylint: disable=missing-function-docstring
    print("Demonstration of get_message function:")
    print(f'get_message() outputs "{get_message()}"')
    print(f'get_message("John") outputs "{get_message("John")}"')


if __name__ == "__main__":
    main()
