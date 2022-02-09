""" O(n * log(n)) - sortowanie Quick Sortem"""
from zad1testy import runtests


def quick_sort(arr, *, fn=lambda x: x):
    _quick_sort(arr, 0, len(arr) - 1, fn)


def _quick_sort(arr, left_idx, right_idx, fn):
    while left_idx < right_idx:
        pivot_position = _partition(arr, left_idx, right_idx, fn)

        if pivot_position - left_idx < right_idx - pivot_position:
            _quick_sort(arr, left_idx, pivot_position - 1, fn)
            left_idx = pivot_position + 1
        else:
            _quick_sort(arr, pivot_position + 1, right_idx, fn)
            right_idx = pivot_position - 1


def _partition(arr, left_idx, right_idx, fn):
    pivot = fn(arr[right_idx])

    # Partition an array into 2 subarrays of elements lower than
    # pivot and of elements greater than a pivot
    i = left_idx
    for j in range(left_idx, right_idx):
        if fn(arr[j]) < pivot:
            _swap(arr, i, j)
            i += 1

    # Place a pivot element on its destination index
    _swap(arr, i, right_idx)

    return i  # Return a pivot position after the last swap


def _swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def dominance_helper(P, fn1, fn2):
    n = len(P)
    # Sort points by the specified coordinate coordinate
    quick_sort(P, fn=fn1)
    # Create an array of tuples sorted by the second coordinate
    # of points which will store also an index to the P array
    A = [(fn2(P[i]), i) for i in range(n)]
    quick_sort(A, fn=lambda p: p[0])
    # Create an array of numbers which will indicate on which
    # positions should be points from the P array stored when
    # sorted by the second coordinate specified. If there are
    # points with the same first coordinate, we will store the
    # same number for them
    order = [-1] * n
    k = 0
    order[A[0][1]] = k
    for i in range(1, n):
        if A[i][0] != A[i - 1][0]:
            k += 1
        order[A[i][1]] = k
    # Create a set of points which dominate all the remaining
    # points by the first coordinate specified and aren't dominated
    # by any of rejected points
    start = float('inf')
    B = []
    for i in range(n):
        if order[i] < start:
            B.append(P[i])
            start = order[i]
    return B


def intersection(A, B):
    C = []
    # Sort points in both arrays by their both coordinates
    # in the same order
    quick_sort(A)
    quick_sort(B)
    # Merge A and B arrays into one array which will contain
    # all elements which are in both A and B array
    i = j = 0
    while i < len(A) and j < len(B):
        if A[i][0] < B[j][0] or (A[i][0] == B[j][0] and A[i][1] < B[j][1]):
            i += 1
        elif A[i][0] > B[j][0] or (A[i][0] == B[j][0] and A[i][1] > B[j][1]):
            j += 1
        else:  # If points have both coordinates the same
            C.append(A[i])
            i += 1
            j += 1
    return C


def dominance(P):
    n = len(P)
    # Sort points in order to easily restore indices later
    temp = [(P[i], i) for i in range(n)]
    quick_sort(temp, fn=lambda p: p[0])
    # Get an array of points which dominate all other points by x coordinate
    A = dominance_helper(P, lambda p: p[0], lambda p: p[1])
    # Get an array of points which dominate all other points by y coordinate
    B = dominance_helper(P, lambda p: p[1], lambda p: p[0])
    # Create an intersection of both arrays of points
    C = intersection(A, B)
    # Map resulting points to their indices in an initial array
    m = len(C)
    D = []
    i = j = 0
    while i < n and j < m:
        if temp[i][0] == C[j]:
            D.append(temp[i][1])
            j += 1
        i += 1
    quick_sort(D)

    return D


runtests(dominance)
