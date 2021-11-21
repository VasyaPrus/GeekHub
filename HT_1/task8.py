#Write a script to replace last value of tuples in a list.

l = [(10, 20, 40), (40, 50, 60, 70), (80, 90), (1000,)]
last = input('Enter the last value of the tuples:')


for i in range(len(l)):
    lt = list(l[i])
    lt[-1] = last
    l[i] = tuple(lt)
print(l)
