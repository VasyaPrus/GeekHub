#Write a script to get the maximum and minimum value in a dictionary.

dict_1 = {1: 32, 2: 64, 3: 12, 4: 46, 5: 28, 6: 6}
l = []


for val in dict_1.values():
    l.append(val)

print("MAX:", max(l))
print("MIN:", min(l))