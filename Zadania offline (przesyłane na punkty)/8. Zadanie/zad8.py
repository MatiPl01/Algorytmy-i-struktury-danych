from copy import deepcopy


def is_consistent(G: 'graph represented using adjacency matrix'):
    n = len(G)
    visited = [False] * n

    def dfs(i):
        visited[i] = True
        for j in range(n):
            if G[i][j] and not visited[j]:
                dfs(j)

    dfs(0)
    return all(visited)


def is_eulerian(G: 'graph represented using adjacency matrix'):
    if not is_consistent(G): return False
    n = len(G)

    for i in range(n):
        deg = 0
        for j in range(n):
            if G[i][j]: deg += 1
        if deg % 2: return False

    return True


def euler(G: 'graph represented using adjacency matrix'):
    if not is_eulerian(G): return None
    n = len(G)
    result = []

    def dfs(i):
        for j in range(n):
            # If an edge hasn't been visited yet
            if G[i][j] == 1:
                G[i][j] = G[j][i] = -1
                dfs(j)
        result.append(i)

    dfs(0)

    # Restore original values of edges (replace -1 with 1)
    for i in range(n):
        for j in range(n):
            G[i][j] = abs(G[i][j])

    return result


# n = 31
# G = [[1] * n for _ in range(n)]
# for i in range(n): G[i][i] = 0
# print(*G)
# print(is_eulerian(G))
# print(euler(G))


G = [[0, 1, 1, 0, 0, 0],
     [1, 0, 1, 1, 0, 1],
     [1, 1, 0, 0, 1, 1],
     [0, 1, 0, 0, 0, 1],
     [0, 0, 1, 0, 0, 1],
     [0, 1, 1, 1, 1, 0]]

GG = deepcopy(G)
cycle = euler(G)
print(cycle)

if cycle is None:
    print("Błąd (1)!")
    exit(0)

u = cycle[0]
for v in cycle[1:]:
    if not GG[u][v]:
        print("Błąd (2)!")
        exit(0)
    GG[u][v] = False
    GG[v][u] = False
    u = v

for i in range(len(GG)):
    for j in range(len(GG)):
        if GG[i][j]:
            print("Błąd (3)!")
            exit(0)

print("OK")
