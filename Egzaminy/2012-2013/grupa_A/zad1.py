"""
[10 pkt.] Zadanie 1. Dana jest struktura danych

Struct Point { double x,y; };

Opisująca punkty w przestrzeni R^2. Proszę zaimplementować funkcję

Void heapsort(Point* A, int n);

Która otrzymuje na wejściu n-elementową tablicę struktur typu Point I sortuje ją w kolejności
rosnącej względem odległości punktu od początku układu współrzędnych, korzystając z algorytmu
heapsort.
"""
from random import randint as rnd


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance_sq(x, y):
    return x ** 2 + y ** 2


def sort_by_dist(points):
    n = len(points)
    for i in range(n):
        points[i] = (points[i], distance_sq(*points[i]))
    heap_sort(points, fn=lambda x: x[1])
    for i in range(n):
        points[i] = points[i][0]


_left = lambda i: 2 * i + 1
_right = lambda i: 2 * i + 2


def max_heapify(arr, curr_idx, end_idx, fn):
    # Loop till the current node has a child larger than itself
    # We assume that when we enter a node which both children are
    # smaller than this node, a subtree which a current node is a
    # root of must fulfill a max-heap property.
    while True:
        i = _left(curr_idx)
        j = _right(curr_idx)
        k = curr_idx

        if i < end_idx:
            if fn(arr[i]) > fn(arr[k]):
                k = i
            if j < end_idx and fn(arr[j]) > fn(arr[k]):
                k = j

        if k == curr_idx: return
        # Swap the current with the largest child
        arr[curr_idx], arr[k] = arr[k], arr[curr_idx]
        curr_idx = k


def build_heap(arr, fn):
    for i in range((len(arr) - 1) // 2, -1, -1):
        max_heapify(arr, i, len(arr), fn)


def heap_sort(arr, fn=lambda x: x):
    build_heap(arr, fn)
    # Swap the currently greatest value (a heap's root) with a value
    # stored on index i in an array representing a heap and fix
    # a heap after doing such a change.
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        # Fix a heap
        max_heapify(arr, 0, i, fn)


def test(fn, n):
    P = [(rnd(-100, 100), rnd(-100, 100)) for _ in range(n)]
    fn(P)
    return sorted(P, key=lambda p: p[0] ** 2 + p[1] ** 2) == P


if __name__ == '__main__':
    print('Ok?', test(sort_by_dist, rnd(0, 10000)))
