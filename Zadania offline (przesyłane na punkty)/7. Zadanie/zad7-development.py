"""
Autor: Mateusz Łopaciński


OPIS ALGORYTMU:

===== Klasa Node =====
Klasa służy do reprezentowania wierzchołków drzewa kodującego, jakie jest tworzone przez funkcję
create_coding_tree.

UWAGA:
Ponieważ dostarczona wraz z Pythonem kolejka, w przypadku, gdy dodawane są elementy o tym samym priorytecie,
porównuje wartości obiektów, aby móc skorzystać z kolejki priorytetowej, musimy dodać metodę specjalną __gt__
(lub __lt__) do klasy Node, aby umożliwić porównywanie instancji tej klasy. Ponieważ dla nas bez znaczenia
jest kolejność elementów o tym samym priorytecie (zawsze otrzymamy rozwiązanie optymalne), metoda __gt__ zwraca
wartość 0.
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
"""

from queue import PriorityQueue


def binary_tree_string(tree_root, *, fn: 'function to get a value of a node' = lambda node: str(node.val)):
    if not tree_root: return ''

    # Store data from a tree
    data = []
    lvl_nodes = [tree_root]
    just = 1

    while True:
        if not lvl_nodes: break

        curr_row = []
        branches = []
        next_nodes = []

        if not any(lvl_nodes):
            break

        for node in lvl_nodes:
            if not node:
                curr_row.append('')
                branches.extend([' ', ' '])
                next_nodes.extend([None, None])
            else:
                val = fn(node)
                just = max(len(val), just)
                curr_row.append(val)

                if node.left:
                    next_nodes.append(node.left)
                    branches.append('/')
                else:
                    next_nodes.append(None)
                    branches.append(' ')

                if node.right:
                    next_nodes.append(node.right)
                    branches.append('\\')
                else:
                    next_nodes.append(None)
                    branches.append(' ')

        data.append((curr_row, branches))
        lvl_nodes = next_nodes

    begin_sep = sep = 3 if just % 2 else 2
    data_iter = iter(data[::-1])
    result = [''] * (len(data) * 2 - 1)
    result[-1] = (' ' * sep).join(val.center(just) for val in next(data_iter)[0])

    # Format the tree string
    for i, (values, branches) in enumerate(data_iter):
        mul = 2 * i + 1
        # Values
        indent = (2 ** (i + 1) - 1) * (just + begin_sep) // 2
        sep = 2 * sep + just
        result[-(mul + 2)] = f"{' ' * indent}{(' ' * sep).join(val.center(just) for val in values)}"
        # Branches
        branch_indent = (3 * indent + just) // 4
        branches_row = []
        d_indent = indent - branch_indent
        branches_sep = ' ' * (2 * (d_indent - 1) + just)
        for i in range(0, len(branches), 2):
            branches_row.append(f"{branches[i]}{branches_sep}{branches[i + 1]}")
        result[-(mul + 1)] = f"{' ' * branch_indent}{(' ' * (sep - 2 * d_indent)).join(branches_row)}"

    return '\n'.join(result)


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
    # pq = PriorityQueue(n)
    pq = []

    # Add all char-frequency pairs to the queue as Node objects
    for i in range(n):
        node = Node()
        # Add a char property (only leaf nodes will have this property)
        node.char = S[i]
        # Insert a node with its priority (frequency of a character)
        # pq.put((F[i], node))
        pq.append((F[i], node))

    # Create a coding tree
    while True:
        # Take a pair of two entries of the lowest priority (frequency)
        pq.sort(key=lambda x: x[0], reverse=True)
        x_priority, x_node = pq.pop()
        pq.sort(key=lambda x: x[0], reverse=True)
        y_priority, y_node = pq.pop()
        # Create a new node and link two nodes from above to this node
        print('Min priorities: ', x_priority, y_priority)
        node = Node()
        node.left  = y_node
        node.right = x_node

        node.char = '(' + node.left.char + ' + ' + node.right.char + ')'
        print('Merged:', node.char)
        # print('\n\nCreated subtree:')
        # print('Root priority:', x_priority + y_priority)
        # print(binary_tree_string(node, fn=lambda node: node.char if hasattr(node, 'char') else '.'))
        # print('\nNew queue:', [f"{p}: {n.char}" for p, n in sorted(pq.queue, key=lambda x: x[0])])
        # first = pq.get()
        # print('First in queue:', f"{first[0]}: {first[1].char}")
        # pq.put(first)

        # Insert this node to the priority queue only if a priority queue
        # hasn't been exhausted yet
        if pq:
            pq.append((x_priority + y_priority, node))
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

    print('HERE')
    print(A)
    print(C)

    B = [False] * n

    # Reorder the array or char-code pairs so that all entries are stored
    # in the same order they were stored in the S array
    for i in range(n):
        if B[i]: continue
        print(f'Swapping: C[{i}] <-> C[{A[i][1]}]')
        swap(C, i, A[i][1])
        B[A[i][1]] = True
        print(C)
    print('\n\n\n')


def swap(A, i, j):
    A[i], A[j] = A[j], A[i]


def calc_required_bits(S, C: 'array of char-code pairs', F: 'array of frequencies of characters') -> int:
    # Calculate total bits required by the huffman encoding
    # (Notice that an array of codes (C array) must be ordered in
    # the same way as the input array of frequencies and corresponding
    # characters to encode)
    total = 0
    for i in range(len(F)):
        print(f'Adding: total ({total}) += F[{i}] * len(C[{i}][1]) ({F[i]} * {len(C[i][1])})    C[{i}] = {C[i]}, S[{i}] = {S[i]}, F[{i}] = {F[i]}')
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
    bits_count = calc_required_bits(S, C, F)
    # Print all the codes and a total number of bits required
    print_codes(C)
    print(f'Długość napisu: {bits_count}')
    # Return the results
    return C, bits_count, ct


if __name__ == '__main__':
    S = ["a", "b", "c", "d", "e", "f"]
    # F = [10, 10, 7, 13, 1, 20]
    F = [10, 11, 7, 13, 1, 20]

    S = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "o", "p", "r", "s", "t", "u", "w", "y", "z",
         "q"]
    F = [865, 395, 777, 912, 431, 42, 266, 989, 524, 498, 415, 941, 803, 850, 311, 992, 489, 367, 598, 914, 930, 224,
         517]

    print('Input')
    print(*(f"{char}: {freq}" for char, freq in sorted(zip(S, F))))
    C, bits, ct = huffman(S, F)
    print(binary_tree_string(ct, fn=lambda node: node.char if hasattr(node, 'char') else '.'))
    print(*(f"{char}: {freq}" for char, freq in sorted(zip(S, F), key=lambda x: x[1])), sep='\n')
