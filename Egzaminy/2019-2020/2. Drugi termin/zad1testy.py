# zad1testy -- testy dla zadania 1 z egzaminu ASD (1. IX 2020)


A1 = [2,2,1,0,0,0]
R1 = 3

A2 = [4,5,2,4,1,2,1,0]
R2 = 2

A3 = [1,2,3,4,5,6,7,8,9,10]
R3 = 4

A4 = [4,2,2,2,1,2,1,1,0]
R4 = 3

A5 = [4,3,0,1,2,0,1,0]
R5 = 2


TESTS = [(A1,R1), (A2,R2), (A3,R3), (A4,R4), (A5,R5) ]
         

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
            
