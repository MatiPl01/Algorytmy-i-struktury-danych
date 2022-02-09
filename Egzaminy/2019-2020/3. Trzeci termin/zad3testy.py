# zad3testy -- testy dla zadania 3 z egzaminu ASD (15. IX 2020)

class Node:
  def __init__( self, val ):
    self.next = None
    self.val = val

def tab2list(T):
    if len(T) == 0:
        return None
    frst = Node(T[0])
    tmp = frst
    for i in range(1,len(T)):
        e2 = Node(T[i])
        tmp.next = e2
        tmp = tmp.next
    return frst

def list2tab(L):
    T = []
    el = L
    while el != None:
        T.append(el.val)
        el = el.next
    return T


Test1 = [[1,4,8,10], [2,3,4,5], [7,16,18,20]]

R1 = [1,2,3,4,4,5,7,8,10,16,18,20]

Test2 = [[0,1], [10,20,30,40], [25,27], [35,45]]

R2 = [0,1,10,20,25,27,30,35,40,45]

Test3 = [[1,2,2,3,4], [2,3,4,5,5]]

R3 = [1,2,2,2,3,3,4,4,5,5]

TESTS = [Test1,Test2,Test3]

Res = [R1,R2,R3]


def runtests( f ):

    OK = True
    for i in range(len(TESTS)):
        X = []
        for li in TESTS[i]:
            X.append(tab2list(li))
        
        y = f(X)
        z = list2tab(y)
        print("----------------------")
        print( "Test:", TESTS[i] )
        print( "oczekiwany wynik =", Res[i] )
        print( "otrzymany wynik  =", z )
        
        if z != Res[i]:
            print( "Blad!" )
            OK = False
    print("----------------------")

    if OK:
        print( "OK!" )
    else:
        print( "Bledy!" )
            
 

