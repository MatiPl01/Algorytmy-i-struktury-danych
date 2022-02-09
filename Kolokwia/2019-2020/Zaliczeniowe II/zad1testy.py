import copy

P1 = [(2, 2), (1, 1), (2.5, 0.5), (3, 2), (0.5, 3)]
L1 = [1, 2, 4]

P2 = [(2, 2), (1, 1), (2.5, 0.5), (3, 2), (0.5, 3), (0.5, 0.5)]
L2 = [5]

P3 = [(2, 2), (1, 1), (2.5, 0.2), (3, 2), (0.5, 3), (0.5, 0.5)]
L3 = [2, 5]

P4 = [(1, 1)]
L4 = [0]

P5 = [(0, 6), (1, 5), (2, 4), (3, 3), (4, 2), (5, 1), (6, 0)]
L5 = [0, 1, 2, 3, 4, 5, 6]

TESTS = [(P1, L1),
         (P2, L2),
         (P3, L3),
         (P4, L4),
         (P5, L5)]

def Diff(li1, li2): 
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2] 
    return li_dif 

def isok(P, result, expected):
    return len(Diff(result, expected)) == 0

def runtests(f):
    OK = True
    for (P, L) in TESTS:
        res = f(copy.deepcopy(P))
        print("----------------------")
        print("P =", P)
        print("otrzymany wynik  =", sorted(res))
        print("oczekiwany wynik =", sorted(L))

        if not isok(P, res, L):
            print("Blad!")
            OK = False
        else:
            print()
    print("----------------------")

    if OK:
        print("OK!")
    else:
        print("Bledy!")
