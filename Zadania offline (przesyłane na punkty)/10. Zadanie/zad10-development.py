from copy import deepcopy


class MaxPriorityQueue:
    def __init__(self):
        self._heap = []

    def __len__(self):
        return len(self._heap)

    def insert(self, priority: int, val: object):
        if not isinstance(priority, int):
            raise TypeError(f"priority must be 'int', not {str(type(priority))[7:-1]}")
        # Add a value as the last node of our Complete Binary Tree
        self._heap.append((priority, val))
        # Fix heap in order to satisfy a max-heap property
        self._heapify_up(len(self) - 1)

    # Removes the first value in a priority queue (of a greatest priority)
    def poll(self):
        if not self:
            raise IndexError(f'poll from an empty {self.__class__.__name__}')
        # Store a value to be returned
        removed = self._heap[0]
        # Place the last leaf in the root position
        last = self._heap.pop()
        if len(self) > 0:
            self._heap[0] = last
            # Fix a heap in order to satisfy a max-heap property
            self._heapify_down(0, len(self))
        return removed

    def get_first(self):
        return self._heap[0] if self._heap else None

    @staticmethod
    def _parent_idx(curr_idx):
        return (curr_idx - 1) // 2

    @staticmethod
    def _left_child_idx(curr_idx):
        return curr_idx * 2 + 1

    @staticmethod
    def _right_child_idx(curr_idx):
        return curr_idx * 2 + 2

    def _swap(self, i, j):
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    def _heapify_up(self, curr_idx, end_idx=0):
        while curr_idx > end_idx:
            parent_idx = self._parent_idx(curr_idx)
            if self._heap[curr_idx][0] > self._heap[parent_idx][0]:
                self._swap(curr_idx, parent_idx)
            curr_idx = parent_idx

    def _heapify_down(self, curr_idx, end_idx):
        while True:
            l = self._left_child_idx(curr_idx)
            r = self._right_child_idx(curr_idx)
            largest_idx = curr_idx

            if l < end_idx:
                if self._heap[l][0] > self._heap[curr_idx][0]:
                    largest_idx = l
                if r < end_idx and self._heap[r][0] > self._heap[largest_idx][0]:
                    largest_idx = r

            if largest_idx != curr_idx:
                self._swap(curr_idx, largest_idx)
                curr_idx = largest_idx
            else:
                break


def reconstruct_path(parents, t):
    path = []

    while t is not None:
        path.append(t)
        t = parents[t]

    n = len(path)
    for i in range(n // 2):
        swap(path, i, n - 1 - i)

    return path


def swap(A, i, j):
    A[i], A[j] = A[j], A[i]


def max_extending_path(G, s, t):
    n = len(G)
    inf = float('inf')
    pq = MaxPriorityQueue()
    parents = [None] * n
    flows = [0] * n
    flows[s] = inf

    for v, flow in G[s]:
        pq.insert(flow, (v, s))

    found = False

    while pq:
        curr_flow, (u, parent) = pq.poll()

        if curr_flow > flows[u]:
            flows[u] = curr_flow
            parents[u] = parent

            if u == t:
                found = True
                break

            for v, flow in G[u]:
                if not flows[v]:  # if flows[v] == 0
                    pq.insert(min(curr_flow, flow), (v, u))

    print(parents)
    print(flows)

    return reconstruct_path(parents, t) if found else []


def directed_weighted_graph_list(E: 'array of edges'):
    # Find a number of vertices
    n = 0
    for e in E:
        n = max(n, e[0], e[1])
    n += 1
    # Create a graph
    G = [[] for _ in range(n)]
    for e in E:
        G[e[0]].append([e[1], e[2]])
    return G


E = [(0, 1, 1), (1, 2, 4), (2, 3, 3), (0, 7, 5), (7, 1, 6), (7, 2, 16), (0, 5, 40),
     (5, 6, 38), (6, 7, 8), (7, 2, 16), (2, 6, 23), (6, 8, 35), (3, 8, 15),
     (4, 8, 20), (4, 3, 80), (4, 5, 30)]

G = directed_weighted_graph_list(E)
s = 0
t = 3
C = 3

# s = 0
# t = 8
# C = 35
#
# s = 4
# t = 8
# C = 30

# s = 7
# t = 8
# C = 16

# s = 0
# t = 4
# C = 0

### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik

# G = [[(1, 4), (2, 3)],  # 0
#      [(3, 2)],  # 1
#      [(3, 5)],  # 2
#      []]  # 3
# s = 0
# t = 3
# C = 3

GG = deepcopy(G)
path = max_extending_path(GG, s, t)

print("Sciezka :", path)

if path == []:
    print("Błąd (1): Spodziewano się ścieżki!")
    exit(0)

if path[0] != s or path[-1] != t:
    print("Błąd (2): Zły początek lub koniec!")
    exit(0)

capacity = float("inf")
u = path[0]

for v in path[1:]:
    connected = False
    for (x, c) in G[u]:
        if x == v:
            capacity = min(capacity, c)
            connected = True
    if not connected:
        print("Błąd (3): Brak krawędzi ", (u, v))
        exit(0)
    u = v

print("Oczekiwana pojemność :", C)
print("Uzyskana pojemność   :", capacity)

if C != capacity:
    print("Błąd (4): Niezgodna pojemność")
else:
    print("OK")
