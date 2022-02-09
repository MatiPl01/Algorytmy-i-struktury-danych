"""
[10 pkt.] Zadanie 3. Niech G = (V, E) będzie pewnym spójnym nieskierowanym grafem. Dla każdych
dwóch wierzchołków u,v ∈ V, przez (u, v) rozumiemy długość najkrótszej ścieżki między u i v
(mierzoną liczbą krawędzi). Długością przekątnej grafu nazywamy wartość max{d(u, v)}, gdzie u, v ∈ V.
Proszę opisać możliwie jak najszybszy algorytm, który mając na wejściu acykliczny graf nieskierowany
(reprezentowany przez listy sąsiedztwa) oblicza długość jego przekątnej (podpowiedź: nasz graf jest
dość szczególnej postaci, co bardzo ułatwia zadanie)
"""

"""
Graf to drzewo. Wyznaczamy najdalszą ścieżkę z dowolnego wierzchołka i z najdalszego wierzchołka
ponownie wyznaczamy najdalszy wierzchołek. Wystarczy 2 razy zwykły algorytm BFS. Rozwiązanie
szczegółowo opisane w plikach z zadaniami z BIT Algo.
"""
