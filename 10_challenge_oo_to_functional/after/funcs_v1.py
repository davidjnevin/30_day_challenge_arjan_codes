from math import pi


def rect_area(width, height) -> float:
    return width * height


def rect_perimeter(width, height) -> float:
    return 2 * (width + height)


def circle_area(radius) -> float:
    return pi * radius**2


def circle_perimeter(radius) -> float:
    return 2 * pi * radius


def main() -> None:
    print("Total Area:", (rect_area(4, 5) + rect_area(3, 3) + circle_area(2)))
    print("Total Perimeter:", (rect_perimeter(4, 5) + rect_perimeter(3, 3) + circle_perimeter(2)))


if __name__ == "__main__":
    main()
