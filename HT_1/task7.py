#7.Write a script to concatenate all elements in a list into a string and print it.

l = [1, 2, 'test', 10, 'foo']
s = ""


for i in l:
    i = str(i)
    s += i

print(s)