from zad1testy import runtests


class Node:
    def __init__(self, vert=None, idx=None):
        self.vert = vert
        self.idx = idx
        self.next = None


def vertices_to_process_ll(n, reps):
    head = Node()
    tail = head
    for u in range(n):
        for i in range(reps):
            tail.next = Node(u, i)
            tail = tail.next
    return head


def get_min_weight_vertices(head, weights):
    if not head.next: return []  # If no more vertices are remaining

    # Find all vertices with the lowest distance paths
    res = []
    min_w = float('inf')
    prev = head

    while prev.next:
        if weights[prev.next.vert][prev.next.idx] < min_w:
            min_w = weights[prev.next.vert][prev.next.idx]
            res = [prev]
        elif weights[prev.next.vert][prev.next.idx] == min_w:
            res.append(prev)
        prev = prev.next

    # Remove nodes found and store vertex-index pairs
    for i in range(len(res) - 1, -1, -1):
        prev = res[i]
        res[i] = prev.next.vert, prev.next.idx
        prev.next = prev.next.next

    return res


def dijkstra(G: 'graph represented by adjacency matrix',
             P: 'array of stations indices',
             d: 'capacity of car\'s fuel tank',
             s: 'source',
             t: 'target'):
    n = len(G)
    inf = float('inf')
    step = d + 1
    # Store information about vertices which haven't been processed yet
    to_process = vertices_to_process_ll(n, step)
    parents = [[None] * step for _ in range(n)]
    weights = [[inf] * step for _ in range(n)]
    weights[s][d] = 0

    is_station = [False] * n
    for i in P: is_station[i] = True

    found = False
    res_fuel = None
    # Loop till there are some vertices which haven't been processed yet
    while not found:
        # Find vertices of the minimum total weight path
        vert = get_min_weight_vertices(to_process, weights)
        # If there are no vertices, no path exists
        if not vert: return (None,) * 2
        # Loop over all vertices in a vert array
        for u, fuel in vert:
            # Break a loop if found a path to the target
            if u == t:
                found = True
                res_fuel = fuel
                break
            # Refuel if u is a station vertex
            curr_fuel = d if is_station[u] else fuel
            # Loop over all reachable neighbours
            for v in range(n):
                new_fuel = curr_fuel - G[u][v]
                if 0 <= G[u][v] <= curr_fuel and weights[u][fuel] + G[u][v] < weights[v][new_fuel]:
                    weights[v][new_fuel] = weights[u][fuel] + G[u][v]
                    parents[v][new_fuel] = u, fuel

    return res_fuel, parents, weights


def get_path(parents, t, fuel):
    path = [t]

    entry = parents[t][fuel]
    while entry:
        t, fuel = entry
        path.append(t)
        entry = parents[t][fuel]

    path.reverse()
    return path


def jak_dojade(G, P, d, a, b):
    fuel, parents, weights = dijkstra(G, P, d, a, b)
    if weights[b][fuel] == float('inf'):
        return None
    return get_path(parents, b, fuel)


runtests(jak_dojade)
