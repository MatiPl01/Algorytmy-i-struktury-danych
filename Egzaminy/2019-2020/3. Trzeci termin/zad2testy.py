# zad2testy -- testy dla zadania 2 z egzaminu poprawkowego ASD (15.09.2020)


TESTS = [

([(1,4),(0,6),(1,5),(2,4),(2,4),(2,3)],5),
([(1,4),(0,6),(1,5),(2,4),(2,4),(2,3),(0,2),(0,2),(0,2),(0,2),(0,2)],6),
([(1,6),(2,7),(3,4),(2,7),(2,7)],3),
([(1,4),(0,5),(1,5),(2,6),(2,4)],3),

]


def runtests( f ):

    OK = True
    for (dane,res) in TESTS:
        y = f(dane)

        print("----------------------")
        print( "A =", dane )
        print( "oczekiwany wynik =", res )
        print( "otrzymany wynik  =", y )
        
        if res != y:
            print( "Blad!" )
            OK = False
        else:
            print()
    print("----------------------")

    if OK:
        print( "OK!" )
    else:
        print( "Bledy!" )
            
 

