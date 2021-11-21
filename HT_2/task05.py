#11.Write a script to remove duplicates from Dictionary.

dict_1 = {
    'a' : 's',
    'b' : 2,
    'c' : 3,
    'd' : 's',
    'e' : 2,
    'f' : 5
}

d = {}

for val in dict_1:
    if dict_1[val] not in d.values():
        d.update({val:dict_1[val]})

print(d)




