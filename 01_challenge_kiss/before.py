from collections import defaultdict


def count_fruits(fruits: list[str]) -> dict[str, int]:
    # frequency counter
    # code here
    pass


def main() -> None:
    assert count_fruits(
        [
            "apple",
            "banana",
            "apple",
            "cherry",
            "banana",
            "cherry",
            "apple",
            "apple",
            "cherry",
            "banana",
            "cherry",
        ]
    ) == {"apple": 4, "banana": 3, "cherry": 4}
    assert count_fruits([]) == {}


if __name__ == "__main__":
    main()
