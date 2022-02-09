"""
ZŁOŻONOŚĆ:
Obliczeniowa: O(m * log(n))
Pamięciowa:   O(log(n))
"""

from zad3testy import runtests


def get_moves(target_idx):
    moves = []

    while target_idx > 1:
        moves.append(target_idx % 2)
        target_idx //= 2

    moves.reverse()
    return moves


def get_key(T, target_idx):
    node = T
    idx = 1

    for move in get_moves(target_idx):
        if move:
            idx = idx * 2 + 1
            node = node.right
        else:
            idx *= 2
            node = node.left

    return node.key


def maxim(T, C):
    max_key = float('-inf')

    for i in C:
        max_key = max(max_key, get_key(T, i))

    return max_key


runtests(maxim)
