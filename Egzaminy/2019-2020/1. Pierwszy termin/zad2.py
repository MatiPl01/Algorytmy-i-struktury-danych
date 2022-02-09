""" O(V^3) """
from zad2testy import runtests


def opt_sum(tab):
    n = len(tab)
    inf = float('inf')
    F = [[inf] * n for _ in range(n)]
    S = [0] * n

    S[0] = tab[0]
    for i in range(1, n):
        S[i] = S[i - 1] + tab[i]

    def recur(i, j):
        if i == j:
            F[i][j] = 0
        elif j - i == 1:
            F[i][j] = abs(tab[i] + tab[j])
        elif F[i][j] == inf:
            curr_sum = abs(S[j] - S[i - 1] if i > 0 else S[j])
            for k in range(i, j):
                F[i][j] = min(F[i][j], max(curr_sum, recur(i, k), recur(k + 1, j)))
        return F[i][j]

    recur(0, n - 1)

    return F[0][n - 1]


runtests(opt_sum)
