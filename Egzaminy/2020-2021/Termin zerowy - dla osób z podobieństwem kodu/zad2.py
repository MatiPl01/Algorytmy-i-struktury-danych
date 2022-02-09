from zad2testy import runtests


class Node:
    def __init__(self):
        self.left = None  # lewe podrzewo
        self.leftval = 0  # wartość krawędzi do lewego poddrzewa jeśli istnieje
        self.right = None  # prawe poddrzewo
        self.rightval = 0  # wartość krawędzi do prawego poddrzewa jeśli istnieje
        self.X = None  # miejsce na dodatkowe dane


class Cache:
    def __init__(self, size):
        self.f = [None] * (size + 1)
        self.g = None


def valuableTree(T, k):
    inf = float('inf')

    if k == 0: return 0
    if k < 0 or not T: return None

    def f(root, t):
        # Return 0 if we look for 0 edges (we have already found t-edges subtree)
        if not t: return 0
        # Return -inf if we still look for some edges but there are no more nodes
        # in a subtree (we haven't managed to find k-edge subtree)
        if not root: return -inf
        # Add cache object if there is no cache in the current subtree root
        if not root.X: root.X = Cache(k)
        # Check if we have already calculated the best k-edge subtree sum rooted
        # in the current node. If not, calculate the desired value.
        if root.X.f[t] is None:
            best = -inf
            # If there is a left branch (and might be a right branch)
            if root.left:
                best = max(best, root.leftval + f(root.left, t - 1))
            # If there is a right branch (and might be a left branch)
            if root.right:
                best = max(best, root.rightval + f(root.right, t - 1))
            # If there are both branches and we still have to take at least 2 edges
            # (this if statement handles cases in which we take both right and left
            # branches)
            if root.left and root.right and t >= 2:
                # i is a number of edges which we will look for in the left subtree.
                # (in the right subtree we have to look for t - 2 - i edges then)
                for i in range(t - 2 + 1):
                    curr = root.leftval + root.rightval + f(root.left, i) + f(root.right, t - 2 - i)
                    if curr > best:
                        best = curr
            root.X.f[t] = best
        # Return the max sum t-edges subtree sum
        return root.X.f[t]

    def g(root):
        # Return -inf if there is no root, that means there are no more edges
        # in the current subtree but we still have to find some edges. -inf is
        # a value that indicates that we haven't found enough edges in a subtree.
        if not root: return -inf
        # Add cache object if there is no cache in the current subtree root
        if not root.X: root.X = Cache(k)
        # Check if we have already calculated desired value. If not, we have to
        # recursively calculate the best subtree k-edges sum
        if root.X.g is None:
            # We can either include an edge (or both edges) connected to the current
            # root node (f function) or we can look for the best k-edges solution
            # in it'
            root.X.g = max(f(root, k), g(root.left), g(root.right))
        # Return the greatest sum obtained in a subtree
        return root.X.g

    return g(T)


runtests(valuableTree)
