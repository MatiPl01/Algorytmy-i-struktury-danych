# zad2testy -- testy dla zadania 2 z kolokwium poprawkowego ASD (3. VII 2020)


TESTS = [

([(10,10),(15,25),(20,20),(30,40)],7),
([(23,56),(12,120),(45,98),(73,37),(1,101)],14),
([(23,56),(12,120)],0),
([(100,100),(100,200),(200,100),(200,200)],0),
([(100,100),(100,200),(210,100),(210,200)],10),
([(100,100),(100,200),(200,100),(200,200),(150,151)],1),
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
            
 

