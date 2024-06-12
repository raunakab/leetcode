"""
Leetcode link:
https://leetcode.com/problems/valid-sudoku/description
"""

from typing import List, Optional, Set


"""
[
        x->
    y  [...],
    |   ... ,
    V  [...],
]
"""


def check_helper(
    nums,
    el,
) -> bool:
    if el:
        if el in nums:
            return False
        else:
            nums.add(el)

    return True


def is_valid_sudoku(
    board: List[List[Optional[int]]],
) -> bool:
    nums: Set[int] = set()

    # process rows:
    for row in board:
        for row_el in row:
            if not check_helper(nums, row_el):
                return False
        nums.clear()

    # process columns:
    for x in range(9):
        for y in range(9):
            el = board[y][x]
            if not check_helper(nums, el):
                return False
        nums.clear()

    # process squares:
    for y_offset in range(3):
        for x_offset in range(3):
            y_off = y_offset * 3
            x_off = x_offset * 3

            for y in range(3):
                for x in range(3):
                    el = board[y + y_off][x + x_off]
                    if not check_helper(nums, el):
                        return False

            nums.clear()

    return True


def prep(
    board: List[List[str]],
) -> List[List[Optional[int]]]:
    prepped_board = []

    for row in board:
        prepped_row: List[Optional[int]] = []
        for el in row:
            if el == ".":
                prepped_row.append(None)
            else:
                prepped_row.append(int(el))

        prepped_board.append(prepped_row)

    return prepped_board


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
assert is_valid_sudoku(prep(board))

board = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
assert not is_valid_sudoku(prep(board))
