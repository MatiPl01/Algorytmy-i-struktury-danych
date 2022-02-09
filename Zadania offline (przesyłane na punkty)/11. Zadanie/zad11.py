"""
Autor: Mateusz Łopaciński


OPIS ALGORYTMU:

W pliku umieściłem dwie implementacje, z których pierwsza jest realizowana, przy pomocy
funkcji, które wykonują operacje 'insert()' oraz 'remove()', pobierając jako argumenty
korzeń drzewa i klucz węzła, który należy usunąć z drzewa. Natomiast druga implementacja
wykorzystuje programowanie obiektowe, przez co łatwiej można zrealizować operację usuwania
z drzewa węzła, jeżeli usuwany węzeł jest korzeniem drzewa. Implemenatcja obiektowa jest
również wygodniejsza w użyciu, bo nie wymaga przekazywania korzenia do jako argument funkcji.

===== Implementacja funkcyjna =====
1) 'insert()':
Operację insert realizuję w sposób przedstawiony na wykładzie. Zakładam również, że możliwe
jest aby drzewo nie miało korzenia (np. po usunięciu ostatniego węzła), co reprezentuję przez
przypisanie klucza 'None' do węzła, który reprezentuje korzeń drzewa. Wówczas, jeżeli wstawiamy
do takiego drzewa pierwszy węzeł, konieczne jest zmodyfikowanie wartości klucza korzenia. 
(Niestety Python nie pozwala na przepięcie wskaźnika zmiennej 'root' na nowy węzeł, który stał
się korzeniem drzewa, więc w sytuacji, w której funkcja ma zwracać wartości boolowskie, nie
możemy postąpić w żaden inny sposób, aby zmodyfikować korzeń drzewa).

2) 'remove()':
Podobnie jak w przypadku funkcji 'insert()', zakładam że klucz 'None' w węźle korzenia oznacza
puste drzewo binarne, więc od razu zwracany jest fałsz, bo nic nie da się usunąć z drzewa.
Jeżeli jednak drzewo jest niepuste, korzystam z funkcji 'find()' do znalezienia węzła o wskazanym
kluczu. Jeżeli taki węzeł nie istnieje, nie ma nic do usunięcia, więc zwracana jest wartość False,
natomiast gdy węzeł został znaleziony, wywołuję pomocniczą funkcję '_remove_node()', która
usuwa odpwiedni węzeł z drzewa binarnego oraz "naprawia" drzewo po jego usunięciu.

Usuwanie węzła z drzewa podzieliłem na 3 przypadki, z których pierwszym jest ten, w którym usuwany
węzeł nie posiada prawego dziecka (ale może, lecz nie musi mieć lewego dziecka). Jeżeli wówczas
węzeł ma rodzica (nie jest korzeniem drzewa), przepinam wskaźniki podobnie do list odsyłaczowych,
usuwając odpowiedni węzeł. Natomiast, gdy ten węzeł jest korzeniem drzewa, to jeżeli ma on lewe
dziecko, to przepisuję klucz tego dziecka do węzła korzenia oraz przepinam wskaźniki lewego
dziecka korzenia do węzła korzenia (tak operacja odpowiada zastąpieniu korzenia drzewa jego
lewym dzieckiem, ale w implementacji funkcyjnej usuwania węzłów z drzewa BST, niemożliwe jest
zastąpienie korzenia drzewa nowym obiektem bez zwracania przez funkcję nowego obiektu, a zwrócić
nowego obiektu nie możemy - co wynika z treści zadania). Jest jeszcze drugi przypadek, w którym
korzeń nie ma również lewego dziecka. Wtedy jest on ostatnim węzłem w drzewie, więc zastępujemy
jego klucz przez 'None'.

W analogiczny sposób postępuję, gdy usuwany węzeł nie ma lewego dziecka, ale ma prawe dziecko.
(Tym razem mamy jednak pewność, że usuwany węzeł ma prawe dziecko, bo inaczej wykonany byłby
fragment kodu opisany wyżej.

Pozostaje nam jeszcze jeden przypadek, gdy węzeł ma oboje dzieci. W takiej sutuacji zastępuję
usuwany węzeł przez jego następnika, którego znajduję przy pomocy funkcji 'successor()'.
Po jego znalezieniu, usuwam ten węzeł z drzewa, ponieważ następnik na co najwyżej jedno dziecko,
więc jego usunięcie można łatwo zrealizować, wykorzystując jeden z dwóch opisanych wyżej 
przypadków. Następnie, jeżeli usuwany węzęł jest korzeniem, musimy przepisać do niego klucz
usuniętego z drzewa następnika korzenia (w implementacji funkcyjnej jest to konieczne). Jeżeli
jednak nie jest to korzeń, a usuwany węzeł jest prawym dzieckiem swojego rodzica, to w miejsce
tego węzła wpinamy jako prawe dziecko rodzica jego następnika (analogicznie, gdy węzeł jest
lewym dzieckiem swojego rodzica). W kolejnym kroku musimy zmodyfikować wskaźniki nowowstawionego
węzła (następnika) w taki sposób, aby wskazywał on na tego samego rodzica, lewe dziecko i prawe
dziecko, co usunięty węzeł, a także wskaźniki na rodzica dzieci usuwanego węzła.


===== Implementacja obiektowa =====
Obie metody są zaimplementowane w analogiczny sposób do tych, które zostały opisane wyżej. Nie
jest jednak konieczne przepinanie klucza w żadnym miejscu, ponieważ z łatwością możemy zastąpić
zapisany jako atrybut instancji klasy BST korzeń drzewa, po usunięciu korzenia i zastąpieniu
go nowym węzłem.


Złożoność obliczeniowa:
O(h) - dla obu operacji, gdzie 'h' - wysokość drzewa. Jeżeli drzewo jest zbalansowane, to złożoność
optymistyczna wynosi O(log(n)), gdzie 'n' - liczba węzłów w drzewie, natomiast gdy drzewo jest
bardzo niezbalansowane (przypomina listę odsyłaczową), to mamy pesymistyczną złożoność, czyli O(n).
"""

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


""" 
Implementacja funkcyjna
"""
def min_child(node):
    while node.left:
        node = node.left
    # Return a node of the minimum key
    return node


def find(root, key):
    curr = root
    while curr:
        # Enter the left subtree
        if key < curr.key:
            curr = curr.left
        # Enter the right subtree
        elif key > curr.key:
            curr = curr.right
        # Return a node which was found
        else:
            return curr
    # If no node of the specified key was found, return None
    return None


def successor(node):
    if node.right:
        return min_child(node.right)
    while node.parent:
        if node.parent.left == node:
            return node.parent
        node = node.parent
    return None


def insert(root, key):
    node = BSTNode(key)
    curr = root
    if root.key is None:
        root.key = key
    else:
        while True:
            # Enter the right subtree if a key of a value inserted is
            # greater than the key of the current BST node
            if node.key > curr.key:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = node
                    node.parent = curr
                    break
            # Enter the left subtree if a key of a value inserted is
            # lower than the key of the current BST node
            elif node.key < curr.key:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = node
                    node.parent = curr
                    break
            # Return False if a node with the same key already exists
            # (We won't change its value)
            else:
                return False
        # Return True if a node was successfully inserted to BST
    return True


def remove(root, key):
    if root.key is None: return False
    # Find a node which will be removed
    node = find(root, key)
    # Return None if no node with the specified key was found
    if not node: return False
    # Remove a node and fix a BST
    _remove_node(root, node)
    return True


def _remove_node(root, node):
    # If the current node has no right child
    # (and might not have a left child)
    if not node.right:
        # If the current node is not a root node
        if node.parent:
            if node is node.parent.right:
                node.parent.right = node.left
            else:
                node.parent.left = node.left
            if node.left:
                node.left.parent = node.parent
        # If the current node is a root node
        else:
            if root.left:
                new_root = root.left
                root.key = new_root.key
                root.left = new_root.left
                root.right = new_root.right
                if root.left:  root.left.parent = root
                if root.right: root.right.parent = root
            else:
                root.key = None

    # If the current node has no left child
    # (and might not have a right child)
    elif not node.left:
        # If the current node is not a root node
        if node.parent:
            if node is node.parent.right:
                node.parent.right = node.right
            else:
                node.parent.left = node.right
            node.right.parent = node.parent
        # If the current node is a root node
        else:
            new_root = root.right
            root.key = new_root.key
            root.left = new_root.left
            root.right = new_root.right
            if root.left: root.left.parent = root
            if root.right: root.right.parent = root

    # If the current node has both children
    else:
        new_node = successor(node)
        _remove_node(root, new_node)

        if node is root:
            root.key = new_node.key
            return
        elif node.parent.right is node:
            node.parent.right = new_node
        else:
            node.parent.left = new_node

        new_node.left = node.left
        new_node.right = node.right
        new_node.parent = node.parent
        if node.right: node.right.parent = new_node
        if node.left:  node.left.parent = new_node


""" 
Implementacja obiektowa
"""
class BST:
    def __init__(self):
        self.root = None

    def __bool__(self):
        return bool(self.root)

    @staticmethod
    def min_child(node):
        while node.left:
            node = node.left
        # Return a node of the minimum key
        return node

    @staticmethod
    def max_child(node):
        while node.right:
            node = node.right
        # Return a node of the maximum key
        return node

    def insert(self, key):
        node = BSTNode(key)
        if not self.root:
            self.root = node
        else:
            curr = self.root
            while True:
                # Enter the right subtree if a key of a value inserted is
                # greater than the key of the current BST node
                if node.key > curr.key:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = node
                        node.parent = curr
                        break
                # Enter the left subtree if a key of a value inserted is
                # lower than the key of the current BST node
                elif node.key < curr.key:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = node
                        node.parent = curr
                        break
                # Return False if a node with the same key already exists
                # (We won't change its value)
                else:
                    return False
        # Return True if a node was successfully inserted to BST
        return True

    def find(self, key):
        curr = self.root
        while curr:
            # Enter the left subtree
            if key < curr.key:
                curr = curr.left
            # Enter the right subtree
            elif key > curr.key:
                curr = curr.right
            # Return a node which was found
            else:
                return curr
        # If no node of the specified key was found, return None
        return None

    def successor(self, node):
        if node.right:
            return self.min_child(node.right)
        while node.parent:
            if node.parent.left == node:
                return node.parent
            node = node.parent
        return None

    def predecessor(self, node):
        if node.left:
            return self.max_child(node.left)
        while node.parent:
            if node.parent.right == node:
                return node.parent
            node = node.parent
        return None

    def remove(self, key):
        # Find a node which will be removed
        node = self.find(key)
        # Return None if no node with the specified key was found
        if not node: return False
        # Remove a node and fix a BST
        self._remove_node(node)
        return True

    def _remove_node(self, node):
        # If the current node has no right child
        # (and might not have a left child)
        if not node.right:
            # If the current node is not a root node
            if node.parent:
                if node is node.parent.right:
                    node.parent.right = node.left
                else:
                    node.parent.left = node.left
                if node.left:
                    node.left.parent = node.parent
            # If the current node is a root node
            else:
                self.root = node.left
                if self.root: self.root.parent = None

        # If the current node has no left child
        # (and might not have a right child)
        elif not node.left:
            # If the current node is not a root node
            if node.parent:
                if node is node.parent.right:
                    node.parent.right = node.right
                else:
                    node.parent.left = node.right
                if node.right:
                    node.right.parent = node.parent
            # If the current node is a root node
            else:
                self.root = node.right
                if self.root: self.root.parent = None

        # If the current node has both children
        else:
            new_node = self.successor(node)
            self._remove_node(new_node)

            if node is self.root:
                self.root = new_node
            elif node.parent.right is node:
                node.parent.right = new_node
            else:
                node.parent.left = new_node

            new_node.left = node.left
            new_node.right = node.right
            new_node.parent = node.parent
            if node.right: node.right.parent = new_node
            if node.left:  node.left.parent = new_node

        node.parent = node.left = node.right = None


""" 
Pomocnicza funkcja, która wypisuje drzewo binarne w postaci ładnie sformatowanego
tekstu. Działa dobrze jedynie dla małych drzew, ponieważ później drzewa robią się
zbyt szerokie.
"""
def binary_tree_string(tree_root, *, fn=lambda node: node.key):
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
                val = str(fn(node))
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


if __name__ == '__main__':
    import random

    t = BSTNode(None)

    for _ in range(2):
        print('===== Inserting values =====')

        inserted = []

        for _ in range(12):
            n = random.randint(0, 20)
            inserted.append(n)
            print('New value:', n)
            print('Inserted?', insert(t, n))
            print('Tree:')
            print(binary_tree_string(t))
            print('\n')

        print('===== Removing values =====')

        random.shuffle(inserted)
        i = 0

        while t.key is not None:
            if random.random() < .2:
                n = random.randint(0, 20)
            else:
                n = inserted[i]
                i += 1
            print('New value:', n)
            print('Removed?', remove(t, n))
            print('Tree:')
            print(binary_tree_string(t))
            print('\n')


    # t = BST()
    #
    # for _ in range(2):
    #     print('===== Inserting values =====')
    #
    #     inserted = []
    #
    #     for _ in range(12):
    #         n = random.randint(0, 20)
    #         inserted.append(n)
    #         print('New value:', n)
    #         print('Inserted?', t.insert(n))
    #         print('Tree:')
    #         print(binary_tree_string(t.root))
    #         print('\n')
    #
    #     print('===== Removing values =====')
    #
    #     random.shuffle(inserted)
    #     i = 0
    #
    #     while t:
    #         if random.random() < .2:
    #             n = random.randint(0, 20)
    #         else:
    #             n = inserted[i]
    #             i += 1
    #         print('New value:', n)
    #         print('Removed?', t.remove(n))
    #         print('Tree:')
    #         print(binary_tree_string(t.root))
    #         print('\n')
