"""
ZŁOŻONOŚĆ:
Obliczeniowa: O(n * log(n))
Pamięciowa:   O(n)
"""

from zad1testy import runtests


def binary_search(arr, val):
    l = 0
    r = len(arr) - 1

    while l <= r:
        m = (l + r) // 2
        if val < arr[m]:
            l = m + 1
        else:
            r = m - 1
    return l


def lds(arr, begin, end):
    if len(arr) < 2: return len(arr)

    n = len(arr)
    last = []
    curr_ind = []
    first_ind = []
    parents = [-1] * n

    for i in (range(begin, end + 1) if begin <= end else range(begin, end - 1, -1)):
        j = binary_search(last, arr[i])
        if j == len(last):
            if j > 0: parents[i] = curr_ind[j - 1]
            first_ind.append(i)
            curr_ind.append(i)
            last.append(arr[i])
        else:
            curr_ind[j] = i
            last[j] = arr[i]
            if j > 0: parents[i] = curr_ind[j - 1]

    return parents, curr_ind, first_ind


def restore_subsequence(arr, parents, first_idx, *, reverse=False):
    res = []

    i = first_idx
    while i >= 0:
        res.append(arr[i])
        i = parents[i]

    if reverse:
        res.reverse()

    return res


def mr(X):
    n = len(X)
    # Get longest decreasing subsequence data
    ds_parents, ds_curr_ind, ds_first_ind = lds(X, 0, n - 1)
    # Get longest increasing subsequence (lds from back) data
    is_parents, is_curr_ind, is_first_ind = lds(X, n - 1, 0)

    # Look for the longest decreasing-increasing subsequence
    best_ds_i = -1
    best_is_i = -1
    best_length = 0

    for ds_i, ds_end_idx in enumerate(ds_first_ind):
        is_i = min(binary_search(is_first_ind, ds_end_idx), len(is_first_ind) - 1)

        if ds_first_ind[ds_i] >= is_first_ind[0]:
            break

        while is_first_ind[is_i] <= ds_first_ind[ds_i] \
                or X[is_first_ind[is_i]] == X[ds_first_ind[ds_i]]:
            is_i -= 1
            if is_i < 0:
                break
        # Execute the code below only if the while loop above hasn't
        # been broken
        else:
            length = is_i + ds_i + 2
            if length > best_length:
                best_length = length
                best_ds_i = ds_i
                best_is_i = is_i

    # Choose the longest subsequence
    lengths = [len(ds_curr_ind), len(is_curr_ind), best_length]
    best = lengths.index(max(lengths))

    if best == 0:
        return restore_subsequence(X, ds_parents, ds_curr_ind[-1], reverse=True)
    elif best == 1:
        return restore_subsequence(X, is_parents, is_curr_ind[-1])
    else:
        ds_end_idx   = ds_first_ind[best_ds_i]
        is_begin_idx = is_first_ind[best_is_i]

        ds_parents, ds_curr_ind, _ = lds(X, 0, ds_end_idx)
        is_parents, is_curr_ind, _ = lds(X, n - 1, is_begin_idx)

        return restore_subsequence(X, ds_parents, ds_curr_ind[-1], reverse=True) +\
               restore_subsequence(X, is_parents, is_curr_ind[-1])


runtests(mr)
