import copy

T1 = [0.1, 0.5, 0.2, 0.78, 0.01 ]
T2 = [0.9, 0.7, 0.7, 0.5, 0.3, 0.2, 0.9]
T3 = [0.1, 0.9,0.2,0.8,0.3,0.7,0.4,0.6]

D1 = [2**x for x in T1]
D2 = [2**x for x in T2]
D3 = [3**x for x in T3]

TESTS = [(D1,2), (D2,2), (D3,3)]



def T2S( T ):
    return " ".join([ "%.3f" % x for x in T ] )


def runtests( f ):
    OK = True
    for (T,a) in TESTS:
        BAD = False
        T1 = copy.deepcopy( T )
        T2 = copy.deepcopy( T )
        T.sort()
        print( "tablica            :", T2S(T2) )
        print( "posortowana tablica:", T2S(T) )
        res = f(T1,a)
        print( "wynik programu     :", T2S(res) )

        if len(res) != len(T):
            OK = False
            print("Tablice sa roznych dlugosci")
            continue

        for i in range(len(T)):
            if abs(T[i] - res[i]) > 0.001:
                   BAD = True
                   break
        if BAD:
            OK = False
            print("Blad!")

        print("----------------------")

    if OK:
        print( "OK!" )
    else:
        print( "Bledy!" )
