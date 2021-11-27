from math import sqrt

def square(a):
    P = int(a*4)
    S = int(a*a)
    d = int(a*sqrt(2))
    t = (P, S, d)
    print(t)

square(8)