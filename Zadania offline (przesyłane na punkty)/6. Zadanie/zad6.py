"""
Autor: Mateusz Łopaciński


OPIS ALGORYTMU:

===== Funkcja dist_between_cities =====
Ta funkcja służy do wyznaczenia odległości pomiędzy parą miast (w metryce Euklidesowej).

===== Funkcja create_dist_matrix =====
Ta funkcja odpowiada za utworzenia 2-wymiarowej tablicy, reprezentującej graf ważony,
w którym wagami są odległości pomiędzy odpowiednimi parami miast. Odpowiednio 'i'. wiersz
i 'j'. kolumna odpowiadają odległości, jaką trzeba pokonać, aby przebyć z miasta o indeksie
'i' do miasta o indeksie 'j'. Jeżeli 'i' == 'j' (tzn. wyznaczamy odległość z danego miasta
do niego samego), przyjmujemy, że odległość, jaką musimy przebyć, wynosi 0, bo już w tym
mieście jesteśmy. Uznaję, że odległości pomiędzy każdymi dwoma miastami są symetryczne
(długość drogi, jaka prowadzi z miasta 'i' do miasta 'j' jest taka sama jak długość drogi
z miasta 'j' do miasta 'i').

===== Funkcja TSP =====
Funkcja, która została przedstawiona na wykładzie. Śłuży ona do wyznaczenia długości najkrótszej
(w przybliżeniu) ścieżki zamkniętej (cyklu Hamiltona) dla danego zbiotu punktów i odległości
między nimi. Funkcja zwraca długość najkrótszej wyznaczonej ścieżki, indeks początkowy ostatniego
fragmenu znalezionej ścieżki o minimalnej długości oraz tablicę F, w której zapisywane były wartości
pomocnicze (długości najkrótszych ścieżek, łączących punkty (miasta) o indeksach 'i' i 'j' takich, że
przechodzą one przez wszystkie punkty o indeksach {0, ..., i, ..., j}.

===== Funkcja get_paths =====
Funkcja ta w sposób rekurencyjny odtwarza od końca kroki algorytmu TSP, a więc wyznacza kolejne
fragmenty ścieżki o najmniejszej sumarycznej długości. Najpierw zostaje zapisany początkowy fragment,
czyli odcinek, który łączy miasto o indeksie 0 z miastem o indeksie 1 (indeksy miast odpowiadają ich
indeksom w posortowanej tablicy miast po pierwszej współrzędnej (x) w sposób rosnący), a następnie
ostatni fragment ścieżki, czyli ten, dla którego znaleziona została ścieżka o minimalnej długości przez
funkcję TSP. Następnie w sposób rekurencyjny odtwarzamy pozostałe fragmenty ścieżki.

===== Funkcja get_path_cycle =====
Funkcja ta łączy obie znalezione przez funkcję get_paths ścieżki (dolną i górną) w ścieżkę zamkniętą
(cykl) o długości n + 1 (jako ostatni element zapisujemy taki sam element jak początkowy).

===== Funkcja get_cities_from_path =====
Funkcja ta, na podstawie znalezionego cyklu (wyznaczonego, przy pomocy funkcji get_path_cycle), tworzy
tablicę z nazwami kolejno odwiedzanych miast. (Kierunek, w którym się poruszamy nie ma znaczenia, więc
kolejność może być dowolna, tzn. czytana od lewej strony do prawej lub odwrotnie).

===== Funkcja bitonicTSP =====
Funkcja ta wykorzystuje opisane wyżej funkcje do znalezienia tablicy kolejno odwiedzanych miast oraz
długości ścieżki zamkniętej. Funkcja wypisuje najpierw długość ścieżki, a następnie kolejne miasta. Na koniec
zwraca długość ścieżki.
(Wewnątrz funkcji korzystam z wbudowanego w Pythona algorytmu sortującego, ponieważ, zgodnie z treścią
zadania, jest to dozwolone, a algorytm ten jest dużo szybszy niż jakakolwiek własna implementacja algorytmu
sortującego (bo jest napisany w C)).
"""


from math import *


def dist_between_cities(c1: 'first city array', c2: 'second city array'):
    return sqrt((c2[1] - c1[1]) ** 2 + (c2[2] - c1[2]) ** 2)


def create_dist_matrix(C: 'array of cities'):
    n = len(C)
    D = [[0.] * n for _ in range(n)]

    for i in range(1, n):
        for j in range(i):
            D[i][j] = D[j][i] = dist_between_cities(C[i], C[j])

    return D


def TSP(D: 'matrix representing weighted graph'):
    # Create a helper matrix to store minimal costs of paths which
    # which include every point of indices from a following set: {0, ..., i, ..., j}
    # (each point is included only once and there are no missed points
    # between any two points)
    n = len(D)
    F = [[float('inf')] * n for _ in range(n)]
    F[0][1] = D[0][1]

    def tspf(i, j):
        if F[i][j] == float('inf'):
            if j - i == 1:
                for k in range(i):
                    F[i][j] = min(F[i][j], tspf(k, i) + D[k][j])
            else:
                F[i][j] = tspf(i, j - 1) + D[j - 1][j]

        return F[i][j]

    min_l = float('inf')
    k = 0  # This variable will hold a pointer to the beginning of the last path's segment
    for i in range(n - 2):
        curr_l = tspf(i, n - 1) + D[n - 1][i]
        if curr_l < min_l:
            min_l = curr_l
            k = i

    return min_l, k, F


def get_paths(k: 'beginning index of the last path segment',
              F: 'matrix of values calculated by the TSP function',
              D: 'matrix representing weighted graph'):
    n = len(D)
    path = [[] for _ in range(n)]
    # There will always be a segment of a resulting path which
    # connects points of index 0 and index 1, so we will store this connection
    # Similar rule applies to the last segment which was found by the TSP function
    path[0].append(1)
    path[k].append(n - 1)

    def find_paths(i, j):
        # If j == 1, then i == 0 and there is no point looking for a path
        # as only 0-1 path is the remaining one which is already stored.
        if j == 1:
            return
        if i < j - 1:
            path[j - 1].append(j)
            find_paths(i, j - 1)
        else:
            min_k = -1
            for k in range(i):
                if F[k][j] + D[k][j] < F[min_k][j] + D[min_k][j]:
                    min_k = k
            path[min_k].append(j)
            find_paths(min_k, i)

    find_paths(k, n - 1)

    return path


def get_path_cycle(P: 'path array'):
    # The first point of a path will always point to two other points so
    # we can iterate over a path array twice in order to get a path from
    # both directions
    n = len(P)
    path_cycle = [0] * (n + 1)

    # Rewrite indices of subsequent cities from the first path (in the
    # first one the two directions)
    k = 1
    i = P[0][0]
    while P[i]:
        path_cycle[k] = i
        i = P[i][0]
        k += 1

    # Store an index of the last point in the path
    path_cycle[k] = i

    # Rewrite indices of subsequent cities from the second path (in the
    # second one the two directions)
    k = n - 1
    i = P[0][1]
    while P[i]:
        path_cycle[k] = i
        i = P[i][0]
        k -= 1

    return path_cycle


def get_cities_from_path(P: 'path array', C: 'array of cities'):
    n = len(P)
    result = [''] * n

    for i in range(n):
        result[i] = C[P[i]][0]

    return result


def bitonicTSP(C: 'array of cities'):
    # Sort array of cities by their 'x' coordinate in an increasing order
    C.sort(key=lambda c: c[1])
    # Create a matrix of distances between cities
    D = create_dist_matrix(C)
    # Get TSP results and find the path which was calculate
    min_l, k, F = TSP(D)
    P = get_path_cycle(get_paths(k, F, D))
    # Print a length of the calculated path and subsequent cities
    print(*get_cities_from_path(P, C)[::-1], sep=', ')
    print(min_l)
    # Return a length of the calculated path
    return min_l


if __name__ == '__main__':
    C = [["Wrocław", 0, 2], ["Warszawa", 4, 3], ["Gdańsk", 2, 4], ["Kraków", 3, 1]]
    bitonicTSP(C)
