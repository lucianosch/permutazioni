from math import factorial

def n2fact(n,l):
    fact = []
    if n<factorial(l):
        for i in range(l-1,-1,-1):
            f = factorial(i)
            c = n//f
            n = n%f
            fact.append(c)
    return fact

def fact2perm(f):
    p0 = [x for x in range(len(f))]
    pn = [p0.pop(f[k]) for k in range(len(f))]
    return pn

'''
    pn = []
    for k in range(len(f)):
        pos = f[k]
        pn.append(p0.pop(pos))
'''

def fact2n(f):
    peso = len(f) - 1
    n = 0
    for k in range(len(f)):
        n += f[k]*factorial(peso)
        peso -= 1
    return n

def perm2fact(p):
    p0 = [x for x in range(len(p))]
    f = []
    for k in range(len(p)):
        pos = p0.index(p[k])
        f.append(pos)
        p0.pop(pos)
    return f

