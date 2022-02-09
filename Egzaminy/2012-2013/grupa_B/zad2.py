"""
[10 pkt.] Zadanie 2. Proszę zaimplementować algorytm, który mając na wejściu dwa drzewa BST
(przechowujące liczby typu int; proszę zadeklarować odpowiednie struktury danych) zwraca nowe
drzewo BST zawierające wyłącznie te liczby, które występują w dokładnie jednym z drzew (ale nie w
obu). Algorytm powinien być jak najszybszy i wykorzystywać jak najmniej pamięci. Jaka jest złożoność
czasowa zaproponowanego algorytmu? Co można powiedzieć o zrównoważeniu drzew tworzonych
przez zaproponowany algorytm?
"""

from random import randint


class BSTNode:
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None


class BST:
    def __init__(self):
        self.root = None

    @property
    def min(self):
        return self.min_child(self.root)

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
        # Return True if an object was successfully inserted to BST
        return True

    @staticmethod
    def min_child(node):
        while node.left:
            node = node.left
        # Return a node of the minimum key
        return node

    def successor(self, node):
        if node.right:
            return self.min_child(node.right)
        while node.parent:
            if node.parent.left == node:
                return node.parent
            node = node.parent
        return None


def disjoint_values_BST(T1, T2):
    curr1 = T1.min
    curr2 = T2.min
    res = BST()

    while curr1 and curr2:
        if curr1.key < curr2.key:
            res.insert(curr1.key)
            curr1 = T1.successor(curr1)
        elif curr2.key < curr1.key:
            res.insert(curr2.key)
            curr2 = T2.successor(curr2)
        else:
            curr1 = T1.successor(curr1)
            curr2 = T2.successor(curr2)

    # Add remaining values which are only in one tree
    while curr1:
        res.insert(curr1.key)
        curr1 = T1.successor(curr1)
    while curr2:
        res.insert(curr2.key)
        curr2 = T1.successor(curr2)

    return res


def test(fn):
    V1 = [randint(-100, 100) for _ in range(100)]
    V2 = [randint(-100, 100) for _ in range(100)]
    disjoint = set(V1).symmetric_difference(V2)

    def create_BST(values):
        bst = BST()
        for v in values:
            bst.insert(v)
        return bst

    bst1 = create_BST(V1)
    bst2 = create_BST(V2)
    res_bst = fn(bst1, bst2)
    res_values = []

    def dfs(node):
        if not node:
            return
        res_values.append(node.key)
        dfs(node.left)
        dfs(node.right)

    dfs(res_bst.root)
    print(V1)
    print(V2)
    print(disjoint)
    print(res_values)
    print(disjoint.symmetric_difference(res_values))
    return not disjoint.symmetric_difference(res_values)


if __name__ == '__main__':
    print('Ok?', test(disjoint_values_BST))
