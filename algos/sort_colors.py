"""
Leetcode link:
https://leetcode.com/problems/sort-colors/description
"""


RED = 0
WHITE = 1
BLUE = 2


def sort_color(colors):
    freqs = [0, 0, 0]

    for color in colors:
        freqs[color] += 1

    offset = 0
    for color, freq in enumerate(freqs):
        for i in range(freq):
            colors[offset + i] = color
        offset += freq


colors = [RED, RED, RED]
sort_color(colors)
assert colors == [RED, RED, RED]

colors = [WHITE, RED, RED]
sort_color(colors)
assert colors == [RED, RED, WHITE]

colors = [BLUE, WHITE, BLUE, RED, RED]
sort_color(colors)
assert colors == [RED, RED, WHITE, BLUE, BLUE]
