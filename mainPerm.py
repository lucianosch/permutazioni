from permutazione import *
import random as rm
from math import factorial

n = int(input('Inserisci un numero intero: '))
nfact = rm.randint(0,factorial(n)-1)
print(f'n: {nfact}')

f = n2fact(nfact,n)
print(f'factoradic: {f}')

permn = fact2perm(f)
print(f'permutazione #{nfact}: {permn}')
print('==============================')
'''
f = perm2fact(permn)
print(f'factoradic di {permn}: {f}')

n = fact2n(f)
print(f'n: {n}')
'''
p = [x for x in range(n)]
rm.shuffle(p)
print(f'permutazione: {p}')

f = perm2fact(p)
print(f'factoradic di {p}: {f}')

n = fact2n(f)
print(f'n: {n}')
