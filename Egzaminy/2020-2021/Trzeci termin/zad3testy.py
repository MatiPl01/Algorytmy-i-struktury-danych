# zad1testy.py
from testy import *
from math  import *
import sys

ALLOWED_TIME = -1

sys.setrecursionlimit(10**6)

class Node:
  def __init__( self ):
    self.left    = None  # lewe podrzewo
    self.right   = None  # prawe poddrzewo
    self.parent  = None  # rodzic drzewa jesli istnieje
    self.key     = None  # klucz


def tree2str(p):
  if p is not None:
    s = tree2str(p.left)
    s += " %d " % p.key 
    s += tree2str(p.right)
    return s
  else:
    return ""

def printarg( T, C ):
  print("Klucze drzewa w kolejności inorder:  [%s]" % limit(tree2str(T), 100))
  print("]")
  print("Lista numerów                     : ", limit(C,100))

def printhint( hint ):
  print("Prawidłowy maksymalny klucz:", hint )
  
def printsol( sol ):
  print("Uzyskany maksymalny klucz  :", sol )

 
def check( T, C, hint, sol ):
    if hint != sol:
      return False
    return True   


  

# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TESTS = [
# 0
  {        
    "arg" :[[5,2,3,1,0,8,15],[3,4,6]],
    "hint": 8
  }, 
# 1
  {        
    "arg" :[[-5,-2,-3,-1,0,-8,-15],[3,4,6]],
    "hint": -1
  }, 
# 2
  {        
    "arg" :[[1,2,3,4,5,6,7],[1,3,7]],
    "hint": 7
  }, 
# 3
  {        
    "arg" :[[5,2,3,1,1,1,1,],[1,3,5]],
    "hint": 5
  }, 
# 4
  {        
    "arg" :[[34,12,22,11,0,-5,17,22,33,44,45,21,13,14,15],[2,4,5,8,9]],
    "hint": 33
  }, 
# 5
  {        
    "arg" :[[MY_random()% 10**6 for i in range(1023)],[(MY_random() % 1000)+1 for ii in range(100)]],
    "hint": 995353
  }, 
# 6
  {        
    "arg" :[[MY_random()% (10**7) for i in range(2047)],[(MY_random() % 2000)+1 for ii in range(500)]],
    "hint": 9998812
  }, 
]


def findplace(p,d):
    if p.left == None or p.right == None:
        return d, p
    g1, p1 = findplace(p.left, d+1)
    g2, p2 = findplace(p.right, d+1)
    if p1 == None:
        return g2, p2
    if p2 == None:
        return g1, p1
    if g1 <= g2:
        return g1, p1
    return g2, p2

def CreateTree(C):
  x = Node()
  x.key = C[0]
  for i in range (1, len(C)):
    d, p = findplace(x, 1)
    n = Node()
    n.parent = p
    n.key = C[i]
    if p.left == None:
        p.left = n
    else:
        p.right = n
  return x      

def Converted(TESTS):
    for t in TESTS:
        tr = CreateTree(t["arg"][0])
        t["arg"][0] = tr
    return TESTS
    


def runtests( f ):
  internal_runtests( printarg, printhint, printsol, check, Converted(TESTS), f, ALLOWED_TIME )
