#6.Write a script to check whether a specified value is contained in a group of values.

N = int(input("Number of values in the list:"))
l = []

while N>0:
    n = int(input("Enter the following value:"))
    l.append(n)
    N -= 1
t = tuple(l)

i = int(input("check value list:"))
k = int(input("check value tuple:"))

if k in t:
    print(k, "->", t, True)
else:
    print(k, "->", t, False)

if i in l:
    print(i, "->", l, True)
else:
    print(i, "->", l, False)
