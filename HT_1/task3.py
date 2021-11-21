#3.Write a script to sum of the first n positive integers.

n = int(input('Enter n:'))
i = 0
l=[]


while n >= 1:
    l.append(n)
    n -= 1
print(sum(l))

  