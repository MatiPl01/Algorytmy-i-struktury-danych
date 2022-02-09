"""
ZŁOŻONOŚĆ:
Obliczeniowa: O(m * log^2(n))
Pamięciowa:   O(1)
"""

from zad3testy import runtests


def turn_left(curr_idx, target_idx):
    l_min = 2 * curr_idx
    l_max = l_min

    while l_max < target_idx:
        l_min *= 2
        l_max = l_max * 2 + 1

    if l_min <= target_idx <= l_max:
        return True
    return False


def get_key(T, target_idx):
    idx = 1
    node = T

    while idx != target_idx:
        if turn_left(idx, target_idx):
            node = node.left
            idx *= 2
        else:
            node = node.right
            idx = 2 * idx + 1

    return node.key


def maxim(T, C):
    max_key = float('-inf')

    for i in C:
        max_key = max(max_key, get_key(T, i))

    return max_key


runtests(maxim)
