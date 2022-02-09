"""
Autor: Mateusz Łopaciński


OPIS ALGORYTMU:

===== Klasa MaxPriorityQueue =====
Klasa jest wykorzystywana do stworzenia obiektu, który reprezentuje kolejkę priorytetową typu 
maksimum.

===== Funkcja reconstruct_path =====
Funkcja ma za zadanie odtworzyć ścieżkę, dla której otrzymamy największy przepływ, na podstawie
tablicy wierzchołków rodziców (tablicy 'parents'), która jest tworzona podczas działania funkcji
'max_extending_path'.

===== Funkcja max_extending_path =====
Główna część algorytmu. Funkcja opiera się na podobnej zasadzie do sposobu działania algorytmu 
Dijkstry. Ponieważ musimy wystartować we wskazanym wierzchołku 's', w kolejce początkowo zostają
umieszczone wszystkie wierzchołki, do których prowadzą krawędzie wychodzące z wierzchołka 's'
wraz z priorytetem równym wadze krawędzi (początkowej przepustowości) (w kolejce umieszczamy również
wierzchołek rodzica (ten, z którego przyszliśmy), tak aby podczas relaksacji móc zapisać odpowiedni
wierzchołek w tablicy 'parents'. Powodem jest to, że relaksację wykonuję jednokrotnie dla każego
wierzchołka (zamiast relaksować sąsiadów obecnie przetwarzanego wierzchołka), dopiero po zdjęciu
wierzchołka o największym priorytecie z kolejki). W kolejnych krokach w pętli z kolejki ściągany 
jest zawsze wierzchołek o największym priorytecie, czyli o największej możliwej przepustowości na 
ścieżce, która do niego prowadzi (przepustowość ścieżki jest zawsze równoważna najmniejszą wadze 
krawędzi na tej ścieżce). Po ściągnięciu wierzchołka, sprawdzamy, czy przepustowość danej ścieżki
jest lepsza od zapisanej dla danego wierzchołka przepustowości najlepszej ścieżki (ścieżki
o największej przepustowości). Jeżeli tak, to aktualizujemy przepustowość ścieżki dla danego 
wierzchołka oraz jego rodzica. Następnie sprawdzamy, czy właśnie zaktualizowany wierzchołek jest
wierzchołkiem docelowym. Jeżeli tak, to możemy od razu zapisać informację o tym, że znaleźliśmy
szukaną ścieżkę i przerwać pętlę (dlaczego od razu przerywamy pętlę, przy pierwszym dotarciu do
wierzchołka docelowego, opisałem poniżej). Jeżeli jednak pętla nie została przerwana (wciąż nie
wyznaczyliśmy ścieżki do celu), sprawdzamy wszystkich sąsiadów poprzednio zaktualizowanegoa 
wierzchołka i jeżeli nie została wcześniej wyznaczona ścieżka o największej przepustowości dla
danego wierzchołka (sąsiada) (tzn. wartość 'flows[v]' wynosi 0), dodajemy tego sąsiada do kolejki
ze zaktualizowanym priorytetem, którym jest minimum z wartości przepływu na ścieżce do wierzchołka
rodzica (wierzchołka 'u') i z wagi krawędzi, która łączy wierzchołek 'u' z 'v' (tzn. dołożona do
ścieżki krawędź może mieć albo przepustowość mniejszą niż przepustowość ścieżki (czyli minimalna
waga krawędzi na danej ścieżce), albo mnieć wagę przynajmniej równą tej przepustowości (wtedy nie
zostaje zmniejszona przepustowość ścieżki, bo i tak przepustowość poprzedniego fragmentu ścieżki
jest już taka sama lub mniejsza od wagi ostatniej krawędzi).


Dlaczego algorytm jest poprawny?

Z kolejki priorytetowej typu maksimum zawsze ściągamy najpierw ścieżkę o maksymalnej przepustowości.
Takie podejście gwarantuje nam, że nie istnieje żadna inna ścieżka, dla której mozemy uzyskać większą
przepustowość, ponieważ nigdy nie możemy zwiększyć przepustowości ścieżki po dodaniu krawędzi (ta
przepustowość i tak będzie ograniczona z góry przez przepustowość poprzedniej ścieżki bez dodawanej
krawędzi). Wiemy więc, że każda nowa ścieżka, jaka pojawi się w kolejce, będzie miała przepustowość
nie większą niż poprzednia największa przepustowość. Z tego powodu zawsze opłaca nam się rozpatrzeć
najpierw ścieżkę, dla której przepustowość jest największa, bo jeżeli nawet do danego wierzchołka
prowadzi kilka różnych ścieżek, to wzięcie ścieżki o największej przepustowości pozwoli nam zawsze
otrzymać największą możliwą przepustowość kolejnej ścieżki (po dołożeniu do niej nowej krawędzi).

Z tego też powodu możemy wykonać relaksację nie przed wrzuceniem wierzchołka do kolejki, poprawiając
wielokrotnie wartość ścieżki o największej przepustowości, jaka do niego dochodzi, lecz zamiast tego
możemy zapisać najlepszą przepustowość ścieżki zaraz po zdjęciu wierzchołka z kolejki. Wtedy warunek
'if curr_flow > flows[u]' zostanie spełniony tylko raz, gdy po raz pierwszy dotrzemy do wierzchołka
'u', ponieważ dotrzemy do niego ścieżką o największej przepustowości. Dlatego też w zagnieżdżonym
warunku sprawdzam później, czy znaleźliśmy ścieżkę do celu, bo pierwsza ścieżka do wierzchołka
docelowego, jaką ściągniemy z kolejki, będzie tą o największej przepustowości.


UWAGA:
Ponieważ w poleceniu nie jest powiedziane, jak należy postąpić, gdy ściezka od wskazanego wierzchołka
's' do 't' nie istnieje (a taka sytuacja może się zdarzyć, np. gdy niemożliwe jest dotarcie do
wierzchołka docelowego - bo to jest graf skierowany), przyjmuję, że w takiej sytuacji należy zwrócić
pustą listę (tablicę).


ANALIZA ZŁOŻONOŚCI OBLICZENIOWEJ:
Obliczeniowa:
O(E * log(E)) = O(E * log(V)) - tak jak dla algorytmu Dijkstry dla grafu w postaci list sąsiedztwa
E - liczba krawędzi w grafie
V - liczba wierzchołków w grafie
"""

from copy import deepcopy


class MaxPriorityQueue:
    def __init__(self):
        self._heap = []

    def __len__(self) -> int:
        return len(self._heap)

    def insert(self, priority: int, val: object):
        if not isinstance(priority, int):
            raise TypeError(f"priority must be 'int', not {str(type(priority))[7:-1]}")
        # Add a value as the last node of our Complete Binary Tree
        self._heap.append((priority, val))
        # Fix heap in order to satisfy a max-heap property
        self._heapify_up(len(self) - 1)

    # Removes the first value in a priority queue (of the greatest priority)
    def poll(self) -> (int, object):
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

    def get_first(self) -> (int, object):
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

            # Break a loop if the current index is an index of an element
            # with the largest priority value
            if largest_idx == curr_idx:
                break

            self._swap(curr_idx, largest_idx)
            curr_idx = largest_idx


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


def max_extending_path(G: 'graph represented by adjacency lists',
                       s: 'start vertex',
                       t: 'target vertex') -> list:
    if s == t: return []

    n = len(G)
    inf = float('inf')
    pq = MaxPriorityQueue()
    parents = [None] * n
    flows = [0] * n
    flows[s] = inf

    # Insert all the neighbours of the start vertex to a priority
    # queue with a priority which is a weight of an edge from 's' to 'v'
    for v, flow in G[s]:
        pq.insert(flow, (v, s))

    found = False

    while pq:
        curr_flow, (u, parent) = pq.poll()

        # Update the max flow value of the 'u' vertex and its parent
        if curr_flow > flows[u]:
            flows[u] = curr_flow
            parents[u] = parent

            # Check if a target was reached
            if u == t:
                found = True
                break

            # Add all neighbours of the current 'u' vertex that have no
            # max flow path calculated yet to a priority queue
            for v, flow in G[u]:
                if not flows[v]:
                    # Update a path's flow value if the last edge's weight
                    # is lower than a total flow od a path to 'u' vertex
                    pq.insert(min(curr_flow, flow), (v, u))

    # Create a path from the source to the target which was calculated as a path
    # of the largest flow if such a path exists (if 't' is reachable from 's')
    return reconstruct_path(parents, t) if found else []


### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik

G = [[(1, 4), (2, 3)],  # 0
     [(3, 2)],  # 1
     [(3, 5)],  # 2
     []]  # 3
s = 0
t = 3
C = 3

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
