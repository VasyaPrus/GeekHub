#11.Write a script to remove duplicates from Dictionary.

dict_1 = {
    'a' : 's',
    'b' : 2,
    'c' : 3,
    'd' : 's',
    'e' : 2,
    'f' : 5
}

print(list(set(dict_1.values())))
