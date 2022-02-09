"""
Druga implementacja: O(d * n + n^2 * log(n)), gdzie:
d - liczba cyfr najdłuższej z liczb,
n - liczba liczb w tablicy T,


Trzecia implementacja (najlepsza): O(d * n + n^2), gdzie:
d - liczba cyfr najdłuższej z liczb,
n - liczba liczb w tablicy T,
Tym razem używam macierzowej implementacji Dijkstry, ponieważ tablicę
T traktujemy trochę jak macierz, a wtedy lepiej zastosować taką wersję
Dijkstry, która zadziała zawsze w czasie O(n^2).
"""
from queue import PriorityQueue
from zad3testy import runtests

# ''' With helper graph created:'''
# def mapped_numbers(T):
#     n = len(T)
#     A = [[]] * n
#     for i in range(n):
#         digits = [False] * 10
#         num = T[i]
#         while num:
#             num, dgt = divmod(num, 10)
#             digits[dgt] = True
#         A[i] = digits
#     return A
#
#
# def have_common_digit(T, i, j):
#     for k in range(10):
#         if T[i][k] and T[j][k]: return True
#     return False
#
#
# def minmax(T):
#     n = len(T)
#     min_i = max_i = n - 1
#     for i in range(1, n, 2):
#         if T[i] > T[i - 1]:
#             if T[i] > T[max_i]:     max_i = i
#             if T[i - 1] < T[min_i]: min_i = i - 1
#         else:
#             if T[i - 1] > T[max_i]: max_i = i - 1
#             if T[i] < T[min_i]:     min_i = i
#     return min_i, max_i
#
#
# def create_graph(T):
#     A = mapped_numbers(T)
#     n = len(T)
#     G = [[] for _ in range(n)]
#
#     for i in range(1, n):
#         for j in range(i):
#             if have_common_digit(A, i, j):
#                 weight = abs(T[i] - T[j])
#                 G[i].append((j, weight))
#                 G[j].append((i, weight))
#
#     return G
#
#
# def dijkstra(G: 'graph represented by adjacency lists', s: 'source', t: 'target'):
#     n = len(G)
#     inf = float('inf')
#     weights = [inf] * n
#     pq = PriorityQueue()
#     pq.put((0, s))
#
#     while not pq.empty():
#         min_w, u = pq.get()
#         # We will find the minimum total weight path only once so the
#         # code below this if statement will be executed only once
#         if min_w < weights[u]:
#             weights[u] = min_w
#             # Break a loop if we found a shortest path to the specified
#             # target
#             if u == t: break
#             # Add all the neighbours of the u vertex to the priority queue
#             for v, weight in G[u]:
#                 if weights[v] == inf:
#                     pq.put((weights[u] + weight, v))
#
#     return weights[t] if weights[t] < inf else -1
#
#
# def min_cost(T):
#     min_idx, max_idx = minmax(T)
#     G = create_graph(T)
#     return dijkstra(G, min_idx, max_idx)
#
#
#
# if __name__ == '__main__':
#     # T = [123, 890, 688, 587, 257, 246]  # 767
#     # T = [587, 990, 257, 246, 668, 132]  # -1
#     # T = [129, 758, 759, 888]
#     # print(T)
#     # print(min_cost(T))
#     runtests(min_cost)


# """Without any data structures (except mapped numbers)"""
# def mapped_numbers(T):
#     n = len(T)
#     A = [[]] * n
#     for i in range(n):
#         digits = [False] * 10
#         num = T[i]
#         while num:
#             num, dgt = divmod(num, 10)
#             digits[dgt] = True
#         A[i] = digits
#     return A
#
#
# def have_common_digit(T, i, j):
#     for k in range(10):
#         if T[i][k] and T[j][k]: return True
#     return False
#
#
# def minmax(T):
#     n = len(T)
#     min_i = max_i = n - 1
#     for i in range(1, n, 2):
#         if T[i] > T[i - 1]:
#             if T[i] > T[max_i]:     max_i = i
#             if T[i - 1] < T[min_i]: min_i = i - 1
#         else:
#             if T[i - 1] > T[max_i]: max_i = i - 1
#             if T[i] < T[min_i]:     min_i = i
#     return min_i, max_i
#
#
# def dijkstra(T, M, s: 'source', t: 'target'):
#     n = len(T)
#     inf = float('inf')
#     weights = [inf] * n
#     pq = PriorityQueue()
#     pq.put((0, s))
#
#     while not pq.empty():
#         min_w, u = pq.get()
#         # We will find the minimum total weight path only once so the
#         # code below this if statement will be executed only once
#         if min_w < weights[u]:
#             weights[u] = min_w
#             # Break a loop if we found a shortest path to the specified
#             # target
#             if u == t: break
#             # Add all the neighbours of the u vertex to the priority queue
#             for v in range(n):
#                 if weights[v] == inf and have_common_digit(M, u, v):
#                     pq.put((weights[u] + abs(T[u] - T[v]), v))
#
#     return weights[t] if weights[t] < inf else -1
#
#
# def min_cost(T):
#     min_idx, max_idx = minmax(T)
#     M = mapped_numbers(T)
#     return dijkstra(T, M, min_idx, max_idx)
#
#
# if __name__ == '__main__':
#     # T = [123, 890, 688, 587, 257, 246]  # 767
#     # T = [587, 990, 257, 246, 668, 132]  # -1
#     # T = [129, 758, 759, 888]
#     # print(T)
#     # print(min_cost(T))
#     runtests(min_cost)


"""With numbers mapped to binary states and matrix based Dijkstra"""
def bin_digits_state(num):
    state = 0
    while num:
        num, dgt = divmod(num, 10)
        state |= 1 << dgt
    return state


def have_common_digit(num1, num2):
    return bool(num1 & num2)


def mapped_numbers(T):
    return [bin_digits_state(num) for num in T]


class Node:
    def __init__(self, idx=None):
        self.idx = idx
        self.next = None


def vertices_to_process_ll(n):
    head = Node()
    tail = head
    for i in range(n):
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


def dijkstra(T: 'numbers array', M: 'numbers states array', s: 'source', t: 'target'):
    n = len(T)
    inf = float('inf')
    # Store information about vertices which haven't been processed yet
    to_process = vertices_to_process_ll(n)
    weights = [inf] * n
    weights[s] = 0

    # Loop till there are some vertices which haven't been processed yet
    while True:
        # Find a vertex of the minimum total weight path
        u = get_min_weight_vertex(to_process, weights)
        # Break if the next vertex to process is the target vertex as we have
        # already found a shortest path to this vertex before
        if u == t: break
        # Iterate over the vertex's neighbours and update weights of the paths
        for v in range(n):
            # Update the weight of a path to the vertex v if found a better one
            if have_common_digit(M[u], M[v]):
                curr_weight = weights[u] + abs(T[u] - T[v])
                if curr_weight < weights[v]:
                    weights[v] = curr_weight

    return weights


def minmax(T):
    n = len(T)
    min_i = max_i = n - 1
    for i in range(1, n, 2):
        if T[i] > T[i - 1]:
            if T[i] > T[max_i]:     max_i = i
            if T[i - 1] < T[min_i]: min_i = i - 1
        else:
            if T[i - 1] > T[max_i]: max_i = i - 1
            if T[i] < T[min_i]:     min_i = i
    return min_i, max_i


def min_cost(T):
    M = mapped_numbers(T)
    s, t = minmax(T)
    weights = dijkstra(T, M, s, t)
    return weights[t] if weights[t] != float('inf') else -1


if __name__ == '__main__':
    # T = [123, 890, 688, 587, 257, 246]  # 767
    # T = [587, 990, 257, 246, 668, 132]  # -1
    # T = [129, 758, 759, 888]
    # print(T)
    # print(min_cost(T))
    runtests(min_cost)
