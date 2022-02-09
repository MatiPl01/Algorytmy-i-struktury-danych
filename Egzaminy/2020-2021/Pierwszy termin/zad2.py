from zad2testy import runtests


class Node:
    def __init__(self, i=None, j=None, idx=None):
        self.i = i
        self.j = j
        self.idx = idx
        self.next = None


def vertices_to_process_ll(G: 'grid',
                           reps: "number of each vertex's repetitions"):
    n = len(G)
    m = len(G[0])
    head = Node()
    tail = head
    for i in range(n):
        for j in range(m):
            if G[i][j] == ' ':
                for k in range(reps):
                    tail.next = Node(i, j, k)
                    tail = tail.next
    return head


def get_min_weight_vertices(head, weights):
    if not head.next: return []  # If no more vertices are remaining

    # Find all vertices with the lowest distance paths
    res = []
    min_w = float('inf')
    prev = head

    while prev.next:
        if weights[prev.next.i][prev.next.j][prev.next.idx] < min_w:
            min_w = weights[prev.next.i][prev.next.j][prev.next.idx]
            res = [prev]
        elif weights[prev.next.i][prev.next.j][prev.next.idx] == min_w:
            res.append(prev)
        prev = prev.next

    # Remove nodes found and store vertex-index pairs
    for i in range(len(res) - 1, -1, -1):
        prev = res[i]
        res[i] = prev.next.i, prev.next.j, prev.next.idx
        prev.next = prev.next.next

    return res


def get_data_init(G, directions):
    A = [
        [(0, 0, (-1, 0)), (1, 45, (0, 1)), (3, 45, (0, -1))],
        [(1, 0, (0, 1)), (0, 45, (-1, 0)), (2, 45, (1, 0))],
        [(2, 0, (1, 0)), (1, 45, (0, 1)), (3, 45, (0, -1))],
        [(3, 0, (0, -1)), (0, 45, (-1, 0)), (2, 45, (1, 0))]
    ]
    times = [60, 40, 30]
    n = len(G)
    m = len(G[0])

    def get_data(prev_state, i, j):
        prev_dir = directions[i][j][prev_state]
        data = []

        for new_dir, rot_time, (d_i, d_j) in A[prev_dir]:
            new_i = i + d_i
            new_j = j + d_j
            if 0 <= new_i < n - 1 and 0 <= new_j < m - 1 and G[new_i][new_j] == ' ':
                new_state = min(prev_state + 1, len(times) - 1) if not rot_time else 0
                d_time = rot_time + times[new_state]
                data.append((new_dir, new_state, d_time, new_i, new_j))

        return data

    return get_data


def dijkstra_dp(G: 'grid matrix',
                s: 'start vertex',
                t: 'target vertex'):
    n = len(G)
    m = len(G[0])
    inf = float('inf')
    # Store information about vertices which haven't been processed yet
    states = 3
    to_process = vertices_to_process_ll(G, states)
    weights = [[[inf] * states for _ in range(m)] for _ in range(n)]
    directions = [[[-1] * states for _ in range(m)] for _ in range(n)]

    s_j, s_i = s
    t_j, t_i = t
    get_data = get_data_init(G, directions)

    directions[s_i][s_j][-1] = 1
    for new_dir, new_state, d_time, i, j in get_data(-1, s_i, s_j):
        directions[i][j][new_state] = new_dir
        weights[i][j][new_state] = d_time

    # Loop till there are some vertices which haven't been processed yet
    while True:
        # Find a vertex of the minimum total weight path
        vert = get_min_weight_vertices(to_process, weights)
        if not vert:
            return None
        # Loop over all the vertices with shortest paths
        for i, j, prev_state in vert:
            # If we reached the target, we must have found the shortest path
            # (or exhausted all shortest paths vertices and there is no path)
            if i == t_i and j == t_j:
                return weights[i][j][prev_state] if weights[i][j][prev_state] < inf else None
            for new_dir, new_state, d_time, new_i, new_j in get_data(prev_state, i, j):
                new_weight = weights[i][j][prev_state] + d_time
                if new_weight < weights[new_i][new_j][new_state]:
                    weights[new_i][new_j][new_state] = new_weight
                    directions[new_i][new_j][new_state] = new_dir


def robot(L, A, B):
    return dijkstra_dp(L, A, B)


runtests(robot)
