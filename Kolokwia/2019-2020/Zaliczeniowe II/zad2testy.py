# zad2testy -- testy dla zadania 2 z kolokwium poprawkowego ASD (1. IX 2020)

L1 = ["k","k","o","o","t","t"]
E1 = [(0,2,2), (1,2,1), (1,4,3), (1,3,2), (2,4,5), (3,4,1), (3,5,3) ]

L2 = ["m","a","g","a","g","m","i","i","a"]
E2 = [(0,2,3),(0,1,1),(1,2,2),(1,4,5),(2,3,1),(3,4,4),(3,5,2),(4,6,1),(4,8,100),(4,7,3),(5,7,7),(5,8,1),(7,8,6) ]



TESTS = [(L1,E1,"kto"    , 4),
         (L1,E1,"kot"    , 3),
         (L1,E1,"kokotok", 8),
         (L2,E2,"magia"  , 15)]




def runtests( f ):

    OK = True
    for (L,E,W,R) in TESTS:
        G = (L,E)
        res = f(G,W)
  

        print("----------------------")
        print( "G = (L, E)" )
        print( "L =", L )
        print( "E =", E )
        print( "W =", W )
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
            
 

