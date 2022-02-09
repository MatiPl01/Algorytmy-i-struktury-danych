def count_moves(A, start=(0, 0)):
    m = len(A)
    n = len(A[0])
    visited = [[False] * n for _ in range(m)]
    counter = 0

    def dfs(i, j):  # Can be also BFS, it doesn't matter as we have to check every field which can be visited
        nonlocal counter
        visited[i][j] = True
        counter += 1

        if i > 0 and A[i - 1][j] and not visited[i - 1][j]:
            dfs(i - 1, j)
        if j > 0 and A[i][j - 1] and not visited[i][j - 1]:
            dfs(i, j - 1)
        if i < m - 1 and A[i + 1][j] and not visited[i + 1][j]:
            dfs(i + 1, j)
        if j < n - 1 and A[i][j + 1] and not visited[i][j + 1]:
            dfs(i, j + 1)

    dfs(start[1], start[0])

    return counter


if __name__ == '__main__':
    from random import randint, seed
    # seed(1)
    m = randint(2, 10)
    n = randint(2, 10)
    A = [[bool(randint(0, 1)) for _ in range(n)] for _ in range(m)]
    x, y = randint(0, n - 1), randint(0, m - 1)
    A[y][x] = True

    print(f'n={n}, m={m}')
    print(f'Start point: (x, y)=({x}, {y})  (x is column index, y is row index)')
    print(f'Board ({m}x{n}):')
    print(*(' '.join(map(str, map(int, row))) for row in A), sep='\n', end='\n\n')

    # I include the starting point in such a number
    print('Number of possible fields to visit:', count_moves(A, start=(x, y)))
