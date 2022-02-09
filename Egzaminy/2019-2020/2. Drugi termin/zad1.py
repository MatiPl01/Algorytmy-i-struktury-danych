""" O(n^3) """

from zad1testy import runtests


def zbigniew(A):
    n = len(A)
    inf = float('inf')
    F = [[inf] * n for _ in range(n)]

    F[0][min(n - 1, A[0])] = 0

    energy = min(n - 1, A[0])
    for used in range(1, energy + 1):
        F[used][energy - used] = 1

    for i in range(1, n):
        for e in range(n):
            if F[i][e] < inf:
                energy = min(e + A[i], n - i - 1)
                for used in range(1, energy + 1):
                    F[i + used][energy - used] = min(F[i + used][energy - used], F[i][e] + 1)

    min_jumps = inf
    for e in range(n):
        if F[n - 1][e] < min_jumps:
            min_jumps = F[n - 1][e]

    return min_jumps


runtests(zbigniew)
