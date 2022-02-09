"""
Autor: Mateusz Łopaciński


OPIS ALGORYTMU:

===== Funkcja dijkstra_min_paths =====
Przy pomocy tej funkcji, bazując na algorytmi Dijkstry, wyznaczam takie dwa wierzchołki u, v,
dla których smuaryczna długość (waga) ścieżki z s do u, s do v oraz długość (waga) krawędzi,
która łączy wierzchołki u i v jest najmniejsza. Aby została wyznaczona ta sumaryczna długość,
musi nastąpić sytuacja, w której wierzchołek u będzie połączony z wierzchołkiem v krawędzią
oraz zarówno z wierzchołka u jak i z wierzchołka v istnieje ścieżka do wierzchołka startowego
(w którym rozpoczęliśmy wywołanie algorytmu Dijkstry). W przypadku, gdy znajdziemy cykl, to
zawsze jeżeli sumaryczna długość (waga) krawędzi będzie mniejsza niż poprzednia najmniejsza,
to zastąpimy tę poprzednią wartość nową wartością, a także zapiszemy wierzchołki u oraz v.

Warto w tym miejscu zawuważyć, że funkcja dijkstra_min_paths nie gwarantuje nam, że znaleziony
cykl będzie cyklem przechodzącym przez wierzchołek startowy s. W związku z tym, ścieżki do
wierzchołków u oraz v mogą się częściowo pokrywać. Nie musimy tego jednak sprawdzać, ponieważ
mamy powiedziane, że wagi krawędzi są nieujemne, więc nawet, jeżeli przy rozpoczęciu algorutmu
Dijkstry z wirzchołka s znajdziemy taką parę wierzchołków u i v, które należą do cyklu, do którego
nie należy s, oznacza to, że cykl o najmniejszej sumaryczne wadze krawędzi znajduje się dalej
w grafie i być może obejmuje wierzchołki u oraz v. Wynika to stąd, że jeżeli wierzchołek s leżałby
na cyklu o najmniejszej długości, to wyznaczone wierzchołki u oraz v musiałyby znajdować się na
ścieżkach, które nie posiadają żadnej wspólnej krawędzi i również należą do tego cyklu. Innymi
słowy, ponieważ wagi krawędzi są nieujemne, nie zdarzy się sytuacja, w której po sprawdzeniu
wszyskich wierzchołków, jakie należą do grafu, nie znajdziemy cyklu o najmniejszej wadze (o ile
w grafie znajduje się jakikolwiek cykl) (tzn. te wliczone wagi pokrywających się ścieżek spowodują,
że łączna waga potencjalnego cyklu, jaką uzyskaliśmy dla danego wierzchołka startowego s, będzie
większa od wagi, którą uzyskamy później, startując z tego wierzchołka, który teraz znajduje się
na rozgałęzieniu wspólnej części ścieżki dla wierzchołków u i v). Spójrzmy na poniższy przykład:

A *
   \
    2
     \
    B *---1---* C
	   \     /
	    3   1
		 \ /
		D *
		
Załóżmy, że najpierw wywołamy funkcję dijkstra_min_paths dla wierzchołka A. Algorytm znajdzie
najkrótszą ścieżkę do wierzchołka C o długości 2 + 1 = 3, ścieżkę (nie najkrótszą - dokładniej to 
najkrótszą, która nie prowadzi przez wierzchołek C) do wierzchołka D o długości 2 + 3 = 5 oraz
krawędź, która łączy wierzchołek C z D o wadze (długości) 1. Jak widać, w obu ścieżkach występuje
krawędź o wadze 2 (krawędź A-B), choć nie istnieje cykl, który zawiera tę krawędź. Jest to wynik,
jakiego można było się spodziewać (opis wyżej), ponieważ funkcja wyznaczyła 2 wierzchołki, leżące
najbliżej tego, dla którego szukamy cykli, czyli wierzchołka A, które nie leżą na tej samej ścieżce.
Otrzymamy więc również na wyjściu długość 5 + 3 + w(C, D) = 5 + 3 + 1 = 9.

Na tym jednak nie kończy się działanie algorytmu, ponieważ w kolejnym kroku "usuwamy" wierzchołek A
z grafu (ponieważ sprawdziliśmy już najkrótsze ścieżki, które go zawierają) i szukamy cykli w pozostałej
części grafu. (Ponieważ wywołujemy funkcję dijkstra_min_paths zawsze dla kolejnych wierzchołków (każdy
kolejny wierzchołek s, przekazany w argumencie, ma indeks o 1 większy od poprzedniego), zamiast usuwania
wierzchołków z grafu, możemy po prostu nie dodawać tych wierzchołków do listy wierzchołków do przetworzenia,
przez co nie będą one brane pod uwagę). W kolejnym kroku zaczniemy więc w wierzchołku B i będziemy szukać
w grafie o wierzchołkach {B, C, D} (A odrzuciliśmy) kandydatów na cykl. Tym razem ponownie dostaniemy
ścieżki do wierzchołków C i D, gdzie ścieżka B -> C ma długość 1, a ścieżka B -> D ma długość 3. Do tego
trzeba doliczyć długość (wagę) krawędzi C-D.

W ten sposób dostaliśmy szukany cykl.

Pozostała jeszcze kwestia krawędzi o zerowych wagach, które mogą zostać odczytane jako brak krawędzi przez
powyższy algorytm i błędnie wliczone do cyklu o najmniejszej długości. Aby temu zaradzić, możemy poza
minimalizowaniem sumarycznej wagi cyklu, minimalizować liczbę krawędzi w tym cyklu. Jeżeli znajdziemy kilka
kandydatów na cykle o tej samej sumarycznej wadze, może to oznaczać, że niektóre z nich zosały wyznaczone
błędnie, ponieważ wspólna część ścieżki od wierzchołka startowego s do wierzchołka u oraz ścieżki z s do v
będzie składała się z krawędzi o zerowych wagach. W takiej sytuacji, wystarczy zapamiętać, ile krawędzi
znalazło się łącznie po drodze i jeżeli mamy sytuację konfliktową, w której znaleźliśmy ponownie kandydata
na cykl o tej samej wadze, wybieramy tego o mniejszej liczbie krawędzi. Spójrzmy na przykład:

	B		    C        D
      *----0----*---1---*
     /         / \     /
    0         0   3   2
   /         /     \ /
  *--1000-- *       * 
A           F        E

Zauważmy, że jeżeli zaczęlibyśmy algorytm w wierzchołku A, początkowo otrzymalibyśmy kandydata na cykl
w postaci wierzchołka startowego w wierzchołku A oraz wierzchołków D i E. Ponieważ waga takiego zestawu
wynosi A -> D: 0 + 0 + 1 = 1,   A -> E: 0 + 0 + 3 = 3,   D - E: 2, czyli razem: 1 + 3 + 2 = 6 i jest to
równocześnie waga cyklu o najmniejszej wadze (C - D - E), zapisalibyśmy, że cykl przechodzi przez wierzchołki
A, D, E, co jest oczywiście błędne. Z tego powodu, postępując w spośób analogiczny jak wyżej, zliczamy również
liczby krawędzi kandydata na cykl. Tutaj np. po wywołaniu funkcji dijkstra_min_paths w wierzchołku C, otrzymujemy
również kandydata na cykl o długości 6 (tym razem prawidłowy cykl), ale mamy mniej krawędzi, więc zapisujemy ten
cykl jako rezultat.

Dlaczego to działa?
Jeżeli w grafie jest choć 1 cykl, to graf zawsze ma najkrótyszy cykl. My sprawdzamy wszystkie możliwe wierzchołki,
w których cykl może się zaczynać, a wynikowy cykl będzie składał się z 2 najkrótszych ścieżek, które się nie 
pokrywają i istnieje krawędź między ich wierzchołkami końcowymi (jej waga również jest wliczana do sumarycznej
długości). Dzięki temu, musimy w którymś wywołaniu funkcji dijkstra_min_paths rozpocząć od wierzchołka, który
znajduje się na najkrótszym cyklu, a startując z tego wierzchołka, jako rezultat zawsze wyznaczymy prawidłowy cykl,
bo nie może istnieć inny najkrótszy cykl o długości (wadze) większej od najkrótszego, więc jeżeli znajdziemy cykl,
to wśród znalezionych cykli znajdzie się szukany cykl o minimalnej długości (wadze).

Obserwacje:
Algorytm wyznacza zawsze najkrótszy cykl pod względem krawędzi spośród cykli o najmniejszej wagowej długości.


===== Funkcja dijkstra_min_cycle =====
Tu już w skrócie, bo najbardziej skomplikowana część została opisana wyżej. W tej funkcji, również bazującej na
algorytmie Dijkstry, wyznaczamy ścieżki do wierzchołków, które tworzą cykl (znalezionych wcześniej). Ważnym
elementem jest to, że jeżeli dojdziemy już do jednego z dwóch wyznaczonych wierzchołków, które znajdują się na
szukanym cyklu, nie wykonujemy relaksacji z tego wierzchołka, ponieważ to mogłoby spowodować, że otrzymalibyśmy
finalnie ścieżkę, na której oba wierzchołki, leżące na cyklu, by się znalazły równocześnie (więc mielibyśmy
tylko fragment cyklu).

Funkcja zwraca tablicę rodziców wierzchołków, z kórej odczytamy ścieżki do wierzchołków końcowych u, v (tych,
dla których ścieżki od wierzchołka początkowego do tych wierzchołków wraz z krawędzią, która łączy te wierzchołki,
utworzą cykl)


===== Funkcja reconstruct_cycle =====
Ta funkcja jest już prosta i jedynei odczytuje dwie ścieżki, zapisując wierzchołki w odpowiedniej kolejności,
aby odpowiadała ona kolejności wierzchołków z cyklu.


===== Funkcja min_cycle =====
Ta funkcja wywołuje funckję dijkstra_min_paths, poszukując cyklu. Następnie korzysta z powyższych funkcji do
jego odtworzenia. Jeżeli cykl nie istnieje, nie dostaniemy nigdy długości kandydata na cykl innej niż nieskończoność
(jako wartość zwrócona przez funkcję dijkstra_min_paths), więc wówczas zwracamy pustą tablicę.


ANALIZA ZŁOŻONOŚCI:
Obliczeniowa:
O(V^3), gdzie V - liczba wierzchołków w grafie
Pamięciowa:
O(V), gdzie V - liczba wierzchołków w grafie
"""


from copy import deepcopy


class Node:
    def __init__(self, idx=None):
        self.idx = idx
        self.next = None


def vertices_to_process_ll(s: 'first vertex index', n: 'last vertex index'):
    """Creates a linked list of vertices to process in a Dijkstra's algorithm"""
    head = Node()
    tail = head
    for i in range(s, n):
        tail.next = Node(i)
        tail = tail.next
    return head


def get_min_weight_vertex(head, weights):
    """
    Finds the next vertex to process in a Dijkstra's algorithm and removes
    a vertex which was found. The vertex returned is always a vertex which
    was relaxed before and its current path to the source vertex has the
    lowest cost (this works as a priority queue used in a Dijkstra's algorithm
    for graphs represented by adjacency lists)
    """
    if not head.next: return None  # If no more vertices are remaining

    # Find a vertex of the lowest weight path to the source
    min_prev = head
    prev = head.next
    while prev.next:
        if weights[prev.next.idx] < weights[min_prev.next.idx]:
            min_prev = prev
        prev = prev.next

    # Remove a vertex that was found
    u = min_prev.next.idx
    min_prev.next = min_prev.next.next

    return u


def dijkstra_min_paths(G: 'graph represented by adjacency matrix', s: 'source vertex index'):
    """
    This function is supposed to find two vertices for which a sum of their
    distances from the source vertex plus a weight of an edge which connect
    them together is the smallest. To handle edges of a weight 0, this function
    also keeps track of the length of each paths in terms of the number of edges
    (not only their weights). A function returns u, v vertices which have the
    minimum value of a sum of shortest paths to them from the source and an edge
    which connects them together (candidates for a cycle), total weight of such
    a path (which may be a cycle) and a total number of edges in this path (if
    u, v and s are not placed on the same cycle, u, v must share some path so
    these edges will be added twice (separately for u and v)).
    """
    n = len(G)
    inf = float('inf')
    # Store information about vertices which haven't been processed yet
    to_process = vertices_to_process_ll(s, n)
    parents = [None] * n
    weights = [inf] * n   # Shortest paths weights from the source s to each vertex
    lengths = [0] * n     # Lengths of the shortest paths (see above) (numbers of edges)
    weights[s] = 0
    min_weight = res_length = inf
    min_u = min_v = None

    # Loop till there are some vertices which haven't been processed yet
    while True:
        # Find a vertex of the minimum total weight path
        u = get_min_weight_vertex(to_process, weights)

        # Check if a vertex was found (if not, all vertices must have
        # been processed before)
        if u is None: break

        for v in range(n):
            # Skip if no edge (-1 means no edge)
            if G[u][v] == -1: continue

            # If there was some other path to the vertex before (there is a weight
            # lower than infinity), we have a cycle
            if weights[v] < inf and parents[u] != v:
                # Check if a weight of a path from the u vertex to the source plus
                # a weight of a path from the v vertex to the source plus a weight
                # of a u-v edge is lower than the previous lowest weight
                curr_weight = weights[v] + weights[u] + G[u][v]
                if curr_weight < min_weight:
                    min_weight = curr_weight
                    res_length = lengths[u] + lengths[v] + 1
                    min_u = u
                    min_v = v

            # Relax the v neighbour of the u vertex
            if weights[u] + G[u][v] < weights[v]:
                weights[v] = weights[u] + G[u][v]
                lengths[v] = lengths[u] + 1
                parents[v] = u

    return min_u, min_v, min_weight, res_length


def dijkstra_min_cycle(G: 'graph represented by adjacency matrix',
                       s: 'source vertex for which a cycle was found',
                       x: 'first of the vertices placed on a cycle',
                       y: 'second of the vertices placed on a cycle'):
    """
    This function finds shortest paths from the source s to x and y vertices
    and returns an array of parents vertices.
    """
    n = len(G)
    inf = float('inf')
    # Store information about vertices which haven't been processed yet
    to_process = vertices_to_process_ll(0, n)
    parents = [None] * n
    weights = [inf] * n
    weights[s] = 0
    # Store flags which indicate whether x and y were processed
    x_processed = y_processed = False

    # Loop till there are some vertices which haven't been processed yet
    while True:
        # Find a vertex of the minimum total weight path
        u = get_min_weight_vertex(to_process, weights)

        # Check if the current vertex is one of two vertices placed on a cycle.
        # If yes, update a flag which correspond to such a vertex
        if u == x:
            x_processed = True
            continue
        elif u == y:
            y_processed = True
            continue

        # If both x and y vertices were processed, break a loop as we don't have
        # to traverse the graph anymore
        if x_processed and y_processed: break

        # Iterate over the vertex's neighbours and relax them
        for v in range(n):
            # Skip if no edge (-1 means no edge)
            if G[u][v] == -1: continue
            # Relax the v neighbour of the u vertex
            if weights[u] + G[u][v] < weights[v]:
                weights[v] = weights[u] + G[u][v]
                parents[v] = u

    return parents


def reconstruct_cycle(parents: 'array of parents vertices',
                      s: 'source vertex for which a cycle was found',
                      x: 'first of the vertices placed on a cycle',
                      y: 'second of the vertices placed on a cycle'):
    """
    This function builds a cycle based on a parents array returned by the
    dijkstra_min_cycle function. A function joins shortest paths from the
    source s to both vertices u and v in such a way that they form a cycle.
    """
    result = []

    def recur(i):
        if i != s:
            recur(parents[i])
        result.append(i)

    recur(x)

    while y != s:
        result.append(y)
        y = parents[y]

    return result


def min_cycle(G: 'graph represented by adjacency matrix'):
    """
    This function finds a cycle of the minimum weight in a graph G which has
    the least number of edges (only if there is more than one cycle of the same
    minimum total weight).
    """
    n = len(G)
    inf = float('inf')
    min_weight = res_length = inf
    min_s = min_u = min_v = -1

    for s in range(n):
        u, v, weight, length = dijkstra_min_paths(G, s)
        if weight < min_weight or (weight == min_weight and length < res_length):
            min_weight = weight
            res_length = length
            min_s = s
            min_u = u
            min_v = v

    # Return an empty array if there is no cycle
    if min_weight == inf:
        return []

    parents = dijkstra_min_cycle(G, min_s, min_u, min_v)
    return reconstruct_cycle(parents, min_s, min_u, min_v)


### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik
  
G = [[-1, 2,-1,-1, 1],
     [ 2,-1, 4, 1,-1],
     [-1, 4,-1, 5,-1],
     [-1, 1, 5,-1, 3],
     [ 1,-1,-1, 3,-1]]
LEN = 7


GG = deepcopy( G )
cycle = min_cycle( GG )

print("Cykl :", cycle)


if cycle == []: 
  print("Błąd (1): Spodziewano się cyklu!")
  exit(0)
  
L = 0
u = cycle[0]
for v in cycle[1:]+[u]:
  if G[u][v] == -1:
    print("Błąd (2): To nie cykl! Brak krawędzi ", (u,v))
    exit(0)
  L += G[u][v]
  u = v

print("Oczekiwana długość :", LEN)
print("Uzyskana długość   :", L)

if L != LEN:
  print("Błąd (3): Niezgodna długość")
else:
  print("OK")
