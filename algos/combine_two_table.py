"""
Leetcode link:
https://leetcode.com/problems/combine-two-tables/description
"""

from dataclasses import dataclass
from typing import List


NULL_STR = "NULL"


@dataclass
class Person:
    person_id: int
    first_name: str
    last_name: str


@dataclass
class Address:
    address_id: int
    person_id: int
    city: str
    state: str


def get_and_map(
    dict,
    key,
    map,
    default,
):
    if key in dict:
        element = dict[key]
        return map(element)
    else:
        return default


def combine_two_tables(
    person_table: List[Person],
    address_table: List[Address],
):
    person_map = {}
    address_map = {}

    for person in person_table:
        person_map[person.person_id] = person

    for address in address_table:
        address_map[address.person_id] = address

    merged_table = []
    for person_id, person in person_map.items():
        person: Person
        object = {
            "first_name": person.first_name,
            "last_name": person.last_name,
        }
        object["city"] = get_and_map(address_map, person_id, lambda address: address.city, NULL_STR)
        object["state"] = get_and_map(address_map, person_id, lambda address: address.state, NULL_STR)
        merged_table.append(object)

    return merged_table


assert combine_two_tables([], []) == []
assert combine_two_tables(
    [
        Person(person_id=0, first_name="A", last_name="B"),
    ],
    [],
) == [
    {
        "first_name": "A",
        "last_name": "B",
        "city": "NULL",
        "state": "NULL",
    }
]
