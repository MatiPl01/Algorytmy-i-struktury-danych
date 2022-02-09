# zad2testy -- testy dla zadania 2 z kolokwium poprawkowego ASD (3. VII 2020)

L  = [59,53,47,43,41,37,31,29,23,19,17,13,11,7,5,3,2]


TESTS = [([], 2),
         ([0], 3),
         ([0,0], 5),
         ([1,0], 7),
         ([1,1], 11),
         ([3,1], 31),
         ([3,1,2,1], 59),
         ([4], 59)]


def runtests_internal( f ):

    q = None
    for a in L:
      q = f(q,a)


    OK = True
    for (LS,Xr) in TESTS:
        p = q
        for sk in LS: 
          p = p.next[sk]
  

        print("----------------------")
        print( "LS =", LS )
        print( "oczekiwany wynik =", Xr )
        print( "otrzymany wynik  =", p.a )
        
        if p.a != Xr:
            print( "Blad!" )
            OK = False
        else:
            print()
    print("----------------------")

    if OK:
        print( "OK!" )
    else:
        print( "Bledy!" )
            
 

def runtests( f ):
    try:
        runtests_internal( f )
    except:
        print("Bledy!")
        
