"""
[10 pkt.] Zadanie 1. Dana jest struktura danych

Struct Rectangle { double x,y; double w,h; };

Opisująca prostokąty (pola x i y to współrzędne lewego górnego rogu prostokąta a w i h to jego
wysokość i szerokość). Proszę zaimplementować funkcję

void heapsort(Rectangle* A, int n);

która otrzymuje na wejściu n elementową tablicę struktur typu Rectangle i sortuje ją w kolejności
rosnącej względem wartości pola prostokąta, korzystając z algorytmu heapsort.
"""

from random import randint as rnd


class Rect:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h


def rect_area(rect):
    w = rect.w
    h = rect.h
    return w * h


def sort_by_dist(rect):
    n = len(rect)
    for i in range(n):
        rect[i] = (rect[i], rect_area(rect[i]))
    heap_sort(rect, fn=lambda x: x[1])
    for i in range(n):
        rect[i] = rect[i][0]


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
    XY = [(rnd(-100, 100), rnd(-100, 100)) for _ in range(n)]
    WH = [(rnd(-100, 100), rnd(-100, 100)) for _ in range(n)]
    rect = [Rect(x, y, w, h) for (x, y), (w, h) in zip(XY, WH)]
    fn(rect)
    return sorted(rect, key=lambda r: r.h * r.w) == rect


if __name__ == '__main__':
    print('Ok?', test(sort_by_dist, rnd(0, 10000)))
