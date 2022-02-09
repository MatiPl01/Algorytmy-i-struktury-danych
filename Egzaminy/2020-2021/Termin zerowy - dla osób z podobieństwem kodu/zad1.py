from zad1testy import runtests
from collections import deque


def tanagram(x, y, t):
    if len(x) != len(y): return False
    ord_a = ord('a')
    indices = [deque() for _ in range(26)]

    for i, char in enumerate(x):
        indices[ord(char) - ord_a].append(i)

    for i, char in enumerate(y):
        # If words aren't anagrams
        if not indices[ord(char) - ord_a]:
            return False
        closest_i = indices[ord(char) - ord_a].popleft()
        # If words aren't t-anagrams
        if abs(closest_i - i) > t:
            return False

    return True


runtests(tanagram)
