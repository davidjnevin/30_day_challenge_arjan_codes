from collections import defaultdict


def count_fruits(fruits: list[str]) -> dict[str, int]:
    # frequency counter
    frequency_dict = defaultdict(int)
    for fruit in fruits:
        if frequency_dict[fruit]:
            frequency_dict[fruit] += 1
        else:
            frequency_dict[fruit] = 1
    return frequency_dict



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
    assert count_fruits(["pear"]) == {"pear": 1}# add more tests


if __name__ == "__main__":
    main()
