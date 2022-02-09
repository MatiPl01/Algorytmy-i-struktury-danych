from queue import Queue


def count_shortest_paths(G: 'graph represented using adjacency lists',
                         u: 'begin vertex',
                         v: 'end vertex'):
    if u == v: return 1

    n = len(G)
    q = Queue()
    q.put(u)
    counts = [0] * n
    lengths = [0] * n
    lengths[u] = 0
    counts[u] = 1

    while not q.empty():
        i = q.get()
        for j in G[i]:
            if not counts[j]:
                counts[j] = counts[i]
                lengths[j] = lengths[i] + 1
                q.put(j)
            elif lengths[i] + 1 == lengths[j]:
                counts[j] += counts[i]
            print(f'{i} -> {j}', counts[j], lengths[j])

    print(counts)
    print(lengths)
    return counts[v]


def undirected_graph_adjacency_lists(E, n):
    G = [[] for _ in range(n)]
    for edge in E:
        G[edge[0]].append(edge[1])
        G[edge[1]].append(edge[0])
    return G


n = 7
E = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (3, 5), (4, 6), (5, 6)]

G = undirected_graph_adjacency_lists(E, n)
print(count_shortest_paths(G, 0, 6))
