"""O(V^3) (UWAGA: O(V^2) nie działa, bo blokuje możliwość poprawienia ścieżki z użyciem butów milowych)"""
from zad3testy import runtests


class Node:
    def __init__(self, idx=None, used=False):
        self.idx = idx
        self.used = used
        self.next = None


def vertices_to_process_ll(n):
    head = Node()
    tail = head
    for i in range(n):
        tail.next = Node(i, False)
        tail = tail.next
        tail.next = Node(i, True)
        tail = tail.next
    return head


def get_min_weight_vertex(head, weights):
    if not head.next: return (None,) * 2  # If no more vertices are remaining

    # Find a vertex of the lowest weight
    min_prev = head
    prev = head.next
    while prev.next:
        if weights[prev.next.idx][prev.next.used] < weights[min_prev.next.idx][min_prev.next.used]:
            min_prev = prev
        prev = prev.next

    # Remove a vertex found
    u = min_prev.next.idx
    used = min_prev.next.used
    min_prev.next = min_prev.next.next

    return u, used


def jumper(G: 'graph represented by adjacency matrix', s: 'source', t: 'target'):
    n = len(G)
    inf = float('inf')
    # Store information about vertices which haven't been processed yet
    to_process = vertices_to_process_ll(n)
    weights = [[inf] * 2 for _ in range(n)]
    weights[s][0] = 0

    t_counter = 0

    # Loop till there are some vertices which haven't been processed yet
    while True:
        # Find a vertex of the minimum total weight path
        u, used = get_min_weight_vertex(to_process, weights)
        # Check if a vertex was found (if not, all vertices must have
        # been processed before)
        if u is None: break
        # If we removed 't' vertex from the linked list 2 times, there
        # must have been two shortest paths already found before so we
        # can terminate a loop
        if u == t:
            t_counter += 1
            if t_counter == 2:
                break
        # Iterate over the vertex's neighbours and update weights of the paths
        for v in range(n):
            # Skip if no edge (0 means no edge)
            if not G[u][v]: continue
            # Update a weight of a path when we don't use mileage shoes
            if weights[u][used] + G[u][v] < weights[v][0]:
                weights[v][0] = weights[u][used] + G[u][v]
            # If we use mileage shoes we have to go one edge deeper
            if not used:
                for w in range(n):
                    # Skip if no edge (0 means no edge) or we try to enter a parent
                    # vertex
                    if not G[v][w] or w == u: continue
                    new_weight = weights[u][used] + max(G[u][v], G[v][w])
                    if new_weight < weights[w][1]:
                        weights[w][1] = new_weight

    return min(weights[t])


runtests(jumper)
