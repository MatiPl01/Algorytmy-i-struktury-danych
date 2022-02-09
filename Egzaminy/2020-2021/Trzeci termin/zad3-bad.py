"""
Rozwiązanie trywialne - przepisanie drzewa do tablicy

ZŁOŻONOŚĆ:
Obliczeniowa: O(n + m)
Pamięciowa:   O(n)
"""

from zad3testy import runtests


def get_height(T):
    h = 0
    curr = T
    while curr:
        curr = curr.right
        h +=1
    return h


def tree_to_arr(T):
    h = get_height(T)
    n = 2 ** h
    arr = [None] * n

    def recur(node, i):
        arr[i] = node.key
        if node.left: recur(node.left, 2 * i)
        if node.right: recur(node.right, 2 * i + 1)

    recur(T, 1)

    return arr


def maxim(T, C):
    arr = tree_to_arr(T)
    max_key = arr[C[0]]

    for i in C:
        max_key = max(max_key, arr[i])

    return max_key

    
runtests(maxim)
