""" O(n * log(n)) """
from zad3testy import runtests
from queue import PriorityQueue


class Node:
    def __init__(self, val):
        self.next = None
        self.val = val


def add_sentinels(L):
    n = len(L)
    for i in range(n):
        sentinel = Node(None)
        sentinel.next = L[i]
        L[i] = sentinel


def get_length(head):
    length = 0
    curr = head.next
    while curr:
        length += 1
        curr = curr.next
    return length


def _merge(head1, head2):
    curr1 = head1.next
    curr2 = head2.next
    head = tail = Node(None)

    while curr1 and curr2:
        if curr1.val < curr2.val:
            tail.next = curr1
            curr1 = curr1.next
        else:
            tail.next = curr2
            curr2 = curr2.next
        tail = tail.next

    if curr1: tail.next = curr1
    else:     tail.next = curr2

    return head

    
def merge_lists(L):
    n = len(L)
    if not L: return None
    if n == 1: return L[0]
    # For each list add a sentinel node
    add_sentinels(L)
    # Get length of each list and add this list with its length
    # as a priority to the minimum priority queue
    pq = PriorityQueue()
    # Second value is a placeholder to allow Python's comparisons
    # when a priority is the same
    i = 0
    while i < n:
        pq.put((get_length(L[i]), i, L[i]))
        i += 1
    # In a loop, merge lists of the lowest length together and add
    # a resulting list back to the priority queue
    while True:
        length1, _, head1 = pq.get()
        length2, _, head2 = pq.get()
        new_head = _merge(head1, head2)
        new_length = length1 + length2
        if not pq.empty():
            pq.put((new_length, i, new_head))
            i += 1
        else:
            return new_head.next


runtests(merge_lists)
