"""Lepsze rozwiązanie"""

from zad1testy import runtests


def counting_sort(arr, fn):
    if arr:
        min_, max_ = minmax(arr, fn)
        _counting_sort(arr, min_, max_, fn)


def minmax(arr, fn):
    global_min = global_max = fn(arr[-1])

    for i in range(0, len(arr) - 1, 2):
        a = fn(arr[i])
        b = fn(arr[i + 1])
        if a > b:
            if a > global_max: global_max = a
            if b < global_min: global_min = b
        else:
            if b > global_max: global_max = b
            if a < global_min: global_min = a
    return global_min, global_max


def _counting_sort(arr, k: 'the lower bound', m: 'the upper bound', fn):
    # Allocate memory for required temporary arrays
    counts = [0] * (m - k + 1)
    temp = [None] * len(arr)
    # Count values repetitions
    for val in arr:
        counts[fn(val) - k] += 1
    # Modify the counts array to indicate how many values are not greater than the current one
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]
    # Rewrite values to the temp sorted array
    for i in range(len(arr) - 1, -1, -1):
        idx = fn(arr[i]) - k
        counts[idx] -= 1
        temp[counts[idx]] = arr[i]
    # Rewrite sorted values to the initial array
    for i in range(len(temp)):
        arr[i] = temp[i]


def tanagram(x, y, t):
    if len(x) != len(y): return False
    n = len(x)
    x_arr = [(x[i], i) for i in range(n)]
    y_arr = [(y[i], i) for i in range(n)]
    counting_sort(x_arr, fn=lambda a: ord(a[0]))
    counting_sort(y_arr, fn=lambda b: ord(b[0]))
    for i in range(n):
        if x_arr[i][0] != y_arr[i][0] or abs(x_arr[i][1] - y_arr[i][1]) > t:
            return False
    return True


runtests(tanagram)
