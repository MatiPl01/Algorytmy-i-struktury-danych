class Node:
    def __init__(self, key, span):
        self.key = key
        self.span = span
        self.parent = None
        self.height = 0
        self.is_leaf = False
        self.left = self.right = None


class BricksTree:
    def __init__(self, spans, insert_spans=False):
        self.root = self.build_tree(self.get_coordinates(spans))
        if insert_spans:
            for span in spans:
                self.insert(span)

    def insert(self, brick):
        nodes, max_h = self._get_data(brick[0], brick[1])
        max_h += brick[2]

        for node in nodes:
            node.is_leaf = True
            while node.height < max_h:
                if node.left and node.left.height < max_h:
                    node.left.height = node.height
                elif node.right and node.right.height < max_h:
                    node.right.height = node.height
                node.height = max_h
                node = node.parent
                if not node: break
                node.is_leaf = False

    @staticmethod
    def build_tree(values):
        inf = float('inf')

        def recur(i, j, l=-inf, r=inf, parent=None):
            # Create a leaf node
            if i > j:
                node = Node(None, (l, parent.key) if l != parent.key else (parent.key, r))
                node.parent = parent
                return node

            mid = (i + j) // 2
            root = Node(values[mid], (l, r))
            root.parent = parent
            root.left = recur(i, mid - 1, l, values[mid], root)
            root.right = recur(mid + 1, j, values[mid], r, root)

            return root

        return recur(0, len(values) - 1)

    @staticmethod
    def get_coordinates(spans):
        # Create an array of sorted begin-end spans coordinates
        A = [c for span in spans for c in span]
        A.sort()
        # Filter out repeated values
        B = [A[0]]
        for i in range(1, len(A)):
            if A[i] != A[i - 1]:
                B.append(A[i])
        return B

    def _get_data(self, l, r):
        nodes_list = []
        max_h = 0

        def recur(node):
            nonlocal max_h
            if node.is_leaf: max_h = max(max_h, node.height)
            # If a node represents a span which is contained in the inserted
            # span, we will add this span to a node's intervals list
            if l <= node.span[0] and node.span[1] <= r:
                max_h = max(max_h, node.height)
                nodes_list.append(node)
            # If the current node's key value splits inserted span, we have
            # to go left and right in a tree
            elif l < node.key < r:
                recur(node.left)
                recur(node.right)
            # If the current node's key is on the right side of the inserted
            # span, we have to go left
            elif r <= node.key:
                recur(node.left)
            # If the current node's key is on the left side, we have to go
            # right
            elif node.key <= l:
                recur(node.right)

        recur(self.root)
        return nodes_list, max_h


def block_height(K: 'array of bricks coordinates'):
    it = BricksTree(K)
    # print('\n\n')
    # print(binary_tree_string(it.root, fn=lambda node: ', '.join(map(str, node.span))))
    for brick in K:
        # print('Inserting:', brick)
        it.insert(brick)
        # print()
        # print('Keys:')
        # print(binary_tree_string(it.root, fn=lambda node: node.key))
        # print('Heights:')
        # print(binary_tree_string(it.root, fn=lambda node: node.height))

    return it.root.height


def binary_tree_string(tree_root, *, fn=lambda node: node.val):
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


K1 = [(1, 3, 1), (2, 5, 2), (0, 3, 2), (8, 9, 3), (4, 6, 1)]
R1 = 5

K2 = [(1, 3, 1), (2, 4, 1), (3, 5, 1), (4, 6, 1), (5, 7, 1), (6, 8, 1)]
R2 = 6

K3 = [(1, 10 ** 10, 1)]
R3 = 1

TESTY = [(K1, R1), (K2, R2), (K3, R3)]

good = True
for KK, RR in TESTY:
    print("Klocki           : ", KK)
    print("Oczekiwany wynik : ", RR)
    WW = block_height(KK)
    print("Otrzymany wynik  : ", WW)
    if WW != RR:
        print("Błąd!!!!")
        good = False

if good:
    print("OK!")
else:
    print("Problemy!")
