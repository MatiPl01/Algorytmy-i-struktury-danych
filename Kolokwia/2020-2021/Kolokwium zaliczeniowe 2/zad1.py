"""
ZŁOŻONOŚĆ
Obliczeniowa: O(N)
Pamięciowa:   O(1)

UWAGA! Nie wiem, czy dobrze.

f(i) - funkcja, która wskazuje, jaki prostokąt należy usunąć spośród wszystkich
prostokątów o indeksach 0, 1, 2, ..., i, aby otrzymane pole powierzchni przecięcia
było jak największe. Rozwiązaniem jest f(n), gdzie n to liczba wszystkich prostokątów.

Kolejne wartości funkcji obliczamy w taki sposób, że sprawdzamy, za każdym razem, czy
bardziej opłaca nam się usunąć nowy prostokąt (o indeksie i), zostawiając wszytkie
poprzednie prostokąty (na przecięcie będą się wtedy składać prostokąty o indeksach 0, 1,
2, ..., i - 1), czy lepiej jest zotawić ten nowy prostokąt i usunąć poprzednio wybrany
do usunięcia prostokąt.
"""


from zad1testy import runtests


def cut(rect1, rect2):
    x11, y11, x12, y12 = rect1
    x21, y21, x22, y22 = rect2
    x1 = max(x11, x21)
    y1 = max(y11, y21)
    x2 = min(x12, x22)
    y2 = min(y12, y22)
    return x1, y1, x2, y2


def rect_area(x1, y1, x2, y2):
    return (x2 - x1) * (y2 - y1)


def rect(D):
    n = len(D)

    # If there is nothing to remove
    if n < 3: return None

    # Choose which rectangle from the first 3 ones
    # might be removed if we had only 3 rectangles
    cuts = [rect_area(*cut(D[i], D[j])) for i, j in ((1, 2), (0, 2), (0, 1))]
    to_remove = cuts.index(max(cuts))
    remaining = [0, 1, 2]
    remaining.remove(to_remove)
    cut_coords = cut(D[remaining[0]], D[remaining[1]])

    for i in range(3, n):
        # If we remove the i-th rectangle
        curr_remove_cut_coords = cut(cut_coords, D[to_remove])
        curr_remove_area = rect_area(*curr_remove_cut_coords)
        # If we remove the previously chosen rectangle
        prev_remove_cut_coords = cut(cut_coords, D[i])
        prev_remove_area = rect_area(*prev_remove_cut_coords)

        # print('prev', to_remove, 'curr', i, 'prev area', prev_remove_area, 'curr area', curr_remove_area)

        # Choose better of both solutions above
        if curr_remove_area > prev_remove_area:
            cut_coords = curr_remove_cut_coords
            to_remove = i
        else:
            cut_coords = prev_remove_cut_coords

    return to_remove


runtests(rect)
