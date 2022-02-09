# zad3testy -- testy dla zadania 3 z kolokwium poprawkowego ASD (3. VII 2020)
import copy

A  = [1,2,3,1,2,3,1,2,3]
Ak = 3
Ar = 2

B  = [1, 5, 10000, 100, 100000000, 10000, 100, 100000000, 100, 10000, 5, 1] 
Bk = 5
Br = 10

C  = [0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0]
Ck = 2
Cr = 5

TESTS = [(A, Ak, Ar),
         (B, Bk, Br),
         (C, Ck, Cr) ]


def runtests( f ):
    OK = True
    for (X,Xk,Xr) in TESTS:
        res = f( copy.deepcopy(X), Xk )
        print("----------------------")
        print( "A =", X )
        print( "k =", Xk )
        print( "oczekiwany wynik =", Xr )
        print( "otrzymany wynik  =", res )
        
        if res != Xr:
            print( "Blad!" )
            OK = False
        else:
            print()
    print("----------------------")

    if OK:
        print( "OK!" )
    else:
        print( "Bledy!" )
            
    
