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

    print(last)

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
    lds_parents, lds_curr_ind, lds_first_ind = lds(X, 0, n - 1)
    print('lds', lds_parents, lds_curr_ind, lds_first_ind)
    # Get longest increasing subsequence (lds from back) data
    lis_parents, lis_curr_ind, lis_first_ind = lds(X, n - 1, 0)
    print('lis', lis_parents, lis_curr_ind, lis_first_ind)

    # Look for the longest decreasing-increasing subsequence
    best_lds_i = -1
    best_lis_i = -1
    best_length = 0

    print('\nLOOP:')
    for lds_i, lds_end_idx in enumerate(lds_first_ind):
        lis_i = min(binary_search(lis_first_ind, lds_end_idx), len(lis_first_ind) - 1)

        print(lds_i, lis_i)

        if lds_first_ind[lds_i] >= lis_first_ind[0]:
            break

        while lis_first_ind[lis_i] <= lds_first_ind[lds_i] \
                or X[lis_first_ind[lis_i]] == X[lds_first_ind[lds_i]]:
            lis_i -= 1
            if lis_i < 0:
                break
        # Execute the code below only if the while loop above hasn't
        # been broken
        else:
            length = lis_i + lds_i + 2
            if length > best_length:
                best_length = length
                best_lds_i = lds_i
                best_lis_i = lis_i

    # Choose the longest subsequence
    lengths = [len(lds_curr_ind), len(lis_curr_ind), best_length]
    print('lengths', lengths)
    best = lengths.index(max(lengths))

    if best == 0:
        return restore_subsequence(X, lds_parents, lds_curr_ind[-1], reverse=True)
    elif best == 1:
        return restore_subsequence(X, lis_parents, lis_curr_ind[-1])
    else:
        print('DEBUG')
        print(best_lds_i, best_lis_i, best_length)
        lds_end_idx = lds_first_ind[best_lds_i]
        lis_begin_idx = lis_first_ind[best_lis_i]

        lds_parents, lds_curr_ind, _ = lds(X, 0, lds_end_idx)
        lis_parents, lis_curr_ind, _ = lds(X, n - 1, lis_begin_idx)

        print('PART 1', f'{0} - {lds_end_idx}')
        print(restore_subsequence(X, lds_parents, lds_curr_ind[-1], reverse=True))
        print('PART 2', f'{lis_begin_idx} - {n - 1}')
        print(restore_subsequence(X, lis_parents, lis_curr_ind[-1]))

        return restore_subsequence(X, lds_parents, lds_curr_ind[-1], reverse=True) \
             + restore_subsequence(X, lis_parents, lis_curr_ind[-1])


# runtests(mr)


a = [3, 1, 5, 7, 2, 4, 9, 3, 17, 3]
a = [4, 10, 5, 1, 8, 2, 3, 4]
a = [1, 10, 5]
print('here', mr(a))
