"""
Leetcode link:
https://leetcode.com/problems/longest-substring-without-repeating-characters/description
"""


from typing import Set


def longest_substring(
    string: str
) -> int:
    longest_length = 0
    current_seen: Set[str] = set()

    for char in string:
        if char in current_seen:
            longest_length = max(longest_length, len(current_seen))
            current_seen.clear()

        current_seen.add(char)

    longest_length = max(longest_length, len(current_seen))
    return longest_length


assert longest_substring("") == 0
assert longest_substring("b") == 1
assert longest_substring("bbb") == 1
assert longest_substring("abc") == 3
assert longest_substring("abcabcab") == 3
assert longest_substring("abcabcdab") == 4
assert longest_substring("pwwkew") == 3
