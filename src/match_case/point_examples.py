from point import Point


def demo_unpack_example(p: Point[int] | None) -> str:
    """Demonstrates pattern matching to unpack Point coordinates."""
    s = "Original Value"
    coordinate = p.coordinate_2d if p is not None else None

    # Note that only the first matching case executes and _ is a catchall
    match coordinate:
        case (0, 0):
            s = "origin"
        case (0, y):
            s = f"y = {y}"
        case (x, 0):
            s = f"x = {x}"
        case (x, y):
            s = f"x = {x} and y = {y}"
        case _:
            s = "No point provided"

    return s
