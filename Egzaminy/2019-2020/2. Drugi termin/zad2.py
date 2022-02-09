"""
O(E * log(E) + E * E * log*(V)) = O(E^2 * log*(V)) = O(V^4 * log*(V))
E = O(V^2), bo łączymy każde miasto z każdym
"""

from zad2testy import runtests


class Node:
    def __init__(self, id_):
        self.id = id_
        self.parent = self
        self.rank = 0  # The upper tree's height limit


def find(x: 'Node object') -> 'set representative id':
    # If we have to compress a path as we are not a root of a tree
    if x != x.parent:
        # Point all sobsequent nodes on a path to the root node
        x.parent = find(x.parent)
    # Return the current (updated) parent of the node
    return x.parent


def union(x: 'Node object', y: 'Node object'):
    # Find parents of both x and y
    x = find(x)
    y = find(y)
    # Return if x and y are in the same set as there is nothing to do
    if x == y: return
    # Otherwise, link the smaller tree to the larger one
    if x.rank < y.rank:
        x.parent = y
    else:
        y.parent = x
        # If both x and y have the same rank and y was linked to x,
        # we have to increase the rank of x
        if x.rank == y.rank: x.rank += 1


def make_set(x: 'id'):
    return Node(x)


def connected(x: 'id', y: 'id'):
    return find(x) == find(y)


def kruskal(G: '(V, E)'):
    V, E = G
    # Makeset for each of the vertices
    vert = [make_set(v) for v in V]
    # In a loop pick an edge of the smallest weight
    # and check if we can add this edge to the minimum
    # spanning tree
    max_edge = None
    for i in range(len(E) - 1, -1, -1):
        edge = E[i]
        u, v, weight = edge
        if not connected(vert[u], vert[v]):
            union(vert[u], vert[v])
            max_edge = edge
    # Check if all vertices are connected (if we got a MST)
    root = find(vert[0])
    for i in range(1, len(V)):
        if find(vert[i]) != root:
            return None
    # Otherwise, if we have a MST, return the max-weight edge
    return max_edge


def distance(A, B):
    return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** .5


def edges_list(A):
    E = []
    n = len(A)
    for i in range(n - 1):
        for j in range(i + 1, n):
            E.append((i, j, distance(A[i], A[j])))
    return E


def highway(A):
    n = len(A)
    V = list(range(n))
    E = edges_list(A)
    # Sort an array of edges by their length in a reversed order
    # (to easily remove shortest edges)
    E.sort(reverse=True, key=lambda e: e[2])
    # Search for minimum difference between max distance and min distance
    G = (V, E)
    min_diff = float('inf')

    while True:
        max_edge = kruskal(G)
        if not max_edge: break
        min_edge = E.pop()
        u, v, min_length = min_edge
        min_diff = min(min_diff, max_edge[2] - min_length)

    return int(min_diff + .5)


runtests(highway)
