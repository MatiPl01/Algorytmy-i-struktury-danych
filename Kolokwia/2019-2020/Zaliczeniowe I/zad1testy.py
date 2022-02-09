# zad1testy -- testy dla zadania 1 z kolokwium poprawkowego ASD (3. VII 2020)
import copy


G1  = [[-1,5,-1,2],[-1,-1,-1,-1],[5,-1,-1,5],[2,2,-1,-1]]
P1 = [2,0]
L1 = 9
# a=2, b=1, d=6

G2  = [[-1,2,-1,-1,3],[2,-1,2,-1,-1],[-1,2,-1,2,-1],[-1,-1,2,-1,3],[3,-1,-1,3,-1]]
P2 = [0,2]
L2 = 6
# a=0, b=3, d=4

G3  = [[-1,3,-1,5,-1,2],[3,-1,4,-1,-1,-1],[-1,4,-1,6,-1,-1],[-1,-1,6,-1,2,-1],[-1,5,-1,2,-1,3],[2,-1,-1,-1,3,-1]]
P3 = [0,4,5]
L3 = -1
# a=5, b=2, d=5


TESTS = [(G1, P1, 6, 2, 1, L1),
         (G2, P2, 4, 0, 3, L2),
         (G3, P3, 5, 5, 2, L3) ]


def isok( G, P, d, a, b, path, exp_len ):
    if exp_len < 0 and path == None:
        print("Brak sciezki, zgodnie z oczekiwaniem")
        return True
    if exp_len >= 0 and path == None:
        print("Rozwiazanie nie zwrocilo sciezki, mimo ze taka istnieje")
        return False
    
    if path[0] != a:
        print("Rozwiazanie zwraca bledny poczatek sciezki")

    tank = d
    sol_len = 0
    v = a
    for u in path[1:]:
        if G[v][u] < 0:
            print("Nie istnieje krawedz z %d to %d" % (v,u))
            return False
        tank -= G[v][u]
        sol_len += G[v][u]
        if tank < 0:
            print("Zabraklo benzyny na krawedzi z %d do %d" % (v,u))
            return False
        v = u
        if v in P:
            tank = d

    print("Dlugosc otrzymanej trasy =", sol_len )
    if sol_len > exp_len:
        print( "Za dluga trasa!" )
        return False
            
    return True
    
    


def runtests( f ):
    OK = True
    for (G,P,d,a,b,L) in TESTS:
        res = f(copy.deepcopy(G),copy.deepcopy(P),d,a,b)
        print("----------------------")
        print( "G =" )
        for i in range(len(G)): print( G[i])
        print( "P =", P )
        print( "d = ", d)
        print( "a = ", a)
        print( "b = ", b)
        print( "otrzymany wynik  =", res )
        print( "oczekiwana dlugosc trasy =", L)
        

        if not isok( G, P, d, a, b, res, L ):
            print( "Blad!" )
            OK = False
        else:
            print()
    print("----------------------")

    if OK:
        print( "OK!" )
    else:
        print( "Bledy!" )
            
