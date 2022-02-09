"""
ZŁOŻONOŚĆ
Obliczeniowa: O(E * log(V))
Pamięciowa:   O(E + V)
"""

from zad3testy import runtests
from queue import PriorityQueue


def dijkstra(G: 'graph represented by adjacency lists', s: 'source'):
    n = len(G)
    inf = float('inf')
    weights = [inf] * n
    parents = [[] for _ in range(n)]
    pq = PriorityQueue()
    pq.put((0, s, None))

    while not pq.empty():
        min_w, u, parent = pq.get()
        if min_w < weights[u]:
            weights[u] = min_w
            parents[u] = [parent]
            for v, weight in G[u]:
                if weights[v] == inf:
                    pq.put((weights[u] + weight, v, u))
        elif min_w == weights[u]:
            parents[u].append(parent)

    parents[s] = []

    return parents


def count_edges(G, t):
    n = len(G)
    visited = [False] * n

    def dfs(u):
        visited[u] = True
        count = 0
        for v in G[u]:
            if not visited[v]:
                count += dfs(v)
            count += 1
        return count

    return dfs(t)


def paths(G, s, t):
    # A directed graph of shortest paths to all vertices from 's' vertex
    G2 = dijkstra(G, s)

    print(*G2, sep='\n')
    # Return a number of edges on shortest paths from 's' to 't'
    return count_edges(G2, t)

    
runtests(paths)
