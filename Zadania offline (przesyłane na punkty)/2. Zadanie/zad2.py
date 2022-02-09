from random import randint, seed


class Node:
    def __init__(self):
        self.next = None
        self.value = None


def qsort(L):
    # Perform sorting only if there are at least 2 elements in a linked list
    if L and L.next:
        # Add a sentinel node to simplify a sorting process
        sentinel = Node()
        sentinel.next = L
        # Perform sorting on a linked list
        _quick_sort(sentinel, None)
        # Return the first node of a linked list
        return sentinel.next
    return L


# begin_idx will be included and end_idx excluded (as in Python's ranges)
def _quick_sort(begin_prev_node, end_node):
    # Loop till the current sublist has at least 2 elements
    # (calling a partition function for a single-element list is pointless and inefficient,
    # thus it's better to check two conditions in a while loop)
    while begin_prev_node.next is not end_node \
            and begin_prev_node.next.next is not end_node:
        first_end_node, second_begin_prev_node = _partition(begin_prev_node, end_node)
        _quick_sort(begin_prev_node, first_end_node)
        begin_prev_node = second_begin_prev_node


def _partition(begin_prev_node, end_node):
    # Store a pivot node and a current node pointers in variables
    # Take the first (leftmost) node as a pivot
    pivot_node = begin_prev_node.next
    curr_node = pivot_node.next

    # Prepare sentinel nodes for sublists which will be created
    lt_pivot_head = Node()
    eq_pivot_head = pivot_node
    gt_pivot_head = Node()

    # Prepare pointers to the sublists
    lt_pivot_curr = lt_pivot_head
    eq_pivot_curr = eq_pivot_head
    gt_pivot_curr = gt_pivot_head

    # Distribute subsequent nodes of a linked list part to appropriate sublists
    while curr_node is not end_node:
        if curr_node.value < pivot_node.value:
            lt_pivot_curr.next = curr_node
            lt_pivot_curr = lt_pivot_curr.next
        elif curr_node.value > pivot_node.value:
            gt_pivot_curr.next = curr_node
            gt_pivot_curr = gt_pivot_curr.next
        else:
            eq_pivot_curr.next = curr_node
            eq_pivot_curr = eq_pivot_curr.next
        curr_node = curr_node.next

    # Join created lists together
    # Link a list of elements lower than pivot (lt_pivot) if is not empty
    if lt_pivot_head.next:
        begin_prev_node.next = lt_pivot_head.next
        lt_pivot_curr.next = eq_pivot_head

        if gt_pivot_head.next:
            eq_pivot_curr.next = gt_pivot_head.next
            gt_pivot_curr.next = end_node
        else:
            eq_pivot_curr.next = end_node
    # Link a list of elements greater than pivot (gt_pivot) if is not empty
    elif gt_pivot_head.next:
        begin_prev_node.next = eq_pivot_head
        eq_pivot_curr.next = gt_pivot_head.next
        gt_pivot_curr.next = end_node
    # Otherwise, there will be only eq_pivot linked list (all elements are equal to a pivot)
    else:
        begin_prev_node.next = eq_pivot_head
        eq_pivot_curr.next = end_node

    return eq_pivot_head, eq_pivot_curr


def tab2list(A):
    H = Node()
    C = H
    for i in range(len(A)):
        X = Node()
        X.value = A[i]
        C.next = X
        C = X
    return H.next


def printlist(L):
    while L != None:
        print(L.value, "->", end=" ")
        L = L.next
    print("|")


seed(42)

n = 10
T = [randint(1, 10) for i in range(10)]
L = tab2list(T)

print("przed sortowaniem: L =", end=" ")
printlist(L)
L = qsort(L)
print("po sortowaniu    : L =", end=" ")
printlist(L)

if L == None:
    print("List jest pusta, a nie powinna!")
    exit(0)

P = L
while P.next != None:
    if P.value > P.next.value:
        print("Błąd sortowania")
        exit(0)
    P = P.next

print("OK")
