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


def demo_class_unpack_example(p: Point[int] | None) -> str:
    """Demonstrates pattern matching to unpack Point properties."""
    s = "Original Value"

    # Note that only the first matching case executes and _ is a catchall
    match p:
        case Point(x=0, y=0, z=0):
            s = "3D origin"
        case Point(x=0, y=0, z=z):
            s = f"Can be projected to the origin on the x,y plane, but z is {z}"
        case Point(x=x, y=y, z=0):
            s = f"Point ({x}, {y}) on the x,y plane with z value of zero"
        case Point(coordinate_3d=coords):
            s = f"A point at {coords}"
        case _:
            s = "No point provided"

    return s
