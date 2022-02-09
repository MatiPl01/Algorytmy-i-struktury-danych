"""
===== Funkcja 'LIS': =====
Przy pomocy funkcji LIS wyznaczam długości najdłuższych podciągów rosnących (niekoniecznie spójnych), które
ZACZYNAJĄ się od wartości 'A[i]'. Pod indeksem 'i' w tablicy 'F' zapisuję długości tych podciągów. Aby móc postąpić
w ten sposób, iteruję po tablicy 'A" od końca, sprawdzając dla każdego elementu 'A[i]', jakie są najdłuższe obecnie
wyznaczone podciągi rosnące, które zaczynają się na indeksie 'j' takim, że 'j' > 'i' oraz 'A[i]' < 'A[j]'. Równocześnie
w pętli, w której sprawdzam te podciągi, zapisuję w tablicy 'N' (od next) indeksy tych ciągów, które może przedłużyć
element 'A[i]' (tzn. na początku których możemy dopisać element 'A[i]' tak, aby wciąż był to podciąg rosnący
i jednocześnie miał największą obecnie długość). Jeżeli trafimy na podciąg o większej długości niż ten, który został
poprzednio uznany za najdłuższy, podmieniamy zapisaną długość podciągu w tablicy 'F' i 'resetujemy' indeksy podciągów,
zapisane w tablicy 'N' (tzn. zapisujemy indeks początkowego elementu nowo znalezionego podciągu, który jest teraz
najdłuższy). Natomiast, gdy natrafiamy na podciąg takiej samej długości jak obecnie najdłuższy, do tablicy indeksów,
znajdującej się w tablicy 'N' dopisujemy (dołączamy) indeks kolejnego najdłuższego podciągu, jaki znaleźliśmy.


===== Funkcja 'getBeginLIS': =====
Funkcja, która służy do znalezienia indeksów początkowych wartości wszystkich wyznaczonych przez funkcję 'LIS'
najdłuższych podciągów rosnących. Funkcja ta wyszukuje w tablicy 'F', zwracanej przez funkcję 'LIS', wszystkie
indeksy, na których zapisane są liczby równe największej wartości w tablicy 'F' (największej długości ciągu rosnącego).


===== Funkcja 'printAllLIS': =====
Funkcja, która w sposób rekurencyjny wypisuje wszystkie podciągi rosnące, które mają taką samą długość, jak najdłuższy
podciąg rosnący. Jednocześnie funkcja ta po wypisaniu ciągu, zwraca wartość 1, która jest dodawana do łącznej
liczby znalezionych podciągów. Aby nie tworzyć każdego podciągu od początku (a podciągi mogą się różnić np. na jednej
pozycji), wykorzystuję pomocniczą tablicę o długości równiej długości najdłuższego podciągu rosnącego, w której
umieszczam kolejne wartości, tworzące ten podciąg i aktualizuję tylko te, na których kolejne podciągi, zaczynające
się od tych samych wartości, różnią się od poprzednich.

Ponieważ w funkcji 'LIS' wyszukiwaliśmy podciągi od końca, zapisane w tablicach, umieszczonych w tablicy 'N' indeksy
kolejnych wartości podciągów są zapisane w odwrotnej kolejności do rzeczywistej kolejności występowania liczb (tzn.
od indeksu największego do najmniejszego - można by użyć listy odsyłaczowej do dodawania wartości na początek zamiast
na koniec zapisanych wartości, ale można to też rozwiązać inaczej). Ponieważ chcemy uzyskać kolejność zgodną
z kolejnością występowania kolejnych podciągów w tablicy wejściowej, wystarczy sprawdzać indeksy odpowiednich tablic
z tablicy 'N' w kolejności odwrotnej do zapisanej. W ten sposób zawsze najpierw w tablicy 'result' umieścimy te
elementy, które w tablicy wejściowej występują wcześniej.


=== UWAGI: ===
Każde dwie takie same liczby, znajdujące się na różnych pozycjach w tablicy wejściowej, traktuję jako różne liczby
(uważam liczby za rozróżnialne).
"""


def LIS(A):
    n = len(A)
    F = [1] * n
    N = [[] for _ in range(n)]

    for i in range(n-1, -1, -1):
        for j in range(n-1, i, -1):
            if A[i] < A[j]:
                if F[i] < F[j] + 1:
                    F[i] = F[j] + 1
                    N[i] = [j]
                elif F[i] == F[j] + 1:
                    N[i].append(j)

    return F, N


def getBeginLIS(F):
    B = []
    n = 0
    for i in range(len(F)):
        if F[i] > n:
            n = F[i]
            B = [i]
        elif F[i] == n:
            B.append(i)
    return B


def printAllLIS(A):
    F, N = LIS(A)
    B = getBeginLIS(F)
    n = F[B[0]]

    if n == 1:
        print(*A, sep='\n')
        return len(A)

    result = [None] * n

    def recur(i, k):
        result[k] = A[i]
        k += 1
        if not N[i]:
            print(*result)
            return 1

        count = 0
        for j in range(len(N[i])-1, -1, -1):
            count += recur(N[i][j], k)
        return count

    count = 0
    for i in B:
        count += recur(i, 0)

    return count


if __name__ == '__main__':
    # a = [3, 1, 5, 7, 2, 4, 9, 3, 17, 3]
    # import random
    # a = [random.randint(0, 100) for _ in range(random.randint(2, 200))]
    a = [2, 1, 4, 3]
    # a = [1, 2, 3, 1, 2, 3, 1, 2, 3]

    # print('Input:', a)
    # print(LIS(a))
    print(printAllLIS(a))
