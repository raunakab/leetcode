"""
Leetcode link:
https://leetcode.com/problems/add-two-numbers/description
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    number: int
    next: Optional["Node"] = None


def add_two_numbers(
    n1: Node,
    n2: Node,
):
    carryover = 0
    current_n1: Optional[Node] = n1
    current_n2: Optional[Node] = n2
    result = None
    last = None

    while (current_n1 is not None) or (current_n2 is not None):
        if current_n1 is not None:
            a = current_n1.number
            current_n1 = current_n1.next
        else:
            a = 0
        if current_n2 is not None:
            b = current_n2.number
            current_n2 = current_n2.next
        else:
            b = 0

        sum = a + b + carryover
        if sum > 9:
            carryover = 1
            sum = sum - 10
        else:
            carryover = 0

        sumnode = Node(number=sum)
        if last:
            last.next = sumnode
        else:
            result = sumnode
        last = sumnode

    if carryover == 1:
        last.next = Node(number=1)

    return result


assert add_two_numbers(
    Node(number=0),
    Node(number=0),
) == Node(number=0)

assert add_two_numbers(
    Node(number=1),
    Node(number=2),
) == Node(number=3)

assert add_two_numbers(
    Node(number=9),
    Node(number=9),
) == Node(number=8, next=Node(number=1))

assert add_two_numbers(
    Node(number=9, next=Node(number=1)),
    Node(number=9, next=Node(number=1)),
) == Node(number=8, next=Node(number=3))

assert add_two_numbers(
    Node(number=9, next=Node(number=8)),
    Node(number=9, next=Node(number=1)),
) == Node(number=8, next=Node(number=0, next=Node(number=1)))

assert add_two_numbers(
    Node(number=0, next=Node(number=1)),
    Node(number=2),
) == Node(number=2, next=Node(number=1))
