""" O(V^2) """

from zad1testy import runtests


def binary_search_first(arr: 'sorted sequence', el: 'searched element') -> int:
    left_idx = 0
    right_idx = len(arr) - 1

    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2
        if el > arr[mid_idx]:
            left_idx = mid_idx + 1
        else:
            right_idx = mid_idx - 1

    return left_idx if left_idx < len(arr) and arr[left_idx] == el else -1


class Node:
    def __init__(self, idx=None, prev_i=None):
        self.prev_i = prev_i  # Index of the previous mean of transport weight
        self.next = None
        self.idx = idx


def vertices_to_process_ll(n, reps):
    head = Node()
    tail = head
    for u in range(n):
        # Skip the starting vertex
        for i in range(reps):
            tail.next = Node(u, i)
            tail = tail.next
    return head


def get_min_weight_vertices(head, weights):
    if not head.next: return []  # If no more vertices are remaining

    m = len(weights[0])
    # Find a vertex of the lowest weight
    prev = head
    min_w = float('inf')
    min_arr = []
    to_remove_prev = []

    while prev.next:
        u = prev.next.idx
        i = prev.next.prev_i
        if weights[u][i] < min_w:
            min_w = weights[u][i]
            min_arr = [(u, i)]
            to_remove_prev = [prev]
        elif weights[u][i] == min_w:
            min_arr.append((u, i))
            to_remove_prev.append(prev)
        prev = prev.next

    # Remove vertices of the lowest weight
    for i in range(len(to_remove_prev) - 1, -1, -1):
        prev = to_remove_prev[i]
        prev.next = prev.next.next

    return min_arr


def dijkstra(G: 'graph represented by adjacency matrix',
             W: 'array of edges weights',
             s: 'start',
             t: 'target'):
    m = len(W)
    n = len(G)
    inf = float('inf')
    W.sort()
    # Store information about vertices which haven't been processed yet
    to_process = vertices_to_process_ll(n, len(W))
    weights = [[inf] * m for _ in range(n)]
    # Set initial weights of the start vertex to 0
    for i in range(m): weights[s][i] = 0
    res_i = None

    # Loop till a path wasn't found
    while res_i is None:
        # Find a vertex of the minimum total weight path
        to_check = get_min_weight_vertices(to_process, weights)
        # Otherwise, relax all neighbours of vertices with the lowest path weight
        for u, prev_i in to_check:
            # Break if the next vertex to process is the target vertex as we have
            # already found a shortest path to this vertex before (or there is no
            # path to the target)
            if u == t:
                if weights[u][prev_i] == inf: return (None,) * 3
                res_i = prev_i
                break
            # Iterate over the vertex's neighbours and update their wieghts
            # (enter only these vertices which can be entered)
            for v in range(n):
                # Skip if no edge (0 means not edge) or if a weight of an edge is the
                # same as a weight of the previous edge
                if not G[u][v] or G[u][v] == W[prev_i]: continue
                # Update the weight of a path to the vertex v that ends with an edge
                # of the weight G[u][v] if found a better one
                i = binary_search_first(W, G[u][v])
                if weights[u][prev_i] + G[u][v] < weights[v][i]:
                    weights[v][i] = weights[u][prev_i] + G[u][v]

    return res_i, weights


def islands(G: 'graph represented by adjacency matrix', a: 'begin city', b: 'target city'):
    W = [1, 5, 8]  # Koszty traktuję jako dane, ponieważ są jawnie podane w poleceniu
    # Koszty muszą być posortowane rosnąco
    res_i, weights = dijkstra(G, W, a, b)
    # Return the result
    return weights[b][res_i]
        

runtests(islands)
