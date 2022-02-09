"""
ZŁOŻONOŚĆ:
Obliczeniowa: O(n)
Pamięciowa:   O(n)
"""

from zad2testy import runtests


def store_sums(T):
    root = T

    def dfs(curr, parent):
        total = 0

        for i, node in enumerate(curr.edges):
            if node is parent:
                continue
            total += dfs(node, curr) + curr.weights[i]

        curr.w_sum = total

        return total

    dfs(root, None)


def balance(T):
    store_sums(T)
    root = T
    total_sum = T.w_sum
    best_diff = float('inf')
    best_edge = None

    def dfs(curr, parent):
        nonlocal best_edge, best_diff

        for i, node in enumerate(curr.edges):
            if node is parent:
                continue
            a = node.w_sum
            b = total_sum - a - curr.weights[i]
            diff = abs(a - b)

            if diff < best_diff:
                best_diff = diff
                best_edge = curr.ids[i]

            dfs(node, curr)

    dfs(root, None)

    return best_edge


runtests(balance)
