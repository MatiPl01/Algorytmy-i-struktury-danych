# zad1testy -- testy dla zadania 1 z egzaminu ASD (3. VII 2020)


G1 = [ [0,5,1,8,0,0,0 ],
       [5,0,0,1,0,8,0 ],
       [1,0,0,8,0,0,8 ],
       [8,1,8,0,5,0,1 ],
       [0,0,0,5,0,1,0 ],
       [0,8,0,0,1,0,5 ],
       [0,0,8,1,0,5,0 ] ]

TESTS = [(G1, 5, 2, 13),
         (G1, 0, 2, 1) ]
         

def runtests( f ):
    OK = True
    for (G,a,b,R) in TESTS:
        res = f(G,a,b)
        print("----------------------")
        print( "G =", G )
        print( "a = ", a, "b = ", b)
        print( "oczekiwany wynik =", R )
        print( "otrzymany wynik  =", res )
        
        if res != R:
            print( "Blad!" )
            OK = False
        else:
            print()
    print("----------------------")

    if OK:
        print( "OK!" )
    else:
        print( "Bledy!" )
            
