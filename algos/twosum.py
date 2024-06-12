"""
Leetcode link:
https://leetcode.com/problems/two-sum/description
"""

def two_sum(
    nums,
    target,
):
    map = {}
    for index, num in enumerate(nums):
        if num in map:
            map[num].append(index)
        else:
            map[num] = [index]
    for index, num in enumerate(nums):
        complement = target - num
        if complement in map:
            complement_indices = map[complement]
            for complement_index in complement_indices:
                if complement_index != index:
                    i1 = min(index, complement_index)
                    i2 = max(index, complement_index)
                    return i1, i2

    return None


# No solutions
assert two_sum([], 0) is None
assert two_sum([0, 1], 2) is None
assert two_sum([1], 1) is None

# At least one solution exists
assert two_sum([0, 1], 1) == (0, 1)
assert two_sum([1, 2, 1], 2) == (0, 2)
