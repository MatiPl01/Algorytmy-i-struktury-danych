"""
Autor: Mateusz Łopaciński


OPIS ALGORYTMU:

===== Klasa Node =====
Klasa służy do reprezentowania wierzchołków drzewa kodującego, jakie jest tworzone przez funkcję
create_coding_tree.

UWAGA:
Ponieważ zaimportowana z biblioteki 'queue' kolejka, w przypadku, gdy dodawane są elementy o tym samym priorytecie,
porównuje wartości obiektów, aby móc skorzystać z kolejki priorytetowej, musimy dodać metodę specjalną __gt__
(lub __lt__) do klasy Node, aby umożliwić porównywanie instancji tej klasy.

Na przykład dla argumentów S = ["a", "b", "c", "d", "e", "f"] oraz F = [10, 11, 10, 13, 1, 20] otrzymalibyśmy
wyjątek: "TypeError: '<' not supported between instances of 'Node' and 'Node'" (gdybyśmy usunęli metodę __gt__).

===== Funkcja create_coding_tree =====
Funkcja, która tworzy drzewo kodujące Huffmana. Krawędź, prowadząca w lewą stronę, odpowiada cyfrze
0 w wynikowym kodzie, a krawędź, prowadząca w prawą stronę drzewa (przy schodzeniu w dół drzewa),
odpowiada cyfrze 1 w wynikowym kodzie. Wierzchołki drzewa nie przechowują żadnej wartości poza tymi,
które są liśćmi drzewa (odpowiadającymi kodowanym znakom), które przechowują kodowany znak.

===== Funkcja create_huffman_codes ======
Funkcja ta, wykorzystując algorytm DFS, przechodzi przez kolejne krawędzie drzewa i zapisuje odpowiadające
im (opisane wyżej) wartości w tymczasowej tablicy dynamicznej 'code', której wartości są łączone do
ciągu tekstowego, reprezentującego wynikowy kod, po dotarciu do liścia drzewa. Wykorzystuję tablicę,
a nie konkatenację stringów, ponieważ dopisywanie nowej wartości na koniec tablicy odbywa się w zamortyzowanym
czasie O(1), a konkatenacja stringów zawsze wiąże się z utworzeniem nowego stringa, więc działa w czasie O(n)
(zależnym od długości wynikowego ciągu tekstowego).

===== Funkcja reorder_codes =====
Funkcja ta przywraca kolejność par znak-kod do początkowej kolejności znaków w tablicy wejściowej. W tym celu,
zapamiętuję początkowe indeksy kodowanych znaków w postaci krotek (znak, indeks), a następnie sortuję utworzoną
tablicę par znak-indeks oraz utworzoną wcześniej, przy pomocy opisanej wyżej funkcji, tablicę par znak-kod, po
kodach Unicode znaków. Następnie, w pętli zamieniam kolejność par znak-kod w tablicy z kodami Huffmana w taki
sposób, aby każda para znalazła się na miejscu, na którym znajdował się kodowany znak w tablicy wejściowej.

===== Funkcja calc_required_bits =====
Funkcja ta ma na celu zliczenie łącznej liczby bitów, jakie są wymagane, aby zakodować informację, przy pomocy
kodowania Huffmana, w której odpowiednie, otrzymane na wejściu znaki, występują tyle razy w kodowanej informacji,
ile wynoszą odpowiednie częstości, otrzymane na wejściu, w postaci tablicy 'F'.

===== Funkcja huffman =====
Funkcja ta korzysta z opisanych wyżej funkcji, w celu otrzymania kodów kolejnych znaków. Na koniec wypisuje
otrzymane kody, odpowiadające kolejnym znakom oraz liczbę bitów, jakie są potrzebne do zakodowania informacji.


ANALIZA ZŁOŻONOŚCI OBLICZENIOWEJ:
Średnia          Najgorsza
O(n * log(n))    O(n^2)

*Najgorsza złożoność osiągana jest wtedy, gdy długości kodów Huffmana bardzo się między sobą różnią. Taki przypadek
może mieć miejsce, gdy utworzone zostanie drzewo kodujące (drzewo binarne) na którego każdym poziomie będzie jedynie
jeden liść, np.:
          *
        /   \
       *     a
     /   \
    *     b
  /   \
...    c
Wówczas złożoność czasowa, jaka jest potrzebna do utworzenia wszystkich kodów wynosi tyle, ile jest równa sumaryczna
złożoność łączenia kolejnych cyfr kodu dla każdego z kodowanych znaków. Np. kod dla znaku 'c' w powyższym drzewie
będzie miał postać '001', a więc tablica 'code', utworzona przez funkcję create_huffman_codes dla tego znaku będzie
wyglądała następująco: ['0', '0', '1'], więc finalnie złączenie kolejnych znaków w wynikowy ciąg tekstowy zajmie O(3)
czasu, bo tablica ma 3 elementy. Ponieważ rozważamy niezbalansowane drzewo binarne, kody kolejnych znaków, którym
odpowiadają kolejne liście drzewa (na każdym poziomie jeden liść - na ostatnim poziomie są 2 liście), kod Huffmana dla
każdego kolejnego znaku będzie miał długość o 1 większą od poprzedniego. Ponieważ kodujemy n znaków, sumaryczna
złożoność obliczeniowa, potrzebna na połączenie w ciągi tekstowe tablic znaków dla kolejnych kodów wynosi:
O(1) + O(2) + O(3) + ... + O(n-1) + O(n-1) = O(1 + 2 + 3 + ... + (n-1) + (n-1)) = O((1 + (n-1)) / 2 * n + (n-1))
= O(n^2)
(Również wypisanie wszystkich kodów zajmie maksymalnie O(n^2) czasu).

*Średnia złożoność obliczeniowa wynika z tego, że utworzenie drzewa kodującego odbywa się w czasie O(n * log(n)),
przejście przez drzewo kodujące O(2n - 1) = O(n) (bo tyle mamy wierzchołków, a każdy odwiedzamy tylko raz),
O(n * log(n)) - złożoność sortowania.
"""

from queue import PriorityQueue


class Node:
    def __init__(self):
        self.left  = None
        self.right = None

    # This method is only to allow PriorityQueue comparisons when elements
    # have the same priority
    def __gt__(self, other):
        return 0


def create_coding_tree(S: 'array of chars to encode', F: 'array of their frequencies') -> Node:
    n = len(S)
    # Create a priority queue of the max size equal to the number
    # of characters to encode
    pq = PriorityQueue(n)

    # Add all char-frequency pairs to the queue as Node objects
    for i in range(n):
        node = Node()
        # Add a char property (only leaf nodes will have this property)
        node.char = S[i]
        # Insert a node with its priority (frequency of a character)
        pq.put((F[i], node))

    # Create a coding tree
    while True:
        # Take a pair of two entries of the lowest priority (frequency)
        x_priority, x_node = pq.get()
        y_priority, y_node = pq.get()
        # Create a new node and link two nodes from above to this node
        node = Node()
        node.left  = y_node
        node.right = x_node
        # Insert this node to the priority queue only if a priority queue
        # hasn't been exhausted yet
        if not pq.empty():
            pq.put((x_priority + y_priority, node))
        # Else, return a resulting root node of the encoding tree
        else:
            return node


def create_huffman_codes(ct: 'Huffman coding tree', n: 'number of characters to encode') -> list:
    # Traverse a tree using a DFS algorithm and create codes of characters
    # (we assume that a left branch corresponds to the '0' code and a right
    # one to the '1' code)
    result = [None] * n

    # Create a temporary array in which a resulting code of a character will
    # be temporarily stored (created by appending subsequent digits of a code)
    code = []
    i = 0

    def encode(node):
        # If we entered the last node, store a character and its code in
        # a resulting array
        if node.left is node.right is None:
            nonlocal i
            result[i] = (node.char, ''.join(code))
            i += 1
            return

        if node.left:
            code.append('0')
            encode(node.left)
            code.pop()
        if node.right:
            code.append('1')
            encode(node.right)
            code.pop()

    encode(ct)

    return result


def reorder_codes(C: 'array of character-code pairs', S: 'initial array of characters'):
    n = len(S)
    # Create an array of char-index pairs
    A = [(S[i], i) for i in range(n)]

    # Sort the array created above and the array of char-code pairs by Unicode
    # codes of characters
    A.sort(key=lambda pair: pair[0])
    C.sort(key=lambda pair: pair[0])

    # Create a temporary array to store information if the current entry was
    # placed on its final position
    T = [False] * n

    # Reorder the array or char-code pairs so that all entries are stored
    # in the same order they were stored in the S array
    for i in range(n):
        if not T[i]:
            swap(C, i, A[i][1])
            T[A[i][1]] = True


def swap(A, i, j):
    A[i], A[j] = A[j], A[i]


def calc_required_bits(C: 'array of char-code pairs', F: 'array of frequencies of characters') -> int:
    # Calculate total bits required by the huffman encoding
    # (Notice that an array of codes (C array) must be ordered in
    # the same way as the input array of frequencies and corresponding
    # characters to encode)
    total = 0
    for i in range(len(F)):
        total += F[i] * len(C[i][1])
    return total


def print_codes(C: 'array of char-code pairs'):
    for char, code in C:
        print(f'{char} : {code}')


def huffman(S, F):
    n = len(S)
    # Create a coding tree
    ct = create_coding_tree(S, F)
    # Get Huffman codes of the characters
    C = create_huffman_codes(ct, n)
    # Restore the initial order of encoded characters
    reorder_codes(C, S)
    # Count total bits required to encode a string using a Huffman encoding
    bits_count = calc_required_bits(C, F)
    # Print all the codes and a total number of bits required
    print_codes(C)
    print(f'dlugosc napisu: {bits_count}')
    # Return the results
    return C, bits_count


if __name__ == '__main__':
    S = ["a", "b", "c", "d", "e", "f"]
    # F = [10, 10, 7, 13, 1, 20]
    F = [10, 11, 7, 13, 1, 20]

    huffman(S, F)
