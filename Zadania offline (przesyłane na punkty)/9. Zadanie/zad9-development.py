from copy import deepcopy


class Node:
    def __init__(self, idx=None):
        self.idx = idx
        self.next = None


def vertices_to_process_ll(s, n):
    head = Node()
    tail = head
    for i in range(s, n):
        tail.next = Node(i)
        tail = tail.next
    return head


def get_min_weight_vertex(head, weights):
    if not head.next: return None  # If no more vertices are remaining

    # Find a vertex of the lowest weight
    min_prev = head
    prev = head.next
    while prev.next:
        if weights[prev.next.idx] < weights[min_prev.next.idx]:
            min_prev = prev
        prev = prev.next

    # Remove a vertex found
    u = min_prev.next.idx
    min_prev.next = min_prev.next.next

    return u


def dijkstra(G: 'graph represented by adjacency matrix', s: 'source'):
    n = len(G)
    inf = float('inf')
    # Store information about vertices which haven't been processed yet
    to_process = vertices_to_process_ll(s, n)
    parents = [None] * n
    weights = [inf] * n
    lengths = [0] * n
    weights[s] = 0
    min_weight = res_length = inf
    min_u = min_v = None

    # Loop till there are some vertices which haven't been processed yet
    while True:
        # Find a vertex of the minimum total weight path
        u = get_min_weight_vertex(to_process, weights)
        # Check if a vertex was found (if not, all vertices must have
        # been processed before)
        if u is None: break
        # Iterate over the vertex's neighbours and update weights of the paths
        for v in range(n):
            # Skip if no edge (-1 means no edge) or a vertex v was processed
            if G[u][v] == -1: continue
            # If there was some other path before to the vertex (there is a weight
            # lower than infinity stored), we have a cycle
            if weights[v] < inf and parents[u] != v:
                # Check if a length of a path from the u vertex to the source plus
                # a length of a path from the v vertex to the source plus a length
                # of a u-v edge is lower than the previous lowest length
                curr_weight = weights[v] + weights[u] + G[u][v]
                if curr_weight < min_weight:
                    min_weight = curr_weight
                    res_length = lengths[u] + lengths[v] + 1
                    min_u = u
                    min_v = v
                    print(s, min_u, min_v, res_length, min_weight, 'xd', parents)

            # Update the weight of a path to the vertex v if found a better one
            if weights[u] + G[u][v] < weights[v]:
                weights[v] = weights[u] + G[u][v]
                parents[v] = u
                lengths[v] = lengths[u] + 1

    return min_u, min_v, min_weight, res_length


def dijkstra2(G: 'graph represented by adjacency matrix', s, x, y):
    n = len(G)
    inf = float('inf')
    # Store information about vertices which haven't been processed yet
    to_process = vertices_to_process_ll(0, n)
    parents = [None] * n
    weights = [inf] * n
    weights[s] = 0
    x_processed = y_processed = False

    # Loop till there are some vertices which haven't been processed yet
    while True:
        # Find a vertex of the minimum total weight path
        u = get_min_weight_vertex(to_process, weights)
        # Check if a vertex was found (if not, all vertices must have
        # been processed before)
        if u == x:
            x_processed = True
            continue
        elif u == y:
            y_processed = True
            continue
        if x_processed and y_processed: break
        # Iterate over the vertex's neighbours and update weights of the paths
        for v in range(n):
            # Skip if no edge (-1 means no edge) or a vertex v was processed
            if G[u][v] == -1: continue
            # Update the weight of a path to the vertex v if found a better one
            if weights[u] + G[u][v] < weights[v]:
                weights[v] = weights[u] + G[u][v]
                parents[v] = u

    return parents


def reconstruct_cycle(parents, s, u, v):
    result = []

    def recur(i):
        if i != s:
            recur(parents[i])
        result.append(i)

    recur(u)

    while v != s:
        result.append(v)
        v = parents[v]

    return result


def min_cycle(G):
    n = len(G)
    inf = float('inf')
    min_weight = res_length = inf
    min_s = min_u = min_v = -1

    for s in range(n):
        u, v, weight, length = dijkstra(G, s)
        print('found', u, v, weight, length)
        if weight < min_weight or (weight == min_weight and length < res_length):
            min_weight = weight
            res_length = length
            min_s = s
            min_u = u
            min_v = v

    print(min_s, min_u, min_v, res_length, min_weight)

    if min_weight == inf: return []

    parents = dijkstra2(G, min_s, min_u, min_v)
    print(parents)

    return reconstruct_cycle(parents, min_s, min_u, min_v)


# G = [[-1, 1,-1, 4, 1],
#      [ 1,-1, 1,-1, 4],
#      [-1, 1,-1, 1, 4],
#      [ 4,-1, 1,-1, 1],
#      [ 1, 4, 4, 1,-1]]
#
# LEN = 5


# G = [[-1, 4, -1, -1, -1, -1, -1, 8, -1],
#      [4, -1, 8, -1, -1, -1, -1, 11, -1],
#      [-1, 8, -1, 7, -1, 4, -1, -1, 2],
#      [-1, -1, 7, -1, 9, 14, -1, -1, -1],
#      [-1, -1, -1, 9, -1, 10, -1, -1, -1],
#      [-1, -1, 4, 14, 10, -1, 2, -1, -1],
#      [-1, -1, -1, -1, -1, 2, -1, 1, 6],
#      [8, 11, -1, -1, -1, -1, 1, -1, 7],
#      [-1, -1, 2, -1, -1, -1, 6, 7, -1]]
# LEN = 14


def undirected_weighted_graph_matrix(E: 'array of edges'):
    # Find a number of vertices
    n = 0
    for e in E:
        n = max(n, e[0], e[1])
    n += 1
    # Create a graph
    G = [[-1] * n for _ in range(n)]  # -1 means no edge
    for e in E:
        G[e[0]][e[1]] = e[2]
        G[e[1]][e[0]] = e[2]
    return G


# E = [(0, 1, 3), (1, 2, 2), (0, 6, 2), (6, 7, 1), (6, 5, 3), (5, 7, 1),
#     (5, 4, 8), (3, 4, 20), (8, 7, 7), (8, 1, 1), (2, 3, 5), (3, 8, 1),
#     (7, 4, 2)]
# LEN = 5


# E = [(0, 1, 9), (1, 2, 18), (2, 3, 15), (3, 4, 20), (4, 5, 5), (5, 6, 5), (6, 7, 7), (7, 8, 10), (8, 9, 8),
#      (0, 15, 10), (1, 15, 4), (1, 14, 5), (15, 14, 4), (14, 3, 10), (15, 13, 6), (13, 14, 5), (16, 15, 6),
#      (16, 13, 2), (18, 17, 2), (17, 16, 3), (16, 12, 5), (12, 13, 4), (13, 11, 10), (11, 10, 4),
#      (12, 10, 12), (10, 5, 10), (11, 4, 6)]
# LEN = 11

# E = [(0, 1, 17), (1, 2, 30), (2, 3, 2), (3, 4, 47), (4, 5, 88), (5, 6, 0), (7, 6, 3), (7, 8, 7), (8, 9, 0), (9, 10, 12),
#      (10, 11, 40), (11, 0, 13), (11, 14, 1), (14, 12, 7), (12, 13, 18), (13, 1, 120), (3, 16, 81), (16, 15, 63),
#      (15, 17, 90), (17, 5, 37), (11, 23, 0), (23, 22, 67), (22, 21, 73), (21, 24, 11), (24, 23, 2), (21, 20, 18),
#      (20, 19, 96), (19, 18, 50), (18, 29, 4), (29, 20, 22), (18, 5, 1), (21, 25, 97), (25, 26, 26), (26, 27, 30),
#      (27, 28, 8), (28, 20, 11), (26, 30, 100), (30, 27, 52), (30, 31, 1), (31, 32, 20), (31, 33, 0), (34, 26, 4),
#      (35, 26, 3), (36, 26, 2), (27, 37, 10), (27, 38, 8), (27, 39, 1)]
# LEN = 120
#
# E = [(0, 2, 0), (2, 3, 0), (0, 1, 1000), (1, 3, 0), (3, 4, 1), (4, 5, 2), (3, 5, 3)]
# LEN = 6

# E = [(0, 1, 0), (1, 2, 0), (2, 0, 0)]
# LEN = 0

# E = [(0, 1, 2), (1, 2, 1), (1, 3, 3), (2, 3, 1)]
# LEN = 5

E = [(0, 1, 1), (1, 2, 2), (2, 3, 5), (3, 4, 3)]
LEN = 0

G = undirected_weighted_graph_matrix(E)


### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik

# G = [[-1, 2, -1, -1, 1],
#      [2, -1, 4, 1, -1],
#      [-1, 4, -1, 5, -1],
#      [-1, 1, 5, -1, 3],
#      [1, -1, -1, 3, -1]]
# LEN = 7

GG = deepcopy(G)
cycle = min_cycle(GG)

print("Cykl :", cycle)

if cycle == []:
    print("Błąd (1): Spodziewano się cyklu!")
    exit(0)

L = 0
u = cycle[0]
for v in cycle[1:] + [u]:
    if G[u][v] == -1:
        print("Błąd (2): To nie cykl! Brak krawędzi ", (u, v))
        exit(0)
    L += G[u][v]
    u = v

print("Oczekiwana długość :", LEN)
print("Uzyskana długość   :", L)

if L != LEN:
    print("Błąd (3): Niezgodna długość")
else:
    print("OK")
