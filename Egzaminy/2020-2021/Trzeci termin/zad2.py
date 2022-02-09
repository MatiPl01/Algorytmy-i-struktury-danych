"""
ZŁOŻONOŚĆ:
Obliczeniowa: O(D)
Pamięciowa:   O(D)
"""


from zad2testy import runtests


class Node:
    def __init__(self):
        self.is_prefix = False
        self.left = None
        self.right = None
        self.parent = None


class PrefixTree:
    def __init__(self):
        self.root = Node()

    def insert(self, string):
        curr = self.root

        for c in string:
            if c == '0':
                if curr.left:
                    curr.left.is_prefix = True
                else:
                    curr.left = Node()
                    curr.left.parent = curr
                curr = curr.left
            else:
                if curr.right:
                    curr.right.is_prefix = True
                else:
                    curr.right = Node()
                    curr.right.parent = curr
                curr = curr.right

    def get_prefixes(self):
        leaves = self.get_prefix_leaves()
        prefixes = []

        for node in leaves:
            prefixes.append(self.get_prefix(node))

        return prefixes

    def get_prefix_leaves(self):
        leaves = []

        def dfs(node):
            is_leaf = True
            if node.left and node.left.is_prefix:
                is_leaf = False
                dfs(node.left)
            if node.right and node.right.is_prefix:
                is_leaf = False
                dfs(node.right)
            if is_leaf:
                leaves.append(node)

        dfs(self.root)

        return leaves

    def get_prefix(self, node):
        chars = []

        while node.parent:
            if node.parent.left is node:
                chars.append('0')
            else:
                chars.append('1')
            node = node.parent

        chars.reverse()
        return ''.join(chars)


def double_prefix(L):
    pt = PrefixTree()
    for s in L:
        pt.insert(s)
    return pt.get_prefixes()


runtests(double_prefix)
