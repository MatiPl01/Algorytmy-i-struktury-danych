# zad1testy.py
from testy import *
from math  import *
import sys
from colorama import Fore, Style

ALLOWED_TIME = -1

sys.setrecursionlimit(10**6)


def log(*msg, color='red'):
    print(f'{getattr(Fore, color.upper())}{" ".join(map(str, msg))}{Style.RESET_ALL}')

def printarg( X ):
  log("Długość ciągu X: ", limit(len(X),120), color='green')
  log("Ciąg X         : ", limit(X,120), color='green')

def printhint( hint ):
  log("Długość najdłuższego podciągu MR:", limit(hint,120), color='green')
  
def printsol( sol ):
  log("Długość uzyskanego ciągu        :" , len(sol), color='green')
  log("Uzyskany ciąg                   :" , limit(sol,120), color='green')

 
def check( X, hint, sol ):
    # zakładamy, że ciągi wejściowe są niepuste,
    # więc ciąg sol ma co najmniej jeden element na tym etapie

    # czy MR?
    prev = sol[0]+1
    i = 0
    while i < len(sol) and prev > sol[i]:
      prev = sol[i]
      i += 1
    while i < len(sol) and prev < sol[i]:
      prev = sol[i]
      i += 1
    if i != len(sol):
      log("Błąd! Ciąg nie jest typu MR!")
      return False

    # czy podciąg?
    j = 0
    for i in range(len(X)):
      if sol[j] == X[i]: j+= 1
      if j == len(sol): break

    if j < len(sol):
      log("Błąd! Wynik nie jest podciągiem!")
      return False

    if len(sol) != hint:
      log("Błąd! Za krótki podciąg")
      return False

    
    return True


MY_seed    = 42
MY_a       = 134775813
MY_c       = 1
MY_modulus = 2**32
def MY_random():
   global MY_seed, MY_a, MY_c, MY_modulus
   MY_seed = (MY_a * MY_seed + MY_c) % MY_modulus
   return MY_seed


MY_choice = 1
MY_value  = 0
def hill( i ):
  global MY_value, MY_choice
  MY_value += MY_choice
  if MY_random() % 100 > 90:
    MY_choice*=-1
  return MY_value
  

# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TESTS = [
# 0
  {        #  I                                    x  y 
    "arg" :[[4,10,5,1,8,2,3,4]],
    "hint": 6
  }, 
# 1
  {        #  I                                    x  y 
    "arg" :[[1000-i**3 for i in range(200)]],
    "hint": 200
  }, 
# 2
  {        #  I                                    x  y 
    "arg" :[[i**2 for i in range(1000)]],
    "hint": 1000
  }, 
# 3
  {        #  I                                    x  y 
    "arg" :[[i*((i % 3)-1) for i in range(2000)]],
    "hint": 668
  }, 
# 4
  {        #  I                                    x  y 
    "arg" :[[int((100+i/40)*cos(i/10)*sin(float(i)/30)) for i in range(5000)]],
    "hint": 172
  }, 
# 5
  {        #  I                                    x  y 
    "arg" :[[MY_random() % 1000  for i in range(10000)]],
    "hint": 269
  }, 
# 6
  {        #  I                                    x  y 
    "arg" :[[hill(i)  for i in range(20000)]],
    "hint": 1234
  }, 
]




    


def runtests( f ):
  internal_runtests( printarg, printhint, printsol, check, TESTS, f, ALLOWED_TIME )
