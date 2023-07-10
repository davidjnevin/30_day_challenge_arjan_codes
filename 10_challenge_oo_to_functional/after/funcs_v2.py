from math import pi
from typing import Callable

Shapefn = Callable[..., float]
Shape = tuple[float, float, Shapefn, Shapefn]


def rectangle(width: float, height: float) -> Shape:
    def area() -> float:
        return width * height

    def perimeter() -> float:
        return 2 * (width + height)

    return (width, height, area, perimeter)


def square(side_lenght: float) -> Shape:
    def area() -> float:
        return side_lenght * side_lenght

    def perimeter() -> float:
        return 2 * (side_lenght + side_lenght)

    return (side_lenght, side_lenght, area, perimeter)


def circle(radius: float) -> Shape:
    def area() -> float:
        return pi * radius**2

    def perimeter() -> float:
        return 2 * pi * radius

    return (radius, radius, area, perimeter)

def total_area(shapes: list[Shape]) -> float:
    return sum(shape[2]() for shape in shapes)

def total_perimeter(shapes: list[Shape]) -> float:
    return sum(shape[3]() for shape in shapes)

def main() -> None:
    shapes: list[Shape] = [rectangle(4,5), square(3), circle(2)]
    print("Total Area:", total_area(shapes))
    print("Total Perimeter:", total_perimeter(shapes))


if __name__ == "__main__":
    main()
