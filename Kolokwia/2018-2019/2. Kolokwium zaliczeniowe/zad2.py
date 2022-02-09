"""
O(V), bo wejdziemy tylko do wierzchołków, których stopień nie przekracza 2,
a więc z takiego wierzchołka wychodzą max. 2 krawędzie, więc liczba
odwiedzonych krawędzi wynosi O(V).

Ważna jest obserwacja taka, że skoro każdy wierzchołek ma stopień nie
większy niż 2, to jeżeli do niego wejdziemy jedną krawędzią, to drugą
krawędzią musimy wyjść (gdy stopień wynosi 2) lub już z niego dalej nie
pójdziemy (gdy stopień wynosi 1). Możemy więc zastosować algorytm DFS/BFS,
trzymając jedną, wspólną dla wszystkich wywołań DFS/BFS, tablicę odwiedzonych
wierzchołków. W pętli będziemy wywoływać DFS/BFS dla każdego nieodwiedzonego
wczesniej wierzchołka, którego stopień nie przekracza 2 i poruszać się po
grafie wyłącznie po wierzchołkach o stopniu nie większym niż 2, zapisując
odległości dla każdego z wierzchołków od punktu startowego. Ponieważ możemy
iść w dwie strony (zacząć po środku ścieżki), jako długość ścieżki zwrócimy
sumę odległości dwóch końców, do których dojdziemy i zwrócimy maksimum ze
wszystkich wywołań.
"""

def longest_easy_path(G):
    n = len(G)
    visited = [False] * n

    def dfs(u):
        visited[u] = True
        length = 0
        for v in G[u]:
            if not visited[v] and len(G[v]) <= 2:
                length += dfs(v) + 1
        return length

    max_length = 0
    for u in range(n):
        # If not visited and has a degree at most 2
        if not visited[u] and len(G[u]) <= 2:
            max_length = max(max_length, dfs(u))

    return max_length


def undirected_graph_list(E: 'array of edges'):
    n = 0
    for e in E:
        n = max(n, e[0], e[1])
    n += 1

    G = [[] for _ in range(n)]
    for edge in E:
        G[edge[0]].append(edge[1])
        G[edge[1]].append(edge[0])
    return G


E = [(0, 1), (0, 10), (1, 5), (1, 4), (1, 2), (2, 3), (3, 4), (4, 5),
     (5, 8), (5, 10), (6, 7), (6, 9), (7, 8), (9, 10)]

G = undirected_graph_list(E)
print(longest_easy_path(G))
