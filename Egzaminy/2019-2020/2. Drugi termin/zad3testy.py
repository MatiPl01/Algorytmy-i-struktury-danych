# zad3testy -- testy dla zadania 2 z kolokwium poprawkowego ASD (3. VII 2020)


TESTS = [

([ [0,2,1,1], [1,0,1,1], [2,2,0,1], [2,2,2,0] ],[1,0,2,3]),
([ [0,0,2,1,1], [1,0,0,0,0], [1,1,0,0,0], [0,0,0,0,1], [2,0,0,0,0] ],[2,1,0,3,4]),
([ [0,0,0,2], [0,0,1,2], [0,2,0,0], [1,1,0,0] ],[3,1,2,0])

]


def runtests( f ):

    OK = True
    for (A,R) in TESTS:
        y = f(A)

        try:
            print("----------------------")
            print( "A =", A )
            print( "otrzymany wynik  =", y )

            n = len( A )
            for j in range(n):
                for i in range(j):
                    if A[y[i]][y[j]] == 2:
                        print("Blad: Zadanie %d poprzedza zadanie %d" % (y[i],y[j]))
                        OK = False
                    
            print("----------------------")

        except TypeError:
            print( "Bledny typ zwracanego wyniku" )
            OK = False

    if OK:
        print( "OK!" )
    else:
        print( "Bledy!" )
            
 

