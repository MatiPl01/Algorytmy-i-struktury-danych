def sail(A, t):
    # Return False if is already aground
    if A[0][0] <= t: return False

    m = len(A)
    n = len(A[0])
    visited = [[False] * n for _ in range(m)]
    target = (n - 1, m - 1)

    def dfs(i, j):
        visited[i][j] = True
        if i == target[1] and j == target[0]:
            return True
        if i > 0 and A[i - 1][j] > t and not visited[i - 1][j]:
            if dfs(i - 1, j): return True
        if i < m - 1 and A[i + 1][j] > t and not visited[i + 1][j]:
            if dfs(i + 1, j): return True
        if j > 0 and A[i][j - 1] > t and not visited[i][j - 1]:
            if dfs(i, j - 1): return True
        if j < n - 1 and A[i][j + 1] > t and not visited[i][j + 1]:
            if dfs(i, j + 1): return True
        return False

    return dfs(0, 0)


if __name__ == '__main__':
    from random import randint, seed
    # seed(10)

    m = 4
    n = 6

    A = [
        [randint(0, 40) for _ in range(n)] for _ in range(m)
    ]

    t = 8
    print('Map of bay:')
    print(*(' '.join((str(n).zfill(2) for n in row)) for row in A), sep='\n', end='\n\n')
    print('Can reach the bay?', sail(A, t))
