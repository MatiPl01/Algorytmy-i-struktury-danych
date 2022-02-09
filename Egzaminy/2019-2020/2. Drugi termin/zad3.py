""" O(n^2), gdzie n - liczba różnych zadań (bo trzeba przejrzeć macierz T """
from zad3testy import runtests


def create_graph(T):
    n = len(T)
    G = [[] for _ in range(n)]

    for a in range(n):
        for b in range(n):
            if T[a][b] == 1:
                G[a].append(b)
            elif T[a][b] == 2:
                G[b].append(a)

    return G


def topological_sort(G: 'graph represented using adjacency lists'):
    n = len(G)
    visited = [False] * n
    result = [None] * n
    idx = n

    def dfs(u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs(v)
        nonlocal idx
        idx -= 1
        result[idx] = u

    for u in range(n):
        if not visited[u]:
            dfs(u)

    return result

    
def tasks(T):
    G = create_graph(T)
    return topological_sort(G)


runtests(tasks)
