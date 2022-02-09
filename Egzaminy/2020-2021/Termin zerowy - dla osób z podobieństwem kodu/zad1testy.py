# zad1testy.py


x1 = "egzamin"
y1 = "gezmina"
r1 = 3

x2 = "kotomysz"
y2 = "tokmysoz"
r2 = 3

x3 = "abaabababaaaababaaaaabaabba"
y3 = "baaaababbaaaaabbaaaabaabaab"
r3 = 1

x4 = "algorytm"
y4 = "logarytm"
r4 = 3

x5 = "sloniatko"
y5 = "oktainols"
r5 = 8

x6 = "darjeeling"
y6 = "darjeeling"
r6 = 0

TESTS = [(x1,y1,r1),
         (x2,y2,r2),
         (x3,y3,r3),
         (x4,y4,r4),
         (x5,y5,r5),
         (x6,y6,r6)]
         

def runtests( f ):
  OK = True
  print("hi")
  for x,y,r in TESTS:
    print("--------")
    print("x = ", x)
    print("y = ", y)
    for t in range(len(x)):
      RESULT = f(x,y,t)

      if RESULT != (t >= r):
        OK = False
        print("t = ", t)     
        print("oczekiwana odpowiedź: ", t >= r )
        print("uzyskana   odpowiedź: ", RESULT )
        print("Problem!")
        
  if OK: print("OK!")
  else : print("Problemy!")
