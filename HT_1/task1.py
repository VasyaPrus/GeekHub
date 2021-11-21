#1.Write a script which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

numbers = str(input("enter numbers through ',':"))
l = numbers.split(",")
t = tuple(l)
print(l)
print(t)

