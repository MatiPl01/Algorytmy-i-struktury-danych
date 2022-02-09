from zad2testy import runtests


class Node:
    def __init__(self):
        self.edges = []
        self.weights = []
        self.ids = []

    def addEdge(self, x, w, id_):
        self.edges.append(x)
        self.weights.append(w)
        self.ids.append(id_)


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


A = Node()
B = Node()
C = Node()
D = Node()
E = Node()
A.addEdge(B, 6, 1)
A.addEdge(C, 10, 2)
B.addEdge(D, 5, 3)
B.addEdge(E, 4, 4)

print(balance(A))

# runtests(balance)
