import copy

P1 = [123, 890, 688, 587, 257, 246]
L1 = 767

P2 = [587, 990, 257, 246, 668, 132]
L2 = -1

P3 = [100, 210, 620, 144, 445, 555]
L3 = 520

P4 = [111, 222]
L4 = -1

TESTS = [(P1, L1),
         (P2, L2),
         (P3, L3),
         (P4, L4)]

def isok(P, result, expected):
    return result == expected

def runtests(f):
    OK = True
    for (P, L) in TESTS:
        res = f(copy.deepcopy(P))
        print("----------------------")
        print("P =", P)
        print("otrzymany wynik  =", res)
        print("oczekiwany wynik =", L)

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
