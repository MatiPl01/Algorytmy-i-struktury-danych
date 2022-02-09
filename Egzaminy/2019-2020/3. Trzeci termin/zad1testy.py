# zad1testy -- testy dla zadania 1 z egzaminu ASD (15. IX 2020)


L1 = [ [ 2 ], [ 2 ], [ 0, 1, 3], [ 2, 4 ],
       [ 3, 5, 6 ], [ 4 ], [ 4 ] ]
R1 = 3

L2 = [ [ 2, 4 ], [ 3 ], [ 0 ], [ 1, 4 ], [ 0, 3 ] ]
R2 = 4

L3 = [ [ 2, 3 ], [ 3, 4, 5, 6 ], [ 0 ],
       [ 0, 1 ], [ 1 ], [ 1 ], [ 1 ] ]
R3 = 3

L4 = [ [ 2 ], [ 2 ], [ 0, 1, 3, 4, 5, 6 ],
       [ 2 ], [ 2 ], [ 2 ], [ 2 ] ]
R4 = 2

TESTS = [ (L1,R1), (L2,R2), (L3,R3), (L4,R4) ]
         

def runtests( f ):
    OK = True
    for (A,R) in TESTS:
        res = f(A)
        print("----------------------")
        print( "A =", A )
        print( "oczekiwany wynik =", R )
        print( "otrzymany wynik  =", res )
        
        if res != R:
            print( "Blad!" )
            OK = False
    print("----------------------")

    if OK:
        print( "OK!" )
    else:
        print( "Bledy!" )
            
