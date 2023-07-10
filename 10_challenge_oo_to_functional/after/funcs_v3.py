from functools import partial
from math import pi
from typing import Callable


def rect_area(width, height) -> float:
    return width * height


def rect_perimeter(width, height) -> float:
    return 2 * (width + height)


def square_area(side_length) -> float:
    return side_length ** 2


def square_perimeter(side_length) -> float:
    return 4 * (side_length)

def circle_area(radius) -> float:
    return pi * radius**2


def circle_perimeter(radius) -> float:
    return 2 * pi * radius

def calculate_total(*args: Callable[[], float]) -> float:
    return sum(arg() for arg in args)

def main() -> None:

    print(
        "Total Area:",
        calculate_total(partial(rect_area, 4, 5), partial(square_area, 3), partial(circle_area, 2)),
    )
    print("Total Perimeter:",
        calculate_total(partial(rect_perimeter, 4, 5), partial(square_perimeter, 3), partial(circle_perimeter, 2)),
          )


if __name__ == "__main__":
    main()
