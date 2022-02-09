""" O(V + E) - 3 razy DFS """
from zad1testy import runtests


def is_connected(G: 'undirected weighted graph represented by adjacency lists'):
    n = len(G)
    visited = [False] * n

    def dfs(u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs(v)

    dfs(0)

    return all(visited)


def max_val_idx(A):
    max_i = 0
    for i in range(1, len(A)):
        if A[i] > A[max_i]:
            max_i = i
    return max_i


def diam_dist(G: 'undirected weighted acyclic graph represented by adjacency lists'):
    n = len(G)
    inf = float('inf')
    # Find the first diameter end vertex
    dist = [inf] * n
    visited = [0] * n
    token = 1

    def dfs(u):
        visited[u] = token
        for v in G[u]:
            if visited[v] != token:
                dist[v] = dist[u] + 1
                dfs(v)

    # Find the first diameter end vertex
    dist[0] = 0
    dfs(0)
    diam_u = max_val_idx(dist)

    # Find distances of all vertices from the first diameter end vertex
    # and the second diameter end vertex
    token += 1
    dist[diam_u] = 0
    dfs(diam_u)
    diam_v = max_val_idx(dist)
    dist1 = dist[:]  # Copy all distances from the first diameter vertex

    # Find all distances from the second diameter end vertex
    token += 1
    dist[diam_v] = 0
    dfs(diam_v)
    dist2 = dist[:]  # Copy all distances from the second diameter vertex

    return dist1, dist2


def best_root(L: 'undirected weighted acyclic graph represented by adjacency lists'):
    inf = float('inf')
    # This case will occur if a graph is not connected
    # (then the max distance will be infinity beacause for every vertex
    # there is at least one verex in another component and each vertex
    # then has its max distance equal to infinity)
    if not is_connected(L):
        return -1

    n = len(L)
    dist1, dist2 = diam_dist(L)
    # Find a vertex of the lowest max dist
    best_u = None
    min_dist = inf
    for u in range(n):
        max_dist = max(dist1[u], dist2[u])
        if max_dist < min_dist:
            min_dist = max_dist
            best_u = u

    return best_u


runtests(best_root)
