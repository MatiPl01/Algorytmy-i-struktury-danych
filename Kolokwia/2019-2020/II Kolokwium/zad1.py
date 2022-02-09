class Node:
    def __init__(self):
        self.children = 0
        self.child = []


def heavy_path(T):
    global_max = 0

    def recur(node):
        # Loop over all node's children and find two (if there are)
        # longest paths
        max_paths = [0, 0]
        for child, weight in node.child:
            length = recur(child) + weight
            update_paths(max_paths, length)
        # Get the max-length path length which ends in the current node
        curr_max = max(max_paths)
        # Update globally longest path
        nonlocal global_max
        global_max = max(global_max, curr_max, sum(max_paths))

        return curr_max

    recur(T)
    return global_max


def update_paths(paths, length):
    if paths[0] < paths[1] and length > paths[0]:
        paths[0] = length
    elif length > paths[1]:
        paths[1] = length


if __name__ == '__main__':
    A = Node()
    B = Node()
    C = Node()
    A.children = 2
    A.child = [(B, 5), (C, -1)]
    print(heavy_path(A))
