import itertools
import operator
from dataclasses import dataclass
from faker import Faker
import random


@dataclass
class Person:
    name: str
    age: int
    city: str
    country: str


# Instantiate the Faker module
fake = Faker()

# List of possible countries
countries = [
    "UK",
    "USA",
    "Japan",
    "Australia",
    "France",
    "Germany",
    "Italy",
    "Spain",
    "Canada",
    "Mexico",
]

# Generate 1000 random Person instances
PERSON_DATA: list[Person] = [
    Person(fake.name(), random.randint(18, 70), fake.city(), random.choice(countries))
    for _ in range(1000)
]


def main() -> None:
    # filtered_data: list[Person] = []
    # for person in PERSON_DATA:
    #     if person.age >= 21:
    #         filtered_data.append(person)
    filtered_data = list(
        itertools.filterfalse(lambda person: person.age < 21, PERSON_DATA)
    )

    # Sort data
    filtered_data.sort(key=operator.attrgetter("country"))

    # Group data by country
    grouped_data = itertools.groupby(filtered_data, key=lambda person: person.country)

    # Create a summary dict from the grouped data
    summary = {country: len(list(group)) for country, group in grouped_data}
    # summary: dict[str, int] = {}
    # for person in filtered_data:
    #     if person.country not in summary:
    #         summary[person.country] = 0
    #     summary[person.country] += 1

    print(summary)


if __name__ == "__main__":
    main()
