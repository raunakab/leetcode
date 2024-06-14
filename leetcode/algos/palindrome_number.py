"""
Leetcode link:
https://leetcode.com/problems/palindrome-number/description
"""


def is_palindrome_number(number: int) -> bool:
    num = str(number)
    length = len(num)

    is_palindrome = True
    start = 0
    end = length - 1

    while start <= end:
        a = num[start]
        b = num[end]
        if a == b:
            start += 1
            end -= 1
        else:
            is_palindrome = False
            break

    return is_palindrome


assert is_palindrome_number(0)
assert is_palindrome_number(101)
assert is_palindrome_number(1001)

assert not is_palindrome_number(10)
assert not is_palindrome_number(1011)
