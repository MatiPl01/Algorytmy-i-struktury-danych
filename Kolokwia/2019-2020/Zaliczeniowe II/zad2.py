""" O(n * m), gdzie n - liczba wierzchołków w grafie, m - długość słowa"""
from zad2testy import runtests


def min_cost(G, W, s):
    n = len(G)
    m = len(W)
    inf = float('inf')

    F = [[inf] * m for _ in range(n)]

    # it = 0

    def dfs(u, i):
        # nonlocal it
        if i == m:
            return 0
        if F[u][i] == inf:
            # it += 1
            for v, weight in G[u][1]:
                if G[v][0] == W[i]:
                    F[u][i] = min(F[u][i], dfs(v, i + 1) + weight)
        return F[u][i]

    res = dfs(s, 0)
    # print(it)

    return res


def create_graph(L, E):
    n = len(L)
    # We will store each vertex as a letter which corresponds to this
    # vertex and its neighbours array
    G = [['', []] for _ in range(n)]

    for i in range(n):
        G[i][0] = L[i]

    for edge in E:
        G[edge[0]][1].append((edge[1], edge[2]))
        G[edge[1]][1].append((edge[0], edge[2]))

    return G


def add_begin_vert(G, W):
    n = len(G)
    G.append(['', []])

    for i in range(n):
        if G[i][0] == W[0]:
            G[n][1].append((i, 0))  # Set weight to 0 as this is a phantom edge

    return n


def letters(G, W):
    # Create a graph
    L, E = G
    G = create_graph(L, E)
    # Add a starting vertex which will be connected with each
    # beginning letter vertex (and the end vertex connected to
    # the last letter vertices)
    begin = add_begin_vert(G, W)
    print(*G, sep='\n')
    # Using modified Dijkstra's algorithm, find the lowest cost
    return min_cost(G, W, begin)


if __name__ == '__main__':
    # L = ["k", "k", "o", "o", "t", "t"]
    # E = [(0, 2, 2), (1, 2, 1), (1, 4, 3), (1, 3, 2), (2, 4, 5), (3, 4, 1), (3, 5, 3)]
    # G = (L, E)
    # W = "kto"
    # print(letters(G, W))
    # print(letters(G, 'ktoto'))
    # print(letters(G, 'otoktoto'))
    # print(letters(G, 'kototo'))

    # # Graf pełny K6
    # L = 'k' * 6
    # E = [(0, 1, 1), (0, 2, 1), (0, 3, 1), (0, 4, 1), (0, 5, 1), (1, 5, 1), (1, 4, 1), (1, 3, 1),
    #      (1, 2, 1), (2, 5, 1), (2, 4, 1), (2, 3, 1), (3, 4, 1), (3, 5, 1), (4, 5, 1)]
    #
    # # Graf pełny K4
    # L = 'k' * 4
    # E = [(0, 1, 1), (1, 2, 1), (2, 3, 1), (3, 0, 1), (0, 2, 1), (1, 3, 1)]

    # W = 'kkkkk'
    # G = L, E
    # print(letters(G, W))

    runtests(letters)
